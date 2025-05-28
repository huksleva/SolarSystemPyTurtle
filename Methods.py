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


    if name == "Earth":
        orbital_period_seconds = DAYS_IN_YEAR * SECONDS_IN_DAY
        angular_velocity = 2 * 3.141592653589793 / orbital_period_seconds
        newAngle = angle - angular_velocity * DELAY * sim_time_speed
    else:
        angular_velocity = planets_data[name]["speed"] / h
        newAngle = angle - angular_velocity * DELAY * sim_time_speed / h


    # Рассчитываем новые координаты
    new_x = h * cos(newAngle)
    new_y = h * sin(newAngle)

    # Обновляем направление и позицию
    planet.setheading(newAngle)
    planet.goto(new_x, new_y)

