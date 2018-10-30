from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Consuelo Chat Bot')

conversation_options = ['Hi', 'Hello', 'What is your name?', 'My name is Consuelo', 'You are a bot?', 'I think so']

bot.set_trainer(ListTrainer)
bot.train(conversation_options)

while True:
    question = input("User: ")
    answer = bot.get_response(question)
    if float(answer.confidence) > 0.5:
        print('Consuelo Bot: ', answer)
    else:
        print('Consuelo Bot: I do not know the answer for the question, sorry')
