#1 Задание Импортировать модуль math, использовать функция sqrt()
from math import sqrt
n=int(input('Введите число,из которого нужно извлечь корень:'))
print(sqrt(n))

#1 Задание импортировать модуль datetime и вывести текущую дату и время(используя модуль Zoneinfo вывела текущее время в Москве)
from datetime import datetime
from zoneinfo import ZoneInfo
a=datetime.now(tz=ZoneInfo('Europe/Moscow'))
date=datetime.strftime(a,'%d %B %Y')
time=datetime.strftime(a,'%H:%M:%S')
print('сегодня дата', date)
print('время сейчас',time)

#2 Задание Создание своего модуля с несколькими функциями
from my_modulel import multiply
print(multiply(5,6))

#3 Задание Создать свой пакет из модулей с функциями внутри
from paket import string,numbers
print(numbers.subs(5,6))
print(string.symbol('bomba'))
