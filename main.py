from Linkedev import LinkeSafe
from urllib.parse import quote
import os
from colorama import Fore, Back, Style
from datetime import date
import time


EMAIL = "YOUR_EMAIL"
PASS = "YOUR_PASSWORD"


def show_options():

    print(Fore.WHITE+"Linkedev options:")
    print(Fore.GREEN+"1 - Login with cookie")
    print(Fore.GREEN+"2 - Login with credentials")
    print(Fore.GREEN+"3 - List jobs")
    print(Fore.GREEN+"4 - EXIT")
    print(Fore.WHITE)


def main():

    linkedin = LinkeSafe(EMAIL, PASS, False)
    print("\n\n\n")
    if os.name == 'posix':  # Unix/Linux/Mac
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')

    while True:
        show_options()
        entrade = input("Selecione uma opção: ")
        entrada = int(entrade)
        if (entrada == 4):
            break
        if (entrada == 1):
            print("Logando com cookie")
            linkedin.load_cookies()
        if (entrada == 2):
            print("Logando com crendenciais")
            linkedin.login()
        if (entrada == 3):
            entrada = input("Selecione as tags: ")
            print("Buscando por jobs de tags: "+entrada)

            continues = True
            currentPage = 0
            count = 1
            while (continues):
                print(Fore.GREEN+"Página: "+str(currentPage)+" Buscando jobs..")
                jobs = linkedin.searchJob(entrada, currentPage)
                print(Fore.YELLOW)

                for job in jobs:
                    print(str(count)+"- " + job)
                   
                    count = count + 1
                continues = input(Fore.WHITE+"CLIQUE "+Fore.GREEN +
                                  "[ENTER]"+Fore.WHITE+" PARA IR PRA PROXIMA PAGINA OU [N] PARA PARAR: ") == ""
                if continues:
                    currentPage = currentPage + 1
    linkedin.close()


main()
