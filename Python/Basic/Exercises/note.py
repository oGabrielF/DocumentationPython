# Segundo Exercício

# Faça um programa que receba duas notas digitadas pelo usuário.
# Se a nota for maior ou igual a seis,escreva aprovado,senão escreva reprovado.













































noteOne = float(input("Digite sua nota de MT: "))
noteTwo = float(input("Digite sua nota de LP: "))

media = (noteOne+noteTwo)/2

if media >= 6:
    print("Este aluno foi aprovado na ETEC com a media de", media)
else:
    print("Este aluno foi reprovado na ETEC.")