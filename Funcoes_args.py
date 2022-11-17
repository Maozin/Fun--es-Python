#Funções *args são utilizadas quando não conhecemos a quantidade de argumentos necessários em uma função
#Deixamos iss flexivel em aberto
#O retorno ou saida dessa função retorna uma tupla

def soma(*args):
    print(*args)

soma(1,3,5,44,52,21,111)


def soma_total(*args):
    total = 0
    for n in args:
        total = n+total
    return total