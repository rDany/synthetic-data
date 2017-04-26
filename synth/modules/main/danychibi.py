#imports
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging

#setting up the bot
bot = ChatBot("Terminal",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="database.db"
)

#checking if trained
if input('Do you want to train the bot? ') == 'no':
    ntbt=False
else:
    ntbt=True
    inp=input('File of training data: ')
    try:
        f=open(inp+'.txt','r')
        TRAININGDATA=[]
        for line in f:
            TRAININGDATA.append(line)
        bot.set_trainer(ListTrainer)
        bot.train(TRAININGDATA)
    except (IOError):
        print ('File does not exist. Please try again.')

#chat with danychidi if he does not need to be trained
if ntbt == False:
    print("You are now talking with DanyChibi, say something!")
    print()
    while True:
        try:
            bot_input = bot.get_response(None)
        except (KeyboardInterrupt, EOFError, SystemExit):
            print ()
            break
