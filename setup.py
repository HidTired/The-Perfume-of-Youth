"""Создание демонстрационной базы TPY. Запустите: python setup.py"""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / 'data' / 'tpy.sqlite'
DB.parent.mkdir(exist_ok=True)
connection = sqlite3.connect(DB)
connection.executescript('''
CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, password_hash TEXT NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, category TEXT NOT NULL, price INTEGER NOT NULL, description TEXT NOT NULL, notes TEXT NOT NULL, image TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS cart_items (user_id INTEGER NOT NULL, product_id INTEGER NOT NULL, quantity INTEGER NOT NULL DEFAULT 1, PRIMARY KEY(user_id,product_id));
CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, total INTEGER NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS order_items (id INTEGER PRIMARY KEY, order_id INTEGER NOT NULL, product_id INTEGER NOT NULL, name TEXT NOT NULL, price INTEGER NOT NULL, quantity INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS reviews (id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, product_id INTEGER NOT NULL, rating INTEGER NOT NULL, body TEXT NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS saved_cards (id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, label TEXT NOT NULL, last_four TEXT NOT NULL);
''')
products = [
(1,'Парфюм 1','women',6490,'Нежная композиция, вдохновлённая первым цветением весны.','Пион · роза · белый мускус','perfume-1.webp'),
(2,'Парфюм 2','unisex',7290,'Свежесть зелёных листьев и утреннего сада.','Бергамот · зелёный чай · кедр','perfume-2.webp'),
(3,'Парфюм 3','women',5990,'Воздушный аромат для самых светлых моментов.','Жасмин · груша · ваниль','perfume-3.webp'),
(4,'Парфюм 4','men',7990,'Тёплый, уверенный характер с древесными оттенками.','Амбра · сандал · кожа','perfume-4.webp'),
(5,'Парфюм 5','unisex',6890,'Спокойная лаванда и мягкий вечерний свет.','Лаванда · ирис · мускус','perfume-5.webp'),
(6,'Парфюм 6','men',7490,'Чистая прохлада, прозрачность и лёгкость.','Морская соль · цитрус · ветивер','perfume-6.webp'),
(7,'Подарочный сертификат 3 000 ₽','gift',3000,'Демонстрационный подарочный сертификат TPY.','Электронный сертификат','perfume-3.webp'),
(8,'Подарочный сертификат 5 000 ₽','gift',5000,'Демонстрационный подарочный сертификат TPY.','Электронный сертификат','perfume-1.webp')]
connection.executemany('INSERT OR IGNORE INTO products VALUES (?,?,?,?,?,?,?)',products)
connection.commit()
connection.close()
print('Готово:', DB)
