from cv2 import cv2 
import glob
import numpy as np

images = []
cont = 0
posicao = (10,25)
dim = (512,512)

watermark = cv2.imread("data/logo.png",cv2.IMREAD_UNCHANGED)
lH,lW = watermark.shape[:2]

def cutname(string):
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
    n = cv2.addWeighted(ovr,0.3,final,1.0,0,final)
    n = cv2.copyMakeBorder(n,40,10,10,10,cv2.BORDER_CONSTANT,value=[255,255,255]) 
    n = cv2.resize(n,dim)   
    n = cv2.putText(n,cutname(img),posicao, 1, 2, 0)
    images.append(n)

ind  = 0
i=1
j=0
while True:       
   img = images[ind]
    for contador in range(11):           
            i+=0.10
            j-=0.10
            n = cv2.addWeighted(img,i,img2,j,1)
            cv2.imshow('Img',n)
            cv2.waitKey(100)
        i=1
        j=0    
        cv2.waitKey(1000)
   cv2.imshow("Fotos", img)
   cv2.waitKey(5000)
   cv2.addWeighted()
   ind+=1
   if cv2.waitKey(1) & 0xFF == ord('q'):
    break 
   if cv2.waitKey(1) & 0xFF == ord('Q'):
    break     
   #if i == 4:
    #i=0   
    #if cv2.waitKey(1) & 0x44 == ord('d'):
     #  i+=1      
    #if cv2.waitKey(1) & 0x41 == ('a'):
     #  i-=1      
    
    

cv2.waitKey()

cv2.destroyAllWindows()

#(COMPLETO) Mostre imagens contidas somente em um diretório. (1 ponto)
#(COMPLETO) Finalizar a aplicação somente quando o usuário teclar 'q' ou 'Q'. (1 ponto).
#(COMPLETO) No diretório pode ter imagens de diferente tamanhos, mas na tela as imagens devem ser apresentadas na resolução 512 x 512 (Dica o cropping ou resize da imagem) (2 pontos).
#(COMPLETO) Trocar de imagem a cada 5 segundos (1 ponto).
#(COMPLETO) Colocar uma borda da cor branca na imagem apresentada de tamanho 10x10x10x40. A margem de tamanho 40 deve ficar no topo (1 ponto).
#(COMPLETO) Escrever dentro da borda do topo o nome da imagem (1 ponto).
#(COMPLETO) Colocar um marca d'água no canto inferior da imagem e fora da borda (1 ponto).
#Aplique uma transição entre uma image e outra (Dica: veja a função  cv2.addWeighted) (1 ponto). 
#Ao teclar seta para direita ou esquerda, avançar para a próxima imagem ou retroceder para a imagem anterior (1 ponto)