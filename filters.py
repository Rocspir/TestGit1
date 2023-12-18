from PIL import Image

class Filters:
    def apply_to_pixel(self, pixel: int):
        pass

    def apply_to_image(self, img: Image.Image):
        for i in range(img.width):
            for j in range(img.height):
                value = img.getpixel((i, j))
                new_value = self.apply_to_pixel(value)
                img.putpixel((i, j), int(new_value))
        return img


class BrightFilter(Filters):
    def apply_to_pixel(self, pixel: int):
        pixel = pixel + 100
        return pixel


class DrakFilter(Filters):
    def apply_to_pixel(self, pixel: int):
        pixel = pixel - 100
        return pixel


class InverseFilter(Filters):
    def apply_to_pixel(self, pixel: int):
        pixel = 255 - pixel
        return pixel