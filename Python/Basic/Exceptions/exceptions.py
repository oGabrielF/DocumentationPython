# TRATAMENTO DE EXCEÇÕES

# Dois divido por dois vai dar 1
a = 2
b = 2
print(a/b)
# Agora se eu tentar dividir dois por zero vai dar erro e o programa vai parar
x = 2 
y = 0
# Para evitar o erro você pode utilizar o try que significa "tentar"
c = 2
d = 0

# Com o try ele vai tentar executar a ação
try:
    print(c/d)
# Caso não seja possível ele ira passar a ter uma exceção ou seja um except que irá passar uma outra ação.
except:
    print("Não é permitido dividir qualquer número por zero.")

