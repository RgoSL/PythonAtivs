from customtkinter import * # Import da Biblioteca GUI
import random # Import da Biblioteca Random, Permite Aleatoriedade em Funções

app = CTk() # Objeto que Recebe as Propriedades da Biblioteca

app.geometry("500x400") # Definição de uma Janela com a Proporção em "()"

vetor = ["blue", "red", "green", "yellow"] # Essa Linha Cria um Vetor Chamado "vetor", que Guarda Valores de Cores
vetor2 = [40, 60, 80, 100] # Essa Linha Cria um Vetor Chamado "vetor2", que Guarda Valores de Largura
vetor3 = [100, 80, 60, 40] # Essa Linha Cria um Vetor Chamado "vetor3", que Guarda Valores de Altura
aleatoriedade = vetor # Essa Linha Define uma Váriavel, que Recebe o Vetor das Cores
aleatoriedade2 = vetor2 # Essa Linha Define uma Váriavel, que Recebe o Vetor das Novas Larguras
aleatoriedade3 = vetor3 # Essa Linha Define uma Váriavel, que Recebe o Vetor das Novas Alturas

def ao_clicar(): # Função que Guarda Ações que Vão Ocorrer Após a Ativação do Botão
    btn.configure(fg_color = random.choice(aleatoriedade)) # Essa Linha Define que o Botão Terá uma Nova Cor ao Ser Acionado
    btn.configure(width = random.choice(aleatoriedade2)) # Essa Linha Define que o Botão Terá uma Nova Largura ao Ser Acionado
    btn.configure(height = random.choice(aleatoriedade3)) # Essa Linha Define que o Botão Terá uma Nova Altura ao Ser Acionado

# Adicionando um Botão Chamado "btn" \ A Propriedade "master" Define Quem é o Elemento Chefe do Componente | A Propriedade "command" Define Qual Ação o Botão Vai Ativar ao Ser Clicado
btn = CTkButton(master = app, text = "Clique Para Randomizar", fg_color = "blue", width = 20, height= 20, command = ao_clicar)

btn.place(relx = 0.5, rely = 0.5, anchor = "center") # A Propriedade "place" Define Posições Fixas Para o Componente


app.mainloop() # Função que Mantém o Script em Execução