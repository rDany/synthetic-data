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

@main.route('/api')
def api():
    test = {
        "text": "#Example\nH:Hi\nR:Hi there[!]",
        "parsed": [
                {"text": "Example", "from": ""},
                {"text": "Hi", "from": "H"},
                {"text": "Hi there[!]", "from": "R", "entities": {"optional":[[8, 11]]}}
            ]
    }
    return jsonify(test)


@main.route('/')
def index():
    return render_template('index.html')
