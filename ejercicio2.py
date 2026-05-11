class PruebaEscritorio:
    
    def __init__(self):
        self.suma = 0
        self.x = 0
        self.y = 0

    def ejecutar_instrucciones(self):
        self.suma = 0
        self.x = 20
        self.suma = self.suma + self.x
        self.y = 40
        self.x = self.x + (self.y ** 2)
        self.suma = self.suma + (self.x / self.y)
        
        return self.suma

mi_prueba = PruebaEscritorio()
resultado = mi_prueba.ejecutar_instrucciones()

print("EL VALOR DE LA SUMA ES:", resultado)
