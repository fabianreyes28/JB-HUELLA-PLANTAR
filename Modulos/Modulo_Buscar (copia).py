#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:47:58 2020

@author: fabian
"""

import sys
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
from PyQt5.QtCore import Qt
from tkinter import *
from tkinter import messagebox
import pymysql.cursors
import mysql.connector
from mysql.connector import Error
import pandas as pd
import glob # esta es una libreria para buscar archivos con la ruta
Error=Tk()   
import sqlite3
Error.withdraw()


class Buscar (QMainWindow):
            
    def __init__(self,parent=None):
        super(Buscar, self).__init__()
        loadUi('../Ventanas_Interfaz/Buscar.ui', self)
       
        self.boton_regresar.clicked.connect(self.Funcion_Regresar)
        self.Boton_Buscar.clicked.connect(self.Funcion_buscar)
        self.Boton_Mostrar.clicked.connect(self.Funcion_Mostar_ruta)
        
        #self.boton_regresar.clicked.connect(self.Funcion_buscar)
    def Funcion_Regresar():
        pass
    def Funcion_Mostar_ruta(self):
        ruta=str(self.lineEdit_Ruta.text())
        for file in glob.glob(ruta):
            print(file)
            img= cv2.imread(file)
            cv2.imshow('Imagen de la ruta ',img)
#            cv2.waitKey(0)
#            cv2.destroyAllWindows()
       
    def Funcion_buscar(self):
        cc=int(self.lineEdit_cc.text()) 
                    
        try:
                       
            connection = mysql.connector.connect(host='localhost',                                            
                                                     database='base_huella',
                                                     user='root',
                                                     password='',
                                                     port='3311')
            if connection.is_connected():
                
                 db_Info = connection.get_server_info()
                 print(" Conectado al Servidor de MySQL version ", db_Info)
                 cursor = connection.cursor()
                 cursor.execute("select database();")
                 record = cursor.fetchone()
                 print("Ya esta conectado a la Base de Datos: ", record)
                
                 ########  Aqui Consultamos los datos ##########
        
                 query = """SELECT id, nombres, apellidos,genero,peso,altura,talla_izq,talla_dere,telefono,ocupacion,observacion,
                             metodo,largo_izq,x_izq,y_izq,clasificacion_izq,
                             largo_dere,x_dere,y_dere,clasificacion_dere,
                             foto_pie,foto_hsv,foto_procesada,
                             fecha
                             from Registro inner join Muestra_izq on Registro.id=Muestra_izq.id1
                                           inner join Muestra_dere on Registro.id=Muestra_dere.id2
                                           inner join Foto on Registro.id=Foto.id3
                                           WHERE id=%d"""%cc
              
                 cursor.execute(query)
                 self.tableWidget.setRowCount(0)
                 for numero_fila, registro in enumerate (cursor):
                     self.tableWidget.insertRow(numero_fila)
                     for numero_columna, data in enumerate (registro):
                         self.tableWidget.setItem (numero_fila,numero_columna,QtWidgets.QTableWidgetItem(str(data)))
                         
                 connection.commit()
                 print("consulta satisfactoria")
                 QMessageBox.information(self, "CONSULTA","Consulta de datos con éxito ")
                 self.boton_regresar.setEnabled(True)
                 #self.thread.start()

                 ######## fin de consultar los datos   #######
            else:
                QMessageBox.information(self, "verificar","Datos guardados con éxito ")
         
        except mysql.connector.Error as error:
            connection.rollback()
            print("Error al consultar los datos en MYSQL {}".format(error))
            QMessageBox.critical(self, "Error!","Error al intentar consultar los datos en la tabla los datos en la tabla {}".format(error) )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Buscar()
    #window.setWindowTitle('OpenCV Color Detector')
    window.show()
    sys.exit(app.exec_())        
        
        