# pytesseract 0.1.6

###  sudo pip install pytesseract 
### sudo apt-get install python-imaging
### sudo apt install tesseract-ocr


def main():
  import Image
  import pytesseract
  print pytesseract.image_to_string(Image.open('test.png'))
