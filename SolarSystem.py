import turtle
from Methods import *
from datetime import datetime



# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(MonitorResolution()[0], MonitorResolution()[1], 0, 0)
screen.title("Симуляция Солнечной системы")
screen.bgpic("S:\\Leo\\projects\\SolarSystemPyTurtle\\stars.png")
screen.tracer(0)



# Черепашка для отображения времени
time_display = turtle.Turtle()
time_display.hideturtle()
time_display.penup()
time_display.color("white")
time_display.goto(0, 0)




# Выстраиваем парад планет
planets = {}
planets_labels = {}
for name, data in planets_data.items():
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(data["color"])
    planet.penup()
    planet.speed(0)

    # Радиус
    radius = data["radius"] * planets_data_multipliers[name]["radius"]
    planet.shapesize(radius)

    # Расстояние до Солнца
    start_distance = data["distanceFromSun"] * planets_data_multipliers[name]["distanceFromSun"]

    # Начинаем, планета под углом 0 градусов и на расстоянии start_distance
    planet.goto(start_distance, 0)
    planets[name] = planet


    # Создаем подпись планеты
    if name == "Sun":
        continue
    label = turtle.Turtle()
    label.hideturtle()
    label.color("white")
    label.penup()
    label.speed(0)
    label.write(name, align="center", font=("Courier", 10, "normal"))
    label.goto(start_distance, 0)
    planets_labels[name] = label



# === Время внутри симуляции ===
sim_time_speed = 1.0  # x1 — скорость симуляции (можно менять через клавиши стрелка вверх/вниз)
is_paused = False        # Флаг паузы. Пауза — это приостановка симуляции нажатием пробела
is_showOrbits = True    # Флаг показа орбит. Орбиты показываются по нажатию клаи
last_update_time = None  # Время последнего обновления для учёта реального времени
sim_seconds = 0          # Время внутри симуляции в секундах




# Обработка нажатий клавиш
def increase_time_speed():
    global sim_time_speed
    sim_time_speed *= 1.5

def decrease_time_speed():
    global sim_time_speed
    sim_time_speed /= 1.5

def toggle_pause():
    global is_paused
    is_paused = not is_paused

def restart():
    global is_paused, sim_seconds
    is_paused = False
    sim_seconds = 0

def showOrbits():
    global is_showOrbits, planets
    # Если орбиты показаны, то скрываем их, иначе показываем
    if is_showOrbits:
        DrawOrbits(planets)
        is_showOrbits = False
    else:
        ClearOrbits(planets)
        is_showOrbits = True


# Привязка клавиш. Важен язык раскладки при нажатии клавиш
screen.onkeypress(increase_time_speed, "Up")
screen.onkeypress(decrease_time_speed, "Down")
screen.onkeypress(toggle_pause, "space")
screen.onkeypress(restart, "r")
screen.onkeypress(showOrbits, "o")
screen.listen()


# Начинаем движение
def Update():
    global last_update_time, is_paused, sim_seconds

    screen.update()

    if not is_paused:
        current_real_time = datetime.now()


        if last_update_time is None:
            last_update_time = current_real_time
            screen.ontimer(Update, int(DELAY * 1000))
            return

        delta_real = (current_real_time - last_update_time).total_seconds()
        delta_sim_seconds = delta_real * sim_time_speed

        # === Обновляем время симуляции в секундах ===
        sim_seconds += delta_sim_seconds

        # === Обновляем позиции планет и их подписей ===
        for name in planets:
            if name != "Sun":
                UpdatePlanetPos(planets, name, sim_seconds)
                UpdateLabelPosition(name, planets_labels, planets)



    # === Очищаем предыдущий текст ===
    time_display.clear()
    time_display.goto(-950, 500)



    # === Формируем текущую строку состояния ===
    if is_paused:
        status = "Пауза"
        seconds = "SS"
        minutes = "MM"
        hours = "HH"
        days = "DDD"
        years = "YYYY"
    else:
        status = f"Скорость: x{sim_time_speed:.2f}"
        seconds = int(sim_seconds % 60)
        minutes = int(sim_seconds / 60 % 60)
        hours = int(sim_seconds / 60 / 60 % 24)
        days = int(sim_seconds / 60 / 60 / 24 % (planets_data["Earth"]["orbitalPeriod"] / 60 / 60 / 24))
        years = int(sim_seconds / planets_data["Earth"]["orbitalPeriod"])



    # === Выводим текущее время внутри симуляции ===
    time_display.write(
        f"Время: {years:4}:{days:3}:{hours:2}:{minutes:2}:{seconds:2}    {status}",
        align="left",
        font=("Courier", 16, "normal")
    )




    # === Планируем следующее обновление ===
    screen.ontimer(Update, int(DELAY * 1000))



# Update() будет выполняться бесконечное кол-во раз, 1 раз за определённый промежуток времени
# Запуск анимации
Update()

turtle.mainloop()




