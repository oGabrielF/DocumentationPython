# DICIONÁRIOS

# Dicionários são listas de associações composta por:
#   -Uma chave
#   -Um valor correspondente
# dicionario = {'CHAVE':'VALOR'}

my_dictionary = {"A":"AMEIXA", "B":"BANANA", "C":"CEREJA"}
# Para localizar os valores você não ira utilizar [0],[1],[2]...
# Você utiliza a chave que você colocou exemplro:
print(my_dictionary["A"])

# Navegar pelo meu dicionário
for key in my_dictionary:
    print(key+"-"+my_dictionary[key])

for i in my_dictionary.items(): # Converte o dicionário em uma dupla.
    print(i)

for i1 in my_dictionary.values(): # Irá retornar somente os valores do meu dicionário
    print(i1)

for i2 in my_dictionary.keys(): # Retorna somente as chaves do meu dicionário
    print(i2)