# FUNCÕES

# Blocos de códigos.
# Executadas apenas quando chamados.
# Em Python as function são definidas usando def
# Definição:
#   def qualquer_name(PARÂMETROS):
#       ~COMANDOS
# Chamada:
#   qualquer_name(ARGUMENTOS) ARGUMENTOS = PARAMENTROS

def soma(x, y): # Uma function para somar
    return x + y

def mult(x, y):
    return x * y

s = soma(2, 3) # Irá somar o valor 2 + 3 que é x e y
m = mult(5, 5) # Irá multiplicar o valor de 5, 5 que é x e y
print(s)
print(m)
print(soma(s, m)) # Irá somar a variavel s que é 2 + 3 e a variavel m que é 5 * 5

