from flask import Blueprint, jsonify
import requests, json
import pandas as pd
import sqlalchemy as db
import time

data = Blueprint('data', __name__)

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
            time.sleep(1)
            responseTemp = requests.get(self.url, headers=self.headers, params={"limit":"50","page":str(index + 1)})
            dataFrameTemp = pd.DataFrame.from_dict(responseTemp.json())
            self.data_frame = pd.concat([self.data_frame,dataFrameTemp], ignore_index=True)
        self.data_frame.to_sql('car_list', con=self.engine, if_exists='replace', index=False)

    def get_data_frame(self):
        if self.data_frame is None:
            with self.engine.connect() as connection:
                query_result = connection.execute(db.text("SELECT * FROM car_list;")).fetchall()
                self.data_frame = pd.DataFrame(query_result)
        return self.data_frame
    
project = Project("6ae4620f9emsh54de9661868b4f9p13701cjsn18705c66c419")

@data.route('/populate_db', methods=['GET'])
def populate_db():
    project.populate_DB()
    return jsonify({"message": "Database populated."})

@data.route('/data', methods=['GET'])
def get_data():
    with project.engine.connect() as connection:
        query_result = connection.execute(db.text("SELECT * FROM car_list LIMIT 10;")).fetchall()
    data = [dict(row) for row in query_result]
    return jsonify(data)
