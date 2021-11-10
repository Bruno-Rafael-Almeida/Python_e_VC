class Contador:
    contador = 0 #atributo de classe

    @classmethod  #metodos de classe
    def inc(cls):
        cls.contador += 1
        return cls.contador

    @classmethod
    def dec(cls):
        cls.contador -= 1
        return cls.contador

# c1 = contador() # instância de classe pode usar os métodos de uma classe,
#                 # mesmo eles sendo métodos de classe e não de instâncias
# print(c1.inc())
# print(c1.inc())
# print(c1.inc())
# print(c1.dec())
# print(c1.dec())
# print(c1.dec())

# Contador.inc() ,as quando se cria métodos e atributos de classe não precisasse cirar instancias
# do mesmo para usalas

print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.dec())
print(Contador.dec())
