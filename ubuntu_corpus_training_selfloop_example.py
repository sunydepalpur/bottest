from chatterbot import ChatBot
import logging


'''
This is an example showing how to train a chat bot using the
Ubuntu Corpus of conversation dialog.
'''

# Enable info level logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot(
    'Example Bot',
    trainer='chatterbot.trainers.UbuntuCorpusTrainer'
)

# Start by training our bot with the Ubuntu corpus data
#chatbot.train()

# Now let's get a response to a greeting
response = chatbot.get_response('Hi?')
print(response)

response = chatbot.get_response('How are you doing today?')
print(response)

print('Type something to begin...')

while True:
    try:
        name = raw_input("your question : ")
        response = bot.get_response(name)
        print response

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
