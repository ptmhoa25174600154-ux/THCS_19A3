import csv

with open("nhan_vien.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    print("Nhân viên có lương trên 50000:")
    for dong in reader:
        luong = int(dong["Lương"])
        if luong > 50000:
            print(
                "ID:", dong["ID"],
                "- Tên:", dong["Tên"],
                "- Lương:", dong["Lương"]
            )
