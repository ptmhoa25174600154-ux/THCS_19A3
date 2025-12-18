m = int(input("Nhap so hang: "))
n = int(input("Nhap so cot: "))
a = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input()))
    a.append(row)

max_tong = None
hang = 0

for i in range(m):
    tong = 0
    for j in range(n):
        tong += a[i][j]
    if max_tong is None or tong > max_tong:
        max_tong = tong
        hang = i

print("Hang co tong lon nhat:", hang)
print("Tong:", max_tong)
