from constants import *
from math import *

def UpdatePlanetPosition(planets, name1, name2):

    # Расчитываем новые координаты для объекта planets[name2] относительно объекта planets[name1],
    # То есть planets[name1] - это точка отсчёта
    # planets[name] - объект типа turtle.Turtle(), name - название планеты и её идентификатор для словарей
    # h - расстояние от planets[name1] до planets[name2] без учёта радиусов самих объектов. h^2 = x^2 + y^2
    h = sqrt(pow(planets[name2].xcor(), 2) + pow(planets[name2].ycor(), 2))
    # H = r1 + r2 + h. H - расстояние с учётом радиусов. Радиусы двух объектов + расстояние между ними
    H = planets[name1].shapesize() + planets[name2].shapesize() + h
    # a - ускорение для planets[name2] к planets[name1]. a = m1 / H^2 * G
    a = m_planets[name1] / pow(H, 2) * G

    return (1, 2)

