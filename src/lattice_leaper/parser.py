"""Parse maze files."""

from pathlib import Path

from lattice_leaper.config import MazeElement


def parse_maze(path: Path) -> list[str]:
    """
    Parse a given maze file into a list of strings.

    Raises ValueErrors on missing starting locations and exits.
    """
    raw_text = path.read_text(encoding='utf-8')

    if MazeElement.START not in raw_text:
        msg = 'No starting point found'
        raise ValueError(msg)

    if MazeElement.EXIT not in raw_text:
        msg = 'No exits found'
        raise ValueError(msg)

    return list(raw_text.splitlines())


def find_starting_point(maze: list[str]) -> tuple[int, ...]:
    """
    Find the starting point from the maze.

    Raises ValueError if a starting point cannot be found.
    """
    for row_idx, row in enumerate(maze):
        for col_idx, cell in enumerate(row):
            if cell == MazeElement.START:
                return row_idx, col_idx

    msg = 'No starting point found'
    raise ValueError(msg)
