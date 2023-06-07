#Clase Playero
from claseMiexcep import*

class Playero:
    def __init__(self,cont,nombre,dni):
        self.__cont=cont
        self.__nombre_apellido= nombre
        self.__dni=dni
        
# Funciones que Muestran
    def ver_cont(self):
        return self.__cont
    def vernom_ape(self):
        return self.__nombre_apellido
    def verdni(self):
        return self.__dni
    
# Funciones que Modifican
    def asignom(self, no):
        self.__nombre_apellido=no
    def asigdni( self,doc):
        self.__dni=doc



    
    







