#Função enumerate enumera indice de estrutura de dados

#Retornar o indice de uma lista

animais = ["Cachorro", "Gato", "Piriquito", "Elefante"]

print(list(enumerate(animais)))

# interara com enumerate 

for i, valor in enumerate(animais):
    print(i,valor)


# interador e enumerate com condicionais

for i,valor in enumerate(animais):
    if i>1:
        break
    else:
        print(valor)