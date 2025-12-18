m = int(input("Nhap so hang A: "))
n = int(input("Nhap so cot A: "))
p = int(input("Nhap so cot B: "))

A = []
B = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input()))
    A.append(row)

for i in range(n):
    row = []
    for j in range(p):
        row.append(int(input()))
    B.append(row)

C = []
for i in range(m):
    row = []
    for j in range(p):
        s = 0
        for k in range(n):
            s += A[i][k] * B[k][j]
        row.append(s)
    C.append(row)

print("Ma tran tich:")
for i in range(m):
    print(C[i])
