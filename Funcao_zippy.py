# Zippy manipula e mescla estruturas de dados e seus valores.
# Porem o resultado sempre será o valor da menor estrutura.

dicverduras ={1:"Cebola",2:"Alface",3:"repolho",4:"Beterraba"}
dicfrutas ={1:"Maça",2:"Laranja",3:"Pera"}

mescla = list(zip(dicverduras,dicfrutas))

print(mescla)

mesclavalores = list(zip(dicverduras.values(),dicfrutas.values()))

print(mesclavalores)

# Interar os valores 

for p in mesclavalores:
    print(p)
    