import turtle
import time
import math




# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("black")
screen.bgpic("stars.png")
screen.setup(1920, 1080)
screen.title("Симуляция Солнечной системы")

# Отключаем автообновление экрана для ускорения
screen.tracer(0)

# Константы
G = 6.67430e-11  # Гравитационная постоянная
TIME_STEP = 60 * 60 * 24  # 1 день в секундах
SCALE = 250 / 149.6e6     # Масштаб: 250 пикселей = 1 а.е.

# Текстовое поле для отображения времени
time_turtle = turtle.Turtle()
time_turtle.hideturtle()
time_turtle.penup()
time_turtle.color("white")
time_turtle.goto(-900, 480)  # Левый верхний угол
sim_days = 0  # Счётчик дней внутри симуляции

# Данные планет (реальные значения)
planets_data = [
    # Название, расстояние от Солнца (м), масса (кг), скорость (м/с), цвет, размер относительно Солнца
    ("Меркурий", 57.9e9, 3.3e23, 47870, "gray", 0.3),
    ("Венера", 108.2e9, 4.9e24, 35020, "orange", 0.5),
    ("Земля", 149.6e9, 5.97e24, 29780, "blue", 0.5),
    ("Марс", 227.9e9, 6.42e23, 24130, "red", 0.3),
    ("Юпитер", 778.5e9, 1.9e27, 13070, "brown", 1.0),
    ("Сатурн", 1433.5e9, 5.7e26, 9690, "green", 0.9),
    ("Уран", 2872.5e9, 8.7e25, 6810, "cyan", 0.8),
    ("Нептун", 4495.1e9, 1.0e26, 5430, "blue", 0.8),
]

# Создание Солнца
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(0.5)  # Увеличим визуально
sun.penup()
sun.goto(0, 0)
sun.pendown()

# Создание планет
planets = []
for name, distance, mass, speed, color, size in planets_data:
    planet = turtle.Turtle()
    planet.name = name
    planet.shape("circle")
    planet.color(color)
    planet.shapesize(size)
    planet.penup()
    planet.speed(0)

    # Угол и радиус орбиты в пикселях
    planet.angle = 0
    planet.radius = distance * SCALE / 10000
    planet.mass = mass
    planet.speed_val = speed
    planet.angular_velocity = 2 * math.pi / (2 * math.pi * distance / speed)  # ω = v / r

    # Первоначальное положение
    planet.goto(planet.radius, 0)

    # Рисование следа
    planet.pendown()
    planet.pencolor(color)
    planet.pensize(1)

    planets.append(planet)

# Основной цикл симуляции
while True:
    screen.update()  # Обновляем экран вручную

    # Обновляем время симуляции
    sim_days += 1  # +1 день за каждый шаг
    years_passed = sim_days / 365  # переводим в годы

    # Обновляем надпись
    time_turtle.clear()
    time_turtle.write(f"Прошло времени:\n{sim_days} дней (~{years_passed:.2f} лет)",
                      align="left", font=("Arial", 16, "normal"))

    # Двигаем планеты
    for planet in planets:
        planet.angle += planet.angular_velocity * TIME_STEP
        x = planet.radius * math.cos(planet.angle)
        y = planet.radius * math.sin(planet.angle)
        planet.goto(x, y)

    time.sleep(0.01)  # Задержка для замедления анимации