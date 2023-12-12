"""Lorem Ipsum."""

from lattice_leaper.config import CHARACTER_NAME, MAZES, MOVES_TO_TEST
from lattice_leaper.heatmap import filter_heatmap, generate_heatmap, render_heatmap
from lattice_leaper.parser import find_starting_point, parse_maze


def main() -> None:
    """Solver."""
    maze_data = [
        parse_maze(maze)
        for maze in MAZES.iterdir()
        if maze.is_file() and maze.name.endswith('.txt')
    ]

    for idx, maze in enumerate(maze_data, 1):

        print(f"Analysing maze #{idx}:")
        starting_point = find_starting_point(maze)
        print(f"  {CHARACTER_NAME}'s location: {starting_point}")

        for allowed_steps in MOVES_TO_TEST:
            print(f"\n  {allowed_steps} steps:\n")
            heatmap = generate_heatmap(maze=maze, depth=allowed_steps)

            try:
                shortest_route = filter_heatmap(heatmap=heatmap, starting_point=starting_point)
            except ValueError:
                print("    No viable path found.")
            else:
                print(f"    The shortest route between {CHARACTER_NAME} and an exit is {len(shortest_route)} steps, with the following solution:")
                print(render_heatmap(maze=maze, heatmap=shortest_route, indent=6))

            print(f"\n    The following areas can reach the exit in {allowed_steps} steps:")
            print(render_heatmap(maze=maze, heatmap=heatmap, indent=6))


if __name__ == '__main__':
    main()
