import requests
import json
import datetime
import csv


def extract_fred_id_from_csv(filename_csv):
    links = []
    links_id = []
    # Aprire il file CSV
    with open(filename_csv, "r") as f:
        reader = csv.reader(f)

        # Estrarre la colonna link
        for row in reader:
            links.append(row[1])
    return [x.split("/")[-1] for x in links]
    # Stampare i dati della colonna

def get_frequency_from_series(series_id):
    API_KEY = "6c9fc270f18daf39f55a5d5f3fed1dbf"
    ####### FRED API RETRIEVE INFORMATION TEST PHASE #######
    SERIES_ID = series_id
    start_date = "1960-01-01"
    end_date = "2022-01-01"
    base_url="https://api.stlouisfed.org/fred/"
    obs_endpoint = "series"
    obs_params={
    "series_id":SERIES_ID,
    "api_key":API_KEY,
    "file_type":"json",
    #"realtime_start":start_date,
    #"realtime_end":end_date,
    #"":""
        
    }

    
    
    response = requests.get(base_url+obs_endpoint,params=obs_params)
    #print(response.url)
    
    data = response.json()
    if "seriess" not in data.keys():
        print(data, response.url)


def single_request_test(series_id):
    API_KEY = "6c9fc270f18daf39f55a5d5f3fed1dbf"
    ####### FRED API RETRIEVE INFORMATION TEST PHASE #######
    SERIES_ID = series_id
    start_date = "1960-01-01"
    end_date = "2022-01-01"
    base_url="https://api.stlouisfed.org/fred/series/"
    obs_endpoint = "observations"
    obs_params={
    "series_id":SERIES_ID,
    "api_key":API_KEY,
    "file_type":"json",
    #"realtime_start":start_date,
    #"realtime_end":end_date,
    #"":""
        
    }

    
    response = requests.get(base_url+obs_endpoint,params=obs_params)
    data = response.json()
    #print(data)
            
    
    

############### T E S T --  Z O N E ############### 



#single_request_test("WPS5811")
#get_frequency_from_series("GFDEGDQ188S")




#### FRED API KEY ###
#
#API_KEY = "6c9fc270f18daf39f55a5d5f3fed1dbf"
######## FRED API RETRIEVE INFORMATION TEST PHASE #######
#SERIES_ID = extract_fred_id_from_csv("usa2.csv")
#start_date = "2005-01-01"
#end_date = "2021-01-01"
#base_url="https://api.stlouisfed.org/fred/"
#obs_endpoint = "series"
#
#
#count_request = 0
#for i in SERIES_ID:
#    obs_params={
#    "series_id":f"{i}",
#    "api_key":API_KEY,
##    "file_type":"json",
##    "observation_start":start_date,
##    "observation_end":end_date,
##    "frequency":'d'
#}
#    response = requests.get(base_url+obs_endpoint,params=obs_params)
#    count_request += 1
#    
#    print(f"[*] {response.}")
#    #print(response.url)
#    #print(response.content)
