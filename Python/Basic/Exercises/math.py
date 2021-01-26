# Terceiro Exercício

# Crie um programa que seja capaz,
# de resolver uma equação do segundo grau.













































from math import sqrt

a = int(input("Digite o valor de X: "))
b = int(input("Digite o valor de Y: "))
c = int(input("Digite o valor de Z: "))

try:
    delta = b**2 - 4*a*c
    raiz_delta = sqrt(delta)

    if raiz_delta < 0:
        print("Delta negativo")
    else:
        x1 = (-b + raiz_delta)/2*a
        x2 = (-b + raiz_delta)/2*a
        print("As raízes são", x1, "e", x2)
except:
    print("Não foi possível resolver esta equação.")