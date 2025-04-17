from customtkinter import * # Import da Biblioteca GUI

app = CTk() # Objeto que Recebe as Propriedades da Biblioteca

app.geometry("500x400") # Definição de uma Janela com a Proporção em "()"

def ao_clicar(): # Definindo uma Função Chamada "ao_clicar" que Executará uma Função Quando Iniciada
    print(f"Informações no Campo : {txtB.get('0.0', 'end')}") # Ação Atribuida à Função, Irá Exibir no Terminal a Mensagem Entre (), Juntamente do Valor Capturado no Campo

# Adicionando um Campo de Texto Chamado "txtB" \ A Propriedade "master" Define Quem é o Elemento Chefe do Componente
txtB = CTkTextbox(master = app, scrollbar_button_color = "#A2356D", corner_radius = 15, border_color = "#A2356D", border_width = 2)

btn = CTkButton(master = app, text = "Enviar", corner_radius = 30, fg_color = "#DA6CA5", text_color = "#A2356D", hover_color = "#DA6CA5" ,
                command = ao_clicar) #  A Propriedade "command" Inicia uma Função Pré-Definida

# Definindo o Posicionamento dos Elementos Usando a Propriedade "pack"
txtB.pack(anchor = "s", expand = True, pady = 15)
btn.pack(anchor = "n", expand = True)


app.mainloop() # Função que Mantém o Script em Execução