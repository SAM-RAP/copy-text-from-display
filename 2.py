import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
from PIL import Image
import clipboard


img = Image.open('image1.png')
text = tess.image_to_string(img)

clipboard.copy((text))  # now the clipboard content will be string "abc"
text = clipboard.paste()



print(text)
