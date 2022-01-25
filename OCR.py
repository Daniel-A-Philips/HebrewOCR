import os

folderPath = "/content"
myRevList = os.listdir(folderPath)
myRevList

!tesseract --list-langs
!apt-get install tesseract-ocr-heb
!tesseract --list-langs

from google.colab.patches import cv2_imshow
import cv2
for image in  myRevList:
    if not '.png' in image and not '.jpeg' in image:
      myRevList.remove(image)
      continue
    img = cv2.imread(f'{folderPath}/{image}',cv2.IMREAD_UNCHANGED)
    print(f'{folderPath}/{image}')
    cv2_imshow(img)
myRevList


import cv2
import pytesseract

corpus = []
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
for images in myRevList:
    print(f'{folderPath}/{images}')
    img = cv2.imread(f'{folderPath}/{images}')
    if img is None:
        corpus.append("Could not read the image.")
    else:
        rev = pytesseract.image_to_string(img,lang='eng+heb')
        rev = rev.split('\n')
        corpus.append(rev)

list(corpus)
corpus
