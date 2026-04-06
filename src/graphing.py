import time
import matplotlib.pyplot as plt
from Algorithm import algorithm, parse_input

sizes = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]
times = []

for i in range(1, 11):
    with open(f'../data/file{i}.in', 'r') as f:
        text = f.read()

    values, a, b = parse_input(text)

    total = 0
    for _ in range(5):
        start = time.perf_counter()
        algorithm(values, a, b)
        end = time.perf_counter()
        total += end - start

    avg = total / 5
    times.append(avg)

plt.plot(sizes, times, marker='o')
plt.xlabel('String Length')
plt.ylabel('Runtime (seconds)')
plt.title('Algorithm Runtime on 10 Input Files')
plt.grid(True)
plt.savefig('runtime_graph.png')
plt.show()

print(sizes)
print(times)