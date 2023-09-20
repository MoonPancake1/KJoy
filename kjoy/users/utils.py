from PIL import Image
from kjoy.settings import BASE_DIR


class CustomErrorForViews():
    pass


def crop_image(img_name: str) -> bool | None:
    """
    Функция обрезает изображение до соотношения 1:1
    """
    image = Image.open(img_name)
    
    width, height = image.size
    if width == height:
        return image
    offset  = int(abs(height-width)/2)
    if width > height:
        image = image.crop([offset, 0, width-offset, height])
    else:
        image = image.crop([0, offset, width, height-offset])

    image.convert('RGB').save(fr'{img_name}')
    return True


if __name__ == "__main__":
    ...