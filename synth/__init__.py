from flask import Flask

app = Flask(__name__)

app.config.from_object('synth.config.Config')

from synth.modules.main import main
app.register_blueprint(main)
