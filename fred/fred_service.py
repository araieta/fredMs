from fred_library import *


def get_configuration(filename):
    import json
    with open(filename, 'r') as f:
        return json.load(f)
#controllare prima la frequency del dato
#prelevare i vari json e dividere in base alle table della frequency
#per ogni record inserire data del giorno e valore

conf = get_configuration("config.json")

#extract fred id from csv
id_list = extract_fred_id_from_csv(conf["fred_id_filename"])
print(id_list)
#retrieve data from every id_list
for i in id_list[1::]:
    #extract frequency list from json
    print(i)
    get_frequency_from_series(i.strip())