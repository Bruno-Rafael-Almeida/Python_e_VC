import numpy as np
from numpy.core import umath
from numpy.core.fromnumeric import reshape
from numpy.core.numeric import ones

a = np.array([1,2,3], dtype='int16')
print(a)

b = np.array([[9.0,8.0,7.0], [6.0,5.0,4.0]])
print(b)

c = np.array([[9.0,8.0,7.0], [6.0,5.0,4.0], [3.0,2.0,1.0]])
print(c)

c = np.array([[9.0,8.0,7.0,6.0,5.0,4.0,3.0,2.0,1.0], [9.0,8.0,7.0,6.0,5.0,4.0,3.0,2.0,1.0]])

# para saber quantas dimenções um array tem
print(f' quantidade de dimenções da var: {c.ndim}')

# para pegar a quantidade de linhas e colunas de um array
print(f' quantidade de linhas e colunas: {c.shape}')

# para saber o tipo dos valores do array e seu tamanho em bits
print(f' tipo e tamanho em bits: {a.dtype}')

# para pegar a quantidade de informações dentro do array, incluindo elementos e instruções
print(f' tamanho do array: {b.itemsize}')

# para pegar a quantidade de elementos do array
print(f' quantidade de elementos: {c.size}')

# para transformar um array unidimencional em uma matriz LxC
# print(f' quantidade de linhas e colunas: {c.reshape(3,3)}')

# para criar uma matriz de de n dimenções com zeros
print(f' apenas zeros: {np.zeros((3,3))}')

# para criar uma matriz de n dimenções com 1's
print(f' apenas uns: {np.ones((3,3,3))}')

# para criar uma matriz de n dimenções com qualquer número, o 1° parâmetro é o tamanho da matriz
# o segundo é o número a ser usado para ser preenchida
print(f' apenas uns: {np.full((3,3,3), 12)}')

# e também pode ser usado um método similar para colocar um elemento escolhido como elemento de
# uma matriz já existente
print('apenas 4')
print(np.full_like(c.shape,4))


# para decobrir o número de bytes do array
print(f' quantidade de bytes: {c.nbytes}')

# para um elemento ecpecifico do array multidimencional 
print(f' elemento buscado: {b[1,2]}')

# para obter uma linha específica do array multidimencional 
print(f' elemento buscado: {b[1,:]}')

# para obter uma coluna específica do array multidimencional 
print(f' elemento buscado: {b[:,1]}')

# para obter elementos entre um intervalo em um array [n° da L, indexDoInic:indexDoFin:passoDePulo] 
print(f' elemento buscado: {c[0, 1:-1:2]}')

d = np.array([[[1,2], [3,4]],[[5,6], [7,8]]])
print(d)

# para que eu consiga pegar um ou mais elementos de um array multidimencional 
# e imprimir caso seja apenas um elemento ou varios
# pode se utiliza a seguinte sintaxe [:,x,:] onde o : liguinifica passar nessas posições do array
print(f' elemento buscado: {d[:,1,:]}')
# como também para trocar um conjunto de elementos ou apenas um, pode se utilizar esse jeito 
# de buscar elementos em um array
d[:,1,:] = [[10,10], [10,10]]
print(d[:,1,:])

# para criar um array randomizado com numeros decimais, entre 0 e 1
print(np.random.random_sample(a))

# para criar um array randomizado com números inteiros, o 1° é o n° max ou um intervalo entre n°
# o 2° é o array                                               (2,7, size=(10,10))
print(np.random.randint(7, size=(10,10)))

# para fazer uma matriz identidade, onde a diagonal principal é formado por 1's e o resto 0
print(np.identity(4))

# para fazer uma matriz incluir todos os elementos de uma outra matriz e os repetilos um n° n de veses
# mas essa nova matriz com as repetições sempre sera unidimencional, por mas q a matrix do parametro
# não seja unidimencional
ae = np.array([[1,2,3,4,5,6],[10,11,12,13,14,15]])
r1 = np.repeat(ae, 3)
print(r1)
# mas caso precise que as repetições sejam espalhadas em cada linha
r1 = np.repeat(ae, 3, axis=0)
print(r1)

t = np.ones((5,5))
t[1, 1:-1:1] = 0
t[2, 1:-1:1] = 0
t[3, 1:-1:1] = 0
t[2,2] = 9
print(t)

# ou

o = np.zeros((3,3))
o[1,1] = 9
u = ones((5,5))
u[1:4,1:4] = o
print(u)

print(np.random.randint(7, size=(3,3,3)))


