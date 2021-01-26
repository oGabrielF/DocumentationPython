# PYTHON AVANÇADO LIST COMPREHENSION

# FORMA SIMPLES DE FAZER ISSO
x = [1,2,3,4,5]
y = []

# Obter os valores dos números da lista x ao quadrado
for i in x:
    y.append(i**2) # Append adicionar um item a lista

print(x) # Números da lista
print(y) # Números da lista x ao quadrado passado pra lista y

# FORMA UTILIZANDO O LIST COMPREHENSION

# Para criação de uma List Comprehension:
#   -Valor a Adicionar
#   -Laço
#   -Condição
# y = [Valor_Adicionar Laço Condição]

x = [1,2,3,4,5]
y = [i**2 for i in x]
print(x)
print(y)

# Valor a Adiconar = (i**2)
# Laço = (for i in x)
# O "i" do valor adicionar deriva-se do "for i in x" que no caso seria a lista x

# Utilizando condições
x = [1,2,3,4,5]
y = [i**2 for i in x]
z = [i for i in x if i%2 == 1]
print(z)
# "i%2 == 1" Irá exibir somente os números impares
# "i%2 == 0" Irá exibir somente os números pares

# Valor a Adicionar = "i"
# Laço = (for i in x)
# Condição = (if i%2 == 1)
# i%2 = Modulo da divisão de i por 2


