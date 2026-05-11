import math

class Circulo:
    
    def __init__(self, radio_ingresado):
        self.radio = radio_ingresado
        
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
        
    def calcular_circunferencia(self):
        return 2 * math.pi * self.radio

radio_usuario = float(input("Ingrese el radio del circulo: "))

mi_circulo = Circulo(radio_usuario)

print("El area del circulo es:", mi_circulo.calcular_area())
print("La longitud de la circunferencia es:", mi_circulo.calcular_circunferencia())
