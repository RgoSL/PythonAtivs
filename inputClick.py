from customtkinter import * # Import da Biblioteca GUI

app = CTk() # Objeto que Recebe as Propriedades da Biblioteca

app.geometry("500x400") # Definição de uma Janela com a Proporção em "()"

def ao_clicar(): # Definindo uma Função Chamada "ao_clicar" que Executará uma Função Quando Iniciada
    print(f"Texto Digitado : {input.get()}") # Ação Atribuida à Função, Irá Exibir no Terminal a Mensagem Entre (), Juntamente do Valor Capturado na Entrada

# Adicionando um Campo de Entrada Chamado "input" \ A Propriedade "master" Define Quem é o Elemento Chefe do Componente
input =  CTkEntry(master = app, placeholder_text = "Digite Aqui", placeholder_text_color = "#7FA235" , width = 300, text_color = "#9AC839")

btn = CTkButton(master = app, text = "Enviar", corner_radius = 30, text_color = "#69852D", fg_color = "#9AC839", hover_color = "#9AC839",
                command = ao_clicar)  #  A Propriedade "command" Inicia uma Função Pré-Definida

# Definindo o Posicionamento Desses Elementos na Tela
input.pack(anchor = "s", expand = True, pady = 15)
btn.pack(anchor = "n", expand = True)


app.mainloop() # Função que Mantém o Script em Execução