import numpy as np

global x
x = 0

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                global x
                x += 1
    return arr

data = np.random.choice(np.arange(0, 10), size=10, replace=False)
print(f"Sebelum: {data}")

hasil = bubble_sort(data.copy())
print(f'Setelah: {hasil}')
print(f'Jumlah pertukaran: {x}')