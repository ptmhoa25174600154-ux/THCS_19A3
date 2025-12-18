n = int(input("Nhap so phan tu: "))
a = []

for i in range(n):
    a.append(int(input()))

k = int(input("Nhap k: "))
k = k % n

b = [0] * n

for i in range(n):
    b[(i + k) % n] = a[i]

print(b)
