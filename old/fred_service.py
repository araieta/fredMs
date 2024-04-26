from fred_library import *
import logging
import json
import time
import os
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
def create_and_write_freddata(filename,data):
    if not os.path.exists(filename):
        write_dict_in_file(filename, data)
    else:
        print("File Exists yet. \n")
"""
Ciclo che prende dalla lista data_id ogni id series effettua
una richiesta presso FRED e ritorna la dei valori che vengono
inseriti dentro il dizionario dict_for_db con questa forma
 { "id":{"frequency": "...", payload_series : {}}}, ....}

"""
def retrieve_observation_data_fred(data):
    dict_for_db = {}
    c = 1
    for i,freq in data.items():
        #print(i,freq)

        try:
            if c % 120 == 0:
                time.sleep(70)
            response = single_request_test(i)
            print(f"{c}) [*]Retrieve for {i}/{freq}... in corso")

            dict_for_db[i] = {'frequency' : freq,
                              'observation_start': response['observation_start'],
                              'observation_end': response['observation_end'],
                              'payload_series_observation': response
                              }
            print(f"{c})[*]Retrieve for {i}/{freq}... complete \n")
            c += 1
        except KeyError:
            print()
            print(f"###### ERROR JSON ######")
            print({response.json()})
            print(f"########################")
    return dict_for_db


#controllare prima la frequency del dato
#prelevare i vari json e dividere in base alle table della frequency
#per ogni record inserire data del giorno e valore

conf = get_configuration("config.json")

#extract fred id from csv
#id_list = extract_fred_id_from_csv(conf["fred_id_filename"])
#frequency_dict = create_frequency_dictionary(id_list)

filename = 'series_frequency.json'


#create_and_write_freddata(filename,frequency_dict)

"""
Estrazione file per ogni series e creazione dizionario
per inserimento in database.
"""
data =  get_configuration(filename)

dict_for_db = retrieve_observation_data_fred(data)

filename='series_retrieve.json'
create_and_write_freddata(filename,dict_for_db)