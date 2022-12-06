from utils import *
import os
clear = lambda: os.system('cls')
import json
import os

configFile = 'secrets/config.json'
with open(configFile,'r') as fichero_config:
    config = fichero_config.read()

configuracion = json.loads(config)
defaultLanguage = configuracion['defaults']['language']

if __name__ == '__main__':

    cabecera()
    titulo()
    lang = choose_language(False)
    try:
        fn=open("languages/" +str(lang) + configuracion["defaults"]["json_ext"],"r") 
    except IOError:
        lang = choose_language(True)
        

    clear()
    print(lang)
    print(defaultLanguage)

