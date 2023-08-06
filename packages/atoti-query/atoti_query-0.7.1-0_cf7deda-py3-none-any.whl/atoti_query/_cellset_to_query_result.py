from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Any,
    Collection,
    Dict,
    Iterable,
    List,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Union,
)

import pandas as pd
from atoti_core import (
    Context,
    DataType,
    HierarchyCoordinates,
    LevelCoordinates,
    convert_to_pandas,
)

from ._cellset import (
    Cellset,
    CellsetAxis,
    CellsetCell,
    CellsetCellProperties,
    CellsetHierarchy,
    CellsetMember,
    MeasureValue,
)
from ._discovery import Discovery
from ._get_dimensions_mapping import DiscoveryDimensionMapping, get_dimensions_mapping
from ._get_level_data_types import GetLevelDataTypes
from .query_result import QueryResult

if TYPE_CHECKING:
    # This requires pandas' optional dependency jinja2.
    from pandas.io.formats.style import Styler  # pylint: disable=nested-import

    IndexDataType = Union[str, float, int, pd.Timestamp]

HierarchyToMaxNumberOfLevels = Mapping[HierarchyCoordinates, int]

MEASURES_HIERARCHY: CellsetHierarchy = {
    "dimension": "Measures",
    "hierarchy": "Measures",
}
MEASURES_HIERARCHY_COORDINATES = HierarchyCoordinates(
    MEASURES_HIERARCHY["dimension"],
    MEASURES_HIERARCHY["hierarchy"],
)

GRAND_TOTAL_CAPTION = "Total"


def _is_slicer(axis: CellsetAxis) -> bool:
    return axis["id"] == -1


def _get_default_measure(cellset: Cellset) -> Optional[CellsetMember]:
    return next(
        (
            CellsetMember(captionPath=member["captionPath"], namePath=member["path"])
            for member in cellset["defaultMembers"]
            if member["dimension"] == MEASURES_HIERARCHY["dimension"]
            and member["hierarchy"] == MEASURES_HIERARCHY["hierarchy"]
        ),
        None,
    )


def _get_measure_names_and_captions(
    cellset: Cellset, *, default_measure: Optional[CellsetMember] = None
) -> Tuple[Sequence[str], Sequence[str]]:
    if not cellset["axes"]:
        # When there are no axes at all, there is only one cell:
        # the value of the default measure aggregated at the top.
        return (
            ([default_measure["namePath"][0]], [default_measure["captionPath"][0]])
            if default_measure
            else ([], [])
        )

    # While looping on all the positions related to the Measures axis, the name of the same measure will come up repeatedly.
    # Only one occurrence of each measure name should be kept and the order of the occurrences must be preserved.
    # Since sets in Python do not preserve the order, a dict comprehension is used instead since a dict guarantees both the uniqueness and order of its keys.
    name_to_caption = {
        position[hierarchy_index]["namePath"][0]: position[hierarchy_index][
            "captionPath"
        ][0]
        for axis in cellset["axes"]
        if not _is_slicer(axis)
        for hierarchy_index, hierarchy in enumerate(axis["hierarchies"])
        if hierarchy == MEASURES_HIERARCHY
        for position in axis["positions"]
    }

    return tuple(name_to_caption), tuple(name_to_caption.values())


# There is a maxLevelPerHierarchy property for that in cellsets returned by the WebSocket API
# but not in those returned by the REST API that atoti uses.
def _get_hierarchy_to_max_number_of_levels(
    cellset: Cellset,
) -> HierarchyToMaxNumberOfLevels:
    hierarchy_to_max_number_of_levels: Dict[HierarchyCoordinates, int] = {}

    for axis in cellset["axes"]:
        if not _is_slicer(axis):
            for hierarchy_index, hierarchy in enumerate(axis["hierarchies"]):
                max_number_of_levels = 0
                for position in axis["positions"]:
                    number_of_levels = len(position[hierarchy_index]["namePath"])
                    if number_of_levels > max_number_of_levels:
                        max_number_of_levels = number_of_levels

                hierarchy_to_max_number_of_levels[
                    HierarchyCoordinates(hierarchy["dimension"], hierarchy["hierarchy"])
                ] = max_number_of_levels

    return hierarchy_to_max_number_of_levels


def _get_level_coordinates(
    dimensions: DiscoveryDimensionMapping,
    *,
    cellset: Cellset,
    hierarchy_to_max_number_of_levels: HierarchyToMaxNumberOfLevels,
) -> List[LevelCoordinates]:
    return [
        LevelCoordinates(hierarchy["dimension"], hierarchy["hierarchy"], level["name"])
        for axis in cellset["axes"]
        if not _is_slicer(axis)
        for hierarchy in axis["hierarchies"]
        if hierarchy != MEASURES_HIERARCHY
        for level_index, level in enumerate(
            dimensions[hierarchy["dimension"]][hierarchy["hierarchy"]]["levels"]
        )
        if level_index
        < hierarchy_to_max_number_of_levels[
            HierarchyCoordinates(hierarchy["dimension"], hierarchy["hierarchy"])
        ]
        and level["type"] != "ALL"
    ]


# See https://docs.microsoft.com/en-us/analysis-services/multidimensional-models/mdx/mdx-cell-properties-fore-color-and-back-color-contents.
# Improved over from https://github.com/activeviam/activeui/blob/ba42f1891cd6908de618fdbbab34580a6fe3ee58/packages/activeui-sdk/src/widgets/tabular/cell/MdxCellStyle.tsx#L29-L48.
def _cell_color_to_css_value(color: Union[int, str]) -> str:
    if isinstance(color, str):
        return "transparent" if color == '"transparent"' else color
    rest, red = divmod(color, 256)
    rest, green = divmod(rest, 256)
    rest, blue = divmod(rest, 256)
    return f"rgb({red}, {green}, {blue})"


# See https://docs.microsoft.com/en-us/analysis-services/multidimensional-models/mdx/mdx-cell-properties-using-cell-properties.
def _cell_font_flags_to_styles(font_flags: int) -> List[str]:
    styles = []
    text_decorations = []

    if font_flags & 1 == 1:
        styles.append("font-weight: bold")
    if font_flags & 2 == 2:
        styles.append("font-style: italic")
    if font_flags & 4 == 4:
        text_decorations.append("underline")
    if font_flags & 8 == 8:
        text_decorations.append("line-through")

    if text_decorations:
        styles.append(f"""text-decoration: {" ".join(text_decorations)}""")

    return styles


def _cell_properties_to_style(properties: CellsetCellProperties) -> str:
    styles = []

    back_color = properties.get("BACK_COLOR")
    if back_color is not None:
        styles.append(f"background-color: {_cell_color_to_css_value(back_color)}")

    font_flags = properties.get("FONT_FLAGS")
    if font_flags is not None:
        styles.extend(_cell_font_flags_to_styles(font_flags))

    font_name = properties.get("FONT_NAME")
    if font_name is not None:
        styles.append(f"font-family: {font_name}")

    font_size = properties.get("FONT_SIZE")
    if font_size is not None:
        styles.append(f"font-size: {font_size}px")

    fore_color = properties.get("FORE_COLOR")
    if fore_color is not None:
        styles.append(f"color: {_cell_color_to_css_value(fore_color)}")

    return "; ".join(styles)


def _get_pythonic_formatted_value(formatted_value: str) -> str:
    lower_formatted_value = formatted_value.lower()

    if lower_formatted_value == "true":
        return "True"

    if lower_formatted_value == "false":
        return "False"

    return formatted_value


CellMembers = Dict[HierarchyCoordinates, CellsetMember]


def _get_cell_members_and_is_total(
    cell: CellsetCell,
    *,
    cellset: Cellset,
    dimensions: DiscoveryDimensionMapping,
    hierarchy_to_max_number_of_levels: HierarchyToMaxNumberOfLevels,
    keep_totals: bool,
) -> Tuple[CellMembers, bool]:
    cell_members: CellMembers = {}
    is_total = False
    ordinal = cell["ordinal"]

    for axis in cellset["axes"]:
        if not _is_slicer(axis):
            ordinal, position_index = divmod(ordinal, len(axis["positions"]))
            for hierarchy_index, hierarchy in enumerate(axis["hierarchies"]):
                hierarchy_coordinates = HierarchyCoordinates(
                    hierarchy["dimension"], hierarchy["hierarchy"]
                )
                member = axis["positions"][position_index][hierarchy_index]

                is_total |= (
                    len(member["namePath"])
                    != hierarchy_to_max_number_of_levels[hierarchy_coordinates]
                )

                if not keep_totals and is_total:
                    return {}, True

                cell_members[hierarchy_coordinates] = (
                    member
                    if hierarchy_coordinates == MEASURES_HIERARCHY_COORDINATES
                    or dimensions[hierarchy_coordinates.dimension_name][
                        hierarchy_coordinates.hierarchy_name
                    ]["slicing"]
                    else {
                        "captionPath": member["captionPath"][1:],
                        "namePath": member["namePath"][1:],
                    }
                )

    return cell_members, is_total


def _get_member_name_index(
    levels_coordinates: Collection[LevelCoordinates],
    *,
    cellset: Cellset,
    get_level_data_types: Optional[GetLevelDataTypes] = None,
    members: Iterable[Tuple[str, ...]],
) -> Optional[pd.Index]:
    if not levels_coordinates:
        return None

    level_names = tuple(
        level_coordinates.level_name for level_coordinates in levels_coordinates
    )
    index_dataframe = pd.DataFrame(
        members,
        columns=level_names,
    )
    object_java_type: DataType = "Object"
    level_data_types: Mapping[LevelCoordinates, DataType] = (
        get_level_data_types(levels_coordinates, cube_name=cellset["cube"])
        if get_level_data_types
        else {
            level_coordinates: object_java_type
            for level_coordinates in levels_coordinates
        }
    )
    for level_coordinates in levels_coordinates:
        index_dataframe[level_coordinates.level_name] = convert_to_pandas(
            index_dataframe[level_coordinates.level_name],
            data_type=level_data_types[level_coordinates],
        )

    if len(levels_coordinates) == 1:
        return pd.Index(index_dataframe.iloc[:, 0])

    return pd.MultiIndex.from_frame(index_dataframe)  # type: ignore[no-any-return]


def _get_member_caption_index(
    levels_coordinates: Collection[LevelCoordinates],
    *,
    dimensions: DiscoveryDimensionMapping,
    members: Iterable[Tuple[str, ...]],
) -> Optional[pd.Index]:
    if not levels_coordinates:
        return None

    level_captions = tuple(
        next(
            level["caption"]
            for level in dimensions[level_coordinates.dimension_name][
                level_coordinates.hierarchy_name
            ]["levels"]
            if level["name"] == level_coordinates.level_name
        )
        for level_coordinates in levels_coordinates
    )

    grand_total: Tuple[str, ...] = tuple()
    members_with_grand_total_caption = (
        (GRAND_TOTAL_CAPTION,) if member == grand_total else member
        for member in members
    )

    index_dataframe = pd.DataFrame(
        members_with_grand_total_caption,
        columns=level_captions,
        dtype="string",
    ).fillna("")

    if len(levels_coordinates) == 1:
        return pd.Index(index_dataframe.iloc[:, 0])

    return pd.MultiIndex.from_frame(index_dataframe)  # type: ignore[no-any-return]


def _create_measure_collection(
    measure_values: Iterable[Mapping[str, Any]],
    *,
    index: Optional[pd.Index],
    measure_name: str,
) -> Union[List[MeasureValue], pd.Series]:
    values: List[MeasureValue] = [values.get(measure_name) for values in measure_values]
    return (
        pd.Series(
            values,
            # Forcing `object` dtypes when some measure values are ``None`` to prevent pandas from inferring a numerical type and ending up with NaNs.
            dtype="object",
            index=index,
        )
        if None in values
        else values
    )


def _get_data_values(
    measure_values: Iterable[Mapping[str, Any]],
    *,
    index: Optional[pd.Index],
    measure_names: Collection[str],
) -> Dict[str, Union[List[MeasureValue], pd.Series]]:
    """Return a mapping of collection where the dtype is ``object`` when some measure values are ``None``."""
    return {
        measure_name: _create_measure_collection(
            measure_values, index=index, measure_name=measure_name
        )
        for measure_name in measure_names
    }


def cellset_to_query_result(
    cellset: Cellset,
    *,
    context: Optional[Context] = None,
    discovery: Discovery,
    get_level_data_types: Optional[GetLevelDataTypes] = None,
    keep_totals: bool,
) -> QueryResult:
    """Convert an MDX cellset to a pandas DataFrame."""
    default_measure = _get_default_measure(cellset)
    dimensions = get_dimensions_mapping(
        next(
            cube
            for catalog in discovery["catalogs"]
            for cube in catalog["cubes"]
            if cube["name"] == cellset["cube"]
        )
    )
    hierarchy_to_max_number_of_levels = _get_hierarchy_to_max_number_of_levels(cellset)

    has_some_style = any(cell for cell in cellset["cells"] if cell["properties"])

    member_captions_to_measure_formatted_values: Dict[
        Tuple[str, ...], Dict[str, str]
    ] = {}
    member_captions_to_measure_styles: Dict[Tuple[str, ...], Dict[str, str]] = {}
    member_names_to_measure_values: Dict[Tuple[str, ...], Dict[str, Any]] = {}

    for cell in cellset["cells"]:
        cell_members, is_total = _get_cell_members_and_is_total(
            cell,
            cellset=cellset,
            dimensions=dimensions,
            hierarchy_to_max_number_of_levels=hierarchy_to_max_number_of_levels,
            keep_totals=keep_totals,
        )

        if keep_totals or not is_total:
            if not default_measure:
                raise RuntimeError(
                    "Expected a default member for measures but found none."
                )

            measure = cell_members.setdefault(
                MEASURES_HIERARCHY_COORDINATES,
                default_measure,
            )

            non_measure_cell_members = tuple(
                cell_member
                for hierarchy, cell_member in cell_members.items()
                if hierarchy != MEASURES_HIERARCHY_COORDINATES
            )
            member_names, member_captions = (
                tuple(
                    name
                    for member in non_measure_cell_members
                    for name in member["namePath"]
                ),
                tuple(
                    name
                    for member in non_measure_cell_members
                    for name in member["captionPath"]
                ),
            )

            member_names_to_measure_values.setdefault(member_names, {})[
                measure["namePath"][0]
            ] = cell["value"]
            member_captions_to_measure_formatted_values.setdefault(member_captions, {})[
                measure["captionPath"][0]
            ] = _get_pythonic_formatted_value(cell["formattedValue"])

            if has_some_style:
                member_captions_to_measure_styles.setdefault(member_captions, {})[
                    measure["captionPath"][0]
                ] = _cell_properties_to_style(cell["properties"])

    levels_coordinates = _get_level_coordinates(
        dimensions,
        cellset=cellset,
        hierarchy_to_max_number_of_levels=hierarchy_to_max_number_of_levels,
    )

    member_name_index = _get_member_name_index(
        levels_coordinates,
        cellset=cellset,
        get_level_data_types=get_level_data_types,
        members=member_names_to_measure_values.keys(),
    )

    member_caption_index = _get_member_caption_index(
        levels_coordinates,
        dimensions=dimensions,
        members=member_captions_to_measure_formatted_values.keys(),
    )

    measure_names, measure_captions = _get_measure_names_and_captions(
        cellset, default_measure=default_measure
    )

    formatted_values_dataframe = pd.DataFrame(
        member_captions_to_measure_formatted_values.values(),
        columns=measure_captions,
        dtype="string",
        index=member_caption_index,
    ).fillna("")

    def _get_styler() -> Styler:
        styler = formatted_values_dataframe.style

        if has_some_style:

            def apply_style(_: pd.DataFrame) -> pd.DataFrame:
                return pd.DataFrame(
                    member_captions_to_measure_styles.values(),
                    columns=measure_captions,
                    index=member_caption_index,
                )

            styler = styler.apply(
                apply_style,
                # None is documented as a valid argument value but pandas-stubs does not support it.
                axis=None,  # type: ignore
            )

        return styler

    return QueryResult(
        _get_data_values(
            member_names_to_measure_values.values(),
            index=member_name_index,
            measure_names=measure_names,
        ),
        context=context,
        formatted_values=formatted_values_dataframe,
        get_styler=_get_styler,
        index=member_name_index,
    )
