import turtle
from Methods import *
from datetime import datetime, timedelta



# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(MonitorResolution()[0], MonitorResolution()[1], 0, 0)
screen.title("Симуляция Солнечной системы")
screen.bgpic("stars2.png")
screen.tracer(0)



# === Время внутри симуляции ===
simulationTime = datetime(year=2025, month=1, day=1, hour=0, minute=0, second=0)
sim_time_speed = 1.0  # x1 — скорость времени (можно менять через клавиши)
paused = False        # Флаг паузы
last_update_time = None  # Время последнего обновления для учёта реального времени
sim_days = 0.0 # Начальное время симуляции в днях



# Черепашка для отображения времени
time_display = turtle.Turtle()
time_display.hideturtle()
time_display.penup()
time_display.color("white")
time_display.goto(0, 0)  # Под текущим текстом

sim_start_seconds = 0  # Счётчик секунд внутри симуляции. Начинаем от нуля.
SlowPlanet = 20    # Во сколько раз замедлится движение планет


# Масштаб всей симуляции, подгонял вручную.
smaller_dist = 4e9
bigger_size = 9e-8


# Размер планет в масштабе относительно Солнца умноженный на 100, то есть все планеты больше в 100 раз,
# чем должны быть (на физические расчёты не влияет). То есть, если изменить размер Солнца, то поменяются
# размеры и других планет. Тем, что есть радиус экваториальный, а есть полюсный принебрёг.




# Выстраиваем парад планет
planets = {}
planets_labels = {}
for name, data in planets_data.items():
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(data["color"])
    #planet.penup()
    planet.speed(0)

    # Устанавливаем размер относительно радиуса
    planet.shapesize(data["radius"] * planets_data_multipliers[name]["radius"] * bigger_size)  # Для наглядности

    # Уменьшаем начальное расстояние
    start_distance = data["distanceFromSun"] * planets_data_multipliers[name]["distanceFromSun"] * smaller_dist

    # Начинаем планету под углом 0 градусов (по оси X)
    planet.goto(start_distance, 0)
    planet.setheading(90)  # Поворачиваем черепашку вверх (движение будет против часовой)
    planets[name] = planet


    # Создаем подпись планеты
    label = turtle.Turtle()
    label.hideturtle()
    label.color("white")
    label.penup()
    label.speed(0)
    label.write(name, align="center", font=("Courier", 10, "normal"))
    label.goto(start_distance, 0)
    planets_labels[name] = label



# Обработка нажатий клавиш
def increase_time_speed():
    global sim_time_speed
    sim_time_speed *= 1.5

def decrease_time_speed():
    global sim_time_speed
    sim_time_speed /= 1.5

def toggle_pause():
    global paused
    paused = not paused


# Привязка клавиш
screen.onkeypress(increase_time_speed, "Up")
screen.onkeypress(decrease_time_speed, "Down")
screen.onkeypress(toggle_pause, "space")
screen.listen()


# Начинаем движение
def Update():
    global simulationTime, last_update_time, paused

    screen.update()

    if not paused:
        current_real_time = datetime.now()

        if last_update_time is None:
            last_update_time = current_real_time
            screen.ontimer(Update, int(DELAY * 1000))
            return

        delta_real = (current_real_time - last_update_time).total_seconds()
        delta_sim_seconds = delta_real * sim_time_speed

        # === Обновляем дату симуляции ===
        simulationTime += timedelta(seconds=delta_sim_seconds)
        last_update_time = current_real_time

        # === Обновляем позиции планет и их подписей ===
        for name in planets:
            if name != "Sun":
                UpdatePlanetPosition(planets, name, sim_time_speed / SlowPlanet)
                UpdateLabelPosition(name, planets_labels, planets)





    # === Очищаем предыдущий текст ===
    time_display.clear()


    # === Формируем текущее время из simulationTime ===
    status = "Пауза" if paused else f"Скорость: x{sim_time_speed:.2f}"

    time_display.goto(-950, 500)
    time_display.write(
        f"Время: {simulationTime.strftime('%Y-%m-%d %H:%M:%S')}   {status}",
        align="left",
        font=("Courier", 16, "normal")
    )

    # === Планируем следующее обновление ===
    screen.ontimer(Update, int(DELAY * 1000))



# Update() будет выполняться бесконечное кол-во раз, 1 раз за определённый промежуток времени
# Запуск анимации
Update()

turtle.mainloop()




