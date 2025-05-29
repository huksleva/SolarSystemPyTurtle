import win32api
import win32con
from math import sqrt, sin, cos, pi
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

def UpdatePlanetPos(planets, name, total_sim_seconds):
    planet = planets[name]


    # Получаем параметры планеты
    r = planets_data[name]["distanceFromSun"]
    period = planets_data[name]["orbitalPeriod"]

    # Угол в радианах: θ = 2π * (t / T)
    angle = 2 * pi * (total_sim_seconds % period) / period

    # Рассчитываем координаты
    scale = planets_data_multipliers[name]["distanceFromSun"]
    x = r * cos(angle) * scale
    y = r * sin(angle) * scale

    planet.goto(x, y)




# Обновляет позицию подписи
def UpdateLabelPosition(name, planets_labels, planets):
    planets_labels[name].clear()
    planets_labels[name].goto(planets[name].xcor(), planets[name].ycor() + 17)
    planets_labels[name].write(name, align="center", font=("Courier", 10, "bold"))



