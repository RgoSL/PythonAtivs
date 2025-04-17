from customtkinter import * # Import da Biblioteca GUI

app = CTk() # Objeto que Recebe as Propriedades da Biblioteca

app.geometry("500x400") # Definição de uma Janela com a Proporção em "()"

count = 0 # Váriavel que Terá o Valor Atualizado com os Clicks

def ao_clicar(): # Definindo uma Função Chamada "ao_clicar" que Executará uma Função Quando Iniciada
   
   global count # Requisição da Váriavel "count"

   count += 999999 # Valor a Ser Adicionado à Váriavel Sempre que a Função for Ativada
   
   label.configure(text = f"Você Clicou no Botão {count} Vezes ") # Essa Linha Altera o Valor do Label Quando a Função for Ativada

# Adicionando uma Label Chamada "label" \ A Propriedade "master" Define Quem é o Elemento Chefe do Componente
label = CTkLabel(master = app, text = "Você Clicou no Botão 0 Vezes", text_color = "#FF00E0") # Definindo o Elemento "label"

btn = CTkButton(master = app, text = "Clique Aqui", corner_radius = 30, fg_color = "#DA6CA5", text_color = "#A2356D", hover_color = "#DA6CA5",
                command = ao_clicar) #  A Propriedade "command" Inicia uma Função Pré-Definida

# Definindo o Posicionamento dos Elementos Usando a Propriedade "pack"
label.pack(anchor = "s", expand = True, pady = 15)
btn.pack(anchor = "n", expand = True)


app.mainloop() # Função que Mantém o Script em Execução