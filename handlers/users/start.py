import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, ReplyKeyboardMarkup, \
    KeyboardButton
from sqlalchemy import create_engine, MetaData, Table

from keyboards.default.but import where_place_murkup, check_place, but12
from loader import dp, bot
from states.bot_state import FSM
from utils.db_api import add_in_db1, changes_in_db, info
from utils.db_api.add_in_db import add_info
from utils.db_api.test import prosmotr_raspisaniya


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    await bot.send_photo(message.chat.id, 'https://im0-tub-ru.yandex.net/i?id=3218ff2f5f84ec6c027a065b6c24399b-l&n=13')
    await message.answer(f"Привет {message.from_user.full_name}, добро пожаловать в бота ПСБ Спорт!"
                         f"\nВыберете регион, в котором находитесь, чтобы получить информацию о меропиятиях"
                         f"в рамках проекта ПСБ Спорт.", reply_markup=but12)

@dp.message_handler()
async def bot_help1(message: types.Message):
    if message.text == 'Профиль':
        await message.answer(f"{message.from_user.full_name}\n"
                             f"Баллы: {info.prosmotr_raspisaniya5(message.from_user.id)[1]}")
    elif message.text == 'Информация о мероприятиях':
        await message.answer(f"Выберете регион, в котором находитесь, чтобы получить информацию о меропиятиях"
                             f" в рамках проекта ПСБ Спорт",reply_markup=where_place_murkup)
        await FSM.menu_state.set()




inline_btn_1 = InlineKeyboardButton('Июнь', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)


@dp.message_handler(state=FSM.menu_state)
async def bot_help(message: types.Message):
    if message.text == 'Назад':
        await bot.send_photo(message.chat.id,
                             'https://im0-tub-ru.yandex.net/i?id=3218ff2f5f84ec6c027a065b6c24399b-l&n=13', )
        await message.answer(f"Привет {message.from_user.full_name}, добро пожаловать в бота ПСБ Спорт!"
                             f"\nВыберете регион, в котором находитесь, чтобы получить информацию о меропиятиях"
                             f" в рамках проекта ПСБ Спорт.", reply_markup=but12)
    else:
        if message.text in check_place:
            await message.answer(f"Вы выбрали {message.text}", reply_markup=ReplyKeyboardRemove())
            await message.answer(f"Выберете месяц проведения мероприятия.", reply_markup=inline_kb1)
            # await FSM.test_state1.set()
        else:
            await message.answer('Не понимаю')


inline_btn_0 = InlineKeyboardButton(' ', callback_data='btn3')
inline_btn_2 = InlineKeyboardButton('1', callback_data='1')
inline_btn_3 = InlineKeyboardButton('2', callback_data='2')
inline_btn_4 = InlineKeyboardButton('3', callback_data='3')
inline_btn_5 = InlineKeyboardButton('4', callback_data='4')
inline_btn_6 = InlineKeyboardButton('5', callback_data='5')
inline_btn_7 = InlineKeyboardButton('6', callback_data='6')
inline_btn_8 = InlineKeyboardButton('7', callback_data='7')
inline_btn_9 = InlineKeyboardButton('8', callback_data='8')
inline_btn_10 = InlineKeyboardButton('9', callback_data='9')
inline_btn_11 = InlineKeyboardButton('10', callback_data='10')
inline_btn_12 = InlineKeyboardButton('11', callback_data='11')
inline_btn_13 = InlineKeyboardButton('12', callback_data='12')
inline_btn_14 = InlineKeyboardButton('13', callback_data='13')
inline_btn_15 = InlineKeyboardButton('14', callback_data='14')
inline_btn_16 = InlineKeyboardButton('15', callback_data='15')
inline_btn_17 = InlineKeyboardButton('16', callback_data='16')
inline_btn_18 = InlineKeyboardButton('17', callback_data='17')
inline_btn_19 = InlineKeyboardButton('18', callback_data='18')
inline_btn_20 = InlineKeyboardButton('19', callback_data='19')
inline_btn_21 = InlineKeyboardButton('20', callback_data='20')
inline_btn_22 = InlineKeyboardButton('21', callback_data='21')
inline_btn_23 = InlineKeyboardButton('22', callback_data='22')
inline_btn_24 = InlineKeyboardButton('23', callback_data='23')
inline_btn_25 = InlineKeyboardButton('24', callback_data='24')
inline_btn_26 = InlineKeyboardButton('25', callback_data='25')
inline_btn_27 = InlineKeyboardButton('26', callback_data='26')
inline_btn_28 = InlineKeyboardButton('27', callback_data='27')
inline_btn_29 = InlineKeyboardButton('28', callback_data='28')
inline_btn_30 = InlineKeyboardButton('29', callback_data='29')
inline_btn_31 = InlineKeyboardButton('30', callback_data='30')
inline_kb2 = InlineKeyboardMarkup()
inline_kb2.row(inline_btn_0, inline_btn_2, inline_btn_3, inline_btn_4, inline_btn_5, inline_btn_6, inline_btn_7).row(
    inline_btn_8, inline_btn_9, inline_btn_10, inline_btn_11, inline_btn_12, inline_btn_13, inline_btn_14).row(
    inline_btn_15, inline_btn_16, inline_btn_17, inline_btn_18, inline_btn_19, inline_btn_20, inline_btn_21).row(
    inline_btn_22, inline_btn_23, inline_btn_24, inline_btn_25, inline_btn_26, inline_btn_27, inline_btn_28).row(
    inline_btn_29, inline_btn_30, inline_btn_31, inline_btn_0, inline_btn_0, inline_btn_0, inline_btn_0)


@dp.callback_query_handler(state=FSM.menu_state)
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 2:
        await bot.answer_callback_query(callback_query.id, text='Нажата вторая кнопка')
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉', show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Календарь событий на Июнь', reply_markup=inline_kb2)
    await FSM.add_info.set()


inline_btn = InlineKeyboardButton('Регистрация', callback_data='reg')
regestration = InlineKeyboardMarkup()
regestration.row(inline_btn)


@dp.callback_query_handler(state=FSM.add_info)
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    print(callback_query.data)
    global day1
    day1 = datetime.date(year=2021, month=6, day=int(callback_query.data))
    print(callback_query.from_user.id)
    prosmotr_raspisaniya(day1)[4]
    await bot.answer_callback_query(callback_query.id)

    await bot.send_message(callback_query.from_user.id,
                               f"<a href='{prosmotr_raspisaniya(day1)[4]}'>{prosmotr_raspisaniya(day1)[0]}</a>",
                               reply_markup=regestration, parse_mode="HTML")
    await FSM.add_info1.set()


inline_btn1 = InlineKeyboardButton('Я участник', callback_data='uch')
inline_btn2 = InlineKeyboardButton('Я болельщик', callback_data='bol')
kem_yavl = InlineKeyboardMarkup()
kem_yavl.row(inline_btn1, inline_btn2)


@dp.callback_query_handler(state=FSM.add_info1)
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    if callback_query.data == 'reg':
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,
                               f"Кем Вы являетесь на мероприятии?",
                               reply_markup=kem_yavl)
        engine = create_engine('sqlite:///utils//db_api//SPORT.db', echo=True)
        conn = engine.connect()
        meta = MetaData(engine)
        raspisanie = Table('PSB_SPORT', meta, autoload=True)
        try:
            add_in_db1.add_info(conn, raspisanie, callback_query.from_user.id, prosmotr_raspisaniya(day1)[0])
        except:
            changes_in_db.change1(callback_query.from_user.id,prosmotr_raspisaniya(day1)[0],t_f=0)
        await FSM.add_info11.set()

markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
)


@dp.callback_query_handler(state=FSM.add_info11)
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    if callback_query.data == 'uch':
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,
                               f"Поделитесь геоданными.",
                               reply_markup=markup_request)
        await FSM.add_info12.set()
    elif callback_query.data == 'bol':
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,
                               f"Поделитесь геоданными.",
                               reply_markup=markup_request)
        await FSM.add_info12.set()

@dp.message_handler(content_types=types.ContentTypes.LOCATION, state=FSM.add_info12)
async def on_geo_change(message: types.Message, state: FSMContext):
    #await message.answer(f"геоданные \n"
     #                    f"{message.location}",)#"latitude":60.034733,"longitude":30.334121
    if (float(message.location.latitude) > prosmotr_raspisaniya(day=day1)[1]-0.0003) & (float(message.location.latitude) < prosmotr_raspisaniya(day=day1)[1]+0.0003) & (float(message.location.longitude) > prosmotr_raspisaniya(day=day1)[2]-0.0003) & (float(message.location.longitude) < prosmotr_raspisaniya(day=day1)[2]+0.0003):
        await message.answer('Мы рады приветсвовать Вас на мероприятии')
        engine = create_engine('sqlite:///utils//db_api//SPORT.db', echo=True)
        conn = engine.connect()
        meta = MetaData(engine)
        raspisanie = Table('PSB_SPORT', meta, autoload=True)
        changes_in_db.change(message.from_user.id,1)
        await bot.send_photo(message.chat.id,
                             'https://im0-tub-ru.yandex.net/i?id=3218ff2f5f84ec6c027a065b6c24399b-l&n=13')
        await message.answer(f"Привет {message.from_user.full_name}, добро пожаловать в бота ПСБ Спорт!"
                             f"\nВыберете регион, в котором находитесь, чтобы получить информацию о меропиятиях"
                             f"в рамках проекта ПСБ Спорт.", reply_markup=but12)
        await state.finish()

    else:
        await message.answer('Вы где-то не там')