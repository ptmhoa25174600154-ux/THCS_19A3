luong_co_ban = float(input("Nhập mức lương cơ bản (VNĐ): "))
so_ngay_cong = int(input("Nhập số ngày công trong tháng: "))

luong_mot_ngay = luong_co_ban / 22
tong_luong = luong_mot_ngay * so_ngay_cong
tien_thuong_phat = 0

if so_ngay_cong > 22:
    tien_thuong_phat = tong_luong * 0.1
elif so_ngay_cong < 22:
    tien_thuong_phat = -tong_luong * 0.05

luong_thuc_nhan = tong_luong + tien_thuong_phat

print(f"Tổng tiền lương thực nhận của nhân viên là: {round(luong_thuc_nhan, 2)} VNĐ")