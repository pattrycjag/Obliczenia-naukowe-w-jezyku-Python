from PIL import Image

image_path = "image.jpg"
image = Image.open(image_path)

print("Mode:", image.mode)
print("Size:", image.size)
print("Format:", image.format)

thumbnail_size = (128, 128)
image.thumbnail(thumbnail_size)

thumbnail_path = "thumbnail.jpg"
image.save(thumbnail_path)
