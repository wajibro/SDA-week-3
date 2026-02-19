import numpy as np
import time as t
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print(f'================ pass ke {i+1} ================')
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
                t.sleep(.5)
        print()
    return arr

data = np.random.choice(np.arange(0, 10), size=10, replace=False)
print(f"Sebelum: {data}")

hasil = bubble_sort(data.copy())
print(f'Setelah: {hasil}')