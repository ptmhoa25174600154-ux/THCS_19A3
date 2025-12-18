n = int(input("Nhap cap ma tran: "))
a = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    a.append(row)

tong = 0
for i in range(n):
    tong += a[i][n - 1 - i]

print("Tong duong cheo phu:", tong)