#Clase Mi Exceptión

class Playero_Existente(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return str(self.value)
    
