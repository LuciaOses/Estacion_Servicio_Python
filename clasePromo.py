# Clase Promoción
class Promocion:
    def __init__(self,cont_promo,tipo_promo,bene,tarjeta):
        self.__cont_promo=cont_promo
        self.__tipo_promo=tipo_promo
        self.__bene=bene
        self.__tarjeta=tarjeta
#Funciones que Muestran       
    def cont_promo(self):
        return self.__cont_promo
    def tipo_promo(self):
        return self.__tipo_promo
    def bene(self):
        return self.__bene
    def tarjeta(self):
        return self.__tarjeta
#Funciones que Modifican  
    def mod_promo(self,pro):
        self.__tipo_promo=pro
    def mold_bene(self,otro):
        self.__bene=otro
    def mod_tarjeta(self,otro):
        self.__tarjeta=otro
        
    
	

    	
