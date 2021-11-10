def soma(*nums):
    total = 0
    for n in nums:
        total += n
    return total

def resultado(**kwargs):
    status = 'aprovado' if kwargs['nota'] >= 7 else 'reprovado'
    return f'{kwargs["nome"]} foi {status}'