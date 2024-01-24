# editing images and enhancing using pillow
from PIL import Image, ImageEnhance, ImageFilter
import os


path = './image'
pathOut= './edited_image'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    factor = 1.5
    edit = img.filter(ImageFilter.SHARPEN) #convert 'L' rotate (-90)
    enhancer= ImageEnhance.Contrast(edit)
    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathOut}/{clean_name}_edited.jpg')

# path = './image'
# pathOut = './edited_image'

# for filename in os.listdir(path):
#     img = Image.open(f"{path}/{filename}")

#     edit = img.filter(ImageFilter.SHARPEN) #.convert('L').rotate(-90)

#     factor = 1.5
#     enhancer = ImageEnhance.Contrast(edit)
#     edit = enhancer.enhance(factor)


#     clean_name = os.path.splitext(filename)[0]

#     edit.save(f'{pathOut}/{clean_name}_edited.jpg')
