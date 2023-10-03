import requests # you need this module to make an API call
import pandas as pd
import pandas as pd
import json

api_url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"

def get_number_of_jobs_T(technology):

    number_of_jobs = 0

    payload={"Key Skills": technology}

    r=requests.get(api_url,params=payload)

    if r.ok: # if all is well() no errors, no network timeouts)

        data = r.json() 

        number_of_jobs = len(data)
        
    else:
        print("Connection Lost!!!")

    return technology,number_of_jobs 

get_number_of_jobs_T("Python")
