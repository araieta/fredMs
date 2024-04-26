import requests



def _make_req(base_url, endpoint, param):
    try:
        response = requests.get(base_url+endpoint, params=param)
        data = response.json()
        return data
    except BaseException:
        print(f"Something Wrong  \ status code: { response.status_code }; ")

'''
I dati di interesse sono solamente di frequenze
    - Giornaliera
    - Mensile
    - Trimestrale
'''
def frequency(series_id, api_key):
    
    base_url='https://api.stlouisfed.org/fred/series?series_id=GNPCA&api_key=abcdefghijklmnopqrstuvwxyz123456'
    endpoint = 'series'
    
    param = {
        "series_id":series_id,
        "api_key":api_key,
        "file_type":"json"
    }
    temporary_frequency = _make_req(base_url, endpoint, param)
    
    #sub DTO logic
    
    #return temporary_frequency
    return {
        "Id":temporary_frequency["seriess"][0]["id"],
        "Title":temporary_frequency["seriess"][0]["title"],
        "Frequency":temporary_frequency["seriess"][0]["frequency"],
        #"Notes":temporary_frequency["seriess"][0]["notes"]
    }
        

#single fred request
def sfreq(series_id, api_key):
    ####### FRED API RETRIEVE INFORMATION TEST PHASE #######
    start_date = "1960-01-01"
    end_date = "2024-01-01"
    base_url="https://api.stlouisfed.org/fred/series/"
    obs_endpoint = "observations"
    
    obs_params={
        "series_id":series_id,
        "api_key": api_key,
        "file_type":"json",
        "realtime_start":start_date,
        "realtime_end":end_date
        
        }
    return _make_req(base_url, obs_endpoint, obs_params)


