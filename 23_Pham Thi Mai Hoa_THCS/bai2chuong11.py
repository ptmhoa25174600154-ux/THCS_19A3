s = input("Nhap chuoi: ")
n = int(input("Nhap n: "))

tu = ""
for ch in s + " ":
    if ch != " ":
        tu += ch
    else:
        if len(tu) > n:
            print(tu)
        tu = ""