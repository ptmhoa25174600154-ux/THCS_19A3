s = input("Nhap chuoi: ")

chu_cai = 0
chu_so = 0
dac_biet = 0

for ch in s:
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        chu_cai += 1
    elif '0' <= ch <= '9':
        chu_so += 1
    else:
        dac_biet += 1

print("So chu cai:", chu_cai)
print("So chu so:", chu_so)
print("So ky tu dac biet:", dac_biet)