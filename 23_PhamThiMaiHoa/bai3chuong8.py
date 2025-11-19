import math

tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))

ucln = math.gcd(tu, mau)

print("Phân số tối giản:", tu // ucln, "/", mau // ucln)
