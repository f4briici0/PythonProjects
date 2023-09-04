try:
    from pytube import YouTube, Playlist
    from colorama import Fore, Style
    from os import system
    from sys import stdout
    from time import sleep
    from requests import get
except Exception as e:
    print("Error:", e)


# Mostrar Libs não instaladas
# Converter mp4 para mp3
#Mudar nome do programa

# FAZER O DOWNLOAD A DIFERENCIAÇÃO DE VÍDEO E PLAYLIST
# 

system("cls")

logo = f"""
 {Style.BRIGHT}{Fore.RED}██╗   ██╗████████╗ {Style.BRIGHT}{Fore.GREEN}  ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
 {Style.BRIGHT}{Fore.RED}╚██╗ ██╔╝╚══██╔══╝ {Style.BRIGHT}{Fore.GREEN}  ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
 {Style.BRIGHT}{Fore.RED} ╚████╔╝    ██║    {Style.BRIGHT}{Fore.GREEN}  ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
 {Style.BRIGHT}{Fore.RED}  ╚██╔╝     ██║    {Style.BRIGHT}{Fore.GREEN}  ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
 {Style.BRIGHT}{Fore.RED}   ██║      ██║    {Style.BRIGHT}{Fore.GREEN}  ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
 {Style.BRIGHT}{Fore.RED}   ╚═╝      ╚═╝    {Style.BRIGHT}{Fore.GREEN}  ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

def loading():
    global i;
    animation = ['[/]', '[—]', '[\\]']
    sleep(0.2)
    stdout.write(f"{Fore.YELLOW}\r " + animation[i % len(animation)] + " Carregando...")
    stdout.flush()
    i+= 1;

def error():
    system("cls")
    print(logo)
    print(f"{Fore.RED} Houve um problema em coletar informações desse vídeo/playlist.\n\n {Fore.WHITE}Possíveis erros:\n  1. Esse(a) vídeo/playlist pode estar privado(a).\n  2. O endereço do(a) vídeo/playlist está incompleto ou incorreto.\n  3. Aconteceu um erro interno.\n\n Tente novamente mais tarde.\n\n {Style.BRIGHT}{Fore.MAGENTA}Error: {e}")
    input(f"{Fore.WHITE}\n -> ")
    exit();


titles = []
i = 0;
c = 0;

while True:
    user = str(input(f"{logo}\n {Fore.CYAN}Insira o endereço de um vídeo ou playlist de {Fore.MAGENTA}www.youtube.com\n\n {Fore.YELLOW}->{Fore.WHITE} "))

    if (get(user).status_code != 200):
        error()
        quit();

    if ("playlist" in user):
        try:
            print()
            playlist = Playlist(user)

            for video in playlist.videos:
                name = video.title
                titles.append(name)
                # system('\033[1F\033[2K')
                loading()

                # print(f"{Style.BRIGHT}{Fore.GREEN}Carregando...")
                # stdout.write("\033[K")

            system("cls")
            print(f"{logo}\n {Style.BRIGHT}{Fore.YELLOW}Baixando a playlist:{Fore.WHITE} {playlist.title}\n")

            for link in playlist:
                print(f" {Fore.MAGENTA}[BAIXANDO] {Fore.CYAN}{titles[c]}")
                c += 1;
                yt = YouTube(link)
                audio = yt.streams.filter(only_audio=True).first()
                audio.download()

            print(f'\n {Fore.GREEN}Playlist foi baixada com sucesso!\n\n {Fore.WHITE}Pressione: "enter", para sair.')
            input("\n -> ")
            exit();

        except Exception as e:
            error()

    else:
        system("cls")
        yt = YouTube(user)
        print(f"{logo}\n {Style.BRIGHT}{Fore.YELLOW}Baixando o vídeo:{Fore.WHITE} {yt.title}")
        audio = yt.streams.filter(only_audio=True).first()
        audio.download()
        print(f'\n {Fore.GREEN}Vídeo foi baixado com sucesso!\n\n {Fore.WHITE}Pressione: "enter", para sair.')
        input("\n -> ")
        exit();
