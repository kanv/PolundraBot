from telebot import types

polundra_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
polundra_markup_btn1 = types.KeyboardButton('/polundra')
polundra_markup.add(polundra_markup_btn1)
