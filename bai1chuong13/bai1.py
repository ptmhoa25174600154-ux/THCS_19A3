file = open("vanban.txt", "r", encoding="utf-8")
noi_dung = file.read()
file.close()

cac_tu = noi_dung.split()
so_tu = len(cac_tu)

print("Nội dung văn bản:")
print(noi_dung)
print("Tổng số từ:", so_tu)