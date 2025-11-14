gia_san_pham = float(input("Nhập giá sản phẩm (VNĐ): "))
so_luong = int(input("Nhập số lượng mua: "))

tong_chi_phi_ban_dau = gia_san_pham * so_luong
thue_vat = tong_chi_phi_ban_dau * 0.1
tong_tien_phai_tra = tong_chi_phi_ban_dau + thue_vat

tong_tien_lam_tron = round(tong_tien_phai_tra, 2)

print(f"Tổng tiền phải trả (đã làm tròn): {tong_tien_lam_tron} VNĐ")