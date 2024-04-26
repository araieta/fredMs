import json
from dotenv import dotenv_values


def _print_dict(dict):
    for k, v in dict.items():
        print( k, "---> ", v)
        
def get_config(filename):
    return dotenv_values(filename)


def write_json(data, filename):
    
    try:
        with open(f"{filename}.json","w") as f:
            f.write(json.dumps(data))
            print("Written File.")
            
    except BaseException:
        print("Write FILE Error!")