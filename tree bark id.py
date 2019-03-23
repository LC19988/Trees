import cv2
import math
import numpy as np 
#variables
rl=0
rh=100
gl=0
gh=70
bl=0
bh=80
mean=[]
oks=0
#importo l'immagine
first = cv2.imread('C:\\Users\\Luisa\\Downloads\\greenview\\treetest\\trees8.jpg') 
#acquisisco alcune info sulle dimensioni   
rows,cols=first.shape[:2]
size=int(cols/50)
width=round(cols/size)
length=round(rows/size)
print(length,width)
i=0
#suddivido l'immagine in riquadri piÃ¹ piccoli per analizzarne il valore medio (colore)
for n in range(size):
	for k in range(size):
		new=first[k*length:(k+1)*length,n*width:(n+1)*width]
		meanval=cv2.mean(new)
		#calcolo la media del colore per ogni riquadro
		color=meanval[0:3]
		#cv2.line(first,(n*width,k*length),((n+1)*width,k*length),(255,0,0),1)
		#cv2.line(first,(n*width,k*length),(n*width,(k+1)*length),(255,0,0),1)
		#print("parametri",n,k,color)
		#creo un vettore con tutte le medie
		mean.append(meanval)
		#se la media rientra in valori che comprendono il colore cercato ricoloro il riquadro
		if ((bl<meanval[0]<bh)and(gl<meanval[1]<gh)and(rl<meanval[2]<rh)):
			#cv2.line(first, (n*68,k*45),((n+1)*68,(k+1)*45),(255,255,255),20)
			#print(meanval)
			#cv2.imshow("img",new)
			#cv2.waitKey(0)
			new[:,:]=(0,255,0)
			#stampo i valori significativi
			#print("there we go",meanval,n,k)
			i=i+1
			#cv2.imshow("img",new)
			#cv2.waitKey(0)
#print(i)

cv2.imshow("img",first)
cv2.waitKey(0)
cv2.imwrite('C:\\Users\\Luisa\\Downloads\\greenview\\treetest\\newim.jpg',first)