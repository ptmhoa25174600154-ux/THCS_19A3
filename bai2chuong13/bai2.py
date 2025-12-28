file = open("vanban.txt", "r", encoding="utf-8")
noi_dung = file.read()
file.close()


cac_tu = noi_dung.split()

tan_suat = {}

for tu in cac_tu:
    tu = tu.lower().strip(",.")
    if tu in tan_suat:
        tan_suat[tu] += 1
    else:
        tan_suat[tu] = 1

print("Tần suất xuất hiện của các từ:")
for tu in tan_suat:
    print(tu, ":", tan_suat[tu])
