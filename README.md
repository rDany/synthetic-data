# synthetic-data
Synthetic Data repository and compiler

This repository holds artificial conversations stored on text files on a special format.
The conversations can then be compiled using to text files to train seq2seq models.

## Installation

    mkdir rdany-synth
    cd rdany-synth
    virtualenv -p python3 venv
    git clone https://github.com/rDany/synthetic-data.git
    . venv/bin/activate
    pip install flask

## Usage
    cd synthetic-data/synth
    python synth.py

Now you can open the site on http://localhost:5000


## Developing ACE highlighter

Link each file on the `synthetic-data/ace` folder to the correspondent `ace` github clone folder

Except for file `synthetic-data/ace/lib/ace/ext/modelist.js_edit` that describes how you need to modify `ace/lib/ace/ext/modelist.js`

Now you can run ace using the following command:

    node ./static.js

And edit the highlight in real time using the following address: http://localhost:8888/tool/mode_creator.html

Once you are done you just need to compile it with the command:

    node ./Makefile.dryice.js -nc

And the you copy and replace the `mode-synth.js` file in the following way `ace/build/src-noconflict/mode-synth.js` -> `synthetic-data/synth/static/ace-noconflict/mode-synth.js`

And you are done, now the highlighter will be successfully updated.