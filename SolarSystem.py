import turtle
import time
import math
from operator import index

# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(1920, 1080)
screen.title("Симуляция Солнечной системы")

# Все данные взяты с сайта NASA
# Радиусы в метрах
r_Sun = 700000000
r_Mercurian = 2440000
r_Venus = 6051800
r_Earth = 6371000
r_Mars = 3390000
r_Jupiter = 69911000
r_Saturn = 58232000
r_Uranus = 25362000
r_Neptune = 24622000

# Дистанция от Солнца до планеты в метрах
dist_Mercurian = 579*(10^5)
dist_Venus = 1082*(10^5)
dist_Earth = 1496*(10^5)
dist_Mars = 2279*(10^5)
dist_Jupiter = 7786*(10^5)
dist_Saturn = 14335*(10^5)
dist_Uranus = 28725*(10^5)
dist_Neptune = 44951*(10^5)

# Массы Солнца и планет в кг
m_Sun = 1.989*(10^30)
m_Mercurian = 3.3*(10^23)
m_Venus = 4.9*(10^24)
m_Earth = 5.97*(10^24)
m_Mars = 6.42*(10^23)
m_Jupiter = 1.89*(10^27)
m_Saturn = 5.68*(10^26)
m_Uranus = 8.68*(10^25)
m_Neptune = 1.02*(10^26)

# Начальные скорости планет в м/c
spd_Mercurian = 47870
spd_Venus = 35020
spd_Earth = 29780
spd_Mars = 24130
spd_Jupiter = 13070
spd_Saturn = 9690
spd_Uranus = 6810
spd_Neptune = 5430


# Масштаб всей симуляции. 0 < global_scale < 1 - уменьшить масштаб, 1 < global_scale - увеличить масштаб
global_scale = 10^-7

# Переменная для сокращения расстояния от планеты до Солнца в 10 млн раз для наглядного представления
smaller_dist = 1000000000

# Во сколько раз планеты будут на анимации больше, чем в реальности и расчётах соответственно
bigger_size = 100






# Размер планет в масштабе относительно Солнца умноженный на 100, то есть все планеты больше в 100 раз,
# чем должны быть (на физические расчёты не влияет). То есть, если изменить размер Солнца, то поменяются
# размеры и других планет. Тем, что есть радиус экваториальный, а есть полюсный принебрёг.

# Солнце
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.speed(0)
sun.shapesize(r_Sun/smaller_dist)


# Параметры планет
planets_data = [
    ("Меркурий", dist_Mercurian/smaller_dist, r_Mercurian/r_Sun*bigger_size, spd_Mercurian, "gray"),
    ("Венера", dist_Venus/smaller_dist, r_Venus/r_Sun*bigger_size, spd_Venus, "orange"),
    ("Земля", dist_Earth/smaller_dist, r_Earth/r_Sun*bigger_size, spd_Earth, "blue"),
    ("Марс", dist_Mars/smaller_dist, r_Mars/r_Sun*bigger_size, spd_Mars, "red"),
    ("Юпитер", dist_Jupiter/smaller_dist, r_Jupiter/r_Sun*bigger_size, spd_Jupiter, "brown"),
    ("Сатурн", dist_Saturn/smaller_dist, r_Saturn/r_Sun*bigger_size, spd_Saturn, "green"),
    ("Уран", dist_Uranus/smaller_dist, r_Uranus/r_Sun*bigger_size, spd_Uranus, "yellow"),
    ("Нептун", dist_Neptune/smaller_dist, r_Neptune/r_Sun*bigger_size, spd_Neptune, "orange")
]

# Выстраиваем парад планет
planets = {}
for name, distance_from_sun, radius, speed, color in planets_data:
    planet = turtle.Turtle()
    # planet.penup()
    planet.shape("circle")
    planet.color(color)
    planet.speed(0)  # Многвенное движение, без анимаций
    planet.goto(distance_from_sun, 0)  # Начальная позиция на орбите
    planet.shapesize(radius)  # Размер планеты
    planets[name] = planet  # Добавляем планету в словарь планет


# Начинаем движение
while True:
    for planet in planets:
        planet.goto()


    # Движение объектов в программе дискретно и на каждый шаг тратится времени: time.sleep(n), то есть n секунд
    time.sleep(1)




