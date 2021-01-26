# FUNÇÃO MAP

# Pegar uma função e aplicar a todos os elementos de uma lista.

def dobro(x):
    return x*2

value = [1,2,3,4,5]

# Map recebe 2 argumentos:
#   -A Função que eu qro chamar
#   -A Minha lista que qro chamar
value_dobro = (map(dobro, value))

# Posso imprimir os valores utilizando for
# Necessario criar uma variavel com o map(function, list)
for v in value_dobro:
    print(v)

# Ou posso exibir criando uma lista:
value_dobro = list(value_dobro)
print(value_dobro)