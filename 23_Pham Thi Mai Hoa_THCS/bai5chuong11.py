n = int(input("Nhap so phan tu: "))
a = []

for i in range(n):
    a.append(int(input()))

b = []

for x in a:
    trung = False
    for y in b:
        if x == y:
            trung = True
            break
    if not trung:
        b.append(x)

print(b)
