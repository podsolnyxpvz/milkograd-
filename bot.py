
import telebot
import random
from telebot import types
import os
import asyncio
import time 

bot = telebot.TeleBot('5514650900:AAHZghYZTVBQV4D2PUEIUxXc8-KVeghQ8Jg')
print ("█▀ ▀█▀ ▄▀█ █▀█ ▀█▀ █▀▀ █▀▄\n▄█ ░█░ █▀█ █▀▄ ░█░ ██▄ █▄▀")
ID = '-1001608307734'
          
@bot.message_handler(commands=["start"])
def start(message):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Открыть🃏")
        item2=types.KeyboardButton("Карты и их редкость🗂️")
        item3=types.KeyboardButton("Милкоград🍼")
        item5=types.KeyboardButton("Предложить свою карту🗣️📝")
        item20=types.KeyboardButton("Лог изменений🆙🤖")
        markup.add(item1)
        markup.add(item2)
        markup.add(item5, item20)
        markup.add(item3)
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEFekFi7eXkYOFVDJOhFEKVIhVM8RVbTQACAQEAAladvQoivp8OuMLmNCkE")
        bot.send_message(message.chat.id, f'''Привет {message.from_user.first_name}👋! Чтобы начать, нажимай на кнопки снизу⬇️''',  reply_markup=markup)
        
        
        
@bot.message_handler(content_types=['text'])
def text(message):
  if message.text == 'Открыть🃏':
  	photo = open('cards/' + random.choice(os.listdir('cards')), 'rb')
  	bot.send_photo(message.chat.id, photo, reply_to_message_id=message.message_id)
  if message.text == 'Карты и их редкость🗂️':
  	bot.reply_to(message, '''<b>КАРТЫ И ИХ РЕДКОСТЬ🃏:</b>\n\n@Krebsonplay - обычный🔵\n@mertvvnytrip - обычный🔵\n@OPOOOOOOOOOOO - обычный🔵\n@Blevota_kozla - обычный🔵\n@Nenabobibi - обычный🔵\n@ijustwntualltoshtup - обычный🔵\n@garry_boy21 - обычный🔵\n\n@Ziro69 - редкий🟢\n@sidr228 - редкий🟢\n@wills_z00 - редкий🟢\n@nekokaktus - редкий🟢\n@siwemt - редкий🟢@Kilkq111 - редкий🟢\n@doziz - редкий🟢\n@Bumagoed редкий🟢\n@ZXCpro100chel - редкий🟢\n@ksenofoni - редкий🟢\n@Artil_glas - редкий🟢\n@guidoomista - редкий🟢\n@Tap1ck - редкий🟢\n@zzu_61 - редкий🟢\n@djxnddsjs - редкий🟢\n@lriska_Milk - редкий🟢\n@fonnre - редкий🟢\n@Expirience_Gold - редкий🟢\n@shirona_shirona - редкий🟢\n@Western_shock - редкий🟢\n@BLET_SUPE - редкий🟢\n@ahuennie_kirieshki - редкий🟢\n@JoRriK7 - редкий🟢\n@Epplot - редкий🟢\n@Dramoed-редкий🟢\n\n@Letun104 - эпический🟣\n@hofhoo - эпический🟣@Izolenta_Kypera - эпический🟣\n@SMsneez - эпический🟣\n@xx_loshad_xx - эпический🟣\n@myBroyyyyy - эпический🟣\n@xawar228 - эпический🟣\n@windings - эпический🟣\n@tetris_ines - эпический🟣\n@bibizyanya - эпический🟣\n@MechusYt - эпический🟣\n@OKUASU_ABCHIHBA - эпический🟣\n@zzu_62 - эпический🟣\n@legenda_pes - эпический🟣\n@elfrvioF - эпический🟣\n\n@gera_oF - легендарныыыый🟡\n@tetbanjojosnus - легендарный🟡\n@omiomiomiomiomiomi - легендарный🟡@Crade9801 - легендарный🟡\n@Krutoibober95 - легендарный🟡\n@SkocthFactit_ines - легендарный🟡\n@blag0o - легендарный🟡\n@xsv19 - легендарный🟡\n@mashaluy - легендарный🟡\n@gegestudio - легендарный🟡\n\n<b>@agentmoloko - IMPOSSIBLE☠️🍀\n@cakaoF - IMPOSSIBLE☠️🍀</b>\n\n<b>Карт на данный момент: 58</b>''', parse_mode = 'HTML')
  if message.text == 'Предложить свою карту🗣️📝':
    	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    	item5=types.KeyboardButton(f'''@{message.from_user.username}''')
    	item93=types.KeyboardButton(f'''Назад🔙''')
    	markup.add(item5)
    	markup.add(item93)
    	bot.reply_to(message, "Отправь свой юзернейм 👤", reply_markup=markup)
  if message.text == f'''@{message.from_user.username}''':
    		markup = telebot.types.ReplyKeyboardRemove()
    		markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    		item6=types.KeyboardButton(f'''Обычный🔵''')
    		item7=types.KeyboardButton(f'''Редкий🟢''')
    		item8=types.KeyboardButton(f'''Эпический🟣''')
    		item9=types.KeyboardButton(f'''Легендарный🟡''')
    		item10=types.KeyboardButton(f'''IMPOSSIBLE☠️🍀''')
    		item100=types.KeyboardButton(f'''Назад🔙''')
    		markup.add(item6, item7)
    		markup.add(item8, item9)
    		markup.add(item10)
    		markup.add(item100)
    		bot.reply_to(message, "Отправь желаемую редкость, но не наглей пожалуйста 🔵 🟢 🟣 🟡 ⚫", reply_markup=markup)
  elif message.text in ["Обычный🔵", "Редкий🟢", "Эпический🟣", "Легендарный🟡", "IMPOSSIBLE☠️🍀"]:
    			bot.send_message(message.chat.id, "Выбрано, ожидайте")
    			bot.send_message(ID, f'''*@{message.from_user.username} хочет редкость {message.text}*''', parse_mode="Markdown")
    			log = open('предложения.txt', 'a+', encoding='utf-8')
    			log.write(f'''@{message.from_user.username} хочет редкость {message.text}''')
    			log.close()
    			markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    			item1=types.KeyboardButton("Открыть🃏")
    			item2=types.KeyboardButton("Карты и их редкость🗂️")
    			item3=types.KeyboardButton("Милкоград🍼")
    			item5=types.KeyboardButton("Предложить свою карту🗣️📝")
    			item20=types.KeyboardButton("Лог изменений🆙🤖")
    			markup.add(item1)
    			markup.add(item2)
    			markup.add(item5, item20)
    			markup.add(item3)
    			bot.send_sticker(message.chat.id, f'''CAACAgIAAxkBAAEFf05i8B8y8i-G9_VZhwbKfgIBtkLOsgACAgEAAladvQpO4myBy0Dk_ykE''',  reply_markup=markup)
    			
  if message.text == 'Милкоград🍼':
    			markup = types.InlineKeyboardMarkup()
    			button1 = types.InlineKeyboardButton("Милкоград🍼", url='https://t.me/+Zn2mJhxQkjM2NmYy')
    			markup.add(button1)
    			bot.reply_to(message, "Лучший чат🔝".format(message.from_user), reply_markup=markup)
  if message.text == 'Лог изменений🆙🤖':
  	bot.reply_to(message, "*Лог изменений в боте*:\n1 обновление:\n--Новая функция предложения своей карты\n--*Уникальные* 36 карточек\nОбновление 2:\n--Бот поставлен на хостинг,и должен работать всегда", parse_mode="Markdown")
  if message.text == 'Назад🔙':
  	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
  	item1=types.KeyboardButton("Открыть🃏")
  	item2=types.KeyboardButton("Карты и их редкость🗂️")
  	item3=types.KeyboardButton("Милкоград🍼")
  	item5=types.KeyboardButton("Предложить свою карту🗣️📝")
  	item20=types.KeyboardButton("Лог изменений🆙🤖")
  	markup.add(item1)
  	markup.add(item2)
  	markup.add(item5, item20)
  	markup.add(item3)
  	bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEFg3pi8plQBCqCb3i4O2JjVeQbDUXFwwAC8wADVp29Cmob68TH-pb-KQQ", reply_to_message_id=message.message_id)
  	bot.reply_to(message, f'''Отменено...''',  reply_markup=markup)
  	
  
	
bot.infinity_polling(none_stop=True)
