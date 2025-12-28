def sap_xep_tang_dan(danh_sach):
    n = len(danh_sach)
    for i in range(n):
        for j in range(i + 1, n):
            if danh_sach[i] > danh_sach[j]:
                temp = danh_sach[i]
                danh_sach[i] = danh_sach[j]
                danh_sach[j] = temp
    return danh_sach
