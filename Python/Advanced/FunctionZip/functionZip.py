# FUNÇÃO ZIP

# Function Zip serve para você juntar 2 ou mais lista ao mesmo tempo.

number = [1,2,3,4,5]
fruits = ["Maça","Banana","Jabuticaba","Uva","Morango"]
price = ["R$10,00","R$6,90","14,90","R$16,90","R$24,90"]

# Para utilizar a função zip é necessarios exibir os argumentos que no caso seria as listas.
for number, name, value in zip(number, fruits, price):
    print(number, name, value)

# Number = Relacionado a lista1
# Name = Relacionado a lista2
# Value = Relacionado a lista3

