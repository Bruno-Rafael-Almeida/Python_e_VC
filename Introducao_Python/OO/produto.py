
class Produto:
    def __init__(self,nome, preco = 1.99, desc = 0):
        self.nome = nome    #se vc quiser fazer um atributo ser privado basta usar 2 __ no seu nome
        self.__preco = preco  #
        self.desc = desc    #

    @property  #decorator 
    def preco_final(self):
        return (1 - self.desc) * self.preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco

         
 

p1 = Produto('Caneta', 5.99, 0.1)
p2 = Produto('Caderno', 12.97, 0.5)

# print(p1.nome,p1.preco, p1.desc, p1.preco_final)  ao tentar acessar esse atributo 'nome' desse jeito
                                                  # ele apresentará um erro dizendo que não existe nessa classe
# print(p1._Produto__nome)                        # mas para que ele possa ser acessado basta usar _nome-da-classe__nome do atributo

p1.preco = 70 
print(p1.nome,p1.preco, p1.desc, p1.preco_final)
print(p2.nome,p2.preco, p2.desc, p2.preco_final)

