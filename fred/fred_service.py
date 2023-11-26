from fred_library import *
import logging
import json
def write_dict_in_file(filename, dict):
    
    json_data = json.dumps(dict)
    with open(filename, "w") as f:
        f.write(json_data)
        
def get_configuration(filename):
    
    with open(filename, 'r') as f:
        return json.load(f)

def create_frequency_dictionary(id_list):
    c = 1
    frequency_dict = {}
    #retrieve data from every id_list
    print("in corso")
    for i in id_list[1::]:

        #extract frequency list from json
        #print(i)
        freq = get_frequency_from_series(i.strip())
        frequency_dict[freq[0]] = freq[1]
        if c % 120 == 0:
           import time
           sec = 70
           print(f"Timing for {sec}s..... waiting")
           time.sleep(sec)

           """
           The FRED API has a limit of 1000 items per request, with a 
           rate limit of 120 requests per minute.
           """
           print("Continue suspended Thread... ")
        print(f"{c}/{len(id_list)-1}..... {i}")
        c += 1
    return frequency_dict



#controllare prima la frequency del dato
#prelevare i vari json e dividere in base alle table della frequency
#per ogni record inserire data del giorno e valore

conf = get_configuration("config.json")

#extract fred id from csv
id_list = extract_fred_id_from_csv(conf["fred_id_filename"])


import os

filename = 'series_frequency.json'

if not os.path.exists(filename):
    
    frequency_dict = create_frequency_dictionary(id_list)
    filename = 'series_frequency.json'
    write_dict_in_file(filename, frequency_dict)
else:
    print("File Exists yet. \n")

"""
Estrazione file per ogni series e creazione dizionario
per inserimento in database.
"""

data =  get_configuration(filename)
print(data)