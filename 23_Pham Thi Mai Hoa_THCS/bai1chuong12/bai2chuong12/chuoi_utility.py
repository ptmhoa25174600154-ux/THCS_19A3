def dao_nguoc_chuoi(chuoi):
    ket_qua = ""
    for i in range(len(chuoi) - 1, -1, -1):
        ket_qua += chuoi[i]
    return ket_qua

def dem_so_tu(chuoi):
    dem = 0
    trong_tu = False

    for ky_tu in chuoi:
        if ky_tu != " ":
            if not trong_tu:
                dem += 1
                trong_tu = True
        else:
            trong_tu = False
    return dem
