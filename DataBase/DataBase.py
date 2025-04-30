import sqlite3 as sq
import asyncio

async def DataBase_start():
    with sq.connect('data_base.db') as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS deal_types (
        deal_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
        deal_type TEXT NOT NULL UNIQUE,
        deal_description TEXT NOT NULL);""")

        cur.execute("""CREATE TABLE IF NOT EXISTS deals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL,
        phone_number TEXT,
        deal_type TEXT NOT NULL,
        status BOOLLEAN, 
        creation_time TEXT,
        tg_username TEXT,
        FOREIGN KEY (deal_type) REFERENCES deal_types(deal_type_code));""")


async def DataBase_add_baseinfo():
    with sq.connect('data_base.db') as con:
        cur = con.cursor()
        cur.execute("""INSERT OR IGNORE INTO deal_types (deal_type, deal_description) VALUES 
    ('onlinereg-seller1-buyer1-object', 'Электронная регистрация сделок с недвижимостью: 1 продавец, 1 покупатель, 1 объект'),
    ('onlinereg-1seller-1buyer-object-extra-seller-or-buyer', 'Электронная регистрация сделок с недвижимостью: 1 продавец, 1 покупатель, 1 объект + доп. Продавец/покупатель'),
    ('onlinereg-1seller-1buyer-1object-1extra-object', 'Электронная регистрация сделок с недвижимостью: 1 продавец, 1 покупатель, 1 объект + доп. объект'),
    ('onlinereg-1seller-1buyer-urface', 'Электронная регистрация сделок с недвижимостью: один из участников юр. лицо'),
    ('deal-meeting-room-rent-yes', 'Аренда переговорной комнаты для сделки в Фора-Банке'),
    ('offline-meeting-yes', 'Аренда переговорной комнаты для сделок не в Фора-Банке'),
    ('storage-key-for-safe-box', 'Другие услуги банка связанные со сделкой хранение ключа для сейфовой ячейки'),
    ('cash-checking-counting', 'Другие услуги банка связанные со сделкой проверка / пересчет денежных средств'),
    ('trustee-safebox', 'Другие услуги банка связанные со сделкой доверенность по форме банка: к сейфовой ячейке'),  
    ('individual-safe-after-deal', 'Другие услуги банка не связанные со сделкой: индивидуальный сейф после сделки'),
    ('deposit-serivice-absolute-garantee', 'Другие услуги банка не связанные со сделкой: вклад (услуга Абсолютная гаратния)'),
    ('openning-current-account', 'Другие услуги банка не связанные со сделкой: открытие текущего счёта'),
    ('cashback-card', 'Другие услуги банка не связанные со сделкой: карта с кешбэком'),
    ('money-exchange', 'Другие услуги банка не связанные со сделкой: обмен валюты'),
    ('coins-or-gold', 'Другие услуги банка не связанные со сделкой: монеты/золото'),  
    ('lawyer-online', 'Другие услуги банка не связанные со сделкой: юрист-онлайн'),
    ('certificate-health-check', 'Другие услуги банка не связанные со сделкой: cертификат "Проверка здоровья"'),
    ('certificate-healthy-child', 'Другие услуги банка не связанные со сделкой: cертификат "Здоровый ребёнок"'),
    ('specialist-consultation', 'Сделки с цепочками: консультация специалиста'),
    ('packagedeal-under10safes-20arenders', 'Сделки с цепочками: предложение до 10 сейфов (20 арендаторов)'),
    ('safe+acred_standart', 'Аккредитив + Сейф "Стандарт"'),
    ('safe+acred_universal', 'Аккредитив + Сейф "Универсал"'),
    ('safe+acred_VIP', 'Аккредитив + Сейф "ВИП"'),
    ('akkreditiv-under-1mill', 'Аккредитив до 1 млн. руб'),
    ('akkreditiv-ahead-1mill-for-free', 'Аккредитив свыше 1 млн. руб. бесплатно'),
    ('safe-standart', 'Сейф "Cтандарт"'),
    ('safe-universal', 'Сейф "Универсал"'),
    ('safe-VIP', 'Сейф "ВИП"'),
    ('safe-universal-and-standart', 'Сейф+зеркальный сейф "Универсал" + "Cтандарт"'),
    ('safe-standart-and-standart', 'Сейф+зеркальный сейф "Cтандарт" + "Cтандарт"'),
    ('safe_VIP-and-standart', 'Сейф+зеркальный сейф "ВИП" + Сейф "Cтандарт"'),
    ('safe-universal-and-standart-and-free-safe-for-ragent', 'Сейф "Универсал" + "Cтандарт" + бесплатный сейф для риелтора'),
    ('safe-standart-and-standart-and-free-safe-for-ragent', 'Сейф "Cтандарт" + "Cтандарт" + бесплатный сейф для риелтора'),
    ('safe-VIP-and-standart-and-free-safe-for-ragent', 'Сейф "ВИП" + "Cтандарт" + бесплатный сейф для риелтора'),
    ('safe-standart-and-free-safe-for-ragent', 'Сейф + бесплатный сейф для риелтора сейф "Cтандарт"'),
    ('safe-universal-and-free-safe-for-ragen', 'Сейф + бесплатный сейф для риелтора сейф "Универсал"'),
    ('safe-VIP-and-free-safe-for-ragent', 'Сейф + бесплатный сейф для риелтора сейф "ВИП"'),
    ('questions-consultant', 'Вопрос консультанту')
    ;""")


async def DataBase_add_1data(user_id, deal_type, status, create_ddt, tg_username):
    with sq.connect('data_base.db') as con:
        cur = con.cursor()
        cur.execute(f"""
       INSERT INTO deals (user_id,  deal_type, status, creation_time, tg_username) VALUES
        ('{user_id}', '{deal_type}', {status}, '{create_ddt}', '{tg_username}');""")
        # cur.execute(f"""INSERT OR REPLACE INTO deals (user_id, deal_type, status, creation_time, tg_username)
        # VALUES (
        #     '{user_id}',
        #     '{deal_type}',
        #     {status},
        #     '{create_ddt}',
        #     '{tg_username}');""")



async def DataBase_add_2data(user_id, phone_number):
    with sq.connect('data_base.db') as con:
        cur = con.cursor()
        cur.execute(f"""
        UPDATE deals SET phone_number = '{phone_number}' WHERE user_id = {user_id}
                AND creation_time = (
                SELECT MAX(creation_time) 
                FROM deals 
                WHERE user_id = {user_id})""")

def DataBase_find_dealtype(user_id):
    with sq.connect('data_base.db') as con:
        cur = con.cursor()

        #cur.execute(f"""SELECT deal_type FROM deals WHERE user_id = {user_id}""")
        cur.execute(f"""SELECT deal_description FROM deals JOIN deal_types ON deals.deal_type = deal_types.deal_type
        WHERE user_id = {user_id} ORDER BY creation_time DESC LIMIT 1""")

        #тут пока закоментила подумать!!!
        # deal_type_res = str(cur.fetchone())
        # cur.execute(f"""SELECT deal_description FROM deal_types WHERE deal_type = {deal_type_res};""")

        deal_description_res = cur.fetchone()[0]
        return deal_description_res
#Дописать функции сохранения данных на каждом этапе для approved_deal_handler.py

async def DataBase_approve_status(user_id):
    with sq.connect('data_base.db') as con:
        cur = con.cursor()
        cur.execute(f"""
                UPDATE deals 
                SET status = true 
                WHERE user_id = {user_id} 
                AND creation_time = (
                SELECT MAX(creation_time) 
                FROM deals 
                WHERE user_id = {user_id});""")




