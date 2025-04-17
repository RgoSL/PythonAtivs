from customtkinter import * # Import da Biblioteca GUI

app = CTk() # Objeto que Recebe as Propriedades da Biblioteca

app.geometry("500x400") # Definição de uma Janela com a Proporção em "()"

# Adicionando um Campo de Texto Chamado "txtB" \ A Propriedade "master" Define Quem é o Elemento Chefe do Componente
txtB = CTkTextbox(master = app, scrollbar_button_color = "#A2356D", corner_radius = 15, border_color = "#A2356D", border_width = 2)

txtB.place(relx = 0.5, rely = 0.5, anchor = "center") # A Propriedade "place" Define Posições Fixas Para o Componente


app.mainloop() # Função que Mantém o Script em Execução