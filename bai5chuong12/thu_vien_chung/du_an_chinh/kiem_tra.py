
thu_vien_path = os.path.abspath("../thu_vien_chung")
sys.path.append(thu_vien_path)

from xu_ly_so import kiem_tra_so_nguyen_to

so = 17

if kiem_tra_so_nguyen_to(so):
    print(so, "là số nguyên tố")
else:
    print(so, "không phải là số nguyên tố")
