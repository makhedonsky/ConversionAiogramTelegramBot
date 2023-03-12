from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import requests# pip install
from unitconv import *
from currency import *


import os, json, string

storage=MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)

async def on_startup(_):
	print('Bot is online')


bt_units = KeyboardButton('Единицы Измерения')
bt_currency = KeyboardButton('Валюты')

kb_ChooseConversion = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
kb_ChooseConversion.add(bt_units).add(bt_currency)

@dp.message_handler(commands = ['start', 'help'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Здравствуйте. Вы обратились к боту конвертатору. Выберите конвертация чего вас интересует.', reply_markup=kb_ChooseConversion)
		#await message.delete()
	except:
		await message.reply('Для использования бота пишите ему в ЛС.')




##############################################################		UNIT CONVERSION    ########################################################          
bt_lentgh = KeyboardButton('Длинна')
bt_weight = KeyboardButton('Масса')
bt_square = KeyboardButton('Площадь')
bt_volume = KeyboardButton('Объем')
bt_back = KeyboardButton('Отмена')

kb_ChooseUnitCategory = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
kb_ChooseUnitCategory.row(bt_lentgh, bt_weight, bt_square, bt_volume).add(bt_back)

@dp.message_handler(Text(equals = 'Единицы Измерения'))
async def command_UnitConversion(message : types.Message):
	await message.answer('Выберите интересующую вас категорию единиц измерения', reply_markup=kb_ChooseUnitCategory)


#																																FSM
class FSMAdminLentgh(StatesGroup):
	choise1 = State()
	convNumber = State()
	choise2 = State()

class FSMAdminWeight(StatesGroup):
	choise1 = State()
	convNumber = State()
	choise2 = State()

class FSMAdminSquare(StatesGroup):
	choise1 = State()
	convNumber = State()
	choise2 = State()

class FSMAdminVolume(StatesGroup):
	choise1 = State()
	convNumber = State()
	choise2 = State()

choise1 = ''
convNumber = 0.0
choise2 = ''

##################################################################################################	LENTGH  ###################################
bt_km = KeyboardButton('Км')
bt_m = KeyboardButton('М')
bt_dm = KeyboardButton('Дм')
bt_cm = KeyboardButton('См')
bt_mm = KeyboardButton('Мм')
bt_back = KeyboardButton('Отмена')

kb_ChooseUnitLength = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
kb_ChooseUnitLength.row(bt_km, bt_m, bt_dm, bt_cm, bt_mm).add(bt_back)

@dp.message_handler(state="*", commands = 'Отмена')
@dp.message_handler(Text(equals = 'Отмена', ignore_case=True), state = "*")
async def command_cancelState(message:types.Message, state: FSMContext):
	#current_state = await state.get_state()
	#if current_state is None:
	#	return
	await state.finish()
	await message.answer('Выберите конвертация чего вас интересует.', reply_markup = kb_ChooseConversion)


@dp.message_handler(Text(equals='Длинна'), state=None)
async def command_UnitConversionLength(message : types.Message):
	await FSMAdminLentgh.choise1.set()#																							 Открываем класс
	await message.answer('Какую е.и желаете конвертировать?', reply_markup=kb_ChooseUnitLength)
		

@dp.message_handler(content_types = ['text'], state=FSMAdminLentgh.choise1)
async def command_UnitConversionLength1(message : types.Message, state: FSMContext):
	global choise1 
	choise1 = message.text
	await FSMAdminLentgh.next()
	await message.answer('Введите число', reply_markup = ReplyKeyboardRemove())
	

@dp.message_handler(content_types = ['text'], state=FSMAdminLentgh.convNumber)
async def command_UnitConversionLength2(message : types.Message, state: FSMContext):
	global convNumber 
	convNumber = float(message.text)
	await FSMAdminLentgh.next()
	await message.answer('В какую е.и желаете конвертировать?', reply_markup=kb_ChooseUnitLength)


@dp.message_handler(content_types = ['text'], state=FSMAdminLentgh.choise2)
async def command_UnitConversionLength3(message : types.Message, state: FSMContext):
	global choise2
	choise2 = message.text
	await message.answer(str(finally_length(choise1, convNumber, choise2)) + " " + str(choise2))
	await message.answer('Выберите интересующую вас категорию единиц измерения', reply_markup=kb_ChooseUnitCategory) 
	await state.finish()#																							 	Закрываем класс
###############################################################################################################################################




##################################################################################################	WEIGHT  ###################################
bt_ton = KeyboardButton('Т')
bt_centner = KeyboardButton('Ц')
bt_kg = KeyboardButton('Кг')
bt_gram = KeyboardButton('Г')
bt_mg = KeyboardButton('Мг')


kb_ChooseUnitWeight = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
kb_ChooseUnitWeight.row(bt_ton, bt_centner, bt_kg, bt_gram, bt_mg).add(bt_back)

@dp.message_handler(Text(equals='Масса'), state=None)
async def command_UnitConversionWeight(message : types.Message):
	await FSMAdminWeight.choise1.set()#																							 Открываем класс
	await message.answer('Какую е.и желаете конвертировать?', reply_markup=kb_ChooseUnitWeight)
		

@dp.message_handler(content_types = ['text'], state=FSMAdminWeight.choise1)
async def command_UnitConversionWeight1(message : types.Message, state: FSMContext):
	global choise1 
	choise1 = message.text
	await FSMAdminWeight.next()
	await message.answer('Введите число', reply_markup = ReplyKeyboardRemove())
	

@dp.message_handler(content_types = ['text'], state=FSMAdminWeight.convNumber)
async def command_UnitConversionWeight2(message : types.Message, state: FSMContext):
	global convNumber 
	convNumber = float(message.text)
	await FSMAdminWeight.next()
	await message.answer('В какую е.и желаете конвертировать?', reply_markup=kb_ChooseUnitWeight)


@dp.message_handler(content_types = ['text'], state=FSMAdminWeight.choise2)
async def command_UnitConversionWeight3(message : types.Message, state: FSMContext):
	global choise2
	choise2 = message.text
	await message.answer(str(finally_weight(choise1, convNumber, choise2)) + " " + str(choise2))
	await message.answer('Выберите интересующую вас категорию единиц измерения', reply_markup=kb_ChooseUnitCategory) 
	await state.finish()#																							 	Закрываем класс
################################################################################################################################################




##################################################################################################	SQUARE  ###################################
bt_km2 = KeyboardButton('Км^2')
bt_m2 = KeyboardButton('М^2')
bt_dm2 = KeyboardButton('Дм^2')
bt_cm2 = KeyboardButton('См^2')
bt_mm2 = KeyboardButton('Мм^2')

kb_ChooseUnitSquare = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
kb_ChooseUnitSquare.row(bt_km2, bt_m2, bt_dm2, bt_cm2, bt_mm2).add(bt_back)

@dp.message_handler(Text(equals='Площадь'), state=None)
async def command_UnitConversionSquare(message : types.Message):
	await FSMAdminSquare.choise1.set()#																							 Открываем класс
	await message.answer('Какую е.и желаете конвертировать?', reply_markup=kb_ChooseUnitSquare)
		

@dp.message_handler(content_types = ['text'], state=FSMAdminSquare.choise1)
async def command_UnitConversionSquare1(message : types.Message, state: FSMContext):
	global choise1 
	choise1 = message.text
	await FSMAdminSquare.next()
	await message.answer('Введите число', reply_markup = ReplyKeyboardRemove())
	

@dp.message_handler(content_types = ['text'], state=FSMAdminSquare.convNumber)
async def command_UnitConversionSquare2(message : types.Message, state: FSMContext):
	global convNumber 
	convNumber = float(message.text)
	await FSMAdminSquare.next()
	await message.answer('В какую е.и желаете конвертировать?', reply_markup=kb_ChooseUnitSquare)


@dp.message_handler(content_types = ['text'], state=FSMAdminSquare.choise2)
async def command_UnitConversionSquare3(message : types.Message, state: FSMContext):
	global choise2
	choise2 = message.text
	await message.answer(str(finally_square(choise1, convNumber, choise2)) + " " + str(choise2))
	await message.answer('Выберите интересующую вас категорию единиц измерения', reply_markup=kb_ChooseUnitCategory) 
	await state.finish()#																							 	Закрываем класс
###############################################################################################################################################




##################################################################################################	VOLUME  ###################################
bt_km3 = KeyboardButton('Км^3')
bt_m3 = KeyboardButton('М^3')
bt_dm3 = KeyboardButton('Дм^3')
bt_cm3 = KeyboardButton('См^3')
bt_mm3 = KeyboardButton('Мм^3')

kb_ChooseUnitVolume = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
kb_ChooseUnitVolume.row(bt_km3, bt_m3, bt_dm3, bt_cm3, bt_mm3).add(bt_back)

@dp.message_handler(Text(equals='Объем'), state=None)
async def command_UnitConversionVolume(message : types.Message):
	await FSMAdminVolume.choise1.set()#																							 Открываем класс
	await message.answer('Какую е.и желаете конвертировать?', reply_markup=kb_ChooseUnitVolume)
		

@dp.message_handler(content_types = ['text'], state=FSMAdminVolume.choise1)
async def command_UnitConversionVolume1(message : types.Message, state: FSMContext):
	global choise1 
	choise1 = message.text
	await FSMAdminVolume.next()
	await message.answer('Введите число', reply_markup = ReplyKeyboardRemove())
	

@dp.message_handler(content_types = ['text'], state=FSMAdminVolume.convNumber)
async def command_UnitConversionVolume2(message : types.Message, state: FSMContext):
	global convNumber 
	convNumber = float(message.text)
	await FSMAdminVolume.next()
	await message.answer('В какую е.и желаете конвертировать?', reply_markup=kb_ChooseUnitVolume)


@dp.message_handler(content_types = ['text'], state=FSMAdminVolume.choise2)
async def command_UnitConversionVolume3(message : types.Message, state: FSMContext):
	global choise2
	choise2 = message.text
	await message.answer(str(finally_volume(choise1, convNumber, choise2)) + " " + str(choise2))
	await message.answer('Выберите интересующую вас категорию единиц измерения', reply_markup=kb_ChooseUnitCategory) 
	await state.finish()#																							 	Закрываем класс	
###############################################################################################################################################



















#																	CURRENCY CONVERSION
bt_currlist = KeyboardButton('Список курса валют')
bt_currconv = KeyboardButton('Конвертация Валют')
bt_back = KeyboardButton('Отмена')

kb_ChooseCurrencyFunction = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
kb_ChooseCurrencyFunction.row(bt_currlist, bt_currconv).add(bt_back)

@dp.message_handler(Text(equals = 'Валюты'))
async def command_UnitConversion(message : types.Message):
	await message.answer('Выберите интересующую вас функцию валют', reply_markup=kb_ChooseCurrencyFunction) 









#																Список курса валют
@dp.message_handler(Text(equals='Список курса валют'), state=None)
async def command_UnitConversionLength(message : types.Message):
	#await message.answer(f'USD - {str(currency_convert("USD", 1))} kzt;\n'	
	#					f'EUR - {str(currency_convert("EUR", 1))} kzt;\n'
	#					f'TRY - {str(currency_convert("TRY", 1))} kzt;\n'	
	#					f'RUB - {str(currency_convert("RUB", 1))} kzt;\n'
	#					f'KGS - {str(currency_convert("KGS", 1))} kzt;\n'	
	#					f'CNY - {str(currency_convert("CNY", 1))} kzt;', )
	await message.answer(currency_list())
	await message.answer('Выберите интересующую вас функцию валют', reply_markup=kb_ChooseCurrencyFunction)




# 																Конвертация валют, фсм
class FSMAdminCurrency(StatesGroup):
	choise1 = State()
	convNumber = State()


bt_usd = KeyboardButton('USD')
bt_rub = KeyboardButton('RUB')
bt_eur = KeyboardButton('EUR')
bt_try = KeyboardButton('TRY')
bt_kgs = KeyboardButton('KGS')
bt_cny = KeyboardButton('CNY')
bt_back = KeyboardButton('Отмена')

kb_ChooseCurrency = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
kb_ChooseCurrency.row(bt_usd, bt_rub, bt_eur, bt_try, bt_kgs, bt_cny).add(bt_back)


@dp.message_handler(Text(equals='Конвертация Валют'), state=None)
async def command_UnitConversionLength(message : types.Message):
	await FSMAdminCurrency.choise1.set()#																							 Открываем класс
	await message.answer('Какую валюту желаете конвертировать?', reply_markup=kb_ChooseCurrency)

@dp.message_handler(content_types = ['text'], state=FSMAdminCurrency.choise1)
async def command_UnitConversionLength1(message : types.Message, state: FSMContext):
	global choise1 
	choise1 = message.text
	await FSMAdminCurrency.next()
	await message.answer('Введите число', reply_markup = ReplyKeyboardRemove())

@dp.message_handler(content_types = ['text'], state=FSMAdminCurrency.convNumber)
async def command_UnitConversionLength1(message : types.Message, state: FSMContext):
	global convNumber 
	convNumber = message.text
	await message.answer(f"{str(currency_convert(choise1, convNumber))} KZT")
	await message.answer('Выберите интересующую вас функцию валют', reply_markup=kb_ChooseCurrencyFunction) 
	await state.finish()









executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
