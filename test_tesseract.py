import pytesseract
import os

# Update this path to match your actual Tesseract installation location
tesseract_path = r'D:\AI models\teceract\tesseract.exe'

print("Current Tesseract path:", pytesseract.pytesseract.tesseract_cmd)
print("Path exists:", os.path.exists(pytesseract.pytesseract.tesseract_cmd))

pytesseract.pytesseract.tesseract_cmd = tesseract_path
print("Updated Tesseract path:", pytesseract.pytesseract.tesseract_cmd)
print("Path exists:", os.path.exists(pytesseract.pytesseract.tesseract_cmd))

try:
    print("Tesseract version:", pytesseract.get_tesseract_version())
except Exception as e:
    print("Error:", str(e))
