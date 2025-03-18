def recursive(i: int, j: int, b: list[int]):
    if i == j:
        return b[i]
    return sum(b[i : j + 1]) - min(recursive(i + 1, j, b), recursive(i, j - 1, b))


def bottom_up(n: int, b: list[int]):
    table = list(list((0, "") for _ in range(n)) for _ in range(n))

    for row in range(n - 1, -1, -1):
        for col in range(row, n):
            if row == col:
                table[row][col] = (b[row], str(row + 1))
            else:
                rp1 = row + 1
                picked = min(
                    (table[rp1][col], rp1),
                    (table[row][col - 1], col),
                    key=lambda x: x[0][0],
                )
                table[row][col] = (
                    sum(b[row : col + 1]) - picked[0][0],
                    f"{picked[1]} {picked[0][1]}",
                )
    return table[0][n - 1]


def main():
    n = int(input())
    b = list(map(int, input().split()))
    print(*bottom_up(n, b), sep="\n")


if __name__ == "__main__":
    main()
