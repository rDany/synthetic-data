from flask import abort
from flask import Flask
from flask import jsonify
from flask import request
from flask import Blueprint
from flask import render_template
#from flask import g

#import json
#import time
#import requests
#import datetime

#import random as rd

from synth import app

main = Blueprint('main', __name__)

#from difflib import SequenceMatcher


@main.route('/')
def index():
    #return jsonify({})
    return render_template('index.html')
