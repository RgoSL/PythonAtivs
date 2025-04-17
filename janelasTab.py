from customtkinter import * # Import da Biblioteca GUI

app = CTk()  # Objeto que Recebe as Propriedades da Biblioteca

app.geometry("500x400") # Definição de uma Janela com a Proporção em "()"

tab = CTkTabview(master = app) # Definindo um Elemento Chamado "tab", Ele é um Conjunto que Permite a Transição Entre Conteúdos Diferentes
tab.pack(padx = 20, pady = 20) # Definindo a Posição Dele em Tela

# Adicionando as Telas do Conjunto
tab.add("Jan 1") 
tab.add("Jan 2")
tab.add("Jan 3")

# Atribuindo labels "lbs" às Telas do Conjunto, e Posicionando Elas com o "pack"
lb = CTkLabel(master = tab.tab("Jan 1"), text = "Primeiro Janela") 
lb.pack(padx = 20, pady = 20)

lb2 = CTkLabel(master = tab.tab("Jan 2"), text = "Segunda Janela")
lb2.pack(padx = 20, pady = 20)

lb3 = CTkLabel(master = tab.tab("Jan 3"), text = "Terceira Janela")
lb3.pack(padx = 20, pady = 20)


app.mainloop() # Função que Mantém o Script em Execução