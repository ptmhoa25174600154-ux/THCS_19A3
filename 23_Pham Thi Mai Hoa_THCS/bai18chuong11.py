n = int(input("Nhap so cap key-value: "))
d = {}
d_nguoc = {}

for i in range(n):
    key = input()
    value = input()
    d[key] = value

for k in d:
    d_nguoc[d[k]] = k

print(d_nguoc)
