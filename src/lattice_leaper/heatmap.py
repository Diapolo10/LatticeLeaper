"""Heatmap generation."""

from typing import TypeVar

from escapyde.colours import FCYAN, FGREEN, FRED, FYELLOW  # type: ignore[import]

from lattice_leaper.config import MazeElement

T = TypeVar('T')


def tuple_sum(*tuples: tuple[T, ...]) -> tuple[T, ...]:
    """
    Create a new tuple with the values of the given tuples summed up elementwise.

    Raises a ValueError if the tuples aren't the same length.
    """
    return tuple(sum(values) for values in zip(*tuples, strict=True))


def generate_heatmap(maze: list[str], depth: int) -> dict[tuple[int, ...], int]:
    """
    Analyse a maze, producing a heatmap of every non-blocking cell of what cells are close enough to reach an exit.

    The output is a dictionary mapping of coordinates and their heat values.
    """
    movable_spots: dict[tuple[int, ...], int] = {
        (y, x): 0
        for y, row in enumerate(maze)
        for x, cell in enumerate(row)
        if cell != MazeElement.BLOCK
    }

    targets: list[tuple[int, ...]] = [
        (y, x)
        for y, row in enumerate(maze)
        for x, cell in enumerate(row)
        if cell == MazeElement.EXIT
    ]

    for num in range(depth, 0, -1):
        new_targets = []
        for target in targets:
            if target in movable_spots and movable_spots[target] < num:
                movable_spots[target] = num
                for modifier in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    cell = tuple_sum(target, modifier)
                    if cell in movable_spots:
                        new_targets.append(cell)
        targets = new_targets

    return movable_spots


def render_heatmap(maze: list[str], heatmap: dict[tuple[int, ...], int], indent: int = 0) -> str:
    """
    Render a human-readable version of the maze, with the heatmap on top.

    NOTE: The colour formatting requires a terminal that supports
          ANSI escape sequences (eg. PowerShell).
    """
    result = []
    for y, row in enumerate(maze):
        text_row = []
        for x, cell in enumerate(row):
            if (y, x) in heatmap and heatmap[(y, x)] > 0 and cell in {MazeElement.START, MazeElement.EXIT}:
                text_row.append(f"{FYELLOW | '■'}")
            elif (y, x) in heatmap and heatmap[(y, x)] > 0:
                text_row.append(f"{FRED | '■'}")
            elif cell in {MazeElement.START, MazeElement.EXIT}:
                text_row.append(f"{FGREEN | cell}")
            else:
                text_row.append(f"{FCYAN | cell}")
        result.append(' ' * indent + ''.join(text_row))

    return '\n'.join(result)


def filter_heatmap(heatmap: dict[tuple[int, ...], int], starting_point: tuple[int, ...]) -> dict[tuple[int, ...], int]:
    """
    Filter unnecessary records from the heatmap, leaving only the shortest route.

    Raises ValueError if no path can be found in the heatmap that can reach the starting point.
    """
    if starting_point not in heatmap or heatmap[starting_point] == 0:
        msg = 'No path between points'
        raise ValueError(msg)

    filtered_heatmap: dict[tuple[int, ...], int] = {starting_point: heatmap[starting_point]}

    current_cell = starting_point
    while True:
        for modifier in ((1, 0),    # down
                         (-1, 0),   # up
                         (0, 1),    # right
                         (0, -1)):  # left
            cell = tuple_sum(current_cell, modifier)
            if cell in heatmap and heatmap[cell] > heatmap[current_cell]:
                filtered_heatmap[cell] = heatmap[cell]
                current_cell = cell
                break
        else:
            # No bigger heatmap values found, we've reached the end
            break

    return filtered_heatmap
