import random
import time
import numpy as np
import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Використовуємо середній елемент
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def measure_time(sort_function, arr, repeats=5):
    times = []
    for _ in range(repeats):
        arr_copy = arr.copy()
        start_time = time.time()
        sort_function(arr_copy)
        times.append(time.time() - start_time)
    return np.mean(times)


# Розміри масивів
sizes = [10_000, 50_000, 100_000, 500_000]
randomized_times = []
deterministic_times = []

for size in sizes:
    test_array = [random.randint(0, 10 ** 6) for _ in range(size)]

    rand_time = measure_time(randomized_quick_sort, test_array)
    det_time = measure_time(deterministic_quick_sort, test_array)

    randomized_times.append(rand_time)
    deterministic_times.append(det_time)

    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")
    print(f"   Детермінований QuickSort: {det_time:.4f} секунд")

# Побудова графіка
plt.figure(figsize=(10, 5))
plt.plot(sizes, randomized_times, label="Рандомізований QuickSort", marker="o")
plt.plot(sizes, deterministic_times, label="Детермінований QuickSort", marker="s")
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняння швидкодії QuickSort")
plt.legend()
plt.grid()
plt.show()