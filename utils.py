import colorama
from main import *
from colorama import Fore
from colorama import Style

configFile = 'secrets/config.json'
with open(configFile,'r', encoding='utf-8') as fichero_config:
    config = fichero_config.read()

configuracion = json.loads(config)
defaultLanguage = configuracion['defaults']['language']

with open("languages/" +str(defaultLanguage) + configuracion["defaults"]["json_ext"],"r", encoding='utf-8') as texto_file:
    config = texto_file.read()
texto = json.loads(config)

configuracion = json.loads(config)

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

def choose_language(retry,defaultLanguage):
    with open('languages/'+ defaultLanguage + '.json','r', encoding='utf-8') as fichero_traduccion:
        traduccion = fichero_traduccion.read()  
    configuracion = json.loads(traduccion)
    if (retry):

        print(configuracion['messages']['choose_lang2'])
        print("1. Español/España")
        print("2. English/USA")
        print("3. English/UK")
        eleccion = input()
        if eleccion == "1":
            return "sp_es"
        elif eleccion == "2":
            return "en_us"
        elif eleccion == "3":
            return "en_uk"
        else:
            return choose_language(True,defaultLanguage)
    else:
        print(configuracion['messages']['choose_lang'])
        print("1. Español/España")
        print("2. English/USA (in construction)")
        print("3. English/UK (in construction)")
        print("4. Français ( en construction )")
        eleccion = input()
        if eleccion == "1":
            return "sp_es"
        elif eleccion == "2":
            return "en_us"
        elif eleccion == "3":
            return "en_uk"
        elif eleccion == "4":
            return "fr_fr"
        else:
            return choose_language(True,defaultLanguage)
        
def cargando(clear):
    if (clear):
        clear()
    print(Fore.RED + "Cargando -")
    time.sleep(0.2)
    clear()
    print("Cargando \\")
    time.sleep(0.2)
    clear()
    print("Cargando |")
    time.sleep(0.2)
    clear()
    print("Cargando /")
    time.sleep(0.2)
    clear()
    print("Cargando -")
    time.sleep(0.2)
    clear()
    print("Cargando \\")
    time.sleep(0.2)
    clear()
    print("Cargando |")
    time.sleep(0.2)
    clear()
    print("Cargando /"+Style.RESET_ALL)
    time.sleep(0.2)
    clear()

def menu(retry):
    clear()
    if (retry):
        print(texto["menus"]["main"]["retry"])    
    print(texto["menus"]["main"]["title"])
    print(texto["menus"]["main"]["config"])
    print(texto["menus"]["main"]["exit"])

    eleccion = input()
    if eleccion=="1":
        config_menu(False)
    elif eleccion=="2":
        exit_game()
    else:
        menu(True)

def exit_game():
    print()
    exit()

def config_menu(retry):
    clear()
    if (retry):
        print(texto["menus"]["config"]["retry"])
    print(texto["menus"]["config"]["title"])
    print(texto["menus"]["config"]["language"])
    print(texto["menus"]["config"]["return"])

    eleccion = input()
    if eleccion=="1":
        print("hay que cambiar el idioma")
    elif eleccion=="2":
        menu(False)
    else:
        config_menu(True)

