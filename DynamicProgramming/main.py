def recursive(i: int, j: int, b: list[int]):
    if i == j:
        return b[i]
    return sum(b[i : j + 1]) - min(recursive(i + 1, j, b), recursive(i, j - 1, b))


def bottom_up_traceback(n: int, b: list[int]):
    table = list(list((0, -1) for _ in range(n)) for _ in range(n))

    sum_table: list[float | int] = [0]
    for num in b:
        sum_table.append(num + sum_table[-1])

    for row in range(n - 1, -1, -1):
        rp1 = row + 1

        table[row][row] = (b[row], str(rp1))
        for col in range(rp1, n):
            cm1 = col - 1
            cp1 = col + 1
            if table[rp1][col][0] <= table[row][cm1][0]:
                picked = table[rp1][col]
                left = True
            else:
                picked = table[row][cm1]
                left = False

            table[row][col] = ((sum_table[cp1] - sum_table[row]) - picked[0], left)
    value = table[0][n - 1][0]

    path = ""
    row, col = 0, n - 1
    while row <= col:
        left = table[row][col][1]
        if left:
            row += 1
            path += str(row) + " "
        else:
            path += str(col + 1) + " "
            col -= 1

    return value, path.rstrip()


def bottom_up(n: int, b: list[int]):
    table = list(list(0 for _ in range(n)) for _ in range(2))

    sum_table: list[float | int] = [0]
    for num in b:
        sum_table.append(num + sum_table[-1])

    for row in range(n - 1, -1, -1):
        rp1 = row + 1
        rp1m2 = rp1 % 2
        rm2 = row % 2

        table[rm2][row] = b[row]
        for col in range(rp1, n):
            cm1 = col - 1
            cp1 = col + 1
            value = min(table[rp1m2][col], table[rm2][cm1])

            table[rm2][col] = sum_table[cp1] - sum_table[row] - value
    return table[0][n - 1]


def main():
    n = int(input())
    b = list(map(int, input().split()))
    print(bottom_up(n, b), sep="\n")


if __name__ == "__main__":
    main()
