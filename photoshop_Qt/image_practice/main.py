from PIL import Image, ImageFilter, ImageEnhance

with Image.open("selfie_1.jpg") as picture:
    picture.show()

    black_white = picture.convert("L")
    black_white.save("gray.jpg")

    mirror = picture.transpose(Image.FLIP_LEFT_RIGHT)
    mirror.save("mirror.jpg")

    blur = picture.filter(ImageFilter.BLUR)
    blur.save("blur.jpg")

    contrast = ImageEnhance.Contrast(picture)
    contrast = contrast.enhance(2.5)
    contrast.save("contrast.jpg")

    color = ImageEnhance.Color(picture).enhance(2.5)
    color.save("color.jpg")
