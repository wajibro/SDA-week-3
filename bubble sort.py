import numpy as np
import time as t

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

while True:
    data = np.random.choice(np.arange(0, 10), size=10, replace=False)
    print(f"Sebelum: {data}")

    s = t.perf_counter()

    hasil = bubble_sort(data.copy())
    print(f'Setelah: {hasil}')

    end = t.perf_counter() - s

    print(f'{end*10**4:.2f} ms')

    t.sleep(.2)