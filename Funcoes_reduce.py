#Função reduce serve para reduzir os valores de uma estrutura de dados á um unico valor.
#precisamos importar um módulo builtin chamado functools.

from functools import reduce
lista = [2,7,10,6,70]

def mult(x,y):
    return x*y
print(reduce(mult,lista))

#Testar o valor usando reduce

lista2 = [30,67,1000,61,90]

testmaior = lambda x,y: x if(x>y) else y

print(reduce(testmaior,lista2))
