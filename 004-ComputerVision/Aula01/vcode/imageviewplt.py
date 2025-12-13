import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread('face.jpg')
#converter bgr para rgb
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)


plt.imshow(imagem_rgb)
plt.show()