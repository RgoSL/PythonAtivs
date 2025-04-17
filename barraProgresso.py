from customtkinter import * # Import da Biblioteca GUI

app = CTk() # Objeto que Recebe as Propriedades da Biblioteca

app.geometry("500x400") # Definição de uma Janela com a Proporção em "()"

# Adicionando uma Barra de Progresso Chamada "brP" \ A Propriedade "master" Define Quem é o Elemento Chefe do Componente
brP = CTkSlider(master = app, from_ = 0, to = 100, number_of_steps = 5, button_color = "#C850C0", button_hover_color = "#C850C0", progress_color = "#7548AF")

brP.place(relx = 0.5, rely = 0.5, anchor = "center") # A Propriedade "place" Define Posições Fixas Para o Componente


app.mainloop() # Função que Mantém o Script em Execução