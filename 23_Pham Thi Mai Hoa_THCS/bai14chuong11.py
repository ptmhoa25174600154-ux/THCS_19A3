n = int(input("Nhap so phan tu A: "))
A = []
for i in range(n):
    A.append(int(input()))

m = int(input("Nhap so phan tu B: "))
B = []
for i in range(m):
    B.append(int(input()))

A_tru_B = []
B_tru_A = []
A_giao_B = []
A_hop_B = []

for x in A:
    co = False
    for y in B:
        if x == y:
            co = True
            break
    if not co:
        A_tru_B.append(x)
    else:
        A_giao_B.append(x)

for x in B:
    co = False
    for y in A:
        if x == y:
            co = True
            break
    if not co:
        B_tru_A.append(x)

for x in A:
    A_hop_B.append(x)
for x in B:
    trung = False
    for y in A:
        if x == y:
            trung = True
            break
    if not trung:
        A_hop_B.append(x)

print("A - B:", A_tru_B)
print("B - A:", B_tru_A)
print("A giao B:", A_giao_B)
print("A hop B:", A_hop_B)
