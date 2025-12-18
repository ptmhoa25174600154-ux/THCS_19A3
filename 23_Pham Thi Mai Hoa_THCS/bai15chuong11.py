n = int(input("Nhap so phan tu tuple: "))
t = ()

for i in range(n):
    t = t + (int(input()),)

chan = ()
le = ()
tong_chan = 0
tong_le = 0

for x in t:
    if x % 2 == 0:
        chan = chan + (x,)
        tong_chan += x
    else:
        le = le + (x,)
        tong_le += x

print("Tuple chan:", chan)
print("Tong chan:", tong_chan)
print("Tuple le:", le)
print("Tong le:", tong_le)
