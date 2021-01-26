# Importar o modúlo random que serve para criar números aleatorios.
import random 

# Utilizando random.seed(1) você irá obter sempre o mesmo número na escolha
number = random.randint(0, 100) # Random.randint(x, y) Irá buscar um número aleatorio de x número até y número
print(number)

list = [1,10,23,45,12,76,34,21,32,42,11,23]
number = random.choice(list) # random.choice(Nome_Da_Lista) é utilizado para escolher um número aleatorio de uma determinada lista.
print(number)