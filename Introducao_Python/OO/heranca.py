class Carro:
    def __init__(self): #atributo de instância
        self.__velocidade = 0

    @property
    def velocidade(self):
        return self.__velocidade

    def acelerar(self): #método de instância
        self.__velocidade += 5
        return self.__velocidade

    def frear(self):
        self.__velocidade -= 5
        return self.__velocidade

class Uno(Carro):
    pass

class Ferrari(Carro):
    def acelerar(self):
        super().acelerar()
        return super().acelerar()

c1 = Carro()

print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())
print(c1.frear())
print(c1.frear())

c2 = Uno()

print(c2.acelerar())
print(c2.acelerar())
print(c2.acelerar())
print(c2.frear())
print(c2.frear())

c3 = Ferrari()

print(c3.acelerar())
print(c3.acelerar())
print(c3.acelerar())
print(c3.frear())
print(c3.frear())


