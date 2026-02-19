def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return "gagal"

data = [15,8,23,42,7,16,31,9]
target = 16

hasil = linear_search(data, target)
if hasil == "gagal":
    print(f"Elemen {target} tidak ditemukan")
else:
    print(f"Elemen {target} ditemukan di indeks {hasil}")