<h2 align="center">Pizza_Bot_Telegram</h2>

### Описание проекта:
Телеграм Бот для магазина пиццерии с помощью framework aiogram.
Функциональные возможности :
- общение с пользователями
- может сбрасывать время работы пиццерии и адрес
- наличие меню пиццерии для пользователей
- наличие кнопок для отправки сообщений
- возможность поделиться контактами с ботом и месторасположением
- также есть аккаунт Админа, с проверкой на идентификацию админа
- группа пиццерии ,для Админа и бота
- панель для Админа с возможностями состовлять ,редактировать меню (загружать фото,описание,цены),также удалять пункты меню



### Инструменты разработки

**Стек:**
- Python >= 3.9
- aoigram
- sqlite3

## Разработка


##### 1) Создать виртуальное окружение

    python -m venv venv
    
##### 2) Активировать виртуальное окружение

##### 3) Загружаем необходимые зависимости aiogram:

    from aiogram import Bot
    from aiogram.dispatcher import Dispatcher
    import os
    from aiogram.contrib.fsm_storage.memory import MemoryStorage

##### 4) Создаем бота и подключаем TOKEN

    TOKEN = "TOKEN"

    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot, storage=storage)
    
##### 5) Настраиваем бота на отправку сообщений
    
##### 6) Создаем кнопки для отправки сообщений боту 
    b1 = KeyboardButton('/Режим_работы')
    b2 = KeyboardButton('/Расположение')
    b3 = KeyboardButton('/Меню')
    b4 = KeyboardButton('Поделиться номером', request_contact=True)
    b5 = KeyboardButton('Отправить где я', request_location=True )


##### 7) Подключаем панель Админа с проверкой на идентификацию админа 
    
##### 8) Подключаем панель Админа с возможностью управлять меню пиццерии 

    button_load = KeyboardButton('/Загрузить')
    button_delete = KeyboardButton('/Удалить')

    button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load)\
            .add(button_delete)

##### 9) База данных для меню пицеерии
    def sql_start():
    global base,cur
    base = sq.connect('pizza_cool.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()
    
##### 10) Создаем инлайн ссылки в чате 
    urlkb = InlineKeyboardMarkup(row_width=2)
    urlButton = InlineKeyboardButton(text='Ссылка', url='https://youtube.com')
    urlButton2 = InlineKeyboardButton(text='Ссылка2', url='https://google.com')
    x = [InlineKeyboardButton(text='Ссылка3', url='https://google.com'), InlineKeyboardButton(text='Ссылка4', url='https://google.com'),\
     InlineKeyboardButton(text='Ссылка5', url='https://google.com')]
    urlkb.add(urlButton, urlButton2).row(*x).insert(InlineKeyboardButton(text='Ссылка6', url='https://google.com'))

##### 11) Подключаем группу для пиццерии