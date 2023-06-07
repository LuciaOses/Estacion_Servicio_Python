import os
from clasePlayero import*
from clasePromo import*
from claseSurtidores import*


class Estacion_Servicio():
    def __init__(self):
        self.__lista_playero=[]
        self.__lista_promocion=[]
        self.__lista_surtidores=[]
        
        
    def ver_ListPlay(self):
        return self.__lista_playero

    def agregar(self,pla):
        if isinstance(pla,Playero):
           self.__lista_playero.append(pla)
            
    def eliminar(self,pla):
        self.__lista_playero.remove(pla)

    def cant_pla(self):
        return len(self.__lista_playero)

    def existe(self,pla):
        return pla in self.__lista_playero
    

    def ver_ListPro(self):
        return self.__lista_promocion

    def agregar_pro(self,pro):
        if isinstance(pro,Promocion):
           self.__lista_promocion.append(pro)
            
    def eliminar_pro(self,otro):
        self.__lista_promocion.remove(otro)

    def cant_pro(self):
        return len(self.__lista_promocion)


    def ver_ListSur(self):
        return self.__lista_surtidores

    def agregar_sur(self,sur):
        if isinstance(sur,Surtidor):
           self.__lista_surtidores.append(sur)
            
    def eliminar_sur(self,otro):
        self.__lista_surtidores.remove(otro)

    def existe(self,sur):
        return sur in self.__lista_surtidores

    def Estado(self,nombre):
        self.__lista_surtidores.mod_estado(nombre)
    

    
