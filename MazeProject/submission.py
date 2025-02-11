import networkx as nx  # type: ignore
from typing import Any

cardinal_to_direction: dict[str, tuple[int, int]] = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
    "NE": (-1, 1),
    "SE": (1, 1),
    "NW": (-1, -1),
    "SW": (1, -1),
    "X": (0, 0),
}


class Cell:
    """Class to represent a cell in the maze"""
    def __init__(
        self, position: tuple[int, int], moves: list[str], step_size_modifier: int
    ) -> None:
        self.position = position
        self.moves = moves
        self.step_size_modifier = step_size_modifier

    def __str__(self) -> str:
        return f"{self.position}, {self.moves}, {self.step_size_modifier}"


def tuple_add(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    "Adds two 'vector' tuples"
    return left[0] + right[0], left[1] + right[1]


def generate_move(start: tuple[int, int], direction: str, step_size: int):
    "Generate the position from a cell plus a direction with a step size"
    move = cardinal_to_direction[direction]
    return tuple_add((move[0] * step_size, move[1] * step_size), start)


def get_weight(source: tuple[int, int], destination: tuple[int, int], edge_data: dict[str, Any]) -> int:
    "Custom weight function for nx Dijkstra"
    if source[0] == destination[0]:
        return 0
    return destination[1]


def between(number: int, lower: int, upper: int):
    "Inclusive between check"
    return number >= lower and number <= upper


def tuple_between(
    pair: tuple[int, int], lower: tuple[int, int], upper: tuple[int, int]
):
    "Inclusive tuple between check"
    return between(pair[0], lower[0], upper[0]) and between(pair[1], lower[1], upper[1])


def generate_maze():
    """Reads the maze information from stdin and generates an array of Cells"""
    size, start_str, goal_str = input().split(" :: ")
    rows, columns = map(int, size.split())
    start = tuple(map(int, start_str.split()))
    goal = tuple(map(int, goal_str.split()))

    maze: list[Cell] = []
    for _ in range(rows * columns):
        coords, direction_str, step_modifier_str = input().split(" :: ")
        row, column = map(int, coords.split())
        directions = direction_str.split()
        step_modifier: int = (
            1 if step_modifier_str == "I" else (-1 if step_modifier_str == "D" else 0)
        )
        maze.append(Cell((row, column), directions, step_modifier))

    return maze, start, goal, rows, columns


def main():
    maze, start, goal, rows, columns = generate_maze()

    graph = nx.DiGraph()
    for cell in maze:
        for step_size in range(1, max(rows, columns)):
            for move in cell.moves:
                other_position = generate_move(cell.position, move, step_size + cell.step_size_modifier)
                if tuple_between(other_position, (1, 1), (rows, columns)):
                    graph.add_edge((cell.position, step_size), (other_position, step_size + cell.step_size_modifier))  # type: ignore
                if (cell.position == goal) and (step_size > 1):
                    graph.add_edge((cell.position, step_size), (cell.position, 1))  # type: ignore

    try:
        dist, path = nx.single_source_dijkstra(graph, (start, 1), (goal, 1), weight=get_weight)  # type: ignore
        if path[-1][0] == goal and path[-2][0] == goal:
            path.pop()
        print(dist, len(path))
        for node in path:
            print(*node[0])
    except:
        print("NO PATH")


if __name__ == "__main__":
    main()
