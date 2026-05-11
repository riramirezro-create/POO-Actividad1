class Empleado:
    
    def __init__(self, horas, pago):
        self.horas_trabajadas = horas
        self.pago_por_hora = pago

    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.pago_por_hora

    def calcular_retencion(self):
        return self.calcular_salario_bruto() * 0.125

    def calcular_salario_neto(self):
        return self.calcular_salario_bruto() - self.calcular_retencion()

mi_empleado = Empleado(48, 5000)

print("Salario Bruto: $", mi_empleado.calcular_salario_bruto())
print("Retención en la fuente: $", mi_empleado.calcular_retencion())
print("Salario Neto: $", mi_empleado.calcular_salario_neto())
