nota = float(input('digite a nota do aluno: '))

if nota >= 9:
    print('duas palavras: para bens! ')
elif nota >= 7:
    print('aprovado')
elif nota < 5:
    print('recuperação')
else:
    print('reprovação imediata')

print(nota)