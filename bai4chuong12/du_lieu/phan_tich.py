from du_lieu.danh_sach import sap_xep_tang_dan
from du_lieu.tu_dien import lay_gia_tri

ds = [5, 2, 9, 1, 7]
print("Danh sách ban đầu:", ds)
print("Danh sách sau khi sắp xếp:", sap_xep_tang_dan(ds))

td = {
    "toan": 8,
    "ly": 7,
    "hoa": 9
}

print("Giá trị của khóa 'hoa':", lay_gia_tri(td, "hoa"))
