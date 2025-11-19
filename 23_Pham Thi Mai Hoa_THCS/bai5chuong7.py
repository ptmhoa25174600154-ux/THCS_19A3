so_tien_gui = float(input("Nhập số tiền gửi ban đầu (VNĐ): "))
lai_suat_nam_phan_tram = float(input("Nhập lãi suất hàng năm (%): "))
lai_suat_nam = lai_suat_nam_phan_tram / 100

lai_1_thang = so_tien_gui * (lai_suat_nam / 12)
lai_2_quy = so_tien_gui * (lai_suat_nam / 4) * 2
lai_3_nam = so_tien_gui * lai_suat_nam * 3

print(f"Tiền lãi sau 1 tháng: {round(lai_1_thang, 2)} VNĐ")
print(f"Tiền lãi sau 2 quý: {round(lai_2_quy, 2)} VNĐ")
print(f"Tiền lãi sau 3 năm: {round(lai_3_nam, 2)} VNĐ")