import random
import main
from time import perf_counter


def generate_random_test_case(n: int = None):
    if n is None:
        n = random.randint(1, 2000)
    return n, [random.randint(1, 1000) for _ in range(n)]


def test_runner(function, name: str, iterations=1000):
    with open(f"{name}.txt", "w") as file:
        for i in range(1, iterations + 1):
            print(f"Test #{i + 1}")
            n, b = generate_random_test_case(i * 2)
            if name == "naive":
                start = perf_counter()
                function(0, n - 1, b)
                time = perf_counter() - start
            else:
                start = perf_counter()
                function(n, b)
                time = perf_counter() - start
            file.write(f"{n} {time}\n")
        print("All tests complete!")


if __name__ == "__main__":
    for method, name in [
        (main.bottom_up, "bottom_up"),
        # (main.bottom_up_traceback, "traceback"),
        # (main.recursive, "naive"),
    ]:
        test_runner(method, name)
