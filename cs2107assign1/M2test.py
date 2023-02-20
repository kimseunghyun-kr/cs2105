from PIL import Image

with open("./cs2107assign1/body.ppm.ecb", "rb") as f:
    data = f.read()

header = b"P6\n940 904\n255\n"
with open("image.ppm", "wb") as f:
    f.write(header)
    f.write(data)

file_name = "image.ppm"
image = Image.open(file_name)
image.show()
