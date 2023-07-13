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
        self.data_frame = None

    def populate_DB(self):
        response = requests.get(self.url, headers=self.headers, params=self.querystring)
        self.data_frame = pd.DataFrame.from_dict(response.json())
        for index in range(1):
            time.sleep(2)
            responseTemp = requests.get(self.url, headers=self.headers, params={"limit":"50","page":str(index + 1)})
            dataFrameTemp = pd.DataFrame.from_dict(responseTemp.json())
            self.data_frame = pd.concat([self.data_frame,dataFrameTemp], ignore_index=True)
        self.data_frame.to_sql('car_list', con=self.engine, if_exists='replace', index=False)

    def dataList(self, searchCategory, searchTerm):
        with self.engine.connect() as connection:
            query_result = connection.execute(db.text(f"SELECT * FROM car_list WHERE {searchCategory}={searchTerm};")).fetchall()
            df = pd.DataFrame(query_result)
            data = df.values.tolist() #here is the one that returns a list of lists
            return data

    def get_data_frame(self):
        return self.data_frame

#test = Project("6ae4620f9emsh54de9661868b4f9p13701cjsn18705c66c419")
#test.populate_DB()
#print(test.dataList(1,2007))
  
   





