from customtkinter import * # Import da Biblioteca GUI

app = CTk() # Objeto que Recebe as Propriedades da Biblioteca

app.geometry("500x400") # Definição de uma Janela com a Proporção em "()"

frame = CTkFrame(master = app, fg_color = "#8D6F3A", border_color = "#FFCC70", border_width = 2) # Essa Linha Define um Container Dentro da Janela Principal (um Frame) Chamdo "frame"
frame.pack(expand = True)  # A Propriedade "expand" Permite um Ajuste Automático e Flexível dos Elementos que Forem Adicionados a Esse Container

label = CTkLabel(master = frame, text = "Conjunto Principal") # Nessa Linha é Definida uma Label Para o Container
input = CTkEntry(master = frame, placeholder_text = "Digite Aqui") # Nessa Linha é Definido um Input 
btn = CTkButton(master = frame, text = "Enviar") # E Nessa é Definido um Botão

# Aqui São Definidos os Posicionamentos dos Elementos 
label.pack(anchor = "s", expand = True, pady = 15, padx = 30) 
input.pack(anchor = "s", expand = True, pady = 15, padx = 30)
btn.pack(anchor = "n", expand = True, pady = 30, padx = 20)


app.mainloop() # Função que Mantém o Script em Execução