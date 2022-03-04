import json
import pandas as pd
import requests
url = "https://api.github.com/repos/pandas-dev/pandas/issues"
data1= requests.get(url).json()

full_data=[]
for row_data in data1:
    new_dict={}
    for key in row_data:
        if type(row_data[key]) is dict:
            for inner_key in row_data[key]:
                new_dict[key+'_'+inner_key]=row_data[key][inner_key]
        else:
            new_dict[key]=row_data[key]
    full_data.append(new_dict)

df_new = pd.DataFrame(full_data)
df_new.to_csv('updated_data.csv')