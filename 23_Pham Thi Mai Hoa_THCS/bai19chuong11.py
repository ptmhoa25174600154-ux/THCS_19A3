n = int(input("Nhap so sinh vien: "))
d = {}

for i in range(n):
    ten = input()
    diem = int(input())
    d[ten] = diem

ket_qua = {}

for ten in d:
    diem = d[ten]
    if diem in ket_qua:
        ket_qua[diem].append(ten)
    else:
        ket_qua[diem] = [ten]

print(ket_qua)