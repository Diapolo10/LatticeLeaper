"""Global fixtures for unit tests."""

from pathlib import Path

import pytest

TEST_MAZES = Path(__file__).parent / 'mazes'


@pytest.fixture
def mazes():
    """Fetch mazes from the test maze directory."""
    return list(TEST_MAZES.glob('*.txt'))


@pytest.fixture
def parsed_maze():
    """Maze."""
    return [
        "##E############################",
        "#     #                    #  #",
        "#  ####  #############  ####  #",
        "#        #     #  #  #        #",
        "#  #######  #  #  #  #  ####  #",
        "#  #  #     #  #  #     #     #",
        "####  #  #######  #  ##########",
        "#  #  #           #  #        #",
        "#  #  ####  #######  ####  ####",
        "#  #           #              #",
        "#  #######  ####  ####  ####  #",
        "#                 #        #  #",
        "#######  #  ####  ##########  #",
        "#        #     #     #  #  #  #",
        "#  #  ####  ####  #  #  #  #  #",
        "#  #  #  #     #  #  #     #  #",
        "#  ####  ####  ####  #  #######",
        "#     #     #     #     #     #",
        "####  #  #######  ####  ####  #",
        "#     #           #           #",
        "############################^##",
    ]


@pytest.fixture
def maze_no_start():
    """Fetch an invalid maze, missing a starting point."""
    return TEST_MAZES / 'maze.nostart'


@pytest.fixture
def maze_no_exit():
    """Fetch an invalid maze, missing a starting point."""
    return TEST_MAZES / 'maze.noexit'


@pytest.fixture
def parsed_maze_no_start():
    """Maze, no start."""
    return [
        "##E############################",
        "#     #                    #  #",
        "#  ####  #############  ####  #",
        "#        #     #  #  #        #",
        "#  #######  #  #  #  #  ####  #",
        "#  #  #     #  #  #     #     #",
        "####  #  #######  #  ##########",
        "#  #  #           #  #        #",
        "#  #  ####  #######  ####  ####",
        "#  #           #              #",
        "#  #######  ####  ####  ####  #",
        "#                 #        #  #",
        "#######  #  ####  ##########  #",
        "#        #     #     #  #  #  #",
        "#  #  ####  ####  #  #  #  #  #",
        "#  #  #  #     #  #  #     #  #",
        "#  ####  ####  ####  #  #######",
        "#     #     #     #     #     #",
        "####  #  #######  ####  ####  #",
        "#     #           #           #",
        "###############################",
    ]
