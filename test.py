import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

# read an image
img = cv2.imread('images/neko.jpg')
img2 = cv2.imread("images/neko.jpg",0)
ret,thresh1 = cv2.threshold(img2,127,255,cv2.THRESH_BINARY)
# show image format (basically a 3-d array of pixel color info, in BGR format)
# print(img)
# print img
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
cv2.imwrite('images/neko.jpg',img)
cv2.imwrite('images/neko2.jpg',img2)
# print img2
print thresh1
cv2.imwrite('images.neko3.jpg',thresh1)
