def naive(n: int):
    if n < 3:
        return n
    if n == 3:
        return 4
    return naive(n - 1) + naive(n - 2) + naive(n - 3)


def top_down(n: int, table: list[int] = None):
    if table is None:
        table = list(None for _ in range(n + 1))
    if table[n]:
        return table[n]
    if n < 3:
        table[n] = n
        return n
    if n == 3:
        table[n] = 4
        return 4
    table[n] = top_down(n - 1) + top_down(n - 2) + top_down(n - 3)
    return table[n]


def bottom_up(n: int):
    table = list(0 for _ in range(n + 1))
    for i in range(min(3, n + 1)):
        table[i] = i
    if n > 2:
        table[3] = 4
        for i in range(4, n + 1):
            table[i] = table[i - 1] + table[i - 2] + table[i - 3]
    return table[n]


def main():
    n = int(input())
    print(bottom_up(n))


if __name__ == "__main__":
    main()
