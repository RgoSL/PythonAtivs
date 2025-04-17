from customtkinter import * # Import da Biblioteca GUI

app = CTk() # Objeto que Recebe as Propriedades da Biblioteca

app.geometry("500x400") # Definição de uma Janela com a Proporção em "()"

def ao_clicar(): # Definindo uma Função Chamada "ao_clicar" que Executará uma Função Quando Iniciada
    print("Botão Acionado") # Ação Atribuida à Função, Irá Exibir no Terminal a Mensagem Entre ()

 # Adicionando um Botão Chamado "btn" \ A Propriedade "master" Define Quem é o Elemento Chefe do Componente \ A Propriedade "command" Inicia uma Função Pré-Definida
btn = CTkButton(master = app, text = "Clique Aqui", command = ao_clicar)

btn.place(relx = 0.5, rely = 0.5, anchor = "center") # A Propriedade "place" Define Posições Fixas Para o Componente


app.mainloop() # Função que Mantém o Script em Execução