# LISTAS

# Representam conjunto de dados
# Podem ser:
#   -Numéricas: [1,2,3,4,5,6,7,8]
#   -Strings: ["peixe","bola","gato"]
my_list_numbers = [1,2,3,4,5,6,7,8,9,10]
my_list_all = ["Maça",1,2,True,14.99]
my_list_fruits = ["Maça","Banana","Mamão","Melancia","Abacaxi"]
print(my_list_fruits)
print(my_list_numbers)
print(my_list_all)

tamanho = len(my_list_fruits) # Saber o tamanho da minha lista
print(tamanho)

# ADICIONAR ELEMENTOS A LISTA


my_list_fruits.append("Limão") # Append utilizado para adicionar um novo item a minha lista
print(my_list_fruits)

# FAZER VERIFICAÇÕES A LISTA

if "Abacate" in my_list_fruits: # Verificar se Abacate está na lista.
    print("Você possui abacate em sua lista de frutas.")
else: # Caso não esteja:
    print("Você não possui abacate em sua lista de frutas.")

# REMOVER ELEMENTOS A LISTA

del my_list_fruits[3:] # Apagar elementos da posição 3 em diante da lista
print(my_list_fruits)

del my_list_fruits[:] # Apagar toda a lista
print(my_list_fruits)

# ORDENAR LISTA

list = [123,433,4,54,67,4,43,2,1,2,0]
list.sort() # Sort utilizado para arrumar a lista em ordem cresente.
print(list)
list.sort(reverse=True) # Sort reverse=True utilizado para arrumar a lista em ordem decresente
print(list)
list.reverse() # Reverse utilizado para reverter a lista
print(list)

listString = ["Bola","Abacate","Dinheiro","Avião"]
listString.sort() # Agora ele irá arrumar a lista em ordem alfabetica pois a lista está em forma de string.
print(listString)