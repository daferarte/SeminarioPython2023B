class Coche:
    #atributos
    rueda=4
    color=''
    aceleracion=0
    velocidad=0

    #constructor
    def __init__(self, color, aceleracion):
        self.color=color
        self.aceleracion=aceleracion

    #metodos
    def acelerar(self):
        self.velocidad += self.aceleracion
        return self.velocidad
    
class autoVolador(Coche):

    def __init__(self, color, aceleracion, esta_volando=False):
        super().__init__(color, aceleracion)
        self.ruedas = 6
        self.esta_volando = esta_volando

    def vuela(self):
        self.esta_volando=True
        return "Estoy volando"

    
    
# c1 = Coche('rojo',5)
# print(c1.acelerar())
# print(c1.acelerar())

# cv1 = autoVolador('negro', 20)
# print(cv1.color)
# print(cv1.vuela())
# print(cv1.rueda)
# print(cv1.ruedas)

