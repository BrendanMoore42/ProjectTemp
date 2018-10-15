from PIL import Image, ImageEnhance, ImageFilter
import pytesseract as pt

im = Image.open("carda.jpg") # the second one
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('carda1.jpg')
text = pt.image_to_string(Image.open('carda1.jpg'))
print(text)

