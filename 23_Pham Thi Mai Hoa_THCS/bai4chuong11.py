n = int(input("Nhap so phan tu: "))
a = []

for i in range(n):
    a.append(int(input()))

lon_nhat = None
lon_thu_hai = None

for x in a:
    if lon_nhat is None or x > lon_nhat:
        lon_thu_hai = lon_nhat
        lon_nhat = x
    elif x != lon_nhat:
        if lon_thu_hai is None or x > lon_thu_hai:
            lon_thu_hai = x

if lon_thu_hai is None:
    print("Khong co so lon thu hai")
else:
    print("So lon thu hai:", lon_thu_hai)