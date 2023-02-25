import os

from PIL import Image
from pillow_heif import register_heif_opener

list_of_files = os.listdir("photo/")
dir = "photo/"

for name_of_file in list_of_files:
    path = dir + name_of_file

    if name_of_file.split(".")[-1] in ["jpg", "jpeg"]:
        continue
    if name_of_file.split(".")[-1] == "heif":
        register_heif_opener()
        print(name_of_file + " - Перетворення виконано")
        with Image.open(path) as file:
            new_file_name = name_of_file.split(".")[0] + ".jpg"
            end_path = f"photo/{new_file_name}"
            file.convert("RGB").save(end_path, "jpeg")
        os.remove(path)
    else:
        print(name_of_file + " - Перетворення виконано")
        with Image.open(path) as file:
            new_file_name = name_of_file.split(".")[0] + ".jpg"
            end_path = f"photo/{new_file_name}"
            file.convert("RGB").save(end_path, "jpeg")
        os.remove(path)

