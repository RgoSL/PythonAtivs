from customtkinter import * # Import da Biblioteca GUI

app = CTk() # Objeto que Recebe as Propriedades da Biblioteca

app.geometry("500x400") # Definição de uma Janela com a Proporção em "()"

# Adicionando um Switch Chamado "switch" \ A Propriedade "master" Define Quem é o Elemento Chefe do Componente
switch = CTkSwitch(master = app, text = "Estrangeiro")

switch.place(relx = 0.5, rely = 0.5, anchor = "center") # A Propriedade "place" Define Posições Fixas Para o Componente


app.mainloop() # Função que Mantém o Script em Execução