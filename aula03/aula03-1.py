from cv2 import cv2 
import glob
import numpy as np

images = []
cont = 0
posicao = (10,25)
dim = (512,512)

watermark = cv2.imread("data/logo.png",cv2.IMREAD_UNCHANGED)
lH,lW = watermark.shape[:2]

def cutname(string): #método para captar apenas o nome da imagem 
    start = 0
    end = 0 
    end = string.find("\\") 
    start = string.find(".")
    return  string[end+1:start]

for img in glob.glob("data/*.jpg"):
    n = cv2.imread(img)
    oH,oW = n.shape[:2]
    n = np.dstack([n, np.ones((oH,oW), dtype="uint8") * 255])
    ovr = np.zeros((oH,oW,4), dtype="uint8")
    ovr[oH - lH - 60:oH - 60, oW - lW - 10:oW - 10] = watermark
    final = n.copy()
    n = cv2.addWeighted(ovr,0.3,final,1.0,0,final) #adiciona marca d'água
    n = cv2.copyMakeBorder(n,40,10,10,10,cv2.BORDER_CONSTANT,value=[255,255,255]) #adiciona borda 
    n = cv2.resize(n,dim) #resize na imagem pra todas terem o mesmo tamnho
    n = cv2.putText(n,cutname(img),posicao, 1, 2, 0) #coloca o nome da imagem na borda
    images.append(n)

ind=0
i=1.0
j=0.0
ok=True

while ok: 

    n = images[ind]
    cv2.imshow('Img',n)

    for repete in range(3):
        cv2.waitKey(5000) #espera por 5 segundos
        if(ind<3): 
            for contador in range(5):           
                i-=0.20
                j+=0.20
                n = cv2.addWeighted(images[ind],i,images[ind+1],j,1) #aplica transição
                cv2.imshow('Img',n)
                cv2.waitKey(100)   
            ind+=1
            i=1.0
            j=0.0   

#        if cv2.waitKeyEx() == 2555904: #seta direita
#            ind+=1
#        if cv2.waitKeyEx() == 2424832:  #seta esquerda
#            ind-=1  

    if cv2.waitKey() & 0xFF == ord('q','Q'): #fecha janela ao pressionar q ou Q
        ok=False

#
cv2.destroyAllWindows()

#(COMPLETO) Mostre imagens contidas somente em um diretório. (1 ponto)
#(COMPLETO?) Finalizar a aplicação somente quando o usuário teclar 'q' ou 'Q'. (1 ponto).
#(COMPLETO) No diretório pode ter imagens de diferente tamanhos, mas na tela as imagens devem ser apresentadas na resolução 512 x 512 (Dica o cropping ou resize da imagem) (2 pontos).
#(COMPLETO) Trocar de imagem a cada 5 segundos (1 ponto).
#(COMPLETO) Colocar uma borda da cor branca na imagem apresentada de tamanho 10x10x10x40. A margem de tamanho 40 deve ficar no topo (1 ponto).
#(COMPLETO) Escrever dentro da borda do topo o nome da imagem (1 ponto).
#(COMPLETO) Colocar um marca d'água no canto inferior da imagem e fora da borda (1 ponto).
#(COMPLETO) Aplique uma transição entre uma image e outra (Dica: veja a função  cv2.addWeighted) (1 ponto). 
#Ao teclar seta para direita ou esquerda, avançar para a próxima imagem ou retroceder para a imagem anterior (1 ponto)