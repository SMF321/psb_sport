import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from sqlalchemy import create_engine, MetaData, Table

from data.config import ADMINS
from keyboards.default.but import but12
from loader import dp, bot
from states.bot_state import FSM
from utils.db_api.add_in_db import add_info


@dp.message_handler(commands=['adminka'], state='*')
async def bot_admin(message: types.Message):
    if str(message.chat.id) == ADMINS:
        await message.answer(f"Привет {message.from_user.full_name}, вы вошли как админ!"
                             f"\nМожете добавить/изменить/удалить  мероприятия.\n"
                             f"/add - Добавить мероприятие\n"
                             f"/change - Изменить данные о мероприятии\n"
                             f"/delete - Удалить мерориятие ")

@dp.message_handler(commands=['add'], state='*')
async def bot_admin(message: types.Message):
    if str(message.chat.id) == ADMINS:
        text = "Ведите дату занятий.\n" \
                "(Например:1.1.2021)\n" \
               "(Не 01.01.2000)"
        await message.answer(text)
        await FSM.add_info.set()
    else:
        pass

@dp.message_handler(state=FSM.add_info)
async def bot_admin(message: types.Message):
    if str(message.chat.id) == ADMINS:
        text = "Напишите название мероприятия."
        date = message.text.split('.')
        year = int(date[2])
        month = int(date[1])
        day = int(date[0])
        global day1
        day1 = datetime.date(year=year, month=month, day=day)
        await message.answer(text=text)
        await FSM.add_info1.set()
    else:
        pass

@dp.message_handler(state=FSM.add_info1)
async def bot_admin(message: types.Message):
    if str(message.chat.id) == ADMINS:
        text = "Напишите ссылку."
        global name
        name = message.text

        await message.answer(text=text)
        await FSM.add_info2.set()
    else:
        pass

@dp.message_handler(state=FSM.add_info2)
async def bot_admin(message: types.Message, state: FSMContext):
    if str(message.chat.id) == ADMINS:
        text = "Поствьте точку на карте.\nРаздел гепозиция."
        global url
        url = message.text

        await message.answer(text=text)
        await FSM.add_info3.set()
    else:
        pass


@dp.message_handler(content_types=types.ContentTypes.LOCATION,state=FSM.add_info3)
async def bot_admin(message: types.Location):
    if str(message.chat.id) == ADMINS:
        text = "Напишите весовой коэффицент мероприятия(сколько баллов за мероприятие)"
        global latitude
        latitude = float(message.location.latitude)
        global longitude
        longitude = float(message.location.longitude)

        await message.answer(text=text)
        await FSM.add_info4.set()

    else:
        pass


@dp.message_handler(state=FSM.add_info4)
async def bot_admin(message: types.Message, state: FSMContext):
    if str(message.chat.id) == ADMINS:
        text = "Тут будет вывод заполненных данных"
        global points
        points = int(message.text)

        engine = create_engine('sqlite:///utils//db_api//SPORT.db', echo=True)
        conn = engine.connect()
        meta = MetaData(engine)
        raspisanie = Table('CONTEST', meta, autoload=True)
        await add_info(conn=conn,raspisanie=raspisanie,date_text=day1,name=name,url=url,latitude=latitude,longitude=longitude,points=points)
        await state.finish()
        await bot.send_photo(message.chat.id,
                             'https://im0-tub-ru.yandex.net/i?id=3218ff2f5f84ec6c027a065b6c24399b-l&n=13')
        await message.answer(f"Привет {message.from_user.full_name}, добро пожаловать в бота ПСБ Спорт!"
                             f"\nВыберете регион, в котором находитесь, чтобы получить информацию о меропиятиях"
                             f"в рамках проекта ПСБ Спорт.", reply_markup=but12)
    else:
        pass