def luy_thua(co_so, so_mu):
    ket_qua = 1
    for _ in range(so_mu):
        ket_qua *= co_so
    return ket_qua

def can_bac_hai(so):
    x = so
    for _ in range(10):
        x = (x + so / x) / 2
    return x
