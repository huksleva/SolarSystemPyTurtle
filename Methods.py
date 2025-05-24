import win32api
import win32con
from math import sqrt, sin, cos, pi
from constants import *

# Возвращает частоту обновления монитора (в Гц)
def MonitorFrameRate():
    devmode = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
    return devmode.DisplayFrequency

# Частота кадров и время на один кадр
FPS = MonitorFrameRate()  # Например, 60 Гц
DELAY = 1 / FPS  # ~0.0167 секунд на кадр

# Функция возвращает новую позицию планеты через равные промежутки времени
def UpdatePlanetPosition(planets, name1, name2, sim_time_speed):
    """
    Обновляет координаты планеты name2 вокруг тела name1 (обычно Солнца).
    Предполагаем круговые орбиты.
    """
    planet = planets[name2]
    sun = planets[name1]

    x = planet.xcor()
    y = planet.ycor()

    # Расстояние до центрального тела
    h = sqrt(x ** 2 + y ** 2)

    # Вычисляем угол текущего положения
    angle = planet.heading()  # Направление черепашки — это угол

    # Угловая скорость: v / r
    angular_speed = planets_data[name2]["speed"] / h

    # Обновляем угол
    new_angle = angle - angular_speed * DELAY * sim_time_speed / h * 180 / pi  # минус для вращения против часовой стрелки

    # Рассчитываем новые координаты
    radius = h
    new_x = radius * cos(new_angle * pi / 180)
    new_y = radius * sin(new_angle * pi / 180)

    # Обновляем направление и позицию
    planet.setheading(new_angle)
    planet.goto(new_x, new_y)

    return (new_x, new_y)

