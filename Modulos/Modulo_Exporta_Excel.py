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
Error=Tk()   
Error.withdraw()
import sqlite3
from openpyxl import Workbook

class Exportar_xlsx:
    def Funcion_Exportar_xlsx(self):
        
        cc="*"
        
        try:
             rut=self.lineEdit_Ruta.text()             
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
                                       
                 SQL= """SELECT %s FROM Registro AS r INNER JOIN Muestra_izq AS i ON r.id=i.id1 INNER JOIN Muestra_dere AS d ON  r.id=d.id2 INNER JOIN Foto AS F ON r.id=F.id3"""%cc #,Muestra_izq,Muestra_dere,Foto
                 cursor.execute(SQL)
                 results = cursor.fetchall()
                 wb = Workbook()
                 ws = wb.create_sheet(0)
                 ws.title = 'Registro'
                 ws.append(cursor.column_names)
                 for row in results:
                     ws.append(row)
                     
                 ruta = rut
                 wb.save(ruta + "/Base de datos JB-HUELLAS.xlsx")   

                 connection.commit()
                 print("Record inserted successfully into Laptop table")
                 QMessageBox.information(self, "Exportación","Exportación de datos con éxito ")
                 self.boton_regresar.setEnabled(True)
                 #self.thread.start()
#  
                 ######## fin de insertar los datos   #######
             else:
                 
                 QMessageBox.information(self, "verificar","Insertar la ruta donde desea guardar el documento ")
                
        except mysql.connector.Error as error:
            connection.rollback()
            print("Error al conectar con MYSQL {}".format(error))
            QMessageBox.critical(self, "Error!","fallo al intentar conectar con MYSQL {}".format(error) )
        except PermissionError as error:
            print("Error en la exportación MYSQL {}".format(error))
            QMessageBox.critical(self, "Error!","fallo al intentar exportar XLSX \n ingrese una ruta valida por favor {}".format(error) )
        
        
        