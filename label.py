from customtkinter import * # Import da Biblioteca GUI

app = CTk() # Objeto que Recebe as Propriedades da Biblioteca

app.geometry("500x400") # Definição de uma Janela com a Proporção em "()"

# Adicionando uma Label Chamada "label" \ A Propriedade "master" Define Quem é o Elemento Chefe do Componente
label = CTkLabel(master = app, text = "Exemplo de Texto...", font = ("Arial", 20), text_color = "#FF00E0") # Definindo o Elemento "label", Atribuindo seu Conteúdo, Fonte e Cor

label.place(relx = 0.5, rely = 0.5, anchor = "center") # A Propriedade "place" Define Posições Fixas Para o Componente


app.mainloop() # Função que Mantém o Script em Execução