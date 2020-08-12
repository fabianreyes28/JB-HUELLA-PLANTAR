#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:24:06 2020

@author: fabian
"""

class Usuario:
    
    usuario="admin"
    # doble piso es para encapsular
    contrasena="admin123"
#    def __init__(self,user,contra):
#        
#        self.usuario=user
#        self.contrasena=contra
    def GetUsuario (self):
        return self.usuario
    
    def GetContrasena (self):
        return self.contrasena
    def hola():
        print("hola gracias a Dios")