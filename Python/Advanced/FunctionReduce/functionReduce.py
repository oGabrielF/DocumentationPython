# FUNÇÃO REDUCE

# Recebe uma lista e retorna um unico valor dessa lista.
# Podemos utilizar essa função para fazer a soma de todos os itens de uma lista determinada lista.

from functools import reduce # Importe a função reduce

def soma(x, y):
    return x+y

list_receive = [1,3,5,10,20]

# Reduce() Recebe 2 argumentos a minha função e a minha lista.
soma = reduce(soma, list_receive)
print(soma)