from matplotlib import pyplot as plt

with open("naive.txt", "r") as file:
    x = []
    y = []
    for line in file:
        a, b = line.rstrip().split()
        x.append(int(a))
        y.append(float(b))

plt.plot(x, y)
plt.ylabel("time (seconds)")
plt.xlabel("size (n)")
plt.title("Recursive")
plt.show()
