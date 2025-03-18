def naive(n: int, k: int):
    if n <= k:
        return 0
    if k == 0 or k == n - 1:
        return 1
    return (n - k) * naive(n - 1, k - 1) + (k + 1) * naive(n - 1, k)


def top_down(n: int, k: int, table: list[list[int]] = None):
    if table is None:
        table = list(list(None for _ in range(k + 1)) for _ in range(n + 1))
    if table[n][k]:
        return table[n][k]
    if n <= k:
        table[n][k] = 0
        return 0
    if k == 0 or k == n - 1:
        table[n][k] = 1
        return 1
    val = (n - k) * top_down(n - 1, k - 1, table) + (k + 1) * top_down(n - 1, k, table)
    table[n][k] = val
    return val


def bottom_up(n: int, k: int):
    table: list[list[int]] = list(list(0 for _ in range(k + 1)) for _ in range(n + 1))
    for i in range(n + 1):
        for j in range(k + 1):
            if i <= j:
                continue
            if j == 0 or j == i - 1:
                table[i][j] = 1
            else:
                table[i][j] = (i - j) * table[i - 1][j - 1] + (j + 1) * table[i - 1][j]
    return table[n][k]


def main():
    n, k = map(int, input().split())
    print(bottom_up(n, k))


if __name__ == "__main__":
    main()
