#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 00:37:16 2020

@author: fabian
"""
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

import mysql.connector
from mysql.connector import Error

class Guardando:
    
    def guardar(self,id,nom,ape,gen,peso,edad,altu,t_izq,t_dere,telf,ocupa,obser):
           
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
                
                 
 
                 ########  Aqui insertamos los datos ##########
        
                 print (id,nom,ape,gen,peso,edad,altu,t_izq,t_dere,telf,ocupa,obser)
                                 
                 mySql_insert_query = """INSERT INTO Registro (id, nombres, apellidos,genero,peso,edad,altura,talla_izq,talla_dere,telefono,ocupacion,observacion) 
                                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """

                 recordTuple = (id,nom,ape,gen,peso,edad,altu,t_izq,t_dere,telf,ocupa,obser)
                 cursor.execute(mySql_insert_query, recordTuple)
                 connection.commit()
                 print("Record inserted successfully into Laptop table")
                 QMessageBox.information(self, "GUARDAR","Datos guardados con éxito ")
                 self.boton_siguiente.setEnabled(True)  #se habilita el modulo siguiente
#  
                 ######## fin de insertar los datos   #######
             else:
                 
                 QMessageBox.information(self, "verificar","Datos guardados con éxito ")
         
         except mysql.connector.Error as error:
             connection.rollback()
             print("Failed to insert into MySQL table {}".format(error))
             QMessageBox.critical(self, "Error!","fallo al intentar insertar los datos en la tabla {}".format(error) )
        
        
    """
           tabla  Foto (num_muestra,id3,foto_hsv,foto_procesada,foto_pie) 
           tabla Muestra_izq(num_muestra,id1,metodo1,largo_izq,x_izq,y_izq,clasificacion_izq)
           tabla Muestra_dere(num_muestra,id2,metodo,largo_dere,x_dere,y_dere,clasificacion_dere)
           
    """
    #def guardar2(self,id3,foto_hsv,foto_procesada,foto):
    def guardar2(self,cedula,foto_hsv,foto_procesada,foto,
                           iz_Largo,iz_Ancho_del_pie,iz_Ancho_del_medio_pie,iz_HC,
                           de_Largo,de_Ancho_del_pie,de_Ancho_del_medio_pie,de_HC):
        metodo=str("HC")
              
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
                
                 
 
                 ########  Aqui insertamos los datos ##########
        
                print (cedula,foto_hsv,foto_procesada,foto)
                                 
                mySql_insert_query = """INSERT INTO Foto  (num_muestra,id3,foto_hsv,foto_procesada,foto_pie)  
                                VALUES (%s, %s , %s,%s, %s ) """

                recordTuple = (None,cedula,foto_hsv,foto_procesada,foto)
                cursor.execute(mySql_insert_query, recordTuple)
                connection.commit()
                print("Record inserted successfully into Laptop table")
                QMessageBox.information(self, "GUARDAR","Datos guardados con éxito ")
                
                """Aqui se guarda el resultadod del pie izquierdo"""
                
                mySql_insert_query = """INSERT INTO Muestra_izq (num_muestra	,id1,metodo1,largo_izq,x_izq,y_izq,clasificacion_izq)  
                                VALUES (%s,%s,%s,%s,%s,%s,%s ) """

                recordTuple = (None,cedula,metodo,iz_Largo,iz_Ancho_del_pie,iz_Ancho_del_medio_pie,iz_HC)
                cursor.execute(mySql_insert_query, recordTuple)
                connection.commit()
                print("Record inserted successfully into Laptop table")
                QMessageBox.information(self, "GUARDAR","Datos guardados con éxito ")
                
                """Aqui se guarda el resultadod del pie derecho"""
                
                mySql_insert_query = """INSERT INTO Muestra_dere(num_muestra,id2,metodo,largo_dere,x_dere,y_dere,clasificacion_dere)  
                                VALUES (%s,%s,%s,%s,%s,%s,%s ) """

                recordTuple = (None,cedula,metodo,de_Largo,de_Ancho_del_pie,de_Ancho_del_medio_pie,de_HC)
                cursor.execute(mySql_insert_query, recordTuple)
                connection.commit()
                print("Record inserted successfully into Laptop table")
                QMessageBox.information(self, "GUARDAR","Datos guardados con éxito ")
#  
                 ######## fin de insertar los datos   #######
            else:
                                
                QMessageBox.information(self, "verificar","Datos guardados con éxito ")
                
                 

        except mysql.connector.Error as error:
             connection.rollback()
             print("Failed to insert into MySQL table {}".format(error))
             QMessageBox.critical(self, "Error!","fallo al intentar insertar los datos en la tabla {}".format(error) )
    
    