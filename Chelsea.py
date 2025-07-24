import cv2 # Importando o Módulo do OpenCV

import customtkinter # Importando o Módulo Para Interfaces

from PIL import Image, ImageTk # Importando o Módulo de Ferramentas Para Imagens

def Play(caminhoVideo, Label, Janela):
    Cap = cv2.VideoCapture(caminhoVideo) # Lendo o Arquivo de Vídeo a Partir do Caminho Especificado

    def AdicionarVideo():
        ret, Tela = Cap.read() # Lê Frame por Frame do Vídeo
        if ret:
            Tela = cv2.cvtColor(Tela, cv2.COLOR_BGR2RGB) # Faz uma Conversão dos Padrões de Cores dos Vídeos
            Img = Image.fromarray(Tela) # Converte o Frame Para um Objeto do Pillow
            ImgCtk = ImageTk.PhotoImage(image = Img) # Converte a Imagem Para um Formato Aceito pelo Tkinter
            Label.Imgctk = ImgCtk # Exibe o Vídeo Dentro do Label
            Label.configure(image = ImgCtk) # Atualiza os Frames do Vídeo
            Janela.after(30, AdicionarVideo) # Define uma Taxa de 30 FPS Para o Vídeo
            
        else:
            Cap.set(cv2.CAP_PROP_POS_FRAMES, 0) # Esse Comando faz o Vídeo Sempre Reiniciar do "Primeiro Frame"
            Janela.after(10, AdicionarVideo) 

    AdicionarVideo() # Chama a Função Pela Primeira Vez Para Iniciar o Loop de Reprodução

# Criando a Janela de Exibição
customtkinter.set_appearance_mode("System") # Define o Tema da Interface, Esse Modo Segue o Padrão do Próprio Sistema 

Janela = customtkinter.CTk() # Inicializando uma Janela CTK
Janela.geometry("800x600") # Definindo a Dimensão Dessa Janela
Janela.title("Janela do Vídeo") # Definindo um Título Para a Janela

Label = customtkinter.CTkLabel(master = Janela, text = "") # Criando um Label Para Exibir o Vídeo do Gatinho
Label.pack(pady = 20, padx = 10) # Definindo uma Posição Para Esse Label

caminhoVideo = r"" # O Caminho Para o Vídeo é Guardado por Essa Variável. o r ao Lado é Para o Compilador não Entender as Possiveis \ do Diretório de Forma Literal

Play(caminhoVideo, Label, Janela) # Inicia a Reprodução do Vídeo na Interface

Janela.mainloop() # Mantem a Janela Sempre Aberta
