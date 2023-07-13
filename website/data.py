from flask import Blueprint, jsonify, request
import json
import pandas as pd
import sqlalchemy as db
import time
import sys
sys.path.append('../') #imports python file from parent directory
from backend import Project

data = Blueprint('data', __name__)


    
project = Project("6ae4620f9emsh54de9661868b4f9p13701cjsn18705c66c419")
project.populate_DB()
#print(project.dataList())

@data.route('/populate_db', methods=['GET'])
def populate_db():
    project.populate_DB()
    return jsonify({"message": "Database populated."})

@data.route('/data', methods=['GET'])
def get_data():
    category = request.args.get('category')
    value = request.args.get('value')
    data = project.dataList(category, value)
    return jsonify(data)
