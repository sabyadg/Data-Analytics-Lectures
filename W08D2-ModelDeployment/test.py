## Python test file for flask to test locally
import requests as r
import pandas as pd
import json
#https://www.postman.com/downloads/

base_url = 'http://127.0.0.1:5000/' #base url local host

json_data = [
    {
    "CRIM" : 11.63,
    "ZN" : 10.0,
    "INDUS" : 2.31,
    "CHAS" : 0.0,
    "NOX" : 0.0538,
    "RM" : 6.575,
    "AGE" : 65.2,
    "DIS" : 4.0900,
    "RAD" : 1.0,
    "TAX" : 2926.0,
    
    }
    ,

        {
    "CRIM" : 0.163,
    "ZN" : 101.0,
    "INDUS" : 2.31,
    "CHAS" : 0.0,
    "NOX" : 0.01538,
    "RM" : 6.575,
    "AGE" : 625.2,
    "DIS" : 4.0900,
    "RAD" : 1.0,
    "TAX" : 296.0,
    "PTRATIO" : 15.3,
    "B" : 369.90,
    "LSTAT": 0
    },
        {
    "CRIM" : 110.63,
    "ZN" : 110.0,
    "INDUS" : 2.31,
    "CHAS" : 0.0,
    "NOX" : 0.0538,
    "RM" : 6.575,
    "AGE" : 65.2,
    "DIS" : 4.0900,
    "RAD" : 1.0,
    "TAX" : 2916.0,
    "PTRATIO" : 15.3,
    "B" : 369.90,
    "LSTAT": 0
    }
]



# Get Response
# response = r.get(base_url)
response = r.post(base_url + "predict", json = json_data)


if response.status_code == 200:
    print('...')
    print('request successful')
    print('...')
    print(response.json())
else:
    print(response.json())
    print('request failed')
