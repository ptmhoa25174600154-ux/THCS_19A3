ten_dang_nhap = input("Nhập tên đăng nhập: ")
mat_khau = input("Nhập mật khẩu: ")

if ten_dang_nhap == "admin" and mat_khau != "password123":
    thong_bao = "Được cấp quyền truy cập"
else:
    thong_bao = "Không được cấp quyền truy cập"

print(thong_bao)