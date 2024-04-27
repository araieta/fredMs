import json
from dotenv import dotenv_values


'''
Và da se...
'''
def _print_dict(dict):
    for k, v in dict.items():
        print( k, "---> ", v)


'''
Semplice funzione per caricare i parametri da un file 
DOTENV
'''  
def get_config(filename):
    return dotenv_values(filename)


'''
Funzionalità per ora solamente per i test e include solo l'adattamento per i json.
'''
def write_json(data, filename):
    
    try:
        with open(f"{filename}.json","w") as f:
            f.write(json.dumps(data))
            print("Written File.")
            
    except BaseException:
        print("Write FILE Error!")