# Quinto Exercício

# Crie um programa que receba dois números,
# e um sinal e resolva a operação matemática definida pelo sinal.













































numberOne = int(input("Digite o primeiro número: "))
sinal = input("Digite o sinal da operação: ")
numberTwo = int(input("Digite o segundo número: "))

try:

    if sinal == "+":
        op = numberOne + numberTwo
        print("O resultado da operação é:", op)

    elif sinal == "-":
        op = numberOne - numberTwo
        print("O resultado da operação é:", op)

    elif sinal == "/":
        op = numberOne / numberTwo
        print("O resultado da operação é:", op)

    elif sinal == "*":
        op = numberOne * numberTwo
        print("O resultado da operação é:", op)

    else:
        print("Sinal Inválido.")
except:
    print("Não foi possível realizar a operação")