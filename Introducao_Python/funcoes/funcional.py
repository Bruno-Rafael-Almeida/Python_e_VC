def soma(a, b):
    return a + b

somar = soma #variavel que armazena uma função, atuando como prototipo da função
print(somar(3,4))

def operacao_aritmetica(fn, a, b):
    return fn(a,b)

resultado = operacao_aritmetica(soma, 13, 12) #função q chama operações e as executa dentro do código
print(resultado)

def soma_parcial(a):
    #processamento pesado T = 1min |isso foi feito usando os paramentro fornecidos na entra-
    #processamento pesado T = 10s  |da da função 'soma_parcial()'
    #processamento pesado T = 10s  |isso vai  polpar tempo de execução ao processar 
    #                              |coisas iguais usando um mesmo paramentro na 1° função de entrrada
    def concluir_soma(b): # T = 10s
        return a+b
    return concluir_soma

resultado_final = soma_parcial(10)(12) #um jeito de passar as duas entradas em uma linha
print(resultado_final)

#para polpar esforço de processamento pode ser usada a tecnica apresentada acima
# r1 = soma parcial(a) T = 1,20 min |vai processar todas as instruções sem processar a segunda função
# soma_total1 = r1(b)
# soma_total2 = r1(c)
