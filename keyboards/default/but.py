from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

check_place = ['Забайкальский край' ,'Республика Адыгея (Адыгея)' ,'Костромская область' ,'Томская область' ,'Архангельская область' ,'Курская область' ,'Оренбургская область' ,'Калининградская область' ,'Чукотский автономный округ' ,'Санкт-Петербург' ,'Тамбовская область' ,'Республика Алтай' ,'Астраханская область' ,'Брянская область' ,'Саратовская область' ,'Республика Башкортостан' ,'Нижегородская область' ,'Волгоградская область' ,'Республика Татарстан' ,'Псковская область' ,'Московская область' ,'Кировская область' ,'Красноярский край' ,'Республика Калмыкия' ,'Приморский край' ,'Иркутская область' ,'Республика Карелия' ,'Свердловская область' ,'Мурманская область' ,'Орловская область' ,'Хабаровский край' ,'Республика Марий Эл' ,'Республика Удмуртия' ,'Ставропольский край' ,'Владимирская область' ,'Ленинградская область' ,'Республика Мордовия' ,'Липецкая область' ,'Тульская область' ,'Тверская область' ,'г. Москва' ,'Смоленская область' ,'Калужская область' ,'Воронежская область' ,'Вся Россия' ,'Ростовская область' ,'Республика Дагестан' ,'Камчатский край' ,'Челябинская область' ,'Пензенская область' ,'Ульяновская область' ,'Республика Бурятия']
place1 = KeyboardButton('Вся Россия')
place2 = KeyboardButton('Архангельская область')
place3 = KeyboardButton('Астраханская область')
place4 = KeyboardButton('Брянская область')
place5 = KeyboardButton('Владимирская область')
place6 = KeyboardButton('Волгоградская область')
place7 = KeyboardButton('Воронежская область')
place8 = KeyboardButton('г. Москва')
place9 = KeyboardButton('Забайкальский край')
place10 = KeyboardButton('Иркутская область')
place11 = KeyboardButton('Калининградская область')
place12 = KeyboardButton('Калужская область')
place13 = KeyboardButton('Камчатский край')
place14 = KeyboardButton('Кировская область')
place15 = KeyboardButton('Костромская область')
place16 = KeyboardButton('Красноярский край')
place17 = KeyboardButton('Курская область')
place18 = KeyboardButton('Ленинградская область')
place19 = KeyboardButton('Липецкая область')
place21 = KeyboardButton('Московская область')
place22 = KeyboardButton('Мурманская область')
place23 = KeyboardButton('Нижегородская область')
place24 = KeyboardButton('Оренбургская область')
place25 = KeyboardButton('Орловская область')
place26 = KeyboardButton('Пензенская область')
place27 = KeyboardButton('Приморский край')
place28 = KeyboardButton('Псковская область')
place29 = KeyboardButton('Республика Адыгея (Адыгея)')
place30 = KeyboardButton('Республика Алтай')
place31 = KeyboardButton('Республика Башкортостан')
place32 = KeyboardButton('Республика Бурятия')
place33 = KeyboardButton('Республика Дагестан')
place34 = KeyboardButton('Республика Калмыкия')
place35 = KeyboardButton('Республика Карелия')
place36 = KeyboardButton('Республика Марий Эл')
place37 = KeyboardButton('Республика Мордовия')
place38 = KeyboardButton('Республика Татарстан')
place40 = KeyboardButton('Республика Удмуртия')
place41 = KeyboardButton('Ростовская область')
place42 = KeyboardButton('Санкт-Петербург')
place43 = KeyboardButton('Саратовская область')
place44 = KeyboardButton('Свердловская область')
place45 = KeyboardButton('Смоленская область')
place46 = KeyboardButton('Ставропольский край')
place47 = KeyboardButton('Тамбовская область')
place48 = KeyboardButton('Тверская область')
place49 = KeyboardButton('Томская область')
place50 = KeyboardButton('Тульская область')
place52 = KeyboardButton('Ульяновская область')
place53 = KeyboardButton('Хабаровский край')
place54 = KeyboardButton('Челябинская область')
place55 = KeyboardButton('Чукотский автономный округ')
place56 = KeyboardButton('Назад')
where_place_murkup = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(place8) \
    .add(place2) \
    .add(place3) \
    .add(place4) \
    .add(place5) \
    .add(place6) \
    .add(place7) \
    .add(place1) \
    .add(place9) \
    .add(place10) \
    .add(place11) \
    .add(place12) \
    .add(place13) \
    .add(place14) \
    .add(place15) \
    .add(place16) \
    .add(place17) \
    .add(place18) \
    .add(place19) \
    .add(place21) \
    .add(place22) \
    .add(place23) \
    .add(place24) \
    .add(place25) \
    .add(place26) \
    .add(place27) \
    .add(place28) \
    .add(place29) \
    .add(place30) \
    .add(place31) \
    .add(place32) \
    .add(place33) \
    .add(place34) \
    .add(place35) \
    .add(place36) \
    .add(place37) \
    .add(place38) \
    .add(place40) \
    .add(place41) \
    .add(place42) \
    .add(place43) \
    .add(place44) \
    .add(place45) \
    .add(place46) \
    .add(place47) \
    .add(place48) \
    .add(place49) \
    .add(place50) \
    .add(place52) \
    .add(place53)\
    .add(place54)\
    .add(place55)\
    .add(place56)

but1 = KeyboardButton('Профиль')
but2 = KeyboardButton('Информация о мероприятиях')
but12 = ReplyKeyboardMarkup(resize_keyboard=True).add(but1).add(but2)