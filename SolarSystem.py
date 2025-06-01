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
    planet.penup()
    planet.speed(0)

    # Радиус
    radius = data["radius"] * planets_data_multipliers[name]["radius"]
    planet.shapesize(radius)

    # Расстояние до Солнца
    start_distance = data["distanceFromSun"] * planets_data_multipliers[name]["distanceFromSun"]

    # Начинаем, планета под углом 0 градусов (по оси X)
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
sim_time_speed = 1.0  # x1 — скорость симуляции (можно менять через клавиши)
is_paused = False        # Флаг паузы
is_showOrbits = False    # Флаг показа орбит
last_update_time = None  # Время последнего обновления для учёта реального времени
display_sim_time = 0     # Время (datetime) внутри симуляции
sim_seconds = 0          # Время внутри симуляции в секундах
years = 0                # Время внутри симуляции в годах




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
    global is_showOrbits
    # Если орбиты показаны, то скрываем их, иначе показываем
    if is_showOrbits:
        is_showOrbits = False
        for name in planets:
            planets[name].penup()
            planets[name].clear()
    else:
        is_showOrbits = True
        for name in planets:
            planets[name].pendown()



# Привязка клавиш. Важен язык раскладки при нажатии клавиш
screen.onkeypress(increase_time_speed, "Up")
screen.onkeypress(decrease_time_speed, "Down")
screen.onkeypress(toggle_pause, "space")
screen.onkeypress(restart, "r")
screen.onkeypress(showOrbits, "o")
screen.listen()


# Начинаем движение
def Update():
    global last_update_time, is_paused, sim_seconds, years

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



    # === Формируем текущее состояние ===
    status = "Пауза" if is_paused else f"Скорость: x{sim_time_speed:.2f}"



    # === Выводим текущее время внутри симуляции ===

    minutes = sim_seconds / 60 % 60
    hours = sim_seconds / 60 / 60 % 24
    days = sim_seconds / 60 / 60 / 24 % (planets_data["Earth"]["orbitalPeriod"] / 60 / 60 / 24)
    years = sim_seconds / planets_data["Earth"]["orbitalPeriod"]



    time_display.write(
        f"Время: {int(years)}:{int(days):3d}:{int(hours):2d}:{int(minutes):2d}:{int(sim_seconds % 60):2d}    {status}    Показать орбиты: {is_showOrbits}",
        align="left",
        font=("Courier", 16, "normal")
    )




    # === Планируем следующее обновление ===
    screen.ontimer(Update, int(DELAY * 1000))



# Update() будет выполняться бесконечное кол-во раз, 1 раз за определённый промежуток времени
# Запуск анимации
Update()

turtle.mainloop()




