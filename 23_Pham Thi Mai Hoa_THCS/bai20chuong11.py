n = int(input("Nhap so cap key-value: "))
d = {}

for i in range(n):
    key = input("Nhap key: ")
    value = int(input("Nhap value: "))
    d[key] = value

ket_qua = {}

for k in d:
    if d[k] > 50:
        ket_qua[k] = d[k]

print("Cac cap key-value co gia tri > 50:")
print(ket_qua)
