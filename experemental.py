import turtle


# Настройка экрана
screen = turtle.Screen()
screen.setup(1920, 1080, 0, 0)
screen.bgcolor("black")
screen.title("Experimental")
screen.tracer(0)


# Создание объекта для надписи
clock = turtle.Turtle()
clock.penup()
clock.hideturtle()
clock.color("white")
clock.goto(0, 0)



counter = 0
def Update():
    global counter
    counter += 1
    clock.clear()
    clock.write(f"Счетчик: {counter}", align="center", font=("Arial", 36, "normal"))
    screen.update()
    screen.ontimer(Update, 1000)  # Срабатывает каждую секунду






Update()


screen.mainloop()

