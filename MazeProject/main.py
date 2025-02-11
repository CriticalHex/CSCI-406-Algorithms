import networkx as nx  # type: ignore
import matplotlib.pyplot as plt


class Maze:
    """Class to represent the maze"""

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
        """A representation of the cells in the original maze"""

        def __init__(
            self,
            position: tuple[int, int],
            moves: list[tuple[int, int]],
            step_size_modifier: int,
        ) -> None:
            self.position = position
            self.moves = moves
            self.step_size_modifier = step_size_modifier

    def tuple_add(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
        "Adds two 'vector' tuples"
        return left[0] + right[0], left[1] + right[1]

    def generate_move(
        start: tuple[int, int], direction: tuple[int, int], step_size: int
    ):
        "Generate the position from a cell plus a direction with a step size"
        return Maze.tuple_add(
            (direction[0] * step_size, direction[1] * step_size), start
        )

    def between(number: int, lower: int, upper: int):
        "Inclusive between check"
        return number >= lower and number <= upper

    def tuple_between(
        pair: tuple[int, int], lower: tuple[int, int], upper: tuple[int, int]
    ):
        "Inclusive tuple between check"
        return Maze.between(pair[0], lower[0], upper[0]) and Maze.between(
            pair[1], lower[1], upper[1]
        )

    def generate_maze(self):
        """Reads the maze information from stdin and generates an array of Cells"""
        size, start_str, goal_str = input().split(" :: ")
        self.rows, self.columns = map(int, size.split())
        self.start = tuple(map(int, start_str.split()))
        self.goal = tuple(map(int, goal_str.split()))

        self.maze: list[Maze.Cell] = []
        for _ in range(self.rows * self.columns):
            coords, direction_str, step_modifier_str = input().split(" :: ")
            row, column = map(int, coords.split())
            directions = list(
                map(lambda x: Maze.cardinal_to_direction[x], direction_str.split())
            )
            step_modifier: int = (
                1
                if step_modifier_str == "I"
                else (-1 if step_modifier_str == "D" else 0)
            )
            self.maze.append(Maze.Cell((row, column), directions, step_modifier))

    def adapt_to_graph(self):
        """Create the graph:
        Vertex: contains the position and the current step size in this format: (pos, step_size), i.e. ((1, 1), 1)
        Edge: directional , models a step from one cell to the next at one step size, potentially increasing it.
        Weight: equal to the step size across that edge (the destinations step size)
        """
        self.posdict = {}
        self.graph = nx.DiGraph()
        for cell in self.maze:
            self.posdict.update(
                {
                    (cell.position, 0): (
                        cell.position[0],
                        cell.position[1],
                    )
                }
            )
            for step_size in range(1, max(self.rows, self.columns)):
                self.posdict.update(
                    {
                        (cell.position, step_size): (
                            cell.position[0] + (step_size * 0.1),
                            cell.position[1] + (step_size * 0.1),
                        )
                    }
                )
                for move in cell.moves:
                    other_position = Maze.generate_move(
                        cell.position, move, step_size + cell.step_size_modifier
                    )
                    if Maze.tuple_between(
                        other_position, (1, 1), (self.rows, self.columns)
                    ):
                        if other_position == self.goal:
                            self.graph.add_edge(
                                (cell.position, step_size),
                                (other_position, 1),
                                weight=step_size + cell.step_size_modifier,
                            )
                        else:
                            self.graph.add_edge(
                                (cell.position, step_size),
                                (other_position, step_size + cell.step_size_modifier),
                                weight=step_size + cell.step_size_modifier,
                            )

    def solve_maze(self):
        try:
            dist, path = nx.single_source_dijkstra(self.graph, (self.start, 1), (self.goal, 1))  # type: ignore
            print(dist, len(path))
            for node in path:
                print(*node[0])
        except:
            print("NO PATH")

    def draw(self):
        nx.draw(self.graph, self.posdict)  # type: ignore
        plt.show()


def main():
    maze = Maze()
    maze.generate_maze()
    maze.adapt_to_graph()
    # maze.draw()
    maze.solve_maze()


if __name__ == "__main__":
    main()
