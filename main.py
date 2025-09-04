import telebot
from currency_converter import CurrencyConverter
from telebot import types
from telebot.types import InlineKeyboardButton

bot = telebot.TeleBot("XXX")
currency = CurrencyConverter()
amount = 0
values = ""
first_msg_id = None
second_msg_id = None
codes = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY","SEK", "NZD", "NOK", "ZAR", "BRL", "INR",
         "RUB", "SGD","HKD", "MXN", "KRW", "TRY", "PLN", "HUF", "CZK", "DKK","BGN", "RON", "PHP", "MYR",
         "IDR", "THB", "ILS", "ISK","HRK", "LVL", "LTL", "SKK", "MTL", "CYP", "TRL", "ROL","EEK", "SIT"]
flags = ["🇺🇸","🇪🇺","🇯🇵","🇬🇧","🇦🇺","🇨🇦","🇨🇭","🇨🇳","🇸🇪","🇳🇿","🇳🇴","🇿🇦","🇧🇷","🇮🇳","🇷🇺","🇸🇬","🇭🇰","🇲🇽","🇰🇷",
         "🇹🇷","🇵🇱","🇭🇺","🇨🇿","🇩🇰","🇧🇬","🇷🇴","🇵🇭","🇲🇾","🇮🇩","🇹🇭","🇮🇱","🇮🇸","🇭🇷","🇱🇻","🇱🇹","🇸🇰","🇲🇹","🇨🇾","🇹🇷","🇷🇴","🇪🇪","🇸🇮"]
currency_symbols = {"USD":"$","EUR":"€","JPY":"¥","GBP":"£","AUD":"$","CAD":"$","CHF":"CHF","CNY":"¥",
                    "SEK":"kr","NZD":"$","NOK":"kr","ZAR":"R","BRL":"R$","INR":"₹","RUB":"₽","SGD":"S$",
                    "HKD":"HK$","MXN":"$","KRW":"₩","TRY":"₺","PLN":"zł","HUF":"Ft","CZK":"Kč","DKK":"kr",
                    "BGN":"лв","RON":"lei","PHP":"₱","MYR":"RM","IDR":"Rp","THB":"฿","ILS":"₪","ISK":"kr",
                    "HRK":"kn","LVL":"Ls","LTL":"LTL","SKK":"Sk","MTL":"₤","CYP":"£","TRL":"₤","ROL":"ROL","EEK":"EEK","SIT":"SIT"}



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello! Please enter the amount of currency you want to change: ")
    bot.register_next_step_handler(message,suma)

def currency_list(limited=True):
    if limited:
        markup = types.InlineKeyboardMarkup(row_width=4)
        btn = [InlineKeyboardButton(f"{codes[i]} {flags[i]}", callback_data=(codes[i])) for i in range(8)]
        markup.add(*btn)
        markup.add(InlineKeyboardButton("More", callback_data="more"))
    else:
        markup = types.InlineKeyboardMarkup(row_width=3)
        btn = [InlineKeyboardButton(f"{codes[i]} {flags[i]}", callback_data=(codes[i])) for i in range(len(codes))]
        markup.add(*btn)
        markup.add(InlineKeyboardButton("Less", callback_data="less"))
    return markup

def format_currency(money, code):
    symbol = currency_symbols.get(code, "")
    return f"{money}{symbol}"

def suma(message):
    global amount
    global first_msg_id
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, "Please enter a number.")
        bot.register_next_step_handler(message, suma)
        return

    if amount > 0:
        msg1 = bot.send_message(message.chat.id, 'Select the currency you want to change: ', reply_markup=currency_list(limited=True))
        first_msg_id = msg1.message_id
    else:
        bot.send_message(message.chat.id, "You cannnot enter numbers below zero.")
        bot.register_next_step_handler(message, suma)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global values, first_msg_id, second_msg_id
    bot.answer_callback_query(call.id)

    if call.data == "more":
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=currency_list(limited=False))
        return
    elif call.data == "less":
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=currency_list(limited=True))
        return

    if call.message.message_id == first_msg_id:
        values = call.data + '/'
        msg2 = bot.send_message(call.message.chat.id, 'Select the currency you want to change to: ', reply_markup=currency_list(limited=True))
        second_msg_id = msg2.message_id
        return

    if call.message.message_id == second_msg_id:
        values += call.data
        values = values.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f"{format_currency(amount,values[0])} to: {format_currency(round(res,2),values[1])}")
        bot.send_message(call.message.chat.id, "Please enter the amount of currency you want to change:")
        bot.register_next_step_handler(call.message, suma)

bot.polling(none_stop=True)