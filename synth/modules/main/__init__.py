from flask import abort
from flask import Flask
from flask import jsonify
from flask import request
from flask import Blueprint
from flask import render_template
#from flask import g

import re
import os
#import json
#import time
#import requests
#import datetime

#import random as rd

from synth import app
from synth.modules.data_compiler import data_compiler

main = Blueprint('main', __name__)

#from difflib import SequenceMatcher

text = """
# Example

H:Hi there
H:Buenas
    R:How are you?
    R:¿Cómo estás?
        H:I'm fine and you?
        H:Bien ¿Y tu?
            R:My systems are working as expected {systems:ok}
            R:Mis sistemas están funcionando según lo esperado {systems:ok}
        H:I'm sad {sadness:0.9}
        H:Estoy triste {sadness:0.9}
            R:What happened?
            R:¿Qué sucedió?
    R:Long time not see you {days_away:2}
    R:Hace mucho que no te veo {days_away:2}
        H:True! Did you miss me?
        H:Cierto! Me extrañaste?
    R:What do you want? {angry:0.7}
    R:¿Qué querés? {angry:0.7}
"""



def parse_synth(text):
    parsed = {"not_found": []}
    tag_search = re.findall(r"\{(?:\/)?(?P<tag>.*?)(?:\:.*?)?(?:\/)?\}", text)
    for found_tag in tag_search:
        if found_tag not in data_compiler.tags:
            parsed["not_found"].append(found_tag)
    return parsed


@main.route('/get_synth_list')
def get_synth_list():
    mypath = 'synth_files'
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    synth_list = {"synth_list": onlyfiles}
    return jsonify(synth_list)


@main.route('/get_synth')
@main.route('/get_synth/<file_name>')
def get_synth(file_name=None):
    if file_name==None:
        abort(404)
    with open(os.path.join('synth_files', file_name), 'r') as myfile:
        text=myfile.read()
    test = {
        "text": text,
        "parsed": parse_synth(text)
    }
    return jsonify(test)


@main.route('/save_synth', methods=['POST'])
def save_synth():
    to_save = request.json
    file_name = to_save["file_name"]

    file = open(os.path.join('synth_files', file_name), 'w')
    file.write(to_save["text"])
    file.close()

    test = {
        "text": to_save["text"],
        "parsed": parse_synth(to_save["text"])
    }
    return jsonify(test)


@main.route('/')
def index():
    return render_template('index.html')
