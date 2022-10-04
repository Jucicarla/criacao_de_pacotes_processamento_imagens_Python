from skimage.transform import resize

def resize_image(image, proportion):
    assert 0<= proportion <= 1, "Specify a valid proportion"
    heigth = round(image.shape[0] * proportion)
    width = round(image.shape[1] * proportion)
    image_resized = resize(image, (heigth, width), anti_aliasing=True)
    return image_resized