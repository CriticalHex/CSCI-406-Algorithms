def find(x: int, parents: list[int]) -> int:
    search = x
    while parents[x] != x:
        x = parents[x]
    parents[search] = x
    return x


def find_rec(get: int, parents: list[int]) -> int:
    if parents[get] == get:
        return get
    parents[get] = find_rec(parents[get], parents)
    return parents[get]


def find_no_op(x: int, parents: list[int]) -> int:
    while parents[x] != x:
        x = parents[x]
    return x


def size(root: int, parents: list[int]) -> int:
    total = 0
    for x in parents:
        if find_no_op(x, parents) == root:
            total += 1
    return total


def union(x: int, y: int, parents: list[int]) -> int:
    root_x = find_rec(x, parents)
    root_y = find_rec(y, parents)

    if root_x != root_y:
        size_x = size(root_x, parents)
        size_y = size(root_y, parents)
        if size_y == size_x:
            parents[max(root_x, root_y)] = min(root_x, root_y)
        elif size_y < size_x:
            parents[root_y] = root_x
        elif size_y > size_x:
            parents[root_x] = root_y


def main():
    size, queries = map(int, input().split())
    parents = list(range(size))  # each element is its own root at first.
    for _ in range(queries):
        x, y = map(int, input().split())
        union(x, y, parents)
        print(*parents)


if __name__ == "__main__":
    main()
