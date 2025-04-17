from customtkinter import * # Import da Biblioteca GUI

app = CTk() # Objeto que Recebe as Propriedades da Biblioteca

app.geometry("500x400") # Definição de uma Janela com a Proporção em "()"

# Adicionando um ComboBox Chamado "cbx" \ A Propriedade "master" Define Quem é o Elemento Chefe do Componente \ A Propriedade "values" Define Quantas e Quais são as Opções do ComboBox
cbx = CTkComboBox(master = app, values = ["Felipe", "Jefferson", "Salomão"], fg_color = "#0CE9C4", text_color = "#54716C",
                  border_color = "#499E8F", dropdown_fg_color = "#0093E9") 

cbx.place(relx = 0.5, rely = 0.5, anchor = "center") # A Propriedade "place" Define Posições Fixas Para o Componente


app.mainloop() # Função que Mantém o Script em Execução