import turtle
from constants import *

# Масштаб всей симуляции. 0 < global_scale < 1 - уменьшить масштаб, 1 < global_scale - увеличить масштаб
global_scale = 1e-7

# Переменная для сокращения расстояния от планеты до Солнца в 10 млн раз для наглядного представления
smaller_dist = 1e8

# Во сколько раз планеты будут на анимации больше, чем в реальности и расчётах соответственно
bigger_size = 1e1



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
    #print(planet.position)


# Выводим на экран консоли информацию про все объекты словаря
for i in planets:
    print("Planet:", i)
    print("shape:", planets[i].shape())
    print("color:", planets[i].color())
    print("pencolor:", planets[i].pencolor())
    print("fillcolor:", planets[i].fillcolor())
    print("shapesize:", planets[i].shapesize())
    print("speed:", planets[i].speed())
    print("xcor:", planets[i].xcor(), ", ycor:", planets[i].ycor())
    print()