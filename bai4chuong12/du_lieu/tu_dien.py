def lay_gia_tri(tu_dien, khoa):
    for key in tu_dien:
        if key == khoa:
            return tu_dien[key]
    return None
