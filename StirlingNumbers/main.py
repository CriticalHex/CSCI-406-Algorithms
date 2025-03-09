def naive(n: int, k: int):
    if (n < k) or (k == 0 and n > 0):
        return 0
    if (n == k and n >= 0 and k >= 0) or (k == 1 and n > 1):
        return 1
    return k * naive(n - 1, k) + naive(n - 1, k - 1)


def top_down(n: int, k: int, table: dict[tuple[int, int] : int] = {}):
    key = (n, k)
    if (n < k) or (k == 0 and n > 0):
        table.update({key: 0})
        return 0
    if (n == k and n >= 0 and k >= 0) or (k == 1 and n > 1):
        table.update({key: 1})
        return 1
    val = table.get(key)
    if val is None:
        new_val = k * top_down(n - 1, k) + top_down(n - 1, k - 1)
        table.update({key: new_val})
        return new_val
    return val


def bottom_up(n: int, k: int):
    table: list[list[int]] = list(list(0 for _ in range(k + 1)) for _ in range(n + 1))
    for i in range(n + 1):
        for j in range(k + 1):
            if (i == j and i >= 0 and j >= 0) or (j == 1 and i > 1):
                table[i][j] = 1
            else:
                table[i][j] = j * table[i - 1][j] + table[i - 1][j - 1]
    return table[n][k]


def main():
    n, k = map(int, input().split())
    print(bottom_up(n, k) % (10**9 + 7))


if __name__ == "__main__":
    main()
