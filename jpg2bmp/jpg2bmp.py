
from PIL import Image

names = ["001", "002", "003", "004", "005", "006"]


for name in names:
    im = Image.open(name + ".jpg").convert("RGB")
    im.save(name + ".bmp")
    print("output: " + name + ".bmp")

print("Done!")
