# Teste Para Dividir o Processamento Entre a Listagem e a Interface Usando Controle de Processos (Threads)


from customtkinter import *# Biblioteca Usada Para Criar a Interface do Teste

import threading # Biblioteca de Controle de Processos do Sistema

import winreg # Biblioteca Para Identificar Ações do Windows

from tkinter import * # Outra Biblioteca de Interfaces, Usada Para uma Feat Especifica de Lista


# Função Principal Para Trazer a Busca de Apps Para uma Thread Controlada
def listar_programas_thread():
    lista_programas.delete(0, 'end') # Método Para Resetar a Lista ao Iniciar Sempre 

    # Função de Listagem dos Programas do PC
    def listar_programas():
        caminhos = [ # As Rotas são dos Caminhos Mais Convencionais, não são Personalizadas
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
            r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
        ]

    # Laço Para Atribuir Identificação Para os Apps Encontrados em Cada Caminho
        for caminho in caminhos: 
            try:
                chave = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, caminho) # Uso da Biblioteca de Ações do Windows Aqui
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

    # Executando a Função em uma Thread Controlada
    thread = threading.Thread(target = listar_programas)
    thread.start()

# Executa a Chamada da Função de Listagem
def iniciar_listagem():
    listar_programas_thread()

# Criação da Interface Onde os Apps Serão Exibidos
app = CTk() # Inicialização da Tela no Padrão da Biblioteca
app.geometry("400x400") # Definição das Dimensões da Interface

# Propriedade List do TK, Passando Junto da Interface CTK
lista_programas = Listbox(app)
lista_programas.pack(expand = True, fill = "both")

# Criação e Estilização do Botão que Chama a Função de Listagem
botao = CTkButton(app, text = "Listar Programas", command = iniciar_listagem) 
botao.pack(pady = 10) # Posicionamento do Botão em Relação a Interface

app.mainloop() # Chamada da Interface