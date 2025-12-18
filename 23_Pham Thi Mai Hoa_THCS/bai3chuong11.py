s = input("Nhap chuoi: ")

ket_qua = ""
i = 0
while i < len(s):
    if s[i] != " ":
        ket_qua += s[i]
    else:
        ket_qua += " "
        while i + 1 < len(s) and s[i + 1] == " ":
            i += 1
    i += 1

print("Chuoi sau khi xu ly:")
print(ket_qua.strip())