# TIPOS DE DADOS STRINGS

# Concatenação significar somar strings
# Strings é um tipo de dado em que se armazena texto.
# São declaradas entre aspas.
# var1 = 1
# var2 = "1"
# Nesse caso var1 é um númeral enquando var2 é uma string
var1 = "Gabriel"
var2 = "Oliveira"

concatenar = var1 + var2 # Irá fazer a "soma" das duas variaveis no caso o resultado foi GabrielOliveira
print(concatenar)

# Para dar espaço utilize
concatenar1 = var1 + " " + var2 # Realizou a "soma" das duas variaveis junto com o espaço no meio.
print(concatenar1)

tamanho = len(concatenar1) # Irá fazer a contagem das letras que possui.
print(tamanho)

# G = 0
# A = 1
# B = 2
# R = 3
# I = 4
# E = 5
# L = 6
print(var1[3]) # Irá pegar a posiçaõ da letra,no caso foi 3 pq em computação começamos contar do 0
print(concatenar1[0:7]) # Primeiro valor é aonde vai começar a exibir e o segundo valor aonde vai terminar de exibir

seq = "CDCEDEDEFSADDSADSADEFDFAFDDA"
seq = seq.lower() # Lower é utilizado para deixar as letras tudo em minusculo.
print(seq)
print(concatenar1.upper()) # Upper é utilizado para deixar as letras tudo em maiusculo.
# .Strip remove caracteres especiais.

seq1 = "DEFD DEFF DESA DEGF CGTD DESA CVCV XXXX"
print(seq1.split()) # Split é utilizado para transformar a string em uma lista com varios argumentos.
print(seq1.split("D")) # Colocando esse atributo D ele irá imprimir novamente a lista porem sem a letra D.
# Case sensitive tbm se aplica no exemplo acima.

busca = seq1.find("XXXX") # find é utilizado para encontrar algo.
print(busca)
print(seq1[busca:]) # Irá imprir de busca até o final.
# Caso ele não encontre sua string ele irá retornar -1

# Substituir uma parte de uma string
my_string = "O Gabriel é muito bom no basquete"

my_string = my_string.replace("bom", "foda") # Replace é utilizado para substituir uma palavra por outra em uma string
print(my_string)
