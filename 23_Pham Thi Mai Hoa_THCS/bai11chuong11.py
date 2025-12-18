n = int(input("Nhap cap ma tran: "))
a = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    a.append(row)

doi_xung = True
for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            doi_xung = False
            break

if doi_xung:
    print("Ma tran doi xung")
else:
    print("Ma tran khong doi xung")
