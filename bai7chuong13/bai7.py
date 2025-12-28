import os

# Tên thư mục gốc
root = "my_project"

# 1. Tạo các thư mục
os.makedirs(os.path.join(root, "src"), exist_ok=True)
os.makedirs(os.path.join(root, "docs"), exist_ok=True)
os.makedirs(os.path.join(root, "data"), exist_ok=True)

# 2. Tạo các tập tin rỗng
open(os.path.join(root, "src", "main.py"), "w").close()
open(os.path.join(root, "docs", "README.md"), "w").close()
open(os.path.join(root, "data", "input.txt"), "w").close()

# 3. In ra cấu trúc thư mục vừa tạo
print("Cấu trúc thư mục:")
for folder in os.listdir(root):
    print("-", folder)
    path = os.path.join(root, folder)
    if os.path.isdir(path):
        for file in os.listdir(path):
            print("   +", file)
