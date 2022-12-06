from utils import *
import os
clear = lambda: os.system('cls')
import json
import os
import time

configFile = 'secrets/config.json'
with open(configFile,'r', encoding='utf-8') as fichero_config:
    config = fichero_config.read()

configuracion = json.loads(config)
defaultLanguage = configuracion['defaults']['language']

if __name__ == '__main__':
    cargando(True)

    lang = choose_language(False,defaultLanguage)
    if (defaultLanguage!=lang):
        with open(configFile,'w', encoding='utf-8') as jsonFile:
            configuracion['defaults']['language'] = lang
            json.dump(configuracion, jsonFile)
    fn=open("languages/" +str(lang) + configuracion["defaults"]["json_ext"],"r") 
    
    clear()
    cabecera()
    titulo()   
    menu(False)
