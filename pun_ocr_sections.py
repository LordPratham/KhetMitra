import cv2
import pytesseract
from pytesseract import Output
from PIL import Image
import numpy as np

# Path to the image file
image_path = 'pdf_ss.png'

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'  # Adjust this path if necessary

# Load the image using OpenCV
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform thresholding to prepare for contour detection
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Find contours to detect sections
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Function to extract text from a section
def extract_text_from_section(section):
    # Convert section to PIL image
    pil_image = Image.fromarray(section)
    # Perform OCR
    text = pytesseract.image_to_string(pil_image, lang='pan')
    return text

# Iterate through the contours and extract text from each section
extracted_text = ""
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    # Skip small contours that are likely to be noise or images
    if w > 50 and h > 50:
        section = image[y:y+h, x:x+w]
        section_text = extract_text_from_section(section)
        extracted_text += section_text + "\n\n"

# Save the extracted text to a file
with open("pdf_ss.txt", "w", encoding="utf-8") as f:
    f.write(extracted_text)

print("OCR completed and text saved.")
