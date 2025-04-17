from customtkinter import * # Import da Biblioteca GUI

app = CTk() # Objeto que Recebe as Propriedades da Biblioteca

app.geometry("500x400") # Definição de uma Janela com a Proporção em "()"

set_default_color_theme("green") # Propriedade que Define uma Cor Padrão Para Todo Elemento Capaz de Ser Editado no Sistema

CTkButton(master = app, text = "Botão").pack(pady = 20, padx = 20) # Essa Linha Define um Botão
CTkCheckBox(master = app, text = "CheckBox").pack(pady = 20, padx = 20) # Essa Linha Define um Item Check
CTkComboBox(master = app, values = ["São Paulo", "Bahia", "Guadalupe"]).pack(pady = 20, padx = 20) # Essa Linha Define uma Caixa de Opções
CTkEntry(master = app, placeholder_text = "Digite Aqui").pack(pady = 20, padx = 20) # Essa Linha Define um Input
CTkProgressBar(master = app).pack(pady = 20, padx = 20) # Essa Linha Define uma Barra de Progresso Não Escalável
CTkRadioButton(master = app, text = "Botão Opcional").pack(pady = 20, padx = 20) # Essa Linha Define um Botão Radius
CTkSlider(master = app).pack(pady = 20, padx = 20) # Essa Linha Define uma Barra Estática
CTkSwitch(master = app, text = "Opção").pack(pady = 20, padx = 20) # Essa Linha Define um Botão com um Sistema Booleano

app.mainloop() # Função que Mantém o Script em Execução