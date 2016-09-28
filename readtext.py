def main():
  import Image
  import pytesseract
  print pytesseract.image_to_string(Image.open('test.png'))

def test1():
  import Image
  import pytesseract
  print pytesseract.image_to_string(Image.open('bill.jpg'))
  #test