#Funções Kwargs
#Passar um numero indeterminado de parametros 
#Para uma função 

def saudacoes(**kwargs):
    print(kwargs)

saudacoes(manha="Bom Dia", tarde ="Boa Tarde")

def saudacoes_dia(**kwargs):
    for periodo_dia,saudacoes in kwargs.items():
        print(f"Durante a {periodo_dia} dizemos {saudacoes}") #fstrings


#Chamar a função

saudacoes_dia(manha= "Bom dia", tarde= "Boa tarde", noite= "Boa noite", madrugada= "Vai dormir")
