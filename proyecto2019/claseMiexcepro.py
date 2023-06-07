#Clase Except Promo Existe
class Promo_Existente(Exception):
    def __init__(self,value,valu):
        self.value=value
        self.valu=valu
    def __str__(self):
        return str(self.value)
