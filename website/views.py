#import functions
from flask import Blueprint, render_template

#create blueprint
views = Blueprint('views', __name__)

#define route using blueprint
@views.route('/')
def home():
    return render_template("home.html")
