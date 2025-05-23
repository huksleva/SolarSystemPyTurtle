import turtle
import time
from constants import *

# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(1920, 1080, 0, 0)
screen.title("Симуляция Солнечной системы")
screen.bgpic("stars.png")
screen.tracer(0)


# Текстовое поле для отображения времени
time_turtle = turtle.Turtle()
time_turtle.hideturtle()
time_turtle.penup()
time_turtle.color("white")
time_turtle.goto(-900, 480)  # Левый верхний угол
sim_days = 0  # Счётчик дней внутри симуляции





# Масштаб всей симуляции. 0 < global_scale < 1 - уменьшить масштаб, 1 < global_scale - увеличить масштаб
global_scale = 1e-7

# Переменная для сокращения расстояния от планеты до Солнца в 10 млн раз для наглядного представления
smaller_dist = 1e8

# Во сколько раз планеты будут на анимации больше, чем в реальности и расчётах соответственно
bigger_size = 1e1


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
    planet.speed(0)  # Мгновенное движение, без анимаций
    planet.goto(distance_from_sun, 0)  # Начальная позиция на орбите
    planet.shapesize(radius)  # Размер планеты
    planets[name] = planet  # Добавляем планету в словарь планет



# Начинаем движение
while True:
    screen.update()
    for planet in planets:
        planet.goto()


    # Движение объектов в программе дискретно и на каждый шаг тратится времени: time.sleep(n), то есть n секунд
    time.sleep(1)




