nam = int(input("Nhập một năm: "))

if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
    ket_qua = "là năm nhuận"
else:
    ket_qua = "không phải là năm nhuận"

print(f"Năm {nam} {ket_qua}.")