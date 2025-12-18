n = int(input("Nhap so cap key-value: "))
d = {}

for i in range(n):
    key = input("Nhap key: ")
    value = int(input("Nhap value: "))
    d[key] = value

dau_tien = True

for k in d:
    if dau_tien:
        key_lon_nhat = k
        gia_tri_lon_nhat = d[k]
        dau_tien = False
    else:
        if d[k] > gia_tri_lon_nhat:
            gia_tri_lon_nhat = d[k]
            key_lon_nhat = k

print("Key co gia tri lon nhat:", key_lon_nhat)
