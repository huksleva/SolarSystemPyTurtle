import win32api
import win32con
from math import *
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




# Функция возвращает новую позицию планеты
def UpdatePlanetPos(planets, name, total_sim_seconds):
    planet = planets[name]

    data = planets_data[name]
    if data["orbitalPeriod"] == 0:
        return  # Не двигается (Солнце)

    a = data["distanceFromSun"]  # Большая полуось
    e = data["eccentricity"]  # Эксцентриситет
    T = data["orbitalPeriod"]  # Орбитальный период

    # Нормализуем время
    t = total_sim_seconds % T
    mean_anomaly = 2 * pi * t / T  # Средняя аномалия

    # Решаем уравнение Кеплера методом Ньютона для получения эксцентрической аномалии E
    E = mean_anomaly
    for _ in range(100):  # итерации
        delta = (E - e * sin(E) - mean_anomaly)
        dE = delta / (1 - e * cos(E))
        E -= dE
        if abs(delta) < 1e-6:
            break

    # Вычисляем истинную аномалию θ из E
    theta = 2 * atan2(sqrt(1 + e) * sin(E / 2), sqrt(1 - e) * cos(E / 2))

    # Расчёт расстояния до Солнца (по закону эллипса)
    r = a * (1 - e ** 2) / (1 + e * cos(theta))

    # Масштабируем
    scale = planets_data_multipliers[name]["distanceFromSun"]
    x = r * cos(theta) * scale
    y = r * sin(theta) * scale

    planet.goto(x, y)




# Обновляет позицию подписи
def UpdateLabelPosition(name, planets_labels, planets):
    planets_labels[name].clear()
    planets_labels[name].goto(planets[name].xcor(), planets[name].ycor() + 17)
    planets_labels[name].write(name, align="center", font=("Courier", 10, "bold"))


def DrawOrbits(planets):
    for name in planets:
        if name == "Sun":
            continue
        data = planets_data[name]
        a = data["distanceFromSun"]
        e = data["eccentricity"]
        scale = planets_data_multipliers[name]["distanceFromSun"]

        planet = planets[name]
        start_x = planet.xcor()
        start_y = planet.ycor()
        planet.hideturtle()


        for angle in range(0, 361, 5):  # шаг 5 градусов
            theta = radians(angle)
            r = a * (1 - e**2) / (1 + e * cos(theta))
            x = r * cos(theta) * scale
            y = r * sin(theta) * scale
            planet.goto(x, y)
            planet.pendown()
            planet.dot(1)

        planet.penup()
        planet.goto(start_x, start_y)
        planet.showturtle()


def ClearOrbits(planets):
    for name in planets:
        planet = planets[name]
        planet.clear()
