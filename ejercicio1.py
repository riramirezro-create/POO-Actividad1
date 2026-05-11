class Familia:
    
    def __init__(self, edad_juan):
        self.edad_juan = edad_juan

    def calcular_edad_alberto(self):
        return (2 / 3) * self.edad_juan

    def calcular_edad_ana(self):
        return (4 / 3) * self.edad_juan

    def calcular_edad_mama(self):
        return self.edad_juan + self.calcular_edad_alberto() + self.calcular_edad_ana()

ingreso_juan = int(input("Ingrese la edad de Juan: "))

mi_familia = Familia(ingreso_juan)

print("La edad de Juan es:", mi_familia.edad_juan)
print("La edad de Alberto es:", mi_familia.calcular_edad_alberto())
print("La edad de Ana es:", mi_familia.calcular_edad_ana())
print("La edad de la mamá es:", mi_familia.calcular_edad_mama())
