#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 20:10:26 2020

@author: fabian
"""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
c=canvas.Canvas("Reporte.pdf")

class Reporte_pdf:
       
    def Pdf_Registro(self):
        c.setLineWidth(.3)
        #Fuente y tamaño a utilizar
        c.setFont('Helvetica',14)
        ##dibujo de texto en x,y 1pto=1/72 pulgadas
        c.drawString(50,760,"RESULTADOS SISTEMA AUTOMÁTICO DE DIAGNÓSTICO PRELIMINAR APLICADO A UN PODOSCOPIO")
        c.drawString(200,740,"APLICADO A UN PODOSCOPIO")
        #POSICION X1 Y1 X2 Y2
        c.line(50,730,550,730)
        c.line(50,705,550,705)
        
        c.drawString(245,710,"Datos del Usuario")
        c.drawString(50,680,"Nombres: " + str(self.lineEdit_nombre.text()))
        c.drawString(300,680,"Apellidos: " + str(self.lineEdit_apellido.text()))
        c.drawString(50,660,"Cedula: " + str(self.lineEdit_cedula.text()))
        c.drawString(300,660,"Telefono: " + str(self.lineEdit_telefono.text()))
        c.drawString(50,640,"Altura: " + str(self.lineEdit_altura.text()))
        c.drawString(50,620,"Talla pie izquierdo:" +str(self.lineEdit_talla_izq.text()) + "        Talla pie derecho:" + str(self.lineEdit_talla_dere.text() )+ 
        "            Ocupación:" + str(self.lineEdit_ocupacion.text()) ) 
        c.drawString(50,600,"Observación" +str(self.textEdit_observacion.toPlainText()) ) 
        c.drawString(50,580,"METODO : HERNANDEZ CORVO")
        
  #  def Pdf_Registro_fotos(self):
        
        
       
    def resultado_HC(self):
        c.drawImage("rectangulos.png", 100, 100, width= 400, height=300)
        c.drawString(50,80,"Izquierdo: " + str(self.textEdit_dere1.toPlainText()))
        c.drawString(300,80," " + str(self.textEdit_dere2.toPlainText()))
        c.drawString(50,60," " + str(self.textEdit_dere3.toPlainText()))
        c.drawString(300,60," " + str(self.textEdit_dere4.toPlainText()))
        
        c.drawString(50,40,"Derecho: " + str(self.textEdit_izq1.toPlainText()))
        c.drawString(300,40," " + str(self.textEdit_izq2.toPlainText()))
        c.drawString(50,20," " + str(self.textEdit_izq3.toPlainText()))
        c.drawString(300,20," " + str(self.textEdit_izq4.toPlainText()))
        
        
        c.showPage() #final de pagina
        c.save()
        
