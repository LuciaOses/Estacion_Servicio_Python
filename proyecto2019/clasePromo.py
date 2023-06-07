
class Promocion:
    def __init__(self,cont_promo,tipo_promo,tarjeta):
        self.__cont_promo=cont_promo
        self.__tipo_promo=tipo_promo
        self.__tarjeta=tarjeta
         
    def cont_promo(self):
        return self.__cont_promo
    
    def tipo_promo(self):
        return self.__tipo_promo
    
    def tarjeta(self):
        return self.__tarjeta
    
    def ver_promo(self,pro):
        self.__tipo_promo=pro
        
    def ver_tarjeta(self,otro):
        self.__tarjeta=otro
        
    
	

    	
