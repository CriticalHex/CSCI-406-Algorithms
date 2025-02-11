import networkx as nx
import queue as q

VISITED = "visited"
PARENT = "parent"
DISTANCE = "distance"


def bfs(graph: nx.Graph, starting_node: int, traversal: list[int]):
    queue: q.SimpleQueue[int] = q.SimpleQueue()

    queue.put(starting_node)
    graph.nodes[starting_node][DISTANCE] = 0
    graph.nodes[starting_node][VISITED] = True

    while not queue.empty():
        node = queue.get()
        traversal.append(node)
        data = graph.nodes[node]
        for adjacent in sorted(graph.neighbors(node)):
            adjacent_data = graph.nodes[adjacent]
            if not adjacent_data[VISITED]:
                adjacent_data[VISITED] = True
                adjacent_data[DISTANCE] = data[DISTANCE] + 1
                adjacent_data[PARENT] = node
                queue.put(adjacent)


def main():
    starting_node = int(input())

    graph = nx.Graph()

    for _ in range(int(input())):
        graph.add_edge(*map(int, input().split(":")))

    v = graph.number_of_nodes()

    nx.set_node_attributes(graph, False, VISITED)
    nx.set_node_attributes(graph, None, PARENT)
    nx.set_node_attributes(graph, -1, DISTANCE)

    traversal = []

    bfs(graph, starting_node, traversal)

    print("Traversal:")
    print(*traversal)
    print("Distances:")
    for i in range(1, v + 1):
        data = graph.nodes[i]
        print(f"Node {i}: {data[DISTANCE]}")
    print("Parents:")
    for i in range(1, v + 1):
        data = graph.nodes[i]
        print(f"Node {i}: {data[PARENT]}")


if __name__ == "__main__":
    main()
