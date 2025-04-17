from customtkinter import * # Import da Biblioteca GUI

app = CTk() # Objeto que Recebe as Propriedades da Biblioteca

app.geometry("500x400") # Definição de uma Janela com a Proporção em "()"

# Essa Linha Define um Container Dentro da Janela Principal (um Frame) Chamdo "frame", Ele é do Tipo "scrollable", o que Permite um Layout Mais Fléxivel e "Infinito" de Itens Verticais
frame = CTkScrollableFrame(master = app, fg_color = "#8D6F3A", border_color = "#FFCC70", border_width = 2, orientation = "vertical", scrollbar_button_color = "#FFCC70")
frame.pack(expand = True) # A Propriedade "expand" Permite um Ajuste Automático e Flexível dos Elementos que Forem Adicionados a Esse Container

#
label = CTkLabel(master = frame, text = "Conjunto Principal") # Nessa Linha é Definida uma Label Para o Container
input = CTkEntry(master = frame, placeholder_text = "Digite Aqui") # Nessa Linha é Definido um Input 
btn = CTkButton(master = frame, text = "Enviar") # E Nessa é Definido um Botão

# Aqui São Definidos os Posicionamentos dos Elementos 
label.pack(anchor = "s", expand = True, pady = 15, padx = 30)
input.pack(anchor = "s", expand = True, pady = 15, padx = 30)
btn.pack(anchor = "n", expand = True, pady = 30, padx = 20)

# Essas Linhas Criam Múltiplos Botões Para Testar o Layout Flexível Desse Tipo de Frame
CTkButton(master = frame, text = "Elementos").pack(expand = True, padx = 30, pady = 20)
CTkButton(master = frame, text = "Elementos").pack(expand = True, padx = 30, pady = 20)
CTkButton(master = frame, text = "Elementos").pack(expand = True, padx = 30, pady = 20)
CTkButton(master = frame, text = "Elementos").pack(expand = True, padx = 30, pady = 20)
CTkButton(master = frame, text = "Elementos").pack(expand = True, padx = 30, pady = 20)


app.mainloop() # Função que Mantém o Script em Execução