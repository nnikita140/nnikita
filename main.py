from telebot import TeleBot
from random import choice


TOKEN = '7508711454:AAEzY80BtaLZ_8vX-T0ydrz_qWQJqnyyNao'
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')


if __name__ == '__main__':
    bot.polling(none_stop=True)


def func(arg_1,arg_2):
    print(arg_1,arg_2)

func(arg_1,arg_2)


def func(arg_1,arg_2):
    value = arg_1 + arg_2

    return value
print(func(3,4))


game_choice = ["камень", "ножницы", "бумага"]
user_poinsts = 0
comp_poinsts = 0

@bot.message_handler(func=lambda x: x.text.lower() in game_choice)
def game(message):
    global user_poinsts
    global comp_poinsts
    user_choice = message.text.lower()
    bot_choice = choice(game_choice)
    bot.send_message(message.chat.id, bot_choice)
    if user_choice == "камень" and bot_choice == "ножницы":
        msg = 'Победа'
        user_poinsts += 1
    elif user_choice == "бумага" and bot_choice == "камень":
        msg = 'Победа'
        user_poinsts += 1
    else:
        msg = "Ты проиграл"
        comp_poinsts += 1
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['poinsts'])
def points(message):
    bot.send_message(message.chat.id, f"бот: {comp_poinsts} игрок: {user_poinsts}")


@bot.message_handler(commands=['reset'])
def reset(message):
    global user_poinsts
    global comp_poinsts
    user_poinsts = 0
    comp_poinsts = 0
    bot.send_message(message.chat.id, "Очки сброшены")


class Game:
    comp = 0
    user = 0
    
    def update(self, user_winner):
        if user_winner:
            self.user += 1
            return 'Победил'
        self.comp += 1
        return 'Проиграл'
    
    def reset(self):
        self.comp = 0
        self.user = 0
        img = open('game.png', 'rb')
        bot,send_photo(message.chat.id, img)
        img.close()