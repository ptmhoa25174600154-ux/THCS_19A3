# Danh sách số nguyên
ds_so = [1, 5, 10, 15, 20, 25]

# Mở file 
file = open("so_nguyen.txt", "w", encoding="utf-8")

for so in ds_so:
    file.write(str(so) + "\n")

file.close()

print("Đã ghi danh sách số nguyên vào file so_nguyen.txt")
