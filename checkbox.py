from customtkinter import * # Import da Biblioteca GUI

app = CTk() # Objeto que Recebe as Propriedades da Biblioteca

app.geometry("500x400") # Definição de uma Janela com a Proporção em "()"

# Adicionando um CheckBox Chamado "chb" \ A Propriedade "master" Define Quem é o Elemento Chefe do Componente
chb = CTkCheckBox(master = app, text = "Estrangeiro", fg_color = "#C850C0", checkbox_height = 30, checkbox_width = 30, corner_radius = 36)

chb.place(relx = 0.5, rely = 0.5, anchor = "center") # A Propriedade "place" Define Posições Fixas Para o Componente


app.mainloop() # Função que Mantém o Script em Execução