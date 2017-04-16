from flask import abort
from flask import Flask
from flask import jsonify
from flask import request
from flask import Blueprint
from flask import render_template
#from flask import g

import re
#import json
#import time
#import requests
#import datetime

#import random as rd

from synth import app

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

tags = {
    "start":            "Conversation start command",
    "silence":          "An empty muted answer",
    "eos":            "A new line",

    "name":             "A name",
    "language":         "A language",
    "switch":           "Mark a change on the subject of the conversation",

    "typo":             "A typo=Where are you {typo}form{}from{/typo}?",

    "request":          "A request={request}Make me a sandwich{/request}",
    "confirmation":     "A confirmation={confirmation}Yes please{/confirmation}",
    "compare":          "A confirmation={compare}{subject:1}Beach{/subject} or {subject:2}mountains{/subject}?{/compare}",

    "taxa":             "A taxa (race)=I am a {taxa}robot{/taxa}",
    "ice_breaker":      "Short question to bring a new theme",
    "greetings":        "Greetings={greetings}Hi there{/greetings}",

    "subject":          "What are we talking about?",
    "subject_owner":    "Who is the owner of that subject?",
    "subject_property": "A property of the subject=The {subject}sun{/subject} is {subject_property}hot{/subject_property}",
    "interest":         "Interest=I like {interest}footbal{/interest}",

    "satisfaction":     "Emotions",
    "surprise":         "Emotions",
    "curiosity":        "Emotions",
    "happyness":        "Emotions",
    "tender":           "Emotions",
}

def parse_synth(text):
    parsed = {"not_found": []}
    tag_search = re.findall(r"\{(?:\/)?(?P<tag>.*?)(?:\:.*?)?(?:\/)?\}", text)
    for found_tag in tag_search:
        if found_tag not in tags:
            parsed["not_found"].append(found_tag)
    return parsed


@main.route('/api')
def api():
    with open('synth_files/0fac76.synth', 'r') as myfile:
        text=myfile.read()
    test = {
        "text": text,
        "parsed": parse_synth(text)
    }
    return jsonify(test)


@main.route('/')
def index():
    return render_template('index.html')
