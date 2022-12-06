import colorama
from colorama import Fore
from colorama import Style

def cabecera():
    print(Fore.LIGHTCYAN_EX + """    ________   _                         _         ___   ___ ___  ____  
   /  ____  \ | |                       | |       |__ \ / _ \__ \|___ \ 
  /  / ___|  \| |     ___  _ __ ___   __| | ___      ) | | | | ) | __) |
 |  | |       | |    / _ \| '__/ _ \ / _` |/ _ \    / /| | | |/ / |__ < 
 |  | |___    | |___| (_) | | | (_) | (_| | (_) |  / /_| |_| / /_ ___) |
  \  \____|  /|______\___/|_|  \___/ \__,_|\___/  |____|\___/____|____/ 
   \________/ 
   """+ Style.RESET_ALL)

def titulo():
    print(Fore.LIGHTCYAN_EX + """   ______               _     _______                                   
  / ____|              | |   |__   __|                                  
 | |  __ _ __ ___  __ _| |_     | |_ __ ___  __ _ ___ _   _ _ __ ___    
 | | |_ | '__/ _ \/ _` | __|    | | '__/ _ \/ _` / __| | | | '__/ _ \   
 | |__| | | |  __/ (_| | |_     | | | |  __/ (_| \__ \ |_| | | |  __/   
  \_____|_|  \___|\__,_|\__|    |_|_|  \___|\__,_|___/\__,_|_|  \___|   
  _    _             _                                                  
 | |  | |           | |                                                 
 | |__| |_   _ _ __ | |_                                                
 |  __  | | | | '_ \| __|                                               
 | |  | | |_| | | | | |_                                                
 |_|  |_|\__,_|_| |_|\__|            """+Style.RESET_ALL)

def choose_language(retry):
    if (retry):

        print("Elige un idioma correcto para el juego")
        print("1. Español/España")
        print("2. English/USA")
        print("3. English/UK")
        eleccion = input()
        if eleccion == 1:
            return "sp_es"
        elif eleccion == 2:
            return "en_us"
        elif eleccion == 3:
            return "en_uk"
    else:
        print("Elige un idioma para el juego")
        print("1. Español/España")
        print("2. English/USA")
        print("3. English/UK")
        eleccion = input()
        if eleccion == 1:
            return "sp_es"
        elif eleccion == 2:
            return "en_us"
        elif eleccion == 3:
            return "en_uk"

        

    

def exit_game():
    print()