can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (mét): "))

bmi = can_nang / (chieu_cao * chieu_cao)
bmi_lam_tron = round(bmi, 2)

print(f"Chỉ số BMI của bạn là: {bmi_lam_tron}")