# Nhập ID và giá mới
id_can_sua = input("Nhập ID sản phẩm cần cập nhật giá: ")
gia_moi = input("Nhập giá mới: ")

# Đọc toàn bộ file
file = open("san_pham.txt", "r", encoding="utf-8")
cac_dong = file.readlines()
file.close()

danh_sach_moi = []

for dong in cac_dong:
    dong = dong.strip()

    # Giữ nguyên dòng tiêu đề
    if dong.startswith("ID"):
        danh_sach_moi.append(dong)
        continue

    parts = dong.split(", ")

    if parts[0] == id_can_sua:
        dong_moi = parts[0] + ", " + parts[1] + ", " + gia_moi
        danh_sach_moi.append(dong_moi)
    else:
        danh_sach_moi.append(dong)

# Ghi lại vào file 
file = open("san_pham.txt", "w", encoding="utf-8")
for dong in danh_sach_moi:
    file.write(dong + "\n")
file.close()

print("Đã cập nhật giá sản phẩm.")
