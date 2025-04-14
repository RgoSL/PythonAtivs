# Atividade -

# Criar uma pasta chamada "Verificar login", dentro dela adicione os arquivos "Senha.txt" e "Login.py".
# Desenvolva um código utilizando o comando "With open" para ler o arquivo "Senha.txt", em seguida faça uma condicional para reconhecer se uma senha digitada é igual ao valor da senha definido no arquivo.


# 1º Passo : Definir uma váriavel para receber o valor do input
inputSn = input("Digite a Senha :")

# 2º Passo : Fazer a condicional que lê o arquivo Senha.txt
with open(r'D:\CÓDIGOS\ativ-drigo\senha.txt', 'r', encoding='utf-8') as Arquivo:
    for linha in Arquivo:
        senhaConferida = linha.strip()

# 3º Passo : Comparar o valor lido com o valor introduzido
    if inputSn != senhaConferida:
        print("Senha Incorreta")
    else:
        print("Logando Usuário...")


