import numpy as np
import time as t

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

while True:
    data = np.random.choice(np.arange(0, 10), size=10, replace=False)
    print(f"Sebelum: {data}")

    s = t.perf_counter()

    hasil = insertion_sort(data.copy())
    print(f'Setelah: {hasil}')

    end = t.perf_counter() - s
    end = end*10**4

    print(f'{end:.2f} ms')
    t.sleep(.2)