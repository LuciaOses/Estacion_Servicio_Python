#Clase Surtidor
class Surtidor:
    def __init__(self,num_surtidor,tipo_com,stock,precio_litro,estado,cant_de_litros,playero,monto_ven,descuento):
        self.__num_surtidor=num_surtidor
        self.__estado=estado
        self.__playero=playero
        self.__tipo_com=tipo_com
        self.__stock=stock
        self.__precio_litro=precio_litro
        self.__cant_de_litros=cant_de_litros
        self.__monto_ven=monto_ven
        self.__descuento=descuento
        
# Funciones que Muestran
    def ver_num_surtidor(self):
        return self.__num_surtidor
    def ver_estado(self):
        return self.__estado
    def ver_playero(self):
        return self.__playero
    def ver_tipo_com(self):
        return self.__tipo_com
    def ver_stock(self):
        return self.__stock
    def ver_precio_litro(self):
        return self.__precio_litro
    def ver_cant_de_litros(self):
        return self.__cant_de_litros
    def ver_monto_ven(self):
        return self.__monto_ven
    def ver_descuento(self):
        return self.__descuento
    
# Funciones que Modifican    
    def mod_num_surtidor(self,otro):
        self.__num_surtidor=otro
    def mod_estado(self,otro):
        self.__estado=otro
    def mod_playero(self,otro):
        self.__playero=otro
    def mod_tipo_com(self,otro):
        self.__tipo_com=otro
    def mod_stock(self,otro):
        self.__stock=otro
    def mod_precio_litro(self,otro):
        self.__precio_litro=otro
    def mod_cant_de_litros(self,otro):
        self.__cant_de_litros=otro
    def mod_monto_ven(self,otro):
        self.__monto_ven=otro
    def mod_descuento(self,otro):
        self.__descuento=otro
    
    

    
    
        
        
    
        
        
    
    
