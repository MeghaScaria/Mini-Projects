import barcode #barcode library is used for generating barcodes
from barcode.writer import ImageWriter #ImageWriter is responsible for saving the barcode as an image file

text = "Python Programming Code"

text1 = str(text)
code  = barcode.get_barcode_class("code128") #code128 is a widely used barcode format that supports alphanumeric data (letters, numbers, and symbols).
image = code(text,writer=ImageWriter())
save_img = image.save('my final barcode')