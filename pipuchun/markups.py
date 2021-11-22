
from os import name
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, callback_game, inline_keyboard
from aiohttp.helpers import parse_mimetype
btnprofile = KeyboardButton(' profil ')
profilekey = ReplyKeyboardMarkup(resize_keyboard= True).add(btnprofile)

btnurchannel = InlineKeyboardButton(text='azo bulish', url='https://t.me/ilmziyomaskani')
btndonesub = InlineKeyboardButton(text='azo buldim', callback_data="subchanneldone")

checksubmenu = InlineKeyboardMarkup(row_width=1)
checksubmenu.insert(btnurchannel)
checksubmenu.insert(btndonesub)





btnmain = InlineKeyboardButton('Quron 🎧')


btnmain2 = InlineKeyboardButton('Bot Haqida 📜')

btnmain3 = InlineKeyboardButton('Namoz ☪️')
btnmain4 = InlineKeyboardButton('Multifilimlar 📺')

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

btnorder = InlineKeyboardButton(datetime.now().strftime("%H:%M:%S"),'boshqa')

sainmenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnmain, btnmain2, btnmain3,btnmain4)







btninfo = KeyboardButton(' quron')

btnerkak = KeyboardButton('Erkaklarga 👨‍🦰')
btnayol = KeyboardButton('Ayollarga 👩‍🦰')
orqaga = KeyboardButton('Menu 📜')
orqagaerkaklar = KeyboardButton('Menu 📜')
orqagaayollar= KeyboardButton('Menu 📜')

namozbulimi = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnayol, btnerkak, orqaga)


namozbulimia = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)


namozbulimie = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)


       
namozlist = ['Bomdod 🌃','Peshin 🌇','Asr 🏙','Shom 🌉','Xufton 🌌','Menu 📜']
for i in namozlist:
    namozbulimie.insert(KeyboardButton(text=i, one_time_keyboard=True))
    
    
    
namozlist2 = ['Bomdod 🌃ㅤ','Peshin 🌇ㅤ','Asr 🏙ㅤ','Shom 🌉ㅤ','Xufton 🌌ㅤ','Menu 📜']
    
for n in namozlist2:
     namozbulimia.insert(KeyboardButton(text=n))
     
     
     
multi = ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)

multilist = ['Menu 📜','Qur\'onda zikri kelgan ajoyibotlar']
for n in multilist:
    multi.insert(KeyboardButton(text=n))