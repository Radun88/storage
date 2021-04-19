import telebot
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from telebot import types


TOKEN ='1779506117:AAFev7IeK2jfKsYLzQ1tKGL1_JAiNLvb0ac'
bot = telebot.TeleBot(TOKEN)

table = types.ReplyKeyboardMarkup()

button_tiker = types.KeyboardButton('Тикеры')
button_pay = types.KeyboardButton('Оплата подписки')
table.add(button_tiker, button_pay)






@bot.message_handler(commands=['start'])
def start_message(message: types.Message):
    bot.send_message(message.chat.id, "Equity Market bot", reply_markup=table)
#   bot.send_message(message.chat.id, "Equity Market bot активирован и готов к работе!")
#   bot.send_message(message.chat.id, "Всем удачи, профитов и хорошего дня!")
#   bot.send_message(message.chat.id, "Введите запрос в формате: TSLA 2020(год)-01(месяц)-01(день)")
#   bot.send_message(message.chat.id, "TSLA AAPL GOOGL 2020-01-01 / несколько тикеров вводится через пробел.")

#@bot.message_handler(content_types=['document']) # Приём документов
#@bot.message_handler(commands=['start'])

@bot.message_handler(content_types=['text'])
def send_text(message):

    if message.text == "Тикеры":
        bot.send_message(message.chat.id, "Сверить список тикеров возможно на Yahoo Finance (https://finance.yahoo.com)/ отличие тикеров только по РФ инвестиционным ценным бумагам ,например: SBER.ME(Сбербанк)")
    if message.text == "Оплата подписки":
        #bot.send_message(message.chat.id, 'Оплата подписки 0,99$ за месяц Свистунов C.Г ИНН 503214219656')
        bot.send_message(message.chat.id, "Equity Market bot активирован и готов к работе!")
        bot.send_message(message.chat.id, "Всем удачи, профитов и хорошего дня!")
        bot.send_message(message.chat.id, "Введите запрос в формате: TSLA 2020(год)-01(месяц)-01(день)")
        bot.send_message(message.chat.id, "TSLA AAPL GOOGL 2020-01-01 / несколько тикеров вводится через пробел.")

    else:
        work1(message)



def work1(message):
    try:
        price: [str, str] = ""
        vol: [str, str] = ""
        assets = []

        mas = parse(message)
        print(mas)

        date = mas[len(mas) -1]

        mas.pop(len(mas)-1)

        print(mas)
        print(date)

        for i in range(0, len(mas)):
            assets.append(str(mas[i]))

        pf_data = pd.DataFrame()

        data_start = date#str(input())  # 2012-1-1

        for a in assets:
            pf_data[a] = wb.DataReader(a, data_source='yahoo', start=data_start)['Adj Close']

        log_returns = np.log(pf_data / pf_data.shift(1))

        # средняя доходность бумаги
        for a in assets:
            income = log_returns[a].mean() * 250

            price = "Cредняя доходность бумаги:\n"
            price = price + '{: <7} {: >7.2%} '.format(a, income)
            bot.send_message(message.chat.id, price)
            print('{: <7} {: >7.2%} '.format(a, income), 'Cредняя доходность бумаги')

        # средняя волатильность бумаги
        for a in assets:
            volatility = log_returns[a].std() * 250 ** 0.5

            vol = "Cредняя волатильность бумаги:\n"
            vol = vol + '{: <7} {: >7.2%}'.format(a, volatility)
            bot.send_message(message.chat.id, vol)
            print('{: <7} {: >7.2%}'.format(a, volatility), 'Cредняя волатильность бумаги')





        # Plot all the close prices
        #((pf_data.pct_change() + 1).cumprod()).plot(figsize=(7, 5))

        # Show the legend
        #plt.legend()

        # Define the label for the title of the figure
        #plt.title("Adjusted Close Price", fontsize=16)

        # Define the labels for x-axis and y-axis
        #plt.ylabel('Price', fontsize=14)
        #plt.xlabel('Year', fontsize=14)

        # Plot the grid lines
        #plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
        #plt.show()


        #def photo_handler(bot, update):

        #print(+str(update.message.photo.plt.show))
        #plt.show.download('photo.jpg')
        #bot.send_photo(message.chat.id, photo=open(plt.title + ".png", 'rb'))

    except:
        bot.send_message(message.chat.id, "Ошибка, попробуйте ввести заново\nПример: TSLA AAPL GOOGL 2020-01-01 ")
        print("error")

def parse(message):
    s = message.text
    arr = s.split(' ')
    return arr



@bot.message_handler(commands=['month'])
def do_with_command(message):
    print("Iam here")



bot.polling()



