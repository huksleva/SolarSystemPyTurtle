import win32api
import win32con
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



def normalize_vector(v):
    length = abs(v)  # длина Vec2D
    if length == 0:
        return turtle.Vec2D(0.0, 0.0)
    return turtle.Vec2D(v[0] / length, v[1] / length)



def UpdatePlanetPosition(planets, name, time_step):
    """
    Обновляет положение планеты на основе гравитационного ускорения.
    time_step — шаг времени в секундах
    """

    if name == "Sun":
        return

    planet = planets[name]
    pos = turtle.Vec2D(planet.xcor(), planet.ycor())
    vel = getattr(planet, 'velocity', turtle.Vec2D(0, 0))  # Получаем или инициализируем скорость

    # Расстояние до Солнца
    r_vec = turtle.Vec2D(0, 0) - pos  # Вектор от планеты к Солнцу
    r_mag = abs(r_vec)

    if r_mag == 0:
        return  # Защита от деления на ноль

    # Нормализованный вектор направления силы тяжести
    r_hat = turtle.Vec2D(r_vec[0] / r_mag, r_vec[1] / r_mag)

    # Ускорение по закону всемирного тяготения
    acceleration = G * SUN_MASS / (r_mag ** 2) * r_hat

    # Интегрируем ускорение для получения скорости и координат
    vel += acceleration * time_step
    new_pos = pos + vel * time_step

    # Сохраняем новую скорость как атрибут черепашки
    planet.velocity = vel
    planet.goto(new_pos)
