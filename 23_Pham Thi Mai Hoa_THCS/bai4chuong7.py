so_tien_vnd = float(input("Nhập số tiền bằng VNĐ: "))
ty_gia = 24500

so_tien_usd = so_tien_vnd / ty_gia
so_tien_usd_lam_tron = round(so_tien_usd, 2)

print(f"Số tiền sau khi chuyển đổi sang USD là: {so_tien_usd_lam_tron} USD")