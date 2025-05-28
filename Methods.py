import win32api
import win32con
from math import sqrt, sin, cos
from constants import *


# Возвращает частоту обновления монитора (в Гц)
def MonitorFrameRate():
    devmode = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
    return devmode.DisplayFrequency

def MonitorResolution():
    # Получаем размеры экрана
    width = win32api.GetSystemMetrics(0)
    height = win32api.GetSystemMetrics(1)
    return width, height

# Частота кадров и время на один кадр
FPS = MonitorFrameRate()  # Например, 60 Гц
DELAY = 1 / FPS  # ~0.0167 секунд на кадр




# Функция возвращает новую позицию планеты относительно Солнца.
# Возвращает время, прошедшее внутри симуляции в секундах, за которое планета прошла один тик.

# Допиши код так, чтобы Часы симуляции должны точно выводить время, то есть Земля, например,
# должна совершить оборот вокруг Солнца ровно за один год. Ещё не должно быть такого, что через, например,
# 10000 лет Земля будет совершать оборот не ровно за год.





def UpdatePlanetPosition(planets, name, sim_time_speed):
    # Обновляет координаты планеты name вокруг Солнца.
    # Предполагаем круговые орбиты.


    planet = planets[name]

    x = planet.xcor()
    y = planet.ycor()

    # Расстояние до центрального тела.
    h = sqrt(x ** 2 + y ** 2)

    # Вычисляем угол текущего положения в радианах
    # Направление черепашки — это угол
    angle = planet.heading()

    # Угловая скорость: v / r
    angular_speed = planets_data[name]["speed"] / h

    # Обновляем угол.
    # Минус для вращения против часовой стрелки
    angle -= angular_speed * DELAY * sim_time_speed / h



    angular_velocity = planets_data[name]["speed"] / h
    newAngle = angle - angular_velocity * DELAY * sim_time_speed / h


    # Рассчитываем новые координаты
    new_x = h * cos(newAngle)
    new_y = h * sin(newAngle)

    # Обновляем направление и позицию
    planet.setheading(newAngle)
    planet.goto(new_x, new_y)




# Обновляет позицию подписи
def UpdateLabelPosition(name, planets_labels, planets):
    planets_labels[name].clear()
    planets_labels[name].goto(planets[name].xcor(), planets[name].ycor() + 17)
    planets_labels[name].write(name, align="center", font=("Courier", 10, "bold"))




