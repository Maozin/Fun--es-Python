# Funções decoradoras servem para potencializar, dar mais recursos para outras funções.
# Para utilizar uma função decoradora, utilizamos o @ antes do nome da função, e acima da funçao decorada.

# Criar função decoradora 

def master(msg):
    def imprime():
        print("Essa é a função decoradora")
        msg()
    return imprime


    # Segunda função que vai ser decorada pela decoradora 
@master
def funcao_simples():
    print("Estou chamando a função Simples")



funcao_simples()