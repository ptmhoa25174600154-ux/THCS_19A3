n = int(input("Nhap so phan tu: "))
a = []

for i in range(n):
    a.append(int(input()))

k = int(input("Nhap k: "))

for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == k:
            print(a[i], a[j])
