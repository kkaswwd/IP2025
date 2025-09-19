import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('dsu2.jpg')
rows,cols,ch = img.shape
pts1 = np.float32([[178,244],[820,224],[821,514],[177,505]])
pts2 = np.float32([[0,0],[300,0],[300,500],[0,500]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
