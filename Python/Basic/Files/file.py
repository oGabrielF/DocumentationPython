# ARQUIVOS

# Funcão Open == Abrir Arquivos
# var = open(nome, modo) 
# Modos:
# r : somente leitura
# w : escrita(caso o arquivo já exista ele será apagado e um novo arquivo será criado)
# a : leitura e escrita(adiciona o novo conteudo ao fim do arquivo)
# r+ : leitura e escrita
# w+ : escrita(o modo w+, assim como o w também apaga o contéudo do arquivo anterios)
# a+ : leitura e escrita(abre o arquivo para atualização)
# read()
#   lê o arquivo inteiro
# readline()
#   lê uma linha
# readlines()
#   lê o arquivo e armazena em uma lista
file = open("file.txt")
line = file.readlines() # Pegou todas as linhas do meu arquivo e criou uma lista.
print(line)

# Criando um arquivo via code
w = open("file2.txt", "a") # Usando o modo W irá criar um arquivo pra vc
w.write("My File2") # Pegar a variavel w aonde está o arquivo e irá escrever o que você quiser
w.close() # Fechar o arquivo