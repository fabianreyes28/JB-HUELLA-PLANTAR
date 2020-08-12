#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 01:41:32 2018

@author: trio_pu
"""
from scipy.spatial.distance import euclidean
from imutils import perspective
from imutils import contours
import sys
import imutils
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
#from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import cv2
import numpy as np
####mas claro para las imagenes
from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
#from verreg import *
import cv2 
import numpy as np
font = cv2.FONT_HERSHEY_COMPLEX
from PIL import Image
import copy
from ModuloUsuario import Usuario ###se importo el usuario y contraseña de la aplicacion 
from tkinter import *
from tkinter import messagebox
import pymysql.cursors
import mysql.connector
from mysql.connector import Error
from Modulo_Guardar import Guardando
from Modulo_Buscar import Buscando
from Modulo_Exporta_Excel import Exportar_xlsx
from Guardar_pdf import Reporte_pdf
from Modulo_Algoritmo import Algoritmo
import glob # esta es una libreria para buscar archivos con la ruta
Error=Tk()   
#Error.eval('tk::PlaceWindow %s center ' % Error.winfo_toplevel())
Error.withdraw()
cedula=0 #variable de cedula de turno
medida_ref=0 #variable de objeto de referencia


#################### inicio de sesion #######################

class inicio_sesion(QMainWindow):
    def __init__(self):

        ####### con esto se carga la interfaz diseñada en Qt Designer
        super(inicio_sesion,self).__init__()
        loadUi('../Ventanas_Interfaz/login.ui', self)
        ######
        self.boton_login.clicked.connect(self.saludo)
        
    def saludo(self):
        Usuario.hola()    # debe salir el mensaje "hola gracias a Dios" en la consola, es una confirmacion del import
        if self.lineEdit_usuario.text()==Usuario.usuario and self.lineEdit_contrasena.text()==Usuario.contrasena:
            print("usuario y contraseña  correctos ")
            ##### abrir la siguiente ventana
            #self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)
            self.hide() #esta linea es para que se esconda la ventana principal cuando se desea abrir  la segunda ventana
            ventana_registro=Form_Registro(self)
            ventana_registro.show()
          
        else:
            i=0
           
            print ('SE EQUIVOCO \n')
#            messagebox.showerror("Error","Usuario o Contraseña incorrecto \n Te queda una oportunidad,  si persiste el error: '\n' El sofware se bloqueará.")
            QMessageBox.critical(self, "Error!", "Usuario o Contraseña incorrecto")
            
            return i
################ fin de inicio de sesion ##################
            
################  Inicio de registro     ##################
class Form_Registro(QMainWindow):
     
     def __init__(self,parent=None):
        super(Form_Registro, self).__init__(parent)
        loadUi('../Ventanas_Interfaz/Registro.ui', self)
        
        #botones--->>
        self.boton_guardar.clicked.connect(self.guardar)
        self.boton_siguiente.clicked.connect(self.siguiente)
        self.boton_buscar.clicked.connect(self.buscar)
        #falta boton manual
        self.boton_siguiente.setEnabled(True)   #inabilitamos el boton siguiente y se habilita en el modulo_Guardar
         
     ####------inicio prueba guardar
     def guardar(self):
         Reporte_pdf.Pdf_Registro(self)
         ######radio button #####
         if self.radioButton_macho.isChecked():
             print ("macho ha sido seleccionado")
             gen=str('masculino')
         elif self.radioButton_femina.isChecked():
             print ("femina ha sido seleccionado")
             gen=str('femenino')
         
         ####### fin de radio button  ####
         
         ########  Aqui insertamos los datos ##########
                      
         id=int(self.lineEdit_cedula.text())
         nom=str(self.lineEdit_nombre.text())
         ape=str(self.lineEdit_apellido.text())
         ##genero
         peso=float(self.lineEdit_peso.text())
         edad=int(self.lineEdit_edad.text())
         altu=float(self.lineEdit_altura.text())
         t_izq=int(self.lineEdit_talla_izq.text())
         t_dere=int(self.lineEdit_talla_dere.text())
         telf=int(self.lineEdit_telefono.text())
         ocupa=str(self.lineEdit_ocupacion.text())
         obser=str(self.textEdit_observacion.toPlainText())  ###este es diferente por que es un tex edit
         global cedula
         cedula=copy.copy(id)
         
         Guardando.guardar(self,id,nom,ape,gen,peso,edad,altu,t_izq,t_dere,telf,ocupa,obser)
         
     def buscar (self):
         
         ###
         self.hide() #esta linea es para que se esconda la ventana principal cuando se desea abrir  la segunda ventana
         ventana_buscar=Buscar(self)
         ventana_buscar.show()   
         
     def siguiente (self):
         
         #self.boton_siguiente.setEnabled(True) 
         ###
         self.hide() #esta linea es para que se esconda la ventana principal cuando se desea abrir  la segunda ventana
         ventana_camara=camara(self)
         ventana_camara.show()
         
           
###############     fin del registro    ###################
         
###############     inicio de Buscar    ###################
class Buscar (QMainWindow):
            
    def __init__(self,parent=None):
        super(Buscar, self).__init__(parent)
        loadUi('../Ventanas_Interfaz/Buscar.ui', self)
       
        
        self.boton_regresar.clicked.connect(self.Funcion_Regresar)
        self.Boton_Buscar.clicked.connect(self.Funcion_buscar)
        self.Boton_Mostrar.clicked.connect(self.Funcion_Mostar_ruta)
        self.Boton_xlsx.clicked.connect(self.Funcion_Exportar)
        
    def Funcion_Regresar(self):
        try:
            self.timer.stop()
            self.capture.release()
        except (AttributeError, FileNotFoundError):
            pass
        
        self.hide()        
        self.parent().show()
        
    def Funcion_Mostar_ruta(self):
        ruta=str(self.lineEdit_Ruta.text())
        for file in glob.glob(ruta):
            print(file)
            img= cv2.imread(file)
            #cv2.imshow('Imagen de la ruta ',img)
    def Funcion_buscar(self):
        cc=int(self.lineEdit_cc.text()) 
        Buscando.Funcion_buscando(self,cc)
    def Funcion_Exportar(self):
        Exportar_xlsx.Funcion_Exportar_xlsx(self)
       
###############     fin de buscar       ##################         
            
############### inicio de Camara      ###################

class camara (QMainWindow):
            
    def __init__(self,parent=None):
        super(camara, self).__init__(parent)
        loadUi('../Ventanas_Interfaz/camara.ui', self)
       # self.image = None
        
        self.start_button.clicked.connect(self.start_webcam)
        self.stop_button.clicked.connect(self.stop_webcam)
        self.boton_capturar.clicked.connect(self.capturar)
        self.boton_regresar.clicked.connect(self.regresar)
#        self.color2_button.clicked.connect(self.set_color2)
        
    def regresar(self):
        try:
            self.timer.stop()
            self.capture.release()
        except (AttributeError, FileNotFoundError):
            pass
        
        self.hide()        
        self.parent().show()
        
    def cual_camaras(self):
        x=self.cual_camara.currentText()
        x=int(x)
        return x
   
        
    def start_webcam(self):
            print("camara: ",self.cual_camaras())
            xx=self.cual_camaras()
            self.capture = cv2.VideoCapture(xx)
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 864) #ALTO
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)  #ANCHO
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(5)
               
    def update_frame(self):
        try:
            global image
            ret, self.image = self.capture.read()
            self.image = cv2.flip(self.image,1)
            self.displayImage(self.image,1)
            hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
            color_lower = np.array([self.h_min.value(), self.s_min.value(), self.v_min.value()], np.uint8)
            color_upper = np.array([self.h_max.value(), self.s_max.value(), self.v_max.value()], np.uint8)
            self.current_value.setText('Current Value -> Min :'+str(color_lower)+' Max: '+str(color_upper))
            global color_mask
            # print('Min :'+str(color_lower)+' Max: '+str(color_upper))
            color_mask = cv2.inRange(hsv, color_lower, color_upper)
            self.displayImage(color_mask,2)
        except (AttributeError, UnboundLocalError):
            pass
        

    def stop_webcam(self):
        self.timer.stop()
        self.capture.release()
        
    
    def capturar (self):
        
        try:
            self.timer.stop()
            self.capture.release()
            global cedula
            global medida_ref
            medida_ref=float(self.lineEdit_ref.text())
            print("medida_ref acumuluda 1 =",medida_ref)
            ###
            print(cedula)
            cv2.imwrite("../Imagenes_Huellas/Muestras_HSV/%d.png"%cedula, color_mask)
            cv2.imwrite("../Imagenes_Huellas/Muestras_fotos/%d.png"%cedula,self.image)
            cv2.imwrite("Temporal_hsv.png",color_mask)
            
            print("Foto tomada correctamente")
            
            self.capture.release()
            self.timer.stop()
            ###
            self.hide() #esta linea es para que se esconda la ventana principal cuando se desea abrir  la segunda ventana
            ventana_Mostrar_Medir_Buscar=Mostrar_Medir_Buscar(self)
            ventana_Mostrar_Medir_Buscar.show()
        except (AttributeError, FileNotFoundError):
            pass   
    def displayImage(self,img,window=1):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3: #[0]=rows, [1]=cols, [2]=channels
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        
        outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0],qformat)
        #BGR to RGB
        outImage = outImage.rgbSwapped()
        
        if window == 1:
            self.image_label1.setPixmap(QPixmap.fromImage(outImage))
            self.image_label1.setScaledContents(True)
        
        if window ==2:
            self.image_label2.setPixmap(QPixmap.fromImage(outImage))
            self.image_label2.setScaledContents(True)
            
            
        
###############  fin de camara       ###################            
            
###############   Inicio de Mostrar_Medir_Buscar ###################          
  
class Mostrar_Medir_Buscar(QMainWindow):
    
    def __init__(self,parent=None):
        super(Mostrar_Medir_Buscar, self).__init__(parent)
        loadUi('../Ventanas_Interfaz/Mostrar_Medir_Buscar.ui', self)
        self.boton_regresar.clicked.connect(self.abrirVentanaAnterior)
        self.boton_mostrar.clicked.connect(self.mostar_imagen)
        self.boton_guardar2.clicked.connect(self.guardar2)
        self.boton_medir.clicked.connect(self.medir_y_clasificar)
    
       # img=cv2.imread('pie1.png')
#        self.image_label3.setPixmap(img)
#        self.image_label3.setScaledContents(True)
     
    def mostar_imagen (self):
        #frame = imutils.resize(frame,width=640)
        self.image_label3.setPixmap(QtGui.QPixmap("rectangulos.png"))

    def abrirVentanaAnterior(self):
        self.parent().show()
        self.close() 
    def medir_y_clasificar(self):
        print("Hola")
        global cedula
        global medida_ref
        print("medida_ref acumuluda 2 =",medida_ref)
        Algoritmo.medir_imagen(self,medida_ref,cedula)
        

        #cv2.imshow("imagen limpia2", img_limpia2)
        #self.image_label3.setPixmap(QtGui.QPixmap("Temporal_hsv.png"))
        
        
    def guardar2(self):
        Reporte_pdf.resultado_HC(self)
        global cedula
        print(cedula)
        # def guardar2(id3,foto_muestra,foto_medidas,foto):
        
        foto_hsv=str('../Imagenes_Huellas/Muestras_HSV/%d.png'%cedula)
        foto_procesada=str('../Imagenes_Huellas/Muestras_procesada/%d.png'%cedula)
        foto=str('../Imagenes_Huellas/Muestras_fotos/%d.png'%cedula)
        
        
        iz_Largo=float(self.textEdit_izq1.toPlainText())
        iz_Ancho_del_pie=float(self.textEdit_izq2.toPlainText())
        iz_Ancho_del_medio_pie=float(self.textEdit_izq3.toPlainText())
        iz_HC=str(self.textEdit_izq4.toPlainText())
        
        de_Largo=float(self.textEdit_dere1.toPlainText())
        de_Ancho_del_pie=float(self.textEdit_dere2.toPlainText())
        de_Ancho_del_medio_pie=float(self.textEdit_dere3.toPlainText())
        de_HC=str(self.textEdit_dere4.toPlainText())

        Guardando.guardar2(self,cedula,foto_hsv,foto_procesada,foto,
                           iz_Largo,iz_Ancho_del_pie,iz_Ancho_del_medio_pie,iz_HC,
                           de_Largo,de_Ancho_del_pie,de_Ancho_del_medio_pie,de_HC)
      
        
    
###############      Fin  de Mostrar_Medir_Buscar   ###################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = inicio_sesion()
    #window.setWindowTitle('OpenCV Color Detector')
    window.show()
    sys.exit(app.exec_())

#app = QApplication(sys.argv)
#main = ventana_principal()
#main.show()
#sys.exit(app.exec_())