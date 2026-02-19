import numpy as np
import time as t

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

data = np.random.choice(np.arange(0, 10), size=10, replace=False)
print(f"Sebelum: {data}")

s = t.perf_counter()

hasil = selection_sort(data.copy())
print(f'Setelah: {hasil}')

end = t.perf_counter() - s

print(f'{end*10**4:.2f} ms')