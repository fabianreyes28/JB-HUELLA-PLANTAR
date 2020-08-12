#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 04:49:15 2020

@author: fabian
"""

 # Create Excel (.xlsx) file -----------------------------------------------


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
from openpyxl import Workbook
Error=Tk()   
#Error.eval('tk::PlaceWindow %s center ' % Error.winfo_toplevel())
Error.withdraw()


#cc=2

#SQL = """SELECT id, nombres, apellidos,genero,peso,altura,talla_izq,talla_dere,telefono,ocupacion,observacion,
#                             metodo,largo_izq,x_izq,y_izq,clasificacion_izq,
#                             largo_dere,x_dere,y_dere,clasificacion_dere,
#                             foto_muestra,foto_medidas,
#                             fecha
#                             from Registro inner join Muestra_izq on Registro.id=Muestra_izq.id1
#                                           inner join Muestra_dere on Registro.id=Muestra_dere.id2
#                                           inner join Foto on Registro.id=Foto.id3
#                                           WHERE id=%d"""%cc 

#wb = Workbook()
#SQL = 'SELECT * from '+ Registro + ';'
#cur.execute(SQL)
#results = cur.fetchall()
#ws = wb.create_sheet(0)
#ws.title = Registro
#ws.append(cur.column_names)
#for row in results:
#    ws.append(row)
#
#workbook_name = "test_workbook"
#wb.save(workbook_name + ".xlsx")


import glob

ruta = "../Imagenes_Huellas/Muestras_HSV/8.png"
for file in glob.glob(ruta):
    print(file)
    a= cv2.imread(file)
    cv2.imshow('Color image', a)
    #wait for 1 second
    cv2.waitKey(0)
    #destroy the window
    cv2.destroyAllWindows()
    

b=int(1234657890)

if b:
    print (b)
#if isinstance(b, int):
#    print ("es entero")
else:
    print("no es entero")
    
    
    



#for name in glob.glob('../Imagenes_Huellas/Muestras_HSV/8.png'): 
#    print(name) 
#    im=Image.open(name)
#    im.show()
    
  
#f=Image.open("../Imagenes_Huellas/Muestras_HSV/8.png")
#f.show()







