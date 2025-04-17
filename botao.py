from customtkinter import * # Import da Biblioteca GUI
from PIL import Image # Import da Biblioteca Pillow Para Adicionar um Ícone ao Botão

app = CTk() # Objeto que Recebe as Propriedades da Biblioteca

app.geometry("500x400") # Definição de uma Janela com a Proporção em "()"

set_appearance_mode("dark") # Propriedade que Altera Entre uma Interface Modo Escuro ou Modo Claro

img = Image.open("exem.png") # Definindo uma Imagem por Referência Externa Padrão do Pillow

# Adicionando um Botão Chamado "btn" \ A Propriedade "master" Define Quem é o Elemento Chefe do Componente
btn = CTkButton(master=app, text= "Clique Aqui", corner_radius = 32, fg_color = "#F78B0A", hover_color = "#C8720C", border_color = "#F3C147", border_width = 2, 
                image = CTkImage(dark_image = img, light_image = img))  # Atribuindo ao Botão um Ícone, Nos Dois Padrões de Tema

btn.place(relx = 0.5, rely = 0.5, anchor = "center") # A Propriedade "place" Define Posições Fixas Para o Componente


app.mainloop() # Função que Mantém o Script em Execução