class OperacionNumero:
    
    def __init__(self, numero_ingresado):
        self.valor = numero_ingresado

    def calcular_cuadrado(self):
        return self.valor ** 2

    def calcular_cubo(self):
        return self.valor ** 3

numero_usuario = float(input("Ingrese un numero: "))

mi_numero = OperacionNumero(numero_usuario)

print("El cuadrado del numero es:", mi_numero.calcular_cuadrado())
print("El cubo del numero es:", mi_numero.calcular_cubo())
