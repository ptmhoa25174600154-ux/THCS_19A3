m = int(input("Nhap so hang: "))
n = int(input("Nhap so cot: "))

a = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input()))
    a.append(row)

if m != n:
    print("Khong phai ma tran vuong")
else:
    don_vi = True
    for i in range(n):
        for j in range(n):
            if i == j and a[i][j] != 1:
                don_vi = False
            if i != j and a[i][j] != 0:
                don_vi = False
    if don_vi:
        print("Ma tran don vi")
    else:
        print("Khong phai ma tran don vi")

