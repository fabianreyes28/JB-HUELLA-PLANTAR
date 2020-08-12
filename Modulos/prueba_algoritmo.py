from scipy.spatial.distance import euclidean
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2
import copy
from PIL import Image 

medida_ref=3.1
print("llego la medida de referencia 3=",medida_ref)
print("medir_imagen")
#img1=cv2.imread("fabian.png")
img1=cv2.imread("Temporal_hsv.png")
cv2.imshow("1",img1)
kernel = np.ones((3,3),np.uint8)  
opening = cv2.morphologyEx(img1,cv2.MORPH_OPEN,kernel)                           #apertura =elimina ruido externo. Útil para eliminar objetos pequeños
closing = cv2.morphologyEx(opening,cv2.MORPH_CLOSE,kernel)                      #clausura =elimina ruido interno, elimina puntos negro en la imagen. Útil para eliminar pequeños agujeros (regiones oscuras).
erosion = cv2.erode(closing,kernel,iterations = 1)                              #erosion= elimina ruidos blancos, erosiona los límites del objeto en primer plano, el grosor o el tamaño del objeto en primer plano disminuye o simplemente disminuye la región blanca en la imagen
dilation = cv2.dilate(erosion,kernel,iterations = 1)                            #dilatación= Es justo lo opuesto a la erosión,aumenta la región blanca en la imagen o aumenta el tamaño del objeto en primer plano. Es útil para unir partes rotas de un objeto
img_limpia= dilation.copy()                                                     #copiamos el resultado de las operaciones morfologicas en una nueva variable                

"""Proceso de reconocimiento de bordes """

canny = cv2.Canny(img_limpia,0, 255)     
cv2.imshow("2",canny)                                       #canny = es un algoritmo detección de bordes que utiliza varias etapas para detectar una amplia gama de bordes en las imágenes (img,umbral min,unbral max) 
alto,ancho,dimensiones=img1.shape
print('alto,ancho,dimensiones en px =',alto,ancho,dimensiones)                                   # se imprime la forma de la imaggen (matriz) (px ancho,px alto,dimensiones)    
print(len(img1))                                                                 # se imprime la longitud de la imagen (# de px de ancho)
contornos,_=cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #findContours= encuentra los contorno ya detectados con canny
mask = np.zeros(img1.shape[:], dtype="uint8") #*255                              #se crea una matriz de ceros, llamada mask con el mismo tamaño de la imagen

for c in contornos:                                                             #con el for se recorre px a px del contorno en contrado con findContours
    area=cv2.contourArea(c)                                                     #se calcula el area los contornos
    if area>2500:                                                               #si  el. area es mayor de 3000 es dibujada                    
        
        cv2.drawContours(img_limpia,[c],-1,(255,255,255),1)                     #se dibujan los contornos internos de color blanco(255,255,255) y grosor  de 2px
        
    elif area<2499:                                                             #las areas menjores a 3000 se les aplica la mascara
        img_limpia = mask             
cv2.imshow("3",img_limpia)
edged = cv2.Canny(img_limpia, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)                                              # toma el valor de tupla apropiado en función de si estamos utilizando OpenCV 2.4, 3 o 4.

# Ordenar contornos de izquierda a derecha ya que el contorno más a la izquierda es un objeto de referencia
(cnts, _) = contours.sort_contours(cnts)

# Eliminar contornos que no sean lo suficientemente grandes
cnts = [x for x in cnts if cv2.contourArea(x) > 100]

# Dimensiones del objeto de referencia

ref_object = cnts[0]
box = cv2.minAreaRect(ref_object)
box = cv2.boxPoints(box)
print("box=",box) #encuentra los puntos
box = np.array(box, dtype="int")
box = perspective.order_points(box)
(tl, tr, br, bl) = box #ordena en sentido de izq superior, derecha superior, derecha inferior, izquierda inferior
print(tl, tr, br, bl) 
dist_in_pixel = euclidean(tl, tr)
dist_in_cm = medida_ref
pixel_per_cm = dist_in_pixel/dist_in_cm
i=0 
ancho= []
alto=[]
esquinas=[]
contornos=[]
# Dibuja los contornos que quedaron
for cnt in cnts:
    i=0
    box = cv2.minAreaRect(cnt)  #calcula el area del contorno --Box en 2D que contiene los siguientes detalles: (centro (x, y), (ancho, alto), ángulo de rotación)
    box = cv2.boxPoints(box)    #saca los puntos de las esquinas -- para dibujar este rectángulo, necesitamos 4 esquinas del rectángulo.
    box = np.array(box, dtype="int") #transforma todo  a entero
    box = perspective.order_points(box) #ordena los puntos en sentido de las manecillas del reloj
    (tl, tr, br, bl) = box
    contornos.append(box)
    esquinas.append(box.astype("int"))
    print("tl, tr, br, bl=",tl, tr, br, bl)
    cv2.drawContours(img_limpia, [box.astype("int")], -1, (0, 0, 255), 1)
#        mid_pt_horizontal = (tl[0] + int(abs(tr[0] - tl[0])/2), tl[1] + int(abs(tr[1] - tl[1])/2))
#        mid_pt_verticle = (tr[0] + int(abs(tr[0] - br[0])/2), tr[1] + int(abs(tr[1] - br[1])/2))
    wid =euclidean(tl, tr)/pixel_per_cm
    ancho.append(wid)
    print("wid=",wid)
    ht = euclidean(tr, br)/pixel_per_cm
    alto.append(ht) 
    print("altos=",ht)
                    
#    cv2.putText(img_limpia, "{:.1f}cm".format(wid), (int(mid_pt_horizontal[0] - 15), int(mid_pt_horizontal[1] - 10)), 
#    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
#    cv2.putText(img_limpia, "{:.1f}cm".format(ht), (int(mid_pt_verticle[0] + 10), int(mid_pt_verticle[1])), 
#    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

print("esquinas=",esquinas)

print("estos son los contornos=",contornos)

box0=contornos[0]
box1=contornos[1]
box2=contornos[2]

print('box0=', box0)
print('box1=', box1)
print('box2=', box2)
#        
x1,y1=box1[1]
x2,y2=box1[2]
img_linea = np.array(cv2.line(img_limpia,(x1,y1),(x2,y2),(0,255,0),1))  

xx1,yy1=box2[0]
xx2,yy2=box2[3]
img_linea = np.array(cv2.line(img_limpia,(xx2,yy2),(xx1,yy1),(0,255,255),1)) 

#cv2.imshow('imagen limpia', img_limpia)
cv2.imwrite("rectangulos.png",img_limpia )

""""Empieza el calculo de las medidas fundamentales"""

rectangulos = Image.open('rectangulos.png')                                     #se lee la imagen con la libreria Pillow
datos = list(rectangulos.getdata())                                             #aqui guardamos en una lista los colores de cada  px de la forma (b,g,r)
pixels = rectangulos.load()                                                     #load Asigna almacenamiento para la imagen y carga los datos de píxeles.           
width, height = rectangulos.size                                                #size nos arroja el ancho y alto de la imagen en px
ancho=width
alto=height
img_limpia2=img_limpia.copy()

"""pie izquierdo"""

verde=(0,255,0)
blanco =(255,255,255)
i =1 
for y in range(alto):                                                         #recorrido de rectangulos para hallar las medidas fundamentales
    for x in range(ancho):
        r, g, b = pixels[x, y]
        #-rectangulo 1 rojo-#
        if (r, g, b) == verde:
            if  i==1:
                #guardar estas posiciones en un array
                R_xx2=copy.copy(x)
                R_yy2=copy.copy(y)
                R_xx3=R_xx2-2
                r2, g2, b2 = pixels[R_xx3, R_yy2]
                #print(f'verde x2= {R_xx3} y2={R_yy2}')
                if (r2, g2, b2) == blanco:
                    #pixels[x, y] = (255, 255,255)
                    print("medida fundamental =",x,y)
                    x1 , y1 =box1[1]
                    print("x1,y1=",x1,y1)        
                    mfxx1=int(x - x1)
                    mfyy1=int(y - y1)
                    
                    print('mfxx1,mfyy1=',mfxx1,mfyy1)
                    x0 , y0 =box1[0]
                    x0mf=int(x0+mfxx1)
                    y0mf=int(y0+mfyy1)
                    
                    print('x0mf,y0mf=',x0mf,y0mf)
#                    blanco=(255,255,255)
                    cv2.line(img_limpia2,(x,y),(x0mf,y0mf),(255,0,0),1)        #mf azul

                    mfxxx1=x+mfxx1
                    mfyyy1=y+mfyy1
                    
                    print("medida fundamental 2 por derecha=",mfxxx1,mfyyy1)
                    x0mf2=int(x0mf+mfxx1)
                    y0mf2=int(y0mf+mfyy1)
                    print("medida fundamental 2 por izquierda=",x0mf2,y0mf2)
                    cv2.line(img_limpia2,(mfxxx1,mfyyy1),(x0mf2,y0mf2),(255,255,100),1) #mf 
                    i=i+1 


"""pie derecho"""
print("pied derecho")
ii=1
#        amarillo=(255,255,0) #amarillo BGR
for y in range(alto):                                                         #recorrido de rectangulos para hallar las medidas fundamentales
    for x in range(ancho):
        r, g, b = pixels[x, y]
        #-rectangulo 1 rojo-#
        if (r, g, b) == (255,255,0):  
                      
            if  ii==1:
                #guardar estas posiciones en un array
                R_xx2=copy.copy(x)
                R_yy2=copy.copy(y)
                R_xx3=R_xx2+2
                r2, g2, b2 = pixels[R_xx3, R_yy2]
                #print(f'verde x2= {R_xx3} y2={R_yy2}')
                if (r2, g2, b2) == blanco:
                    #pixels[x, y] = (255, 255,255)
                    print("medida fundamental  del cuadro 2=",x,y)
                    x1 , y1 =box2[0]
                    print("x1,y1=",x1,y1)        
                    mfxx1=int(x-x1)
                    mfyy1=int(y - y1)
                    print('DISTANCIA mfxx1,mfyy1=',mfxx1,mfyy1)
                    x0 , y0 =box2[1]
                    x0mf=int(x0+mfxx1)
                    y0mf=int(y0+mfyy1)
                    
                    print('x0mf,y0mf=',x0mf,y0mf)
#                    blanco=(255,255,255)
                    cv2.line(img_limpia2,(x,y),(x0mf,y0mf),(255,0,0),1)        #mf azul

                    mfxxx1=x+mfxx1
                    mfyyy1=y+mfyy1
                    
                    print("medida fundamental 2 por derecha=",mfxxx1,mfyyy1)
                    x0mf2=int(x0mf+mfxx1)
                    y0mf2=int(y0mf+mfyy1)
                    print("medida fundamental 2 por izquierda=",x0mf2,y0mf2)
                    cv2.line(img_limpia2,(mfxxx1,mfyyy1),(x0mf2,y0mf2),(255,255,120),1) #mf fucsia
                    ii=ii+1 

                    
                    
                    """Medios pies"""
#        print("imagen procesada con cedula= ",cedula)                    
#        
#        cv2.imwrite("../Imagenes_Huellas/Muestras_procesada/%d.png"%cedula,img_limpia2)
cv2.imwrite("rectangulos.png",img_limpia2 )
cv2.imshow("4",img_limpia2)
rectangulos = Image.open('rectangulos.png')                                     #se lee la imagen con la libreria Pillow
datos = list(rectangulos.getdata())                                             #aqui guardamos en una lista los colores de cada  px de la forma (b,g,r)
pixels = rectangulos.load()                                                     #load Asigna almacenamiento para la imagen y carga los datos de píxeles.           
width, height = rectangulos.size                                                #size nos arroja el ancho y alto de la imagen en px
ancho=width
alto=height
blanco =(255,255,255)
"""medio pie Izq"""
j=1
medio_pie_izq=[]
for y in range(alto):                                                         #recorrido de rectangulos para hallar las medidas fundamentales
    for x in range(ancho):
        r, g, b = pixels[x, y]
        
        #-rectangulo 1 rojo-#
        if (r, g, b) == (100,255,255):  
            if  j==1:
                
                #guardar estas posiciones en un array
                R_xx2=copy.copy(x)
                R_yy2=copy.copy(y)
                R_yy3=R_yy2-1
                r2, g2, b2 = pixels[R_xx2, R_yy3]
                #print("R_xx2,R_yy3",R_xx2,R_yy3)

                if (r2, g2, b2) == (255,255,255):
                    #pixels[x, y] = (255, 255,255)
                    print("este es un punto=",x,y)
                    medio_pie=[]
                    medio_pie.append(x)
                    medio_pie.append(y)
                    medio_pie_izq.append(medio_pie)
print(" ")
print("medio_pie=",medio_pie_izq)
largo_pie_izquierdo=euclidean(box1[0], box1[3])/pixel_per_cm
largo_pie_izquierdo=round(largo_pie_izquierdo,2)

ancho_pie_izq=euclidean(box1[0], box1[1])/pixel_per_cm
ancho_pie_izq=round(ancho_pie_izq,2)

ancho_medio_pie_izq = euclidean(medio_pie_izq[0], medio_pie_izq[1])/pixel_per_cm
ancho_medio_pie_izq=round(ancho_medio_pie_izq,2)

HC1=(ancho_pie_izq-ancho_medio_pie_izq)/ancho_pie_izq
HC1=HC1*100
HC1=round(HC1,2)

print("HC:",HC1)
print("largo_pie_izquierdo=",largo_pie_izquierdo)
print("ancho_pie_izq=",ancho_pie_izq)
print("ancho_medio_pie_izq=",ancho_medio_pie_izq)
print(" ")

resul_izq="Largo:"+str(largo_pie_izquierdo) + " cm \n"
resul_izq2="Ancho del pie:"+str(ancho_pie_izq) + " cm \n"
resul_izq3="Ancho del medio pie:"+str(ancho_medio_pie_izq) + " cm \n"
resul_izq4="HC:"+str(HC1) + " % \n"
tipo_pie="tipo :  "
if HC1>=0 and HC1<=34.99:
    print("pie plano")
    tipo_pie=" pie plano"
elif HC1>35 and HC1<=39.99:
    print("pie plano/normal")
    tipo_pie="pie plano/normal"
elif HC1>=40 and HC1<=54.99:
    print("pie normal")
    tipo_pie="pie normal"
elif HC1>=55 and HC1<=59.99:
    print("pie normal")
    tipo_pie="pie normal"
elif HC1>=60 and HC1<=74.99:
    print("pie cavo")
    tipo_pie="pie cavo"
elif HC1>=75 and HC1<=84.99:
    print("pie cavo fuerte")
    tipo_pie="pie cavo fuerte"
elif HC1>=85 and HC1<=100:
    print("pie cavo extremo")
    tipo_pie="pie cavo extremo"
#    
#self.textEdit_izq1.setText(resul_izq )
#self.textEdit_izq2.setText(resul_izq2)
#self.textEdit_izq3.setText(resul_izq3)
#self.textEdit_izq4.setText(resul_izq4 + tipo_pie)



"""medio pie Derecho"""
jj=1
medio_pie_derecho=[]
for y in range(alto):                                                         #recorrido de rectangulos para hallar las medidas fundamentales
    for x in range(ancho):
        r, g, b = pixels[x, y]
        
        #-rectangulo 1 rojo-#255,255,120
        if (r, g, b) == (120,255,255):  
            if  jj==1:
                
                #guardar estas posiciones en un array
                R_xx2=copy.copy(x)
                R_yy2=copy.copy(y)
                R_yy3=R_yy2-1
                r2, g2, b2 = pixels[R_xx2, R_yy3]
                #print("R_xx2,R_yy3",R_xx2,R_yy3)

                if (r2, g2, b2) == (255,255,255):
                    #pixels[x, y] = (255, 255,255)
                    print("este es un punto=",x,y)
                    medio_pie=[]
                    medio_pie.append(x)
                    medio_pie.append(y)
                    medio_pie_derecho.append(medio_pie)

print("medio_pie_derecho=",medio_pie_derecho)
largo_pie_derecho=euclidean(box2[0], box2[3])/pixel_per_cm
largo_pie_derecho=round(largo_pie_derecho,2)

ancho_pie_derecho=euclidean(box2[0], box2[1])/pixel_per_cm
ancho_pie_derecho=round(ancho_pie_derecho,2)

ancho_medio_pie_derecho = euclidean(medio_pie_derecho[0], medio_pie_derecho[1])/pixel_per_cm
ancho_medio_pie_derecho=round(ancho_medio_pie_derecho,2)

HC=(ancho_pie_derecho-ancho_medio_pie_derecho)/ancho_pie_derecho
HC=HC*100
HC=round(HC,2)
       

print("HC=",HC)
print("largo_pie_derecho=",largo_pie_derecho)
print("ancho_pie_derecho=",ancho_pie_derecho)
print("ancho_medio_pie_derecho=",ancho_medio_pie_derecho)

resul_dere="Largo:"+str(largo_pie_derecho) + " cm \n"
resul_dere2="Ancho del pie:"+str(ancho_pie_derecho) + " cm \n"
resul_dere3="Ancho del medio pie:"+str(ancho_medio_pie_derecho) + " cm \n"
resul_dere4="HC:"+str(HC) + " % \n"


tipo_pie2="tipo :  "
if HC>=0 and HC<=34.99:
    print("pie plano")
    tipo_pie2=" pie plano"
elif HC>35 and HC<=39.99:
    print("pie plano/normal")
    tipo_pie2="pie plano/normal"
elif HC>=40 and HC<=54.99:
    print("pie normal")
    tipo_pie2="pie normal"
elif HC>=55 and HC<=59.99:
    print("pie normal")
    tipo_pie2="pie normal"
elif HC>=60 and HC<=74.99:
    print("pie cavo")
    tipo_pie2="pie cavo"
elif HC>=75 and HC<=84.99:
    print("pie cavo fuerte")
    tipo_pie2="pie cavo fuerte"
elif HC>=85 and HC<=100:
    print("pie cavo extremo")
    tipo_pie2="pie cavo extremo"
    

#self.textEdit_dere1.setText(resul_dere )
#self.textEdit_dere2.setText(resul_dere2)
#self.textEdit_dere3.setText(resul_dere3)
#self.textEdit_dere4.setText(resul_dere4 + tipo_pie2)
#

#cv2.imshow("imagen limpia2", img_limpia2)





cv2.waitKey(0)
cv2.destroyAllWindows()