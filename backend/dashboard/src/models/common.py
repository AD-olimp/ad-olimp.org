from enum import Enum
from typing import TypeAlias


class Grades(str, Enum):
    winner = 'Победитель'
    pre_winner = 'Призер'
    loser = 'Участник'


class Step(str, Enum):
    final = 'Заключительный'
    region = 'Региональный'
    qualifying = 'Отборочный'


class OlympTitle(str, Enum):
    vseros = 'Всероссийская олимпиада школьников. Заключительный этап'
    region = 'Всероссийская олимпиада школьников. Региональный этап'
    vp = 'Высшая проба'
    mosh = 'Московская олимпиада школьников'
    finashka = 'Миссия выполнима'
    sibiriada = 'Сибириада'
    kondrat = 'Олимпиада им. Кондратьева'
