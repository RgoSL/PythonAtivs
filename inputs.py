from customtkinter import * # Import da Biblioteca GUI

app = CTk() # Objeto que Recebe as Propriedades da Biblioteca

app.geometry("500x400") # Definição de uma Janela com a Proporção em "()"

# Adicionando um Campo de Entrada Chamado "input" \ A Propriedade "master" Define Quem é o Elemento Chefe do Componente
input =  CTkEntry(master = app, placeholder_text = "Digite Aqui", placeholder_text_color = "#7FA235" , width = 300, text_color = "#9AC839")

input.place(relx = 0.5, rely = 0.5, anchor = "center") # A Propriedade "place" Define Posições Fixas Para o Componente


app.mainloop() # Função que Mantém o Script em Execução