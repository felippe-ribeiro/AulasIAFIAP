import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread('face.jpg')
#converter para grayscale
imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)


#Detectar bordas
bordas = cv2.Canny(imagem_gray, 100,200)

#exibir com bordas detectadas
plt.imshow(imagem_gray, cmap='gray')
plt.axis('off') #desabilita eixos
plt.show()