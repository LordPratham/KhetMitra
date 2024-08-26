from PIL import Image
import pytesseract
import time


screenshot=r"ss.png"
img = Image.open(screenshot)
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
text = pytesseract.image_to_string(img, lang='pan')

with open("pdf_ss.txt", "w", encoding="utf-8") as f:
    f.write(text)