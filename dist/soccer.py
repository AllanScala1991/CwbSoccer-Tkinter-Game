from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk
import random
import time

#VARIAVEIS GLOBAIS
cordefundo = '#78F898'
Times = ['Santos','Palmeiras','São Paulo','Corinthians']
Rodadas = [1]
JogadoresSantos = ['Sampaoli','Vanderlei','Felipe Aguilar','Gustavo Henrique','Jorge','Victor Ferraz','Diego Pituca',
'Alison','Jean Motta','Rodrygo', 'Carlos Sanchez','Derliz Gonzales']
JogadoresPalmeiras = ['Felipão','Weverton','Edu Dracena','Antonio Carlos','Diogo Barbosa', 'Marcos Rocha','Felipe Melo',
'Bruno Henrique','G. Scarpa','Dudu','Ricardo Goulart','Deyverson']
JogadoresSaoPaulo = ['Cuca','Thiago Volpi','Bruno Alves','Anderson Martins','Bruno Peres','Reinaldo','Jucilei','Hudson',
'Hernanes','Éverton','Alexandre Pato','Pablo']
JogadoresCorinthians = ['Fabio Carile','Cassio','Henrique','Manoel','Danilo Avelar','Fagner','Ralf','Junior Urso',
'Jadson','Pedrinho','Clayson','Vagner Love']
Teams = []
SantosPT = [0,0]
PalmeirasPT = [0,0]
SaoPauloPT = [0,0]
CorinthiansPT = [0,0]






def Inicio () :
    #INICIALIZADOR
    janela = Tk()
    janela.title('Soccer CWB - Inicio')
    janela['bg'] = '#78F898'
    janela.minsize(width = 1280, height = 720)
    janela.maxsize(width = 1280, height = 720)

    #FUNÇÕES
    def BotaoJogar():
        janela.destroy()
        SelecionaTime()
    


    #TEXTO PRINCIPAL
    ImgLogo = Image.open('imagens/titulo.png')
    ImgTitulo = ImageTk.PhotoImage(ImgLogo)
    Titulo = Label(janela, image=ImgTitulo,bg=cordefundo)
    Titulo.place(x=400,y=10)
    #BOTOES E LABELS
    ImgBotaoJogar = Image.open('imagens/play.png')
    ImgJogar = ImageTk.PhotoImage(ImgBotaoJogar)
    BotaoJogar2 = Button(janela,image=ImgJogar, bg=cordefundo,command=BotaoJogar)
    BotaoJogar2.place(x=500,y=430)
    TextoBotaoJogar = Label(janela,text='JOGAR',font=('Comic Sans',30,'bold'),bg=cordefundo)
    TextoBotaoJogar.place(x=600,y=440)

    #CREDITOS
    Creditos1= Label(janela,text='Desenvolvido por Allan Scala',font=('Comic Sans',10,'bold'),bg=cordefundo)
    Creditos1.place(x=550,y=680)

    #ESCUDOS TIMES
    ImgSantos = Image.open('imagens/santosescudo.png')
    ImgSantosEscudo = ImageTk.PhotoImage(ImgSantos)
    SantosEscudo = Label(janela,image=ImgSantosEscudo,bg=cordefundo)
    SantosEscudo.place(x=100,y=50)
    
    ImgPalmeiras = Image.open('imagens/palmeiras.png')
    ImgPalmeirasEscudo = ImageTk.PhotoImage(ImgPalmeiras)
    PalmeirasEscudo = Label(janela,image=ImgPalmeirasEscudo,bg=cordefundo)
    PalmeirasEscudo.place(x=100,y=550)

    ImgCampPaulista = Image.open('imagens/campeonatopaulista.png')
    ImgCampPaulistaLogo = ImageTk.PhotoImage(ImgCampPaulista)
    CampPaulistaLogo = Label(janela,image=ImgCampPaulistaLogo,bg=cordefundo)
    CampPaulistaLogo.place(x=100,y=300)

    ImgSaoPaulo = Image.open('imagens/saopaulo.png')
    ImgSaoPauloEscudo = ImageTk.PhotoImage(ImgSaoPaulo)
    SaoPauloEscudo = Label(janela,image=ImgSaoPauloEscudo,bg=cordefundo)
    SaoPauloEscudo.place(x=1000,y=50)

    ImgCampPaulista2 = Image.open('imagens/campeonatopaulista.png')
    ImgCampPaulistaLogo2 = ImageTk.PhotoImage(ImgCampPaulista2)
    CampPaulistaLogo2 = Label(janela,image=ImgCampPaulistaLogo2,bg=cordefundo)
    CampPaulistaLogo2.place(x=1000,y=300)

    ImgCorinthians = Image.open('imagens/corinthians.png')
    ImgCorinthiansEscudo = ImageTk.PhotoImage(ImgCorinthians)
    CorinthiansEscudo = Label(janela,image=ImgCorinthiansEscudo,bg=cordefundo)
    CorinthiansEscudo.place(x=1000,y=550)
   
    janela.mainloop()
#===================================================================================================================================================================================
#===================================================================================================================================================================================    
def SelecionaTime():
    #INICIALIZADOR
    janela2 = Tk()
    janela2.title('Soccer CWB - Seleção de time')
    janela2['bg']= cordefundo
    janela2.minsize(width =1280, height = 720)
    janela2.maxsize(width =1280, height = 720)
    
   
    

    #FUNÇÕES BOTOES
    def Santos():
        janela2.destroy()
        Teams.append('SANTOS')
        PlantelSantos()
        
    def Palmeiras():
        janela2.destroy()
        Teams.append('PALMEIRAS')
        PlantelPalmeiras()
        
    def SaoPaulo():
        janela2.destroy()
        Teams.append('SAO PAULO')
        PlantelSaoPaulo()
    def Corinthians():
        janela2.destroy()
        Teams.append('CORINTHIANS')
        PlantelCorinthians()


    #BOTÕES E LABELS
    titulo = Label(janela2,text='SELECIONE UM TIME',font=('Impact',60,'bold'),bg=cordefundo)
    titulo.place(x=320,y=50)

    BotaoSantos = Button(janela2,text='SANTOS',font=('Impact',20,'bold'),bg='black',fg='white',width=15,command=Santos)
    BotaoSantos.place(x=100,y=290)
    ImgSantos = Image.open('imagens/santosescudo.png')
    ImgSantosEscudo = ImageTk.PhotoImage(ImgSantos)
    SelecionarSantos = Label(janela2,image=ImgSantosEscudo,bg=cordefundo)
    SelecionarSantos.place(x=350,y=250)

    BotaoPalmeiras = Button(janela2,text='PALMEIRAS',font=('Impact',20,'bold'),bg='green',fg='white',width=15,command=Palmeiras)
    BotaoPalmeiras.place(x=100,y=490)
    ImgPalmeiras = Image.open('imagens/palmeiras.png')
    ImgPalmeirasEscudo = ImageTk.PhotoImage(ImgPalmeiras)
    SelecionarPalmeiras = Label(janela2,image=ImgPalmeirasEscudo,bg=cordefundo)
    SelecionarPalmeiras.place(x=350,y=450)

    BotaoSaoPaulo = Button(janela2,text='SÃO PAULO',font=('Impact',20,'bold'),bg='red',fg='black',width=15,command=SaoPaulo)
    BotaoSaoPaulo.place(x=950,y=290)
    ImgSaoPaulo = Image.open('imagens/saopaulo.png')
    ImgSaoPauloEscudo = ImageTk.PhotoImage(ImgSaoPaulo)
    SelecionarSaoPaulo = Label(janela2,image=ImgSaoPauloEscudo,bg=cordefundo)
    SelecionarSaoPaulo.place(x=770,y=250)

    BotaoCorinthians = Button(janela2,text='CORINTHIANS',font=('Impact',20,'bold'),bg='white',fg='black',width=15,command=Corinthians)
    BotaoCorinthians.place(x=950,y=490)
    ImgCorinthians = Image.open('imagens/corinthians.png')
    ImgCorinthiansEscudo = ImageTk.PhotoImage(ImgCorinthians)
    SelecionarCorinthians = Label(janela2,image=ImgCorinthiansEscudo,bg=cordefundo)
    SelecionarCorinthians.place(x=770,y=450)

    janela2.mainloop()

#=========================================================================================================================
#=========================================================================================================================
def PlantelSantos():
    #INICIALIZADOR
    janela3 = Tk()
    janela3.title('Soccer CWB - Plantel do Time')
    janela3.minsize(width =1280, height = 720)
    janela3.maxsize(width =1280, height = 720)

    
    #CAPA DO TIME
    janela3['bg'] = 'black'
    TituloSantos = Label(janela3,text='SANTOS',font=('Arial Black',68,'bold'),bg='black',fg='white')
    TituloSantos.place(x=440,y=30)
    ImgMascote = Image.open('imagens/mascotesantos.png')
    MascoteImg = ImageTk.PhotoImage(ImgMascote)
    MascoteSantos = Label(janela3,image=MascoteImg,bg='black')
    MascoteSantos.place(x=50,y=30)
    MascoteSantos2 = Label(janela3,image=MascoteImg,bg='black')
    MascoteSantos2.place(x=1080,y=30)
    SantosPlayers = Text(janela3,width=25,height=25)
    SantosPlayers.place(x=0,y=200)
    SantosPlayers.configure(font=('Arial Black',10,'bold'))
    SantosPlayers.insert(INSERT,'ELENCO SANTOS:\n\n')
    SantosPlayers.insert(INSERT,'Tecnico - '+ JogadoresSantos[0]+'\n\n')
    SantosPlayers.insert(INSERT,'GL - '+ JogadoresSantos[1] +'\n\n')
    SantosPlayers.insert(INSERT,'ZG - '+ JogadoresSantos[2]+'\n\n')
    SantosPlayers.insert(INSERT,'ZG - '+ JogadoresSantos[3]+'\n\n')
    SantosPlayers.insert(INSERT,'LD - '+ JogadoresSantos[4]+'\n\n')
    SantosPlayers.insert(INSERT,'LE - '+ JogadoresSantos[5]+'\n\n')
    SantosPlayers.insert(INSERT,'VL - '+ JogadoresSantos[6]+'\n\n')
    SantosPlayers.insert(INSERT,'VL - '+ JogadoresSantos[7]+'\n\n')
    SantosPlayers.insert(INSERT,'MEI - '+ JogadoresSantos[8]+'\n\n')
    SantosPlayers.insert(INSERT,'MEI - '+ JogadoresSantos[9]+'\n\n')
    SantosPlayers.insert(INSERT,'ATA - '+ JogadoresSantos[10]+'\n\n')
    SantosPlayers.insert(INSERT,'ATA - '+ JogadoresSantos[11]+'\n\n')
    
    #FUNÇÃO DO BOTAO INICAR
    def IniciarPartida():
        if Rodadas[0] == 1:
            janela3.destroy()
            Rodada1()
        if Rodadas[0] == 2:
            janela3.destroy()
            Rodada2()
        if Rodadas[0] == 3:
            janela3.destroy()
            Rodada3()
        if Rodadas[0] == 4:
            janela3.destroy()
            Rodada4()
        if Rodadas[0] == 5:
            janela3.destroy()
            Rodada5()
        if Rodadas[0] == 6:
            janela3.destroy()
            Rodada6()

    
    #RODADAS
    if(Rodadas[0] == 1):
        ProximoJogo = Text(janela3,width=20,height=10)
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 1''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[0] + ' x '+  Times[1]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[2]+' x ' + Times[3]+'\n\n')
    if(Rodadas[0]==2):
        ProximoJogo = Text(janela3,width=20,height=10)
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 2''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[3] + ' x ' +  Times[0]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[1]+ ' x ' + Times[2]+'\n\n')
    if(Rodadas[0]==3):
        ProximoJogo = Text(janela3,width=20,height=10)
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 3''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[2] + ' x ' +  Times[0]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[1]+ ' x ' + Times[3]+'\n\n')
    if(Rodadas[0]==4):
        ProximoJogo = Text(janela3,width=20,height=10)
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 4''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[1] + ' x '+  Times[0]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[3]+ ' x ' + Times[2]+'\n\n')
    if(Rodadas[0]==5):
        ProximoJogo = Text(janela3,width=20,height=10)
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 5''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[0] + ' x ' +  Times[3]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[2]+ ' x ' + Times[1]+'\n\n')
    if(Rodadas[0]==6):
        ProximoJogo = Text(janela3,width=20,height=10)
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 6''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[0] + ' x ' +  Times[2]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[3]+ ' x ' + Times[1]+'\n\n')
    #BOTOES
    ImgBotao = Image.open('imagens/botaobola.png')
    BotaoImg = ImageTk.PhotoImage(ImgBotao)
    BotaoIniciarPartida = Button(janela3,image=BotaoImg,bg='black',command =IniciarPartida)
    BotaoIniciarPartida.place(x=900,y=350)
    IniciarLabel = Label(janela3,text='INICIAR JOGO',font=('Arial Black',12,'bold'),bg='black',fg='white')
    IniciarLabel.place(x=900,y=490)
    janela3.mainloop()


def PlantelPalmeiras():
    #INICIALIZADOR
    janela3 = Tk()
    janela3.title('Soccer CWB - Plantel do Time')
    janela3.minsize(width =1280, height = 720)
    janela3.maxsize(width =1280, height = 720)

    #CAPA DO TIME
    janela3['bg'] = '#1bcc35'
    Titulo = Label(janela3,text='PALMEIRAS',font=('Arial Black',68,'bold'),bg='#1bcc35',fg='white')
    Titulo.place(x=370,y=30)
    ImgMascote99 = Image.open('imagens/mascotepalmeiras.jpg')
    MascoteImg99 = ImageTk.PhotoImage(ImgMascote99)
    Mascote = Label(janela3,image=MascoteImg99,bg='#1bcc35')
    Mascote.place(x=50,y=30)
    Mascote2 = Label(janela3,image=MascoteImg99,bg='#1bcc35')
    Mascote2.place(x=1080,y=30)
    Players = Text(janela3,width=25,height=25)
    Players.place(x=0,y=200)
    Players.configure(font=('Arial Black',10,'bold'))
    Players.insert(INSERT,'ELENCO PALMEIRAS:\n\n')
    Players.insert(INSERT,'Tecnico - '+ JogadoresPalmeiras[0]+'\n\n')
    Players.insert(INSERT,'GL - '+ JogadoresPalmeiras[1] +'\n\n')
    Players.insert(INSERT,'ZG - '+ JogadoresPalmeiras[2]+'\n\n')
    Players.insert(INSERT,'ZG - '+ JogadoresPalmeiras[3]+'\n\n')
    Players.insert(INSERT,'LD - '+ JogadoresPalmeiras[4]+'\n\n')
    Players.insert(INSERT,'LE - '+ JogadoresPalmeiras[5]+'\n\n')
    Players.insert(INSERT,'VL - '+ JogadoresPalmeiras[6]+'\n\n')
    Players.insert(INSERT,'VL - '+ JogadoresPalmeiras[7]+'\n\n')
    Players.insert(INSERT,'MEI - '+ JogadoresPalmeiras[8]+'\n\n')
    Players.insert(INSERT,'ATA - '+ JogadoresPalmeiras[9]+'\n\n')
    Players.insert(INSERT,'ATA - '+ JogadoresPalmeiras[10]+'\n\n')
    Players.insert(INSERT,'ATA - '+ JogadoresPalmeiras[11]+'\n\n')
    
    #FUNÇÃO DO BOTAO INICAR
    def IniciarPartida():
        if Rodadas[0] == 1:
            janela3.destroy()
            Rodada1()
        if Rodadas[0] == 2:
            janela3.destroy()
            Rodada2()
        if Rodadas[0] == 3:
            janela3.destroy()
            Rodada3()
        if Rodadas[0] == 4:
            janela3.destroy()
            Rodada4()
        if Rodadas[0] == 5:
            janela3.destroy()
            Rodada5()
        if Rodadas[0] == 6:
            janela3.destroy()
            Rodada6()
    
    #RODADAS
    if(Rodadas[0] == 1):
        ProximoJogo = Text(janela3,width=20,height=10)
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 1''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[0] + ' x '+  Times[1]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[2]+' x ' + Times[3]+'\n\n')
    if(Rodadas[0]==2):
        ProximoJogo = Text(janela3,width=20,height=10)
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 2''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[3] + ' x ' +  Times[0]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[1]+ ' x ' + Times[2]+'\n\n')
    if(Rodadas[0]==3):
        ProximoJogo = Text(janela3,width=20,height=10)
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 3''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[2] + ' x ' +  Times[0]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[1]+ ' x ' + Times[3]+'\n\n')
    if(Rodadas[0]==4):
        ProximoJogo = Text(janela3,width=20,height=10)
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 4''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[1] + ' x '+  Times[0]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[3]+ ' x ' + Times[2]+'\n\n')
    if(Rodadas[0]==5):
        ProximoJogo = Text(janela3,width=20,height=10)
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 5''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[0] + ' x ' +  Times[3]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[2]+ ' x ' + Times[1]+'\n\n')
    if(Rodadas[0]==6):
        ProximoJogo = Text(janela3,width=20,height=10)
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 6''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[0] + ' x ' +  Times[2]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[3]+ ' x ' + Times[1]+'\n\n')
    #BOTOES
    ImgBotao = Image.open('imagens/botaobola.png')
    BotaoImg = ImageTk.PhotoImage(ImgBotao)
    BotaoIniciarPartida = Button(janela3,image=BotaoImg,bg='#1bcc35',command=IniciarPartida)
    BotaoIniciarPartida.place(x=900,y=350)
    IniciarLabel = Label(janela3,text='INICIAR JOGO',font=('Arial Black',12,'bold'),bg='#1bcc35',fg='white')
    IniciarLabel.place(x=900,y=490)
        
    janela3.mainloop()


def PlantelSaoPaulo():
    #INICIALIZADOR
    janela3 = Tk()
    janela3.title('Soccer CWB - Plantel do Time')
    janela3.minsize(width =1280, height = 720)
    janela3.maxsize(width =1280, height = 720)

    #CAPA DO TIME
    janela3['bg'] = 'red'
    Titulo = Label(janela3,text='SÃO PAULO',font=('Arial Black',68,'bold'),bg='red',fg='white')
    Titulo.place(x=370,y=30)
    ImgMascote88 = Image.open('imagens/mascotesaopaulo.jpg')
    MascoteImg88 = ImageTk.PhotoImage(ImgMascote88)
    Mascote = Label(janela3,image=MascoteImg88,bg='red')
    Mascote.place(x=50,y=30)
    Mascote2 = Label(janela3,image=MascoteImg88,bg='red')
    Mascote2.place(x=1080,y=30)
    Players = Text(janela3,width=25,height=25)
    Players.place(x=0,y=200)
    Players.configure(font=('Arial Black',10,'bold'))
    Players.insert(INSERT,'ELENCO SÃO PAULO:\n\n')
    Players.insert(INSERT,'Tecnico - '+ JogadoresSaoPaulo[0]+'\n\n')
    Players.insert(INSERT,'GL - '+ JogadoresSaoPaulo[1] +'\n\n')
    Players.insert(INSERT,'ZG - '+ JogadoresSaoPaulo[2]+'\n\n')
    Players.insert(INSERT,'ZG - '+ JogadoresSaoPaulo[3]+'\n\n')
    Players.insert(INSERT,'LD - '+ JogadoresSaoPaulo[4]+'\n\n')
    Players.insert(INSERT,'LE - '+ JogadoresSaoPaulo[5]+'\n\n')
    Players.insert(INSERT,'VL - '+ JogadoresSaoPaulo[6]+'\n\n')
    Players.insert(INSERT,'VL - '+ JogadoresSaoPaulo[7]+'\n\n')
    Players.insert(INSERT,'MEI - '+ JogadoresSaoPaulo[8]+'\n\n')
    Players.insert(INSERT,'ATA - '+ JogadoresSaoPaulo[9]+'\n\n')
    Players.insert(INSERT,'ATA - '+ JogadoresSaoPaulo[10]+'\n\n')
    Players.insert(INSERT,'ATA - '+ JogadoresSaoPaulo[11]+'\n\n')
    
    #FUNÇÃO DO BOTAO INICAR
    def IniciarPartida():
        if Rodadas[0] == 1:
            janela3.destroy()
            Rodada1()
        if Rodadas[0] == 2:
            janela3.destroy()
            Rodada2()
        if Rodadas[0] == 3:
            janela3.destroy()
            Rodada3()
        if Rodadas[0] == 4:
            janela3.destroy()
            Rodada4()
        if Rodadas[0] == 5:
            janela3.destroy()
            Rodada5()
        if Rodadas[0] == 6:
            janela3.destroy()
            Rodada6()
    
    #RODADAS
    if(Rodadas[0] == 1):
        ProximoJogo = Text(janela3,width=20,height=10)
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 1''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[0] + ' x '+  Times[1]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[2]+' x ' + Times[3]+'\n\n')
    if(Rodadas[0]==2):
        ProximoJogo = Text(janela3,width=20,height=10)
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 2''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[3] + ' x ' +  Times[0]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[1]+ ' x ' + Times[2]+'\n\n')
    if(Rodadas[0]==3):
        ProximoJogo = Text(janela3,width=20,height=10)
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 3''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[2] + ' x ' +  Times[0]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[1]+ ' x ' + Times[3]+'\n\n')
    if(Rodadas[0]==4):
        ProximoJogo = Text(janela3,width=20,height=10)
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 4''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[1] + ' x '+  Times[0]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[3]+ ' x ' + Times[2]+'\n\n')
    if(Rodadas[0]==5):
        ProximoJogo = Text(janela3,width=20,height=10)
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 5''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[0] + ' x ' +  Times[3]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[2]+ ' x ' + Times[1]+'\n\n')
    if(Rodadas[0]==6):
        ProximoJogo = Text(janela3,width=20,height=10)
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 6''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[0] + ' x ' +  Times[2]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[3]+ ' x ' + Times[1]+'\n\n')
    #BOTOES
    ImgBotao = Image.open('imagens/botaobola.png')
    BotaoImg = ImageTk.PhotoImage(ImgBotao)
    BotaoIniciarPartida = Button(janela3,image=BotaoImg,bg='red',command=IniciarPartida)
    BotaoIniciarPartida.place(x=900,y=350)
    IniciarLabel = Label(janela3,text='INICIAR JOGO',font=('Arial Black',12,'bold'),bg='red',fg='white')
    IniciarLabel.place(x=900,y=490)
        
    janela3.mainloop()

def PlantelCorinthians():
    #INICIALIZADOR
    janela3 = Tk()
    janela3.title('Soccer CWB - Plantel do Time')
    janela3.minsize(width =1280, height = 720)
    janela3.maxsize(width =1280, height = 720)

    #CAPA DO TIME
    janela3['bg'] = 'white'
    Titulo = Label(janela3,text='CORINTHIANS',font=('Arial Black',68,'bold'),bg='white',fg='black')
    Titulo.place(x=300,y=30)
    ImgMascote77 = Image.open('imagens/mascotecorinthians.jpg')
    MascoteImg77 = ImageTk.PhotoImage(ImgMascote77)
    Mascote = Label(janela3,image=MascoteImg77,bg='white')
    Mascote.place(x=50,y=30)
    Mascote2 = Label(janela3,image=MascoteImg77,bg='white')
    Mascote2.place(x=1080,y=30)
    Players = Text(janela3,width=25,height=25,bg='black',fg='white')
    Players.place(x=0,y=200)
    Players.configure(font=('Arial Black',10,'bold'))
    Players.insert(INSERT,'ELENCO CORINTHIANS:\n\n')
    Players.insert(INSERT,'Tecnico - '+ JogadoresCorinthians[0]+'\n\n')
    Players.insert(INSERT,'GL - '+ JogadoresCorinthians[1] +'\n\n')
    Players.insert(INSERT,'ZG - '+ JogadoresCorinthians[2]+'\n\n')
    Players.insert(INSERT,'ZG - '+ JogadoresCorinthians[3]+'\n\n')
    Players.insert(INSERT,'LD - '+ JogadoresCorinthians[4]+'\n\n')
    Players.insert(INSERT,'LE - '+ JogadoresCorinthians[5]+'\n\n')
    Players.insert(INSERT,'VL - '+ JogadoresCorinthians[6]+'\n\n')
    Players.insert(INSERT,'VL - '+ JogadoresCorinthians[7]+'\n\n')
    Players.insert(INSERT,'MEI - '+ JogadoresCorinthians[8]+'\n\n')
    Players.insert(INSERT,'ATA - '+ JogadoresCorinthians[9]+'\n\n')
    Players.insert(INSERT,'ATA - '+ JogadoresCorinthians[10]+'\n\n')
    Players.insert(INSERT,'ATA - '+ JogadoresCorinthians[11]+'\n\n')
    
    #FUNÇÃO DO BOTAO INICAR
    def IniciarPartida():
        if Rodadas[0] == 1:
            janela3.destroy()
            Rodada1()
        if Rodadas[0] == 2:
            janela3.destroy()
            Rodada2()
        if Rodadas[0] == 3:
            janela3.destroy()
            Rodada3()
        if Rodadas[0] == 4:
            janela3.destroy()
            Rodada4()
        if Rodadas[0] == 5:
            janela3.destroy()
            Rodada5()
        if Rodadas[0] == 6:
            janela3.destroy()
            Rodada6()
    
    #RODADAS
    if(Rodadas[0] == 1):
        ProximoJogo = Text(janela3,width=20,height=10,bg='black',fg='white')
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 1''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[0] + ' x '+  Times[1]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[2]+' x ' + Times[3]+'\n\n')
    if(Rodadas[0]==2):
        ProximoJogo = Text(janela3,width=20,height=10,bg='black',fg='white')
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 2''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[3] + ' x ' +  Times[0]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[1]+ ' x ' + Times[2]+'\n\n')
    if(Rodadas[0]==3):
        ProximoJogo = Text(janela3,width=20,height=10,bg='black',fg='white')
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 3''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[2] + ' x ' +  Times[0]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[1]+ ' x ' + Times[3]+'\n\n')
    if(Rodadas[0]==4):
        ProximoJogo = Text(janela3,width=20,height=10,bg='black',fg='white')
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 4''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[1] + ' x '+  Times[0]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[3]+ ' x ' + Times[2]+'\n\n')
    if(Rodadas[0]==5):
        ProximoJogo = Text(janela3,width=20,height=10,bg='black',fg='white')
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 5''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[0] + ' x ' +  Times[3]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[2]+ ' x ' + Times[1]+'\n\n')
    if(Rodadas[0]==6):
        ProximoJogo = Text(janela3,width=20,height=10,bg='black',fg='white')
        ProximoJogo.place(x=400,y=300)
        ProximoJogo.configure(padx=60,font=('Arial Black',12))
        ProximoJogo.insert(INSERT,'RODADA 6''\n\n')
        ProximoJogo.insert(INSERT,'PROXIMO JOGO:''\n\n')
        ProximoJogo.insert(INSERT,Times[0] + ' x ' +  Times[2]+'\n\n' )
        ProximoJogo.insert(INSERT,Times[3]+ ' x ' + Times[1]+'\n\n')
    #BOTOES
    ImgBotao = Image.open('imagens/botaobola.png')
    BotaoImg = ImageTk.PhotoImage(ImgBotao)
    BotaoIniciarPartida = Button(janela3,image=BotaoImg,bg='white',command=IniciarPartida)
    BotaoIniciarPartida.place(x=900,y=350)
    IniciarLabel = Label(janela3,text='INICIAR JOGO',font=('Arial Black',12,'bold'),bg='white',fg='black')
    IniciarLabel.place(x=900,y=490)
        
    janela3.mainloop()

def Rodada1():
    janela4 = Tk()
    janela4.title('CWB SOCCER - PARTIDA')
    janela4['bg']= '#87CEEB'
    janela4.minsize(width = 1280, height = 720)
    janela4.maxsize(width = 1280, height = 720)
    

    def VoltarAoTime():

        SantosPT[1] = 0
        PalmeirasPT[1] =0
        SaoPauloPT[1] =0
        CorinthiansPT[1] =0
        if Teams[0] == 'SANTOS':
            janela4.destroy()
            PlantelSantos()
        if Teams[0] == 'PALMEIRAS':
            janela4.destroy()
            PlantelPalmeiras()
        if Teams[0] == 'SAO PAULO':
            janela4.destroy()
            PlantelSaoPaulo()
        if Teams[0] == 'CORINTHIANS':
            janela4.destroy()
            PlantelCorinthians()
            
 
    def Comecou():
        TempoDeJogo = -1
        ResultadoSantos = 0
        ResultadoPalmeiras = 0  
        ResultadoSaoPaulo = 0
        ResultadoCorinthians = 0
        while TempoDeJogo< 90:
            BotaoComecar['command'] = 0
            TempoDeJogo += 1
            Tempo = Label(janela4, text = TempoDeJogo, width =5, height = 2,bg='black',fg='red',font=('Arial Black',10, 'bold'))
            Tempo.place(x=600,y=100)
            Tempo.update()
            ListaDeTimes = ['SANTOS','PALMEIRAS','SAO PAULO','CORINTHIANS','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA',
            'NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA',
            'NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA',
            'NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA']
            TimeEscolhido = random.choice(ListaDeTimes)
            
            Resultado1 = Label(janela4,text = ResultadoSantos,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado1.place(x=190,y=250)
            Resultado1.update()
            Resultado2 = Label(janela4,text = ResultadoPalmeiras,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado2.place(x=250,y=250)
            Resultado2.update()
            Resultado3 = Label(janela4,text = ResultadoSaoPaulo,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado3.place(x=920,y=250)
            Resultado3.update()
            Resultado4 = Label(janela4,text = ResultadoCorinthians,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado4.place(x=980,y=250)
            Resultado4.update()
            
            
                
            if TimeEscolhido == 'SANTOS':  
                BoxDeGols.insert(INSERT, 'GOOOL DO SANTOS' + ' - ')
                GolSantos = [JogadoresSantos[11],JogadoresSantos[11],JogadoresSantos[11],JogadoresSantos[10],JogadoresSantos[10],
                JogadoresSantos[10],JogadoresSantos[9],JogadoresSantos[9],JogadoresSantos[9],JogadoresSantos[8],JogadoresSantos[8],JogadoresSantos[7],JogadoresSantos[7],JogadoresSantos[6],
                JogadoresSantos[5],JogadoresSantos[4],JogadoresSantos[3],JogadoresSantos[2]]
                JogadorEscolhido = random.choice(GolSantos)
                BoxDeGols.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoSantos +=1
                SantosPT[1] +=1
                
              
            if TimeEscolhido == 'PALMEIRAS':             
                BoxDeGols.insert(INSERT, 'GOOOL DO PALMEIRAS' + ' - ')
                GolPalmeiras = [JogadoresPalmeiras[11],JogadoresPalmeiras[11],JogadoresPalmeiras[11],JogadoresPalmeiras[10],JogadoresPalmeiras[10],
                JogadoresPalmeiras[10],JogadoresPalmeiras[9],JogadoresPalmeiras[9],JogadoresPalmeiras[9],JogadoresPalmeiras[8],JogadoresPalmeiras[8],JogadoresPalmeiras[7],JogadoresPalmeiras[7],JogadoresPalmeiras[6],
                JogadoresPalmeiras[5],JogadoresPalmeiras[4],JogadoresPalmeiras[3],JogadoresPalmeiras[2]]
                JogadorEscolhido = random.choice(GolPalmeiras)
                BoxDeGols.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoPalmeiras +=1
                PalmeirasPT[1] +=1

            if TimeEscolhido == 'SAO PAULO':             
                BoxDeGols2.insert(INSERT, 'GOOOL DO SAO PAULO' + ' - ')
                GolSaoPaulo = [JogadoresSaoPaulo[11],JogadoresSaoPaulo[11],JogadoresSaoPaulo[11],JogadoresSaoPaulo[10],JogadoresSaoPaulo[10],
                JogadoresSaoPaulo[10],JogadoresSaoPaulo[9],JogadoresSaoPaulo[9],JogadoresSaoPaulo[9],JogadoresSaoPaulo[8],JogadoresSaoPaulo[8],JogadoresSaoPaulo[7],JogadoresSaoPaulo[7],JogadoresSaoPaulo[6],
                JogadoresSaoPaulo[5],JogadoresSaoPaulo[4],JogadoresSaoPaulo[3],JogadoresSaoPaulo[2]]
                JogadorEscolhido = random.choice(GolSaoPaulo)
                BoxDeGols2.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoSaoPaulo +=1
                SaoPauloPT[1] +=1

            if TimeEscolhido == 'CORINTHIANS':             
                BoxDeGols2.insert(INSERT, 'GOOOL DO CORINTHIANS' + ' - ')
                GolCorinthians = [JogadoresCorinthians[11],JogadoresCorinthians[11],JogadoresCorinthians[11],JogadoresCorinthians[10],JogadoresCorinthians[10],
                JogadoresCorinthians[10],JogadoresCorinthians[9],JogadoresCorinthians[9],JogadoresCorinthians[9],JogadoresCorinthians[8],JogadoresCorinthians[8],JogadoresCorinthians[7],JogadoresCorinthians[7],JogadoresCorinthians[6],
                JogadoresCorinthians[5],JogadoresCorinthians[4],JogadoresCorinthians[3],JogadoresCorinthians[2]]
                JogadorEscolhido = random.choice(GolCorinthians)
                BoxDeGols2.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoCorinthians +=1
                CorinthiansPT[1] +=1
               
            if TimeEscolhido == 'NADA':
                pass            

            time.sleep(1)
            
        else:
            if SantosPT[1] >PalmeirasPT[1]:
                    SantosPT[0] +=3
            if SantosPT[1] <PalmeirasPT[1]:
                PalmeirasPT[0]+=3
            if SantosPT[1] == PalmeirasPT[1]:
                SantosPT[0]+=1
                PalmeirasPT[0]+=1
            if SaoPauloPT[1]>CorinthiansPT[1]:
                SaoPauloPT[0]+=3
            if SaoPauloPT[1]<CorinthiansPT[1]:
                CorinthiansPT[0]+=3
            if SaoPauloPT[1] == CorinthiansPT[1]:
                SaoPauloPT[0]+=1
                CorinthiansPT[0]+=1
            Rodadas[0] += 1
            BotaoComecar['text'] = 'VOLTAR AO TIME'
            BotaoComecar['command'] = VoltarAoTime
            LabelJogo['text'] = 'FIM DE JOGO'
        

    
        


    #BOTOES E LABELS  
     
    LabelTitulo = Label(janela4,text='CAMPEONATO PAULISTA',font=('Impact',60,'bold'),bg='#87CEEB')
    LabelTitulo.place(x=250,y=10)    
    LabelMin = Label(janela4,text='Minutos',font=('Arial Black',16,'bold'),bg='#87CEEB')
    LabelMin.place(x=655,y=100)
    LabelTempo = Label(janela4,text='Tempo de Jogo: ',font=('Arial Black',16,'bold'),bg='#87CEEB')  
    LabelTempo.place(x=400,y=100)  
    LabelJogo = Label(janela4,text='PARTIDA EM ANDAMENTO',font=('Arial Black',20,'bold'),bg='#87CEEB')
    LabelJogo.place(x=530,y=150)
    LabelRodada = Label(janela4,text='1° RODADA',font=('Arial Black',20,'bold'),bg='#87CEEB')
    LabelRodada.place(x=520,y=250)
    TimeCasa1 = Label(janela4,text = 'SANTOS',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa1.place(x=20,y=250)   
    X1 = Label(janela4,text = 'X',font=('Arial Black',16,'bold'),bg='#87CEEB')
    X1.place(x=220,y=250)   
    TimeCasa2 = Label(janela4,text = 'PALMEIRAS',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa2.place(x=300,y=250)
    Gols1 = Label(janela4,text = 'GOLS:',font=('Arial Black',16,'bold'),bg='#87CEEB')
    Gols1.place(x=190,y=300)
    BoxDeGols= Text(width = 60,height = 20)
    BoxDeGols.place(x=10,y=340)

    TimeCasa3 = Label(janela4,text = 'SÃO PAULO',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa3.place(x=750,y=250)
    X1 = Label(janela4,text = 'X',font=('Arial Black',16,'bold'),bg='#87CEEB')
    X1.place(x=950,y=250)  
    TimeCasa4 = Label(janela4,text = 'CORINTHIANS',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa4.place(x=1030,y=250)   
    Gols2 = Label(janela4,text = 'GOLS:',font=('Arial Black',16,'bold'),bg='#87CEEB')
    Gols2.place(x=930,y=300)
    BoxDeGols2= Text(width = 60,height = 20)
    BoxDeGols2.place(x=740,y=340)

    PontosLabel = Label(janela4,text='PONTUAÇÃO',bg='#87CEEB',font=('Arial Black',12,'bold'))
    PontosLabel.place(x=550,y=428)
    BoxPontos = Text(width= 25,height = 13)
    BoxPontos.place(x=513,y=452)
    BoxPontos.insert(INSERT, 'SANTOS: '+str(SantosPT[0])+' \n\n\n')
    BoxPontos.insert(INSERT, 'PALMEIRAS: '+str(PalmeirasPT[0])+' \n\n\n')
    BoxPontos.insert(INSERT, 'SAO PAULO: '+str(SaoPauloPT[0])+' \n\n\n')
    BoxPontos.insert(INSERT, 'CORINTHIANS: '+str(CorinthiansPT[0])+' \n\n\n')


    
        
    BotaoComecar = Button(janela4,text='COMEÇAR JOGO',command=Comecou,width = 20,height = 5,font=('Arial Black',12,'bold'))
    BotaoComecar.place(x=500,y=300)



    
    janela4.mainloop()




def Rodada2():
    janela4 = Tk()
    janela4.title('CWB SOCCER - PARTIDA')
    janela4['bg']= '#87CEEB'
    janela4.minsize(width = 1280, height = 720)
    janela4.maxsize(width = 1280, height = 720)
    

    def VoltarAoTime():

        SantosPT[1] = 0
        PalmeirasPT[1] =0
        SaoPauloPT[1] =0
        CorinthiansPT[1] =0
        if Teams[0] == 'SANTOS':
            janela4.destroy()
            PlantelSantos()
        if Teams[0] == 'PALMEIRAS':
            janela4.destroy()
            PlantelPalmeiras()
        if Teams[0] == 'SAO PAULO':
            janela4.destroy()
            PlantelSaoPaulo()
        if Teams[0] == 'CORINTHIANS':
            janela4.destroy()
            PlantelCorinthians()
            
 
    def Comecou():
        TempoDeJogo = -1
        ResultadoSantos = 0
        ResultadoPalmeiras = 0  
        ResultadoSaoPaulo = 0
        ResultadoCorinthians = 0
        while TempoDeJogo< 90:
            BotaoComecar['command'] = 0
            TempoDeJogo += 1
            Tempo = Label(janela4, text = TempoDeJogo, width =5, height = 2,bg='black',fg='red',font=('Arial Black',10, 'bold'))
            Tempo.place(x=600,y=100)
            Tempo.update()
            ListaDeTimes = ['SANTOS','PALMEIRAS','SAO PAULO','CORINTHIANS','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA',
            'NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA',
            'NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA',
            'NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA']
            TimeEscolhido = random.choice(ListaDeTimes)
            
            Resultado1 = Label(janela4,text = ResultadoCorinthians,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado1.place(x=190,y=250)
            Resultado1.update()
            Resultado2 = Label(janela4,text = ResultadoSantos,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado2.place(x=250,y=250)
            Resultado2.update()
            Resultado3 = Label(janela4,text = ResultadoPalmeiras,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado3.place(x=920,y=250)
            Resultado3.update()
            Resultado4 = Label(janela4,text = ResultadoSaoPaulo,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado4.place(x=980,y=250)
            Resultado4.update()
            
            
                
            if TimeEscolhido == 'SANTOS':  
                BoxDeGols.insert(INSERT, 'GOOOL DO SANTOS' + ' - ')
                GolSantos = [JogadoresSantos[11],JogadoresSantos[11],JogadoresSantos[11],JogadoresSantos[10],JogadoresSantos[10],
                JogadoresSantos[10],JogadoresSantos[9],JogadoresSantos[9],JogadoresSantos[9],JogadoresSantos[8],JogadoresSantos[8],JogadoresSantos[7],JogadoresSantos[7],JogadoresSantos[6],
                JogadoresSantos[5],JogadoresSantos[4],JogadoresSantos[3],JogadoresSantos[2]]
                JogadorEscolhido = random.choice(GolSantos)
                BoxDeGols.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoSantos +=1
                SantosPT[1] +=1
                
              
            if TimeEscolhido == 'PALMEIRAS':             
                BoxDeGols2.insert(INSERT, 'GOOOL DO PALMEIRAS' + ' - ')
                GolPalmeiras = [JogadoresPalmeiras[11],JogadoresPalmeiras[11],JogadoresPalmeiras[11],JogadoresPalmeiras[10],JogadoresPalmeiras[10],
                JogadoresPalmeiras[10],JogadoresPalmeiras[9],JogadoresPalmeiras[9],JogadoresPalmeiras[9],JogadoresPalmeiras[8],JogadoresPalmeiras[8],JogadoresPalmeiras[7],JogadoresPalmeiras[7],JogadoresPalmeiras[6],
                JogadoresPalmeiras[5],JogadoresPalmeiras[4],JogadoresPalmeiras[3],JogadoresPalmeiras[2]]
                JogadorEscolhido = random.choice(GolPalmeiras)
                BoxDeGols2.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoPalmeiras +=1
                PalmeirasPT[1] +=1

            if TimeEscolhido == 'SAO PAULO':             
                BoxDeGols2.insert(INSERT, 'GOOOL DO SAO PAULO' + ' - ')
                GolSaoPaulo = [JogadoresSaoPaulo[11],JogadoresSaoPaulo[11],JogadoresSaoPaulo[11],JogadoresSaoPaulo[10],JogadoresSaoPaulo[10],
                JogadoresSaoPaulo[10],JogadoresSaoPaulo[9],JogadoresSaoPaulo[9],JogadoresSaoPaulo[9],JogadoresSaoPaulo[8],JogadoresSaoPaulo[8],JogadoresSaoPaulo[7],JogadoresSaoPaulo[7],JogadoresSaoPaulo[6],
                JogadoresSaoPaulo[5],JogadoresSaoPaulo[4],JogadoresSaoPaulo[3],JogadoresSaoPaulo[2]]
                JogadorEscolhido = random.choice(GolSaoPaulo)
                BoxDeGols2.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoSaoPaulo +=1
                SaoPauloPT[1] +=1

            if TimeEscolhido == 'CORINTHIANS':             
                BoxDeGols.insert(INSERT, 'GOOOL DO CORINTHIANS' + ' - ')
                GolCorinthians = [JogadoresCorinthians[11],JogadoresCorinthians[11],JogadoresCorinthians[11],JogadoresCorinthians[10],JogadoresCorinthians[10],
                JogadoresCorinthians[10],JogadoresCorinthians[9],JogadoresCorinthians[9],JogadoresCorinthians[9],JogadoresCorinthians[8],JogadoresCorinthians[8],JogadoresCorinthians[7],JogadoresCorinthians[7],JogadoresCorinthians[6],
                JogadoresCorinthians[5],JogadoresCorinthians[4],JogadoresCorinthians[3],JogadoresCorinthians[2]]
                JogadorEscolhido = random.choice(GolCorinthians)
                BoxDeGols.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoCorinthians +=1
                CorinthiansPT[1] +=1
               
            if TimeEscolhido == 'NADA':
                pass            

            time.sleep(1)
            
        else:
            if SantosPT[1] >CorinthiansPT[1]:
                SantosPT[0] +=3
            if SantosPT[1] <CorinthiansPT[1]:
                CorinthiansPT[0]+=3
            if SantosPT[1] == CorinthiansPT[1]:
                SantosPT[0]+=1
                CorinthiansPT[0]+=1
            if SaoPauloPT[1]>PalmeirasPT[1]:
                SaoPauloPT[0]+=3
            if SaoPauloPT[1]<PalmeirasPT[1]:
                PalmeirasPT[0]+=3
            if SaoPauloPT[1] == PalmeirasPT[1]:
                SaoPauloPT[0]+=1
                PalmeirasPT[0]+=1
            Rodadas[0] += 1
            BotaoComecar['text'] = 'VOLTAR AO TIME'
            BotaoComecar['command'] = VoltarAoTime
            LabelJogo['text'] = 'FIM DE JOGO'
        

    
    
                       


    #BOTOES E LABELS  
     
    LabelTitulo = Label(janela4,text='CAMPEONATO PAULISTA',font=('Impact',60,'bold'),bg='#87CEEB')
    LabelTitulo.place(x=250,y=10)    
    LabelMin = Label(janela4,text='Minutos',font=('Arial Black',16,'bold'),bg='#87CEEB')
    LabelMin.place(x=655,y=100)
    LabelTempo = Label(janela4,text='Tempo de Jogo: ',font=('Arial Black',16,'bold'),bg='#87CEEB')  
    LabelTempo.place(x=400,y=100)  
    LabelJogo = Label(janela4,text='EM ANDAMENTO',font=('Arial Black',20,'bold'),bg='#87CEEB')
    LabelJogo.place(x=530,y=150)
    LabelRodada = Label(janela4,text='2° RODADA',font=('Arial Black',20,'bold'),bg='#87CEEB')
    LabelRodada.place(x=520,y=250)
    TimeCasa1 = Label(janela4,text = 'CORINTHIANS',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa1.place(x=20,y=250)   
    X1 = Label(janela4,text = 'X',font=('Arial Black',16,'bold'),bg='#87CEEB')
    X1.place(x=220,y=250)   
    TimeCasa2 = Label(janela4,text = 'SANTOS',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa2.place(x=300,y=250)
    Gols1 = Label(janela4,text = 'GOLS:',font=('Arial Black',16,'bold'),bg='#87CEEB')
    Gols1.place(x=190,y=300)
    BoxDeGols= Text(width = 60,height = 20)
    BoxDeGols.place(x=10,y=340)

    TimeCasa3 = Label(janela4,text = 'PALMEIRAS',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa3.place(x=750,y=250)
    X1 = Label(janela4,text = 'X',font=('Arial Black',16,'bold'),bg='#87CEEB')
    X1.place(x=950,y=250)  
    TimeCasa4 = Label(janela4,text = 'SÃO PAULO',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa4.place(x=1030,y=250)   
    Gols2 = Label(janela4,text = 'GOLS:',font=('Arial Black',16,'bold'),bg='#87CEEB')
    Gols2.place(x=930,y=300)
    BoxDeGols2= Text(width = 60,height = 20)
    BoxDeGols2.place(x=740,y=340)

    PontosLabel = Label(janela4,text='PONTUAÇÃO',bg='#87CEEB',font=('Arial Black',12,'bold'))
    PontosLabel.place(x=550,y=428)
    BoxPontos = Text(width= 25,height = 13)
    BoxPontos.place(x=513,y=452)
    BoxPontos.insert(INSERT, 'SANTOS: '+str(SantosPT[0])+' \n\n\n')
    BoxPontos.insert(INSERT, 'PALMEIRAS: '+str(PalmeirasPT[0])+' \n\n\n')
    BoxPontos.insert(INSERT, 'SAO PAULO: '+str(SaoPauloPT[0])+' \n\n\n')
    BoxPontos.insert(INSERT, 'CORINTHIANS: '+str(CorinthiansPT[0])+' \n\n\n')


    
        
    BotaoComecar = Button(janela4,text='COMEÇAR JOGO',command=Comecou,width = 20,height = 5,font=('Arial Black',12,'bold'))
    BotaoComecar.place(x=500,y=300)



    
    janela4.mainloop()


def Rodada3():
    janela4 = Tk()
    janela4.title('CWB SOCCER - PARTIDA')
    janela4['bg']= '#87CEEB'
    janela4.minsize(width = 1280, height = 720)
    janela4.maxsize(width = 1280, height = 720)
    

    def VoltarAoTime():

        SantosPT[1] = 0
        PalmeirasPT[1] =0
        SaoPauloPT[1] =0
        CorinthiansPT[1] =0
        if Teams[0] == 'SANTOS':
            janela4.destroy()
            PlantelSantos()
        if Teams[0] == 'PALMEIRAS':
            janela4.destroy()
            PlantelPalmeiras()
        if Teams[0] == 'SAO PAULO':
            janela4.destroy()
            PlantelSaoPaulo()
        if Teams[0] == 'CORINTHIANS':
            janela4.destroy()
            PlantelCorinthians()
            
 
    def Comecou():
        TempoDeJogo = -1
        ResultadoSantos = 0
        ResultadoPalmeiras = 0  
        ResultadoSaoPaulo = 0
        ResultadoCorinthians = 0
        while TempoDeJogo< 90:
            BotaoComecar['command'] = 0
            TempoDeJogo += 1
            Tempo = Label(janela4, text = TempoDeJogo, width =5, height = 2,bg='black',fg='red',font=('Arial Black',10, 'bold'))
            Tempo.place(x=600,y=100)
            Tempo.update()
            ListaDeTimes = ['SANTOS','PALMEIRAS','SAO PAULO','CORINTHIANS','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA',
            'NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA',
            'NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA',
            'NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA']
            TimeEscolhido = random.choice(ListaDeTimes)
            
            Resultado1 = Label(janela4,text = ResultadoSaoPaulo,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado1.place(x=190,y=250)
            Resultado1.update()
            Resultado2 = Label(janela4,text = ResultadoSantos,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado2.place(x=250,y=250)
            Resultado2.update()
            Resultado3 = Label(janela4,text = ResultadoPalmeiras,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado3.place(x=920,y=250)
            Resultado3.update()
            Resultado4 = Label(janela4,text = ResultadoCorinthians,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado4.place(x=980,y=250)
            Resultado4.update()
            
            
                
            if TimeEscolhido == 'SANTOS':  
                BoxDeGols.insert(INSERT, 'GOOOL DO SANTOS' + ' - ')
                GolSantos = [JogadoresSantos[11],JogadoresSantos[11],JogadoresSantos[11],JogadoresSantos[10],JogadoresSantos[10],
                JogadoresSantos[10],JogadoresSantos[9],JogadoresSantos[9],JogadoresSantos[9],JogadoresSantos[8],JogadoresSantos[8],JogadoresSantos[7],JogadoresSantos[7],JogadoresSantos[6],
                JogadoresSantos[5],JogadoresSantos[4],JogadoresSantos[3],JogadoresSantos[2]]
                JogadorEscolhido = random.choice(GolSantos)
                BoxDeGols.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoSantos +=1
                SantosPT[1] +=1
                
              
            if TimeEscolhido == 'PALMEIRAS':             
                BoxDeGols2.insert(INSERT, 'GOOOL DO PALMEIRAS' + ' - ')
                GolPalmeiras = [JogadoresPalmeiras[11],JogadoresPalmeiras[11],JogadoresPalmeiras[11],JogadoresPalmeiras[10],JogadoresPalmeiras[10],
                JogadoresPalmeiras[10],JogadoresPalmeiras[9],JogadoresPalmeiras[9],JogadoresPalmeiras[9],JogadoresPalmeiras[8],JogadoresPalmeiras[8],JogadoresPalmeiras[7],JogadoresPalmeiras[7],JogadoresPalmeiras[6],
                JogadoresPalmeiras[5],JogadoresPalmeiras[4],JogadoresPalmeiras[3],JogadoresPalmeiras[2]]
                JogadorEscolhido = random.choice(GolPalmeiras)
                BoxDeGols2.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoPalmeiras +=1
                PalmeirasPT[1] +=1

            if TimeEscolhido == 'SAO PAULO':             
                BoxDeGols.insert(INSERT, 'GOOOL DO SAO PAULO' + ' - ')
                GolSaoPaulo = [JogadoresSaoPaulo[11],JogadoresSaoPaulo[11],JogadoresSaoPaulo[11],JogadoresSaoPaulo[10],JogadoresSaoPaulo[10],
                JogadoresSaoPaulo[10],JogadoresSaoPaulo[9],JogadoresSaoPaulo[9],JogadoresSaoPaulo[9],JogadoresSaoPaulo[8],JogadoresSaoPaulo[8],JogadoresSaoPaulo[7],JogadoresSaoPaulo[7],JogadoresSaoPaulo[6],
                JogadoresSaoPaulo[5],JogadoresSaoPaulo[4],JogadoresSaoPaulo[3],JogadoresSaoPaulo[2]]
                JogadorEscolhido = random.choice(GolSaoPaulo)
                BoxDeGols.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoSaoPaulo +=1
                SaoPauloPT[1] +=1

            if TimeEscolhido == 'CORINTHIANS':             
                BoxDeGols2.insert(INSERT, 'GOOOL DO CORINTHIANS' + ' - ')
                GolCorinthians = [JogadoresCorinthians[11],JogadoresCorinthians[11],JogadoresCorinthians[11],JogadoresCorinthians[10],JogadoresCorinthians[10],
                JogadoresCorinthians[10],JogadoresCorinthians[9],JogadoresCorinthians[9],JogadoresCorinthians[9],JogadoresCorinthians[8],JogadoresCorinthians[8],JogadoresCorinthians[7],JogadoresCorinthians[7],JogadoresCorinthians[6],
                JogadoresCorinthians[5],JogadoresCorinthians[4],JogadoresCorinthians[3],JogadoresCorinthians[2]]
                JogadorEscolhido = random.choice(GolCorinthians)
                BoxDeGols2.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoCorinthians +=1
                CorinthiansPT[1] +=1
               
            if TimeEscolhido == 'NADA':
                pass            

            time.sleep(1)
            
        else:
            if SantosPT[1] >SaoPauloPT[1]:
                SantosPT[0] +=3
            if SantosPT[1] <SaoPauloPT[1]:
                SaoPauloPT[0]+=3
            if SantosPT[1] == SaoPauloPT[1]:
                SantosPT[0]+=1
                SaoPauloPT[0]+=1
            if PalmeirasPT[1]>CorinthiansPT[1]:
                PalmeirasPT[0]+=3
            if PalmeirasPT[1]<CorinthiansPT[1]:
                CorinthiansPT[0]+=3
            if PalmeirasPT[1] == CorinthiansPT[1]:
                PalmeirasPT[0]+=1
                CorinthiansPT[0]+=1
            Rodadas[0] += 1
            BotaoComecar['text'] = 'VOLTAR AO TIME'
            BotaoComecar['command'] = VoltarAoTime
            LabelJogo['text'] = 'FIM DE JOGO'
        

    
    

    #BOTOES E LABELS  
     
    LabelTitulo = Label(janela4,text='CAMPEONATO PAULISTA',font=('Impact',60,'bold'),bg='#87CEEB')
    LabelTitulo.place(x=250,y=10)    
    LabelMin = Label(janela4,text='Minutos',font=('Arial Black',16,'bold'),bg='#87CEEB')
    LabelMin.place(x=655,y=100)
    LabelTempo = Label(janela4,text='Tempo de Jogo: ',font=('Arial Black',16,'bold'),bg='#87CEEB')  
    LabelTempo.place(x=400,y=100)  
    LabelJogo = Label(janela4,text='PARTIDA EM ANDAMENTO',font=('Arial Black',20,'bold'),bg='#87CEEB')
    LabelJogo.place(x=530,y=150)
    LabelRodada = Label(janela4,text='3° RODADA',font=('Arial Black',20,'bold'),bg='#87CEEB')
    LabelRodada.place(x=520,y=250)
    TimeCasa1 = Label(janela4,text = 'SÃO PAULO',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa1.place(x=20,y=250)   
    X1 = Label(janela4,text = 'X',font=('Arial Black',16,'bold'),bg='#87CEEB')
    X1.place(x=220,y=250)   
    TimeCasa2 = Label(janela4,text = 'SANTOS',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa2.place(x=300,y=250)
    Gols1 = Label(janela4,text = 'GOLS:',font=('Arial Black',16,'bold'),bg='#87CEEB')
    Gols1.place(x=190,y=300)
    BoxDeGols= Text(width = 60,height = 20)
    BoxDeGols.place(x=10,y=340)

    TimeCasa3 = Label(janela4,text = 'PALMEIRAS',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa3.place(x=750,y=250)
    X1 = Label(janela4,text = 'X',font=('Arial Black',16,'bold'),bg='#87CEEB')
    X1.place(x=950,y=250)  
    TimeCasa4 = Label(janela4,text = 'CORINTHIANS',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa4.place(x=1030,y=250)   
    Gols2 = Label(janela4,text = 'GOLS:',font=('Arial Black',16,'bold'),bg='#87CEEB')
    Gols2.place(x=930,y=300)
    BoxDeGols2= Text(width = 60,height = 20)
    BoxDeGols2.place(x=740,y=340)

    PontosLabel = Label(janela4,text='PONTUAÇÃO',bg='#87CEEB',font=('Arial Black',12,'bold'))
    PontosLabel.place(x=550,y=428)
    BoxPontos = Text(width= 25,height = 13)
    BoxPontos.place(x=513,y=452)
    BoxPontos.insert(INSERT, 'SANTOS: '+str(SantosPT[0])+' \n\n\n')
    BoxPontos.insert(INSERT, 'PALMEIRAS: '+str(PalmeirasPT[0])+' \n\n\n')
    BoxPontos.insert(INSERT, 'SAO PAULO: '+str(SaoPauloPT[0])+' \n\n\n')
    BoxPontos.insert(INSERT, 'CORINTHIANS: '+str(CorinthiansPT[0])+' \n\n\n')


    
        
    BotaoComecar = Button(janela4,text='COMEÇAR JOGO',command=Comecou,width = 20,height = 5,font=('Arial Black',12,'bold'))
    BotaoComecar.place(x=500,y=300)



    
    janela4.mainloop()

def Rodada4():
    janela4 = Tk()
    janela4.title('CWB SOCCER - PARTIDA')
    janela4['bg']= '#87CEEB'
    janela4.minsize(width = 1280, height = 720)
    janela4.maxsize(width = 1280, height = 720)
    

    def VoltarAoTime():

        SantosPT[1] = 0
        PalmeirasPT[1] =0
        SaoPauloPT[1] =0
        CorinthiansPT[1] =0
        if Teams[0] == 'SANTOS':
            janela4.destroy()
            PlantelSantos()
        if Teams[0] == 'PALMEIRAS':
            janela4.destroy()
            PlantelPalmeiras()
        if Teams[0] == 'SAO PAULO':
            janela4.destroy()
            PlantelSaoPaulo()
        if Teams[0] == 'CORINTHIANS':
            janela4.destroy()
            PlantelCorinthians()
            
 
    def Comecou():
        TempoDeJogo = -1
        ResultadoSantos = 0
        ResultadoPalmeiras = 0  
        ResultadoSaoPaulo = 0
        ResultadoCorinthians = 0
        while TempoDeJogo< 90:
            BotaoComecar['command'] = 0
            TempoDeJogo += 1
            Tempo = Label(janela4, text = TempoDeJogo, width =5, height = 2,bg='black',fg='red',font=('Arial Black',10, 'bold'))
            Tempo.place(x=600,y=100)
            Tempo.update()
            ListaDeTimes = ['SANTOS','PALMEIRAS','SAO PAULO','CORINTHIANS','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA',
            'NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA',
            'NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA',
            'NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA']
            TimeEscolhido = random.choice(ListaDeTimes)
            
            Resultado1 = Label(janela4,text = ResultadoPalmeiras,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado1.place(x=190,y=250)
            Resultado1.update()
            Resultado2 = Label(janela4,text = ResultadoSantos,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado2.place(x=250,y=250)
            Resultado2.update()
            Resultado3 = Label(janela4,text = ResultadoCorinthians,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado3.place(x=920,y=250)
            Resultado3.update()
            Resultado4 = Label(janela4,text = ResultadoSaoPaulo,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado4.place(x=980,y=250)
            Resultado4.update()
            
            
                
            if TimeEscolhido == 'SANTOS':  
                BoxDeGols.insert(INSERT, 'GOOOL DO SANTOS' + ' - ')
                GolSantos = [JogadoresSantos[11],JogadoresSantos[11],JogadoresSantos[11],JogadoresSantos[10],JogadoresSantos[10],
                JogadoresSantos[10],JogadoresSantos[9],JogadoresSantos[9],JogadoresSantos[9],JogadoresSantos[8],JogadoresSantos[8],JogadoresSantos[7],JogadoresSantos[7],JogadoresSantos[6],
                JogadoresSantos[5],JogadoresSantos[4],JogadoresSantos[3],JogadoresSantos[2]]
                JogadorEscolhido = random.choice(GolSantos)
                BoxDeGols.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoSantos +=1
                SantosPT[1] +=1
                
              
            if TimeEscolhido == 'PALMEIRAS':             
                BoxDeGols.insert(INSERT, 'GOOOL DO PALMEIRAS' + ' - ')
                GolPalmeiras = [JogadoresPalmeiras[11],JogadoresPalmeiras[11],JogadoresPalmeiras[11],JogadoresPalmeiras[10],JogadoresPalmeiras[10],
                JogadoresPalmeiras[10],JogadoresPalmeiras[9],JogadoresPalmeiras[9],JogadoresPalmeiras[9],JogadoresPalmeiras[8],JogadoresPalmeiras[8],JogadoresPalmeiras[7],JogadoresPalmeiras[7],JogadoresPalmeiras[6],
                JogadoresPalmeiras[5],JogadoresPalmeiras[4],JogadoresPalmeiras[3],JogadoresPalmeiras[2]]
                JogadorEscolhido = random.choice(GolPalmeiras)
                BoxDeGols.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoPalmeiras +=1
                PalmeirasPT[1] +=1

            if TimeEscolhido == 'SAO PAULO':             
                BoxDeGols2.insert(INSERT, 'GOOOL DO SAO PAULO' + ' - ')
                GolSaoPaulo = [JogadoresSaoPaulo[11],JogadoresSaoPaulo[11],JogadoresSaoPaulo[11],JogadoresSaoPaulo[10],JogadoresSaoPaulo[10],
                JogadoresSaoPaulo[10],JogadoresSaoPaulo[9],JogadoresSaoPaulo[9],JogadoresSaoPaulo[9],JogadoresSaoPaulo[8],JogadoresSaoPaulo[8],JogadoresSaoPaulo[7],JogadoresSaoPaulo[7],JogadoresSaoPaulo[6],
                JogadoresSaoPaulo[5],JogadoresSaoPaulo[4],JogadoresSaoPaulo[3],JogadoresSaoPaulo[2]]
                JogadorEscolhido = random.choice(GolSaoPaulo)
                BoxDeGols2.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoSaoPaulo +=1
                SaoPauloPT[1] +=1

            if TimeEscolhido == 'CORINTHIANS':             
                BoxDeGols2.insert(INSERT, 'GOOOL DO CORINTHIANS' + ' - ')
                GolCorinthians = [JogadoresCorinthians[11],JogadoresCorinthians[11],JogadoresCorinthians[11],JogadoresCorinthians[10],JogadoresCorinthians[10],
                JogadoresCorinthians[10],JogadoresCorinthians[9],JogadoresCorinthians[9],JogadoresCorinthians[9],JogadoresCorinthians[8],JogadoresCorinthians[8],JogadoresCorinthians[7],JogadoresCorinthians[7],JogadoresCorinthians[6],
                JogadoresCorinthians[5],JogadoresCorinthians[4],JogadoresCorinthians[3],JogadoresCorinthians[2]]
                JogadorEscolhido = random.choice(GolCorinthians)
                BoxDeGols2.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoCorinthians +=1
                CorinthiansPT[1] +=1
               
            if TimeEscolhido == 'NADA':
                pass            

            time.sleep(1)
            
        else:
            if SantosPT[1] >PalmeirasPT[1]:
                SantosPT[0] +=3
            if SantosPT[1] <PalmeirasPT[1]:
                PalmeirasPT[0]+=3
            if SantosPT[1] == PalmeirasPT[1]:
                SantosPT[0]+=1
                PalmeirasPT[0]+=1
            if SaoPauloPT[1]>CorinthiansPT[1]:
                SaoPauloPT[0]+=3
            if SaoPauloPT[1]<CorinthiansPT[1]:
                CorinthiansPT[0]+=3
            if SaoPauloPT[1] == CorinthiansPT[1]:
                SaoPauloPT[0]+=1
                CorinthiansPT[0]+=1
            Rodadas[0] += 1
            BotaoComecar['text'] = 'VOLTAR AO TIME'
            BotaoComecar['command'] = VoltarAoTime
            LabelJogo['text'] = 'FIM DE JOGO'
        

    
    
                       


    #BOTOES E LABELS  
     
    LabelTitulo = Label(janela4,text='CAMPEONATO PAULISTA',font=('Impact',60,'bold'),bg='#87CEEB')
    LabelTitulo.place(x=250,y=10)    
    LabelMin = Label(janela4,text='Minutos',font=('Arial Black',16,'bold'),bg='#87CEEB')
    LabelMin.place(x=655,y=100)
    LabelTempo = Label(janela4,text='Tempo de Jogo: ',font=('Arial Black',16,'bold'),bg='#87CEEB')  
    LabelTempo.place(x=400,y=100)  
    LabelJogo = Label(janela4,text='PARTIDA EM ANDAMENTO',font=('Arial Black',20,'bold'),bg='#87CEEB')
    LabelJogo.place(x=530,y=150)
    LabelRodada = Label(janela4,text='4° RODADA',font=('Arial Black',20,'bold'),bg='#87CEEB')
    LabelRodada.place(x=520,y=250)
    TimeCasa1 = Label(janela4,text = 'PALMEIRAS',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa1.place(x=20,y=250)   
    X1 = Label(janela4,text = 'X',font=('Arial Black',16,'bold'),bg='#87CEEB')
    X1.place(x=220,y=250)   
    TimeCasa2 = Label(janela4,text = 'SANTOS',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa2.place(x=300,y=250)
    Gols1 = Label(janela4,text = 'GOLS:',font=('Arial Black',16,'bold'),bg='#87CEEB')
    Gols1.place(x=190,y=300)
    BoxDeGols= Text(width = 60,height = 20)
    BoxDeGols.place(x=10,y=340)

    TimeCasa3 = Label(janela4,text = 'CORINTHIANS',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa3.place(x=750,y=250)
    X1 = Label(janela4,text = 'X',font=('Arial Black',16,'bold'),bg='#87CEEB')
    X1.place(x=950,y=250)  
    TimeCasa4 = Label(janela4,text = 'SÃO PAULO',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa4.place(x=1030,y=250)   
    Gols2 = Label(janela4,text = 'GOLS:',font=('Arial Black',16,'bold'),bg='#87CEEB')
    Gols2.place(x=930,y=300)
    BoxDeGols2= Text(width = 60,height = 20)
    BoxDeGols2.place(x=740,y=340)

    PontosLabel = Label(janela4,text='PONTUAÇÃO',bg='#87CEEB',font=('Arial Black',12,'bold'))
    PontosLabel.place(x=550,y=428)
    BoxPontos = Text(width= 25,height = 13)
    BoxPontos.place(x=513,y=452)
    BoxPontos.insert(INSERT, 'SANTOS: '+str(SantosPT[0])+' \n\n\n')
    BoxPontos.insert(INSERT, 'PALMEIRAS: '+str(PalmeirasPT[0])+' \n\n\n')
    BoxPontos.insert(INSERT, 'SAO PAULO: '+str(SaoPauloPT[0])+' \n\n\n')
    BoxPontos.insert(INSERT, 'CORINTHIANS: '+str(CorinthiansPT[0])+' \n\n\n')


    
        
    BotaoComecar = Button(janela4,text='COMEÇAR JOGO',command=Comecou,width = 20,height = 5,font=('Arial Black',12,'bold'))
    BotaoComecar.place(x=500,y=300)



    
    janela4.mainloop()

def Rodada5():
    janela4 = Tk()
    janela4.title('CWB SOCCER - PARTIDA')
    janela4['bg']= '#87CEEB'
    janela4.minsize(width = 1280, height = 720)
    janela4.maxsize(width = 1280, height = 720)
    

    def VoltarAoTime():

        SantosPT[1] = 0
        PalmeirasPT[1] =0
        SaoPauloPT[1] =0
        CorinthiansPT[1] =0
        if Teams[0] == 'SANTOS':
            janela4.destroy()
            PlantelSantos()
        if Teams[0] == 'PALMEIRAS':
            janela4.destroy()
            PlantelPalmeiras()
        if Teams[0] == 'SAO PAULO':
            janela4.destroy()
            PlantelSaoPaulo()
        if Teams[0] == 'CORINTHIANS':
            janela4.destroy()
            PlantelCorinthians()
            
 
    def Comecou():
        TempoDeJogo = -1
        ResultadoSantos = 0
        ResultadoPalmeiras = 0  
        ResultadoSaoPaulo = 0
        ResultadoCorinthians = 0
        while TempoDeJogo< 90:
            BotaoComecar['command'] = 0
            TempoDeJogo += 1
            Tempo = Label(janela4, text = TempoDeJogo, width =5, height = 2,bg='black',fg='red',font=('Arial Black',10, 'bold'))
            Tempo.place(x=600,y=100)
            Tempo.update()
            ListaDeTimes = ['SANTOS','PALMEIRAS','SAO PAULO','CORINTHIANS','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA',
            'NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA',
            'NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA',
            'NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA']
            TimeEscolhido = random.choice(ListaDeTimes)
            
            Resultado1 = Label(janela4,text = ResultadoSantos,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado1.place(x=190,y=250)
            Resultado1.update()
            Resultado2 = Label(janela4,text = ResultadoCorinthians,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado2.place(x=250,y=250)
            Resultado2.update()
            Resultado3 = Label(janela4,text = ResultadoSaoPaulo,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado3.place(x=920,y=250)
            Resultado3.update()
            Resultado4 = Label(janela4,text = ResultadoPalmeiras,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado4.place(x=980,y=250)
            Resultado4.update()
            
            
                
            if TimeEscolhido == 'SANTOS':  
                BoxDeGols.insert(INSERT, 'GOOOL DO SANTOS' + ' - ')
                GolSantos = [JogadoresSantos[11],JogadoresSantos[11],JogadoresSantos[11],JogadoresSantos[10],JogadoresSantos[10],
                JogadoresSantos[10],JogadoresSantos[9],JogadoresSantos[9],JogadoresSantos[9],JogadoresSantos[8],JogadoresSantos[8],JogadoresSantos[7],JogadoresSantos[7],JogadoresSantos[6],
                JogadoresSantos[5],JogadoresSantos[4],JogadoresSantos[3],JogadoresSantos[2]]
                JogadorEscolhido = random.choice(GolSantos)
                BoxDeGols.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoSantos +=1
                SantosPT[1] +=1
                
              
            if TimeEscolhido == 'PALMEIRAS':             
                BoxDeGols2.insert(INSERT, 'GOOOL DO PALMEIRAS' + ' - ')
                GolPalmeiras = [JogadoresPalmeiras[11],JogadoresPalmeiras[11],JogadoresPalmeiras[11],JogadoresPalmeiras[10],JogadoresPalmeiras[10],
                JogadoresPalmeiras[10],JogadoresPalmeiras[9],JogadoresPalmeiras[9],JogadoresPalmeiras[9],JogadoresPalmeiras[8],JogadoresPalmeiras[8],JogadoresPalmeiras[7],JogadoresPalmeiras[7],JogadoresPalmeiras[6],
                JogadoresPalmeiras[5],JogadoresPalmeiras[4],JogadoresPalmeiras[3],JogadoresPalmeiras[2]]
                JogadorEscolhido = random.choice(GolPalmeiras)
                BoxDeGols2.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoPalmeiras +=1
                PalmeirasPT[1] +=1

            if TimeEscolhido == 'SAO PAULO':             
                BoxDeGols2.insert(INSERT, 'GOOOL DO SAO PAULO' + ' - ')
                GolSaoPaulo = [JogadoresSaoPaulo[11],JogadoresSaoPaulo[11],JogadoresSaoPaulo[11],JogadoresSaoPaulo[10],JogadoresSaoPaulo[10],
                JogadoresSaoPaulo[10],JogadoresSaoPaulo[9],JogadoresSaoPaulo[9],JogadoresSaoPaulo[9],JogadoresSaoPaulo[8],JogadoresSaoPaulo[8],JogadoresSaoPaulo[7],JogadoresSaoPaulo[7],JogadoresSaoPaulo[6],
                JogadoresSaoPaulo[5],JogadoresSaoPaulo[4],JogadoresSaoPaulo[3],JogadoresSaoPaulo[2]]
                JogadorEscolhido = random.choice(GolSaoPaulo)
                BoxDeGols2.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoSaoPaulo +=1
                SaoPauloPT[1] +=1

            if TimeEscolhido == 'CORINTHIANS':             
                BoxDeGols.insert(INSERT, 'GOOOL DO CORINTHIANS' + ' - ')
                GolCorinthians = [JogadoresCorinthians[11],JogadoresCorinthians[11],JogadoresCorinthians[11],JogadoresCorinthians[10],JogadoresCorinthians[10],
                JogadoresCorinthians[10],JogadoresCorinthians[9],JogadoresCorinthians[9],JogadoresCorinthians[9],JogadoresCorinthians[8],JogadoresCorinthians[8],JogadoresCorinthians[7],JogadoresCorinthians[7],JogadoresCorinthians[6],
                JogadoresCorinthians[5],JogadoresCorinthians[4],JogadoresCorinthians[3],JogadoresCorinthians[2]]
                JogadorEscolhido = random.choice(GolCorinthians)
                BoxDeGols.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoCorinthians +=1
                CorinthiansPT[1] +=1
               
            if TimeEscolhido == 'NADA':
                pass            

            time.sleep(1)
            
        else:
            if SantosPT[1] >CorinthiansPT[1]:
                SantosPT[0] +=3
            if SantosPT[1] <CorinthiansPT[1]:
                CorinthiansPT[0]+=3
            if SantosPT[1] == CorinthiansPT[1]:
                SantosPT[0]+=1
                CorinthiansPT[0]+=1
            if SaoPauloPT[1]>PalmeirasPT[1]:
                SaoPauloPT[0]+=3
            if SaoPauloPT[1]<PalmeirasPT[1]:
                PalmeirasPT[0]+=3
            if SaoPauloPT[1] == PalmeirasPT[1]:
                SaoPauloPT[0]+=1
                PalmeirasPT[0]+=1
            Rodadas[0] += 1
            BotaoComecar['text'] = 'VOLTAR AO TIME'
            BotaoComecar['command'] = VoltarAoTime
            LabelJogo['text'] = 'FIM DE JOGO'
        

    
    

    #BOTOES E LABELS  
     
    LabelTitulo = Label(janela4,text='CAMPEONATO PAULISTA',font=('Impact',60,'bold'),bg='#87CEEB')
    LabelTitulo.place(x=250,y=10)    
    LabelMin = Label(janela4,text='Minutos',font=('Arial Black',16,'bold'),bg='#87CEEB')
    LabelMin.place(x=655,y=100)
    LabelTempo = Label(janela4,text='Tempo de Jogo: ',font=('Arial Black',16,'bold'),bg='#87CEEB')  
    LabelTempo.place(x=400,y=100)  
    LabelJogo = Label(janela4,text='PARTIDA EM ANDAMENTO',font=('Arial Black',20,'bold'),bg='#87CEEB')
    LabelJogo.place(x=530,y=150)
    LabelRodada = Label(janela4,text='5° RODADA',font=('Arial Black',20,'bold'),bg='#87CEEB')
    LabelRodada.place(x=520,y=250)
    TimeCasa1 = Label(janela4,text = 'SANTOS',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa1.place(x=20,y=250)   
    X1 = Label(janela4,text = 'X',font=('Arial Black',16,'bold'),bg='#87CEEB')
    X1.place(x=220,y=250)   
    TimeCasa2 = Label(janela4,text = 'CORINTHIANS',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa2.place(x=300,y=250)
    Gols1 = Label(janela4,text = 'GOLS:',font=('Arial Black',16,'bold'),bg='#87CEEB')
    Gols1.place(x=190,y=300)
    BoxDeGols= Text(width = 60,height = 20)
    BoxDeGols.place(x=10,y=340)

    TimeCasa3 = Label(janela4,text = 'SÃO PAULO',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa3.place(x=750,y=250)
    X1 = Label(janela4,text = 'X',font=('Arial Black',16,'bold'),bg='#87CEEB')
    X1.place(x=950,y=250)  
    TimeCasa4 = Label(janela4,text = 'PALMEIRAS',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa4.place(x=1030,y=250)   
    Gols2 = Label(janela4,text = 'GOLS:',font=('Arial Black',16,'bold'),bg='#87CEEB')
    Gols2.place(x=930,y=300)
    BoxDeGols2= Text(width = 60,height = 20)
    BoxDeGols2.place(x=740,y=340)

    PontosLabel = Label(janela4,text='PONTUAÇÃO',bg='#87CEEB',font=('Arial Black',12,'bold'))
    PontosLabel.place(x=550,y=428)
    BoxPontos = Text(width= 25,height = 13)
    BoxPontos.place(x=513,y=452)
    BoxPontos.insert(INSERT, 'SANTOS: '+str(SantosPT[0])+' \n\n\n')
    BoxPontos.insert(INSERT, 'PALMEIRAS: '+str(PalmeirasPT[0])+' \n\n\n')
    BoxPontos.insert(INSERT, 'SAO PAULO: '+str(SaoPauloPT[0])+' \n\n\n')
    BoxPontos.insert(INSERT, 'CORINTHIANS: '+str(CorinthiansPT[0])+' \n\n\n')


    
        
    BotaoComecar = Button(janela4,text='COMEÇAR JOGO',command=Comecou,width = 20,height = 5,font=('Arial Black',12,'bold'))
    BotaoComecar.place(x=500,y=300)



    
    janela4.mainloop()

def Rodada6():
    janela4 = Tk()
    janela4.title('CWB SOCCER - PARTIDA')
    janela4['bg']= '#87CEEB'
    janela4.minsize(width = 1280, height = 720)
    janela4.maxsize(width = 1280, height = 720)
    

    def Campeao():
        janela4.destroy()
        Titulo()
 
    def Comecou():
        TempoDeJogo = -1
        ResultadoSantos = 0
        ResultadoPalmeiras = 0  
        ResultadoSaoPaulo = 0
        ResultadoCorinthians = 0
        while TempoDeJogo< 90:
            BotaoComecar['command'] = 0
            TempoDeJogo += 1
            Tempo = Label(janela4, text = TempoDeJogo, width =5, height = 2,bg='black',fg='red',font=('Arial Black',10, 'bold'))
            Tempo.place(x=600,y=100)
            Tempo.update()
            ListaDeTimes = ['SANTOS','PALMEIRAS','SAO PAULO','CORINTHIANS','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA',
            'NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA',
            'NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA',
            'NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA','NADA']
            TimeEscolhido = random.choice(ListaDeTimes)
            
            Resultado1 = Label(janela4,text = ResultadoSantos,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado1.place(x=190,y=250)
            Resultado1.update()
            Resultado2 = Label(janela4,text = ResultadoSaoPaulo,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado2.place(x=250,y=250)
            Resultado2.update()
            Resultado3 = Label(janela4,text = ResultadoCorinthians,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado3.place(x=920,y=250)
            Resultado3.update()
            Resultado4 = Label(janela4,text = ResultadoPalmeiras,font=('Arial Black',16,'bold'),bg='#87CEEB')
            Resultado4.place(x=980,y=250)
            Resultado4.update()
            
            
                
            if TimeEscolhido == 'SANTOS':  
                BoxDeGols.insert(INSERT, 'GOOOL DO SANTOS' + ' - ')
                GolSantos = [JogadoresSantos[11],JogadoresSantos[11],JogadoresSantos[11],JogadoresSantos[10],JogadoresSantos[10],
                JogadoresSantos[10],JogadoresSantos[9],JogadoresSantos[9],JogadoresSantos[9],JogadoresSantos[8],JogadoresSantos[8],JogadoresSantos[7],JogadoresSantos[7],JogadoresSantos[6],
                JogadoresSantos[5],JogadoresSantos[4],JogadoresSantos[3],JogadoresSantos[2]]
                JogadorEscolhido = random.choice(GolSantos)
                BoxDeGols.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoSantos +=1
                SantosPT[1] +=1
                
              
            if TimeEscolhido == 'PALMEIRAS':             
                BoxDeGols2.insert(INSERT, 'GOOOL DO PALMEIRAS' + ' - ')
                GolPalmeiras = [JogadoresPalmeiras[11],JogadoresPalmeiras[11],JogadoresPalmeiras[11],JogadoresPalmeiras[10],JogadoresPalmeiras[10],
                JogadoresPalmeiras[10],JogadoresPalmeiras[9],JogadoresPalmeiras[9],JogadoresPalmeiras[9],JogadoresPalmeiras[8],JogadoresPalmeiras[8],JogadoresPalmeiras[7],JogadoresPalmeiras[7],JogadoresPalmeiras[6],
                JogadoresPalmeiras[5],JogadoresPalmeiras[4],JogadoresPalmeiras[3],JogadoresPalmeiras[2]]
                JogadorEscolhido = random.choice(GolPalmeiras)
                BoxDeGols2.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoPalmeiras +=1
                PalmeirasPT[1] +=1

            if TimeEscolhido == 'SAO PAULO':             
                BoxDeGols.insert(INSERT, 'GOOOL DO SAO PAULO' + ' - ')
                GolSaoPaulo = [JogadoresSaoPaulo[11],JogadoresSaoPaulo[11],JogadoresSaoPaulo[11],JogadoresSaoPaulo[10],JogadoresSaoPaulo[10],
                JogadoresSaoPaulo[10],JogadoresSaoPaulo[9],JogadoresSaoPaulo[9],JogadoresSaoPaulo[9],JogadoresSaoPaulo[8],JogadoresSaoPaulo[8],JogadoresSaoPaulo[7],JogadoresSaoPaulo[7],JogadoresSaoPaulo[6],
                JogadoresSaoPaulo[5],JogadoresSaoPaulo[4],JogadoresSaoPaulo[3],JogadoresSaoPaulo[2]]
                JogadorEscolhido = random.choice(GolSaoPaulo)
                BoxDeGols.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoSaoPaulo +=1
                SaoPauloPT[1] +=1

            if TimeEscolhido == 'CORINTHIANS':             
                BoxDeGols2.insert(INSERT, 'GOOOL DO CORINTHIANS' + ' - ')
                GolCorinthians = [JogadoresCorinthians[11],JogadoresCorinthians[11],JogadoresCorinthians[11],JogadoresCorinthians[10],JogadoresCorinthians[10],
                JogadoresCorinthians[10],JogadoresCorinthians[9],JogadoresCorinthians[9],JogadoresCorinthians[9],JogadoresCorinthians[8],JogadoresCorinthians[8],JogadoresCorinthians[7],JogadoresCorinthians[7],JogadoresCorinthians[6],
                JogadoresCorinthians[5],JogadoresCorinthians[4],JogadoresCorinthians[3],JogadoresCorinthians[2]]
                JogadorEscolhido = random.choice(GolCorinthians)
                BoxDeGols2.insert(INSERT, JogadorEscolhido +' '+ str(TempoDeJogo) +' Min '+'\n')
                ResultadoCorinthians +=1
                CorinthiansPT[1] +=1
               
            if TimeEscolhido == 'NADA':
                pass            

            time.sleep(1)
            
        else:
            if SantosPT[1] >SaoPauloPT[1]:
                SantosPT[0] +=3
            if SantosPT[1] <SaoPauloPT[1]:
                SaoPauloPT[0]+=3
            if SantosPT[1] == SaoPauloPT[1]:
                SantosPT[0]+=1
                SaoPauloPT[0]+=1
            if PalmeirasPT[1]>CorinthiansPT[1]:
                PalmeirasPT[0]+=3
            if PalmeirasPT[1]<CorinthiansPT[1]:
                CorinthiansPT[0]+=3
            if PalmeirasPT[1] == CorinthiansPT[1]:
                PalmeirasPT[0]+=1
                CorinthiansPT[0]+=1
            Rodadas[0] += 1
            BotaoComecar['text'] = 'FIM DO CAMPEONATO'
            BotaoComecar['command'] = Campeao
            LabelJogo['text'] = 'FIM DE JOGO'
        

    
    


    #BOTOES E LABELS  
     
    LabelTitulo = Label(janela4,text='CAMPEONATO PAULISTA',font=('Impact',60,'bold'),bg='#87CEEB')
    LabelTitulo.place(x=250,y=10)    
    LabelMin = Label(janela4,text='Minutos',font=('Arial Black',16,'bold'),bg='#87CEEB')
    LabelMin.place(x=655,y=100)
    LabelTempo = Label(janela4,text='Tempo de Jogo: ',font=('Arial Black',16,'bold'),bg='#87CEEB')  
    LabelTempo.place(x=400,y=100)  
    LabelJogo = Label(janela4,text='PARTIDA EM ANDAMENTO',font=('Arial Black',20,'bold'),bg='#87CEEB')
    LabelJogo.place(x=530,y=150)
    LabelRodada = Label(janela4,text='6° RODADA',font=('Arial Black',20,'bold'),bg='#87CEEB')
    LabelRodada.place(x=520,y=250)
    TimeCasa1 = Label(janela4,text = 'SANTOS',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa1.place(x=20,y=250)   
    X1 = Label(janela4,text = 'X',font=('Arial Black',16,'bold'),bg='#87CEEB')
    X1.place(x=220,y=250)   
    TimeCasa2 = Label(janela4,text = 'SÃO PAULO',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa2.place(x=300,y=250)
    Gols1 = Label(janela4,text = 'GOLS:',font=('Arial Black',16,'bold'),bg='#87CEEB')
    Gols1.place(x=190,y=300)
    BoxDeGols= Text(width = 60,height = 20)
    BoxDeGols.place(x=10,y=340)

    TimeCasa3 = Label(janela4,text = 'CORINTHIANS',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa3.place(x=750,y=250)
    X1 = Label(janela4,text = 'X',font=('Arial Black',16,'bold'),bg='#87CEEB')
    X1.place(x=950,y=250)  
    TimeCasa4 = Label(janela4,text = 'PALMEIRAS',font=('Arial Black',16,'bold'),bg='#87CEEB') 
    TimeCasa4.place(x=1030,y=250)   
    Gols2 = Label(janela4,text = 'GOLS:',font=('Arial Black',16,'bold'),bg='#87CEEB')
    Gols2.place(x=930,y=300)
    BoxDeGols2= Text(width = 60,height = 20)
    BoxDeGols2.place(x=740,y=340)

    PontosLabel = Label(janela4,text='PONTUAÇÃO',bg='#87CEEB',font=('Arial Black',12,'bold'))
    PontosLabel.place(x=550,y=428)
    BoxPontos = Text(width= 25,height = 13)
    BoxPontos.place(x=513,y=452)
    BoxPontos.insert(INSERT, 'SANTOS: '+str(SantosPT[0])+' \n\n\n')
    BoxPontos.insert(INSERT, 'PALMEIRAS: '+str(PalmeirasPT[0])+' \n\n\n')
    BoxPontos.insert(INSERT, 'SAO PAULO: '+str(SaoPauloPT[0])+' \n\n\n')
    BoxPontos.insert(INSERT, 'CORINTHIANS: '+str(CorinthiansPT[0])+' \n\n\n')


    
        
    BotaoComecar = Button(janela4,text='COMEÇAR JOGO',command=Comecou,width = 20,height = 5,font=('Arial Black',12,'bold'))
    BotaoComecar.place(x=500,y=300)



    
    janela4.mainloop()

def Titulo():
    janela4 = Tk()
    janela4.title('CWB SOCCER - FIM DE JOGO')
    janela4['bg']= '#87CEEB'
    janela4.minsize(width = 1280, height = 720)
    janela4.maxsize(width = 1280, height = 720)
    
    if SantosPT[0]>PalmeirasPT[0] and SantosPT[0]>CorinthiansPT[0]and SantosPT[0]>SaoPauloPT[0]:
        SantosCampeao= Image.open('imagens/santoscampeao.jpg')
        CampeaoSantos = ImageTk.PhotoImage(SantosCampeao)
        Fundo = Label(janela4,image=CampeaoSantos)
        Fundo.place(x=0,y=0)
    elif PalmeirasPT[0]>SantosPT[0] and PalmeirasPT[0]>CorinthiansPT[0]and PalmeirasPT[0]>SaoPauloPT[0]:
        SantosCampeao= Image.open('imagens/palmeirascampeao.jpg')
        CampeaoSantos = ImageTk.PhotoImage(SantosCampeao)
        Fundo = Label(janela4,image=CampeaoSantos)
        Fundo.place(x=0,y=0)
    elif CorinthiansPT[0]>SantosPT[0] and CorinthiansPT[0]>PalmeirasPT[0]and CorinthiansPT[0]>SaoPauloPT[0]:
        SantosCampeao= Image.open('imagens/corinthianscampeao.jpg')
        CampeaoSantos = ImageTk.PhotoImage(SantosCampeao)
        Fundo = Label(janela4,image=CampeaoSantos)
        Fundo.place(x=0,y=0)
    elif SaoPauloPT[0]>SantosPT[0] and SaoPauloPT[0]>PalmeirasPT[0]and SaoPauloPT[0]>CorinthiansPT[0]:
        SantosCampeao= Image.open('imagens/saopaulocampeao.jpg')
        CampeaoSantos = ImageTk.PhotoImage(SantosCampeao)
        Fundo = Label(janela4,image=CampeaoSantos)
        Fundo.place(x=0,y=0)
    else:
        PontosLabel = Label(janela4,text='PONTUAÇÃO',bg='#87CEEB',font=('Arial Black',12,'bold'))
        PontosLabel.place(x=550,y=428)
        BoxPontos = Text(width= 25,height = 13)
        BoxPontos.place(x=513,y=452)
        BoxPontos.insert(INSERT, 'SANTOS: '+str(SantosPT[0])+' \n\n\n')
        BoxPontos.insert(INSERT, 'PALMEIRAS: '+str(PalmeirasPT[0])+' \n\n\n')
        BoxPontos.insert(INSERT, 'SAO PAULO: '+str(SaoPauloPT[0])+' \n\n\n')
        BoxPontos.insert(INSERT, 'CORINTHIANS: '+str(CorinthiansPT[0])+' \n\n\n')

    



    janela4.mainloop()
    

Inicio()