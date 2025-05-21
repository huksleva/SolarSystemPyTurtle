import turtle
import time
import math


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
dist_Mercurian = 579e5
dist_Venus = 1082e5
dist_Earth = 1496e5
dist_Mars = 2279e5
dist_Jupiter = 7786e5
dist_Saturn = 14335e5
dist_Uranus = 28725e5
dist_Neptune = 44951e5

# Массы Солнца и планет в кг
m_Sun = 1.989e30
m_Mercurian = 3.3e23
m_Venus = 4.9e24
m_Earth = 5.97e24
m_Mars = 6.42e23
m_Jupiter = 1.89e27
m_Saturn = 5.68e26
m_Uranus = 8.68e25
m_Neptune = 1.02e26

# Начальные скорости планет в м/c
spd_Mercurian = 47870
spd_Venus = 35020
spd_Earth = 29780
spd_Mars = 24130
spd_Jupiter = 13070
spd_Saturn = 9690
spd_Uranus = 6810
spd_Neptune = 5430

# Гравитационная постоянная
G = 6.6728835e-11

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
#while True:
    screen.update()
    #for planet in planets:
        #planet.goto()


    # Движение объектов в программе дискретно и на каждый шаг тратится времени: time.sleep(n), то есть n секунд
    #time.sleep(1)




screen.mainloop()