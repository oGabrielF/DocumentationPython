# COMANDO IF

# Realiza testes condicionais.
# Executa um bloco se uma determinada condição for atendida.
# Avalia-se condição é verdadeira ou não.
# IF significa SE ou seja:
# A linha de baixo se lê: (Se x for igual a y:)
# if x == y:
#   print("x é maior que y")

# Sintaxe:
# if condição:
#      Executa_O_Code_Que_Tiver_Aqui

x = 1
y = 2

# Essa linha de baixo não foi exibida no console pois x não é maior que y então o comando ira parar pois não possui um else
if x > y: # Essa linha se lê: (Se x for maior que y:)
    print("x é maior que y")

if y > x: # Essa linha se lê: (Se y for maior que x:)
    print("y é maior que x")

# COMANDO ELSE

# O comando ELSE significa SE NÃO ou seja:
# x = 1 / y = 2
# if x > y:
#   print("x é maior que y") 
# else:
#   print("x não é maior que y")
# O comando acima se lê: (Se x for maior que y: [executa uma linha de codigo] Se não: [Executa outra linha de codigo])
a = 1
b = 2

if a > b:
    print("a é maior que b")
else:
    print("a não é maior que b")

# COMANDO ELIF

# Caso haja necessidade de mais condições entre o if e o else
# ELIF siginifa SE NÃO SE ou seja:
if x == y: # Fazendo uma verificação
    print("x é igual a y")
elif x == a: # Caso a verificação de cima der false ira começar essa verificação
    print("x é igual a c")
else: # Caso as duas verificações de cima der falso irá passar essa linha de code
    print("Todos os resultados estão errados.")


c = 1
d = 2
if x == y:
    print("Números Iguais")
elif y > x:
    print("y maior que x")
else:
    print("Número Diferentes")