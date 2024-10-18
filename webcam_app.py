import cv2

#Define o comando para salvar a imagem
imgcapture = cv2.VideoCapture(0)

#Testar se a câmera foi inicializada corretamente
result = True 

#Capturar uma imagem e salvar
while(result):
    ret, frame = imgcapture.read()
    cv2.imwrite("teste.jpg", frame)
    result = False
    print("Imagem Capturada")

#Fechar a câmera
imgcapture.release() 

