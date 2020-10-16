import pytesseract
from PIL import Image
from gtts import gTTS
pytesseract.pytesseract.tesseract_cmd='Tesseract-OCR/tesseract.exe'
img=Image.open('img/fog.jpg')
text=pytesseract.image_to_string(img)
speech=gTTS(text)
speech.save('spek.mp3')