from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import dp, bot

# #Эхо хендлер, куда летят текстовые сообщения без указанного состояния
# @dp.message_handler(state=None)
# async def bot_echo(message: types.Message):
#     await message.answer(f"Эхо без состояния."
#                          f"Сообщение:\n"
#                          f"{message.text}",reply_markup=inline_kb1)
#

# @dp.message_handler(content_types=types.ContentTypes.LOCATION)
# async def on_geo_change(message: types.Message):
#     await message.answer(f"геоданные \n"
#                          f"{message.location}",)#"latitude":60.034733,"longitude":30.334121
#     if (float(message.location.latitude) > 60.034200) & (float(message.location.latitude) < 60.034900) & (float(message.location.longitude) > 30.334000) & (float(message.location.longitude) < 30.334500):
#         await message.answer('1')
#     else:
#         await message.answer('2')
#
# # Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
# @dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
# async def bot_echo_all(message: types.Message, state: FSMContext):
#     state = await state.get_state()
#     await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
#                          f"\nСодержание сообщения:\n"
#                          f"<code>{message}</code>")
