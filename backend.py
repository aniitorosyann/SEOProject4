import requests,json
import pandas as pd
import sqlalchemy as db
import time


#I'll change the name of this class
#this class will contain the main methods to select, store, and return data
class Project:
    def __init__(self, api_key):
        self.url = "https://car-data.p.rapidapi.com/cars"
        self.engine = db.create_engine('sqlite:///cars_database.db')
        self.headers = {
	        "X-RapidAPI-Key": api_key,
	        "X-RapidAPI-Host": "car-data.p.rapidapi.com"
        }
        self.querystring = {"limit":"50","page":"0"}

    def populate_DB(self):
        response = requests.get(self.url, headers=self.headers, params=self.querystring)
        data_frame = pd.DataFrame.from_dict(response.json())
        for index in range(1):
            time.sleep(1)
            responseTemp = requests.get(self.url, headers=self.headers, params={"limit":"50","page":str(index + 1)})
            dataFrameTemp = pd.DataFrame.from_dict(responseTemp.json())
            data_frame = pd.concat([data_frame,dataFrameTemp], ignore_index=True)
        data_frame.to_sql('car_list', con=self.engine, if_exists='replace', index=False)
        with self.engine.connect() as connection:
            query_result = connection.execute(db.text("SELECT * FROM car_list;")).fetchall()
            print(pd.DataFrame(query_result))

test = Project("6ae4620f9emsh54de9661868b4f9p13701cjsn18705c66c419")
test.populate_DB()
  
   





