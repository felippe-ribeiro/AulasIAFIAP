import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread('face.jpg')

inicio = (900, 50)
fim = (2200, 1600)
cor = (255,0,0) #Blue em BGR
espessura = 20
#retangulo na copia da imagem
imagem_com_retangulo = cv2.rectangle(imagem.copy(), inicio, fim, cor, espessura)

#converter para rgb
imagem_rgb = cv2.cvtColor(imagem_com_retangulo, cv2.COLOR_BGR2RGB)


plt.imshow(imagem_rgb)
plt.axis('off')
plt.show()