import numpy as np

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return "gagal"

data = np.random.randint(1, 100, size=10)
print(data)
target = input("Angka yang ingin anda cari?: ")
target = int(target)

hasil = linear_search(data, target)
if hasil == "gagal":
    print(f"Elemen {target} tidak ditemukan")
else:
    print(f"Elemen {target} ditemukan di indeks {hasil}")