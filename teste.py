# Teste Para Listagem Rudimentar e Exibição em uma Interface Diretamente


from customtkinter import *# Biblioteca Usada Para Criar a Interface do Teste

import winreg # Biblioteca Para Identificar Ações do Windows

from tkinter import * # Outra Biblioteca de Interfaces, Usada Para uma Feat Especifica de Lista

    # Função de Listagem dos Programas do PC
def listar_programas():
    lista_programas.delete(0, 'end') 

    caminhos = [ # As Rotas são dos Caminhos Mais Convencionais, não são Personalizadas
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]

    # Laço Para Atribuir Identificação Para os Apps Encontrados em Cada Caminho
    for caminho in caminhos:
        try:
            chave = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, caminho)
            for i in range(winreg.QueryInfoKey(chave)[0]):
                subchave_nome = winreg.EnumKey(chave, i)
                subchave = winreg.OpenKey(chave, subchave_nome)
                try:
                    nome = winreg.QueryValueEx(subchave, "DisplayName")[0]
                    lista_programas.insert('end', nome)
                except FileNotFoundError:
                    continue
        except FileNotFoundError:
            continue

def iniciar_listagem():
    listar_programas()

# Criação da Interface Onde os Apps Serão Exibidos
app = CTk() # Inicialização da Tela no Padrão da Biblioteca
app.geometry("400x400") # Definição das Dimensões da Interface

# Propriedade List do TK, Passando Junto da Interface CTK
lista_programas = Listbox(app)
lista_programas.pack(expand = True, fill = "both")

# Criação e Estilização do Botão que Chama a Função de Listagem
botao = CTkButton(app, text = "Listar Programas", command = iniciar_listagem)
botao.pack(pady = 10) # Posicionamento do Botão em Relação a Interface

app.mainloop() #  Chamada da Interface