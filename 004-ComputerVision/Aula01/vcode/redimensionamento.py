import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread('face.jpg')

imagem_suavizada = cv2.GaussianBlur(imagem, (15, 15), 0)


#converter em BGR em RGB
imagem_suavizada_rgb = cv2.cvtColor(imagem_suavizada, cv2.COLOR_BGR2RGB)

plt.imshow(imagem_suavizada_rgb)
plt.axis('off')
plt.show()