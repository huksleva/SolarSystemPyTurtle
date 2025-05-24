# Все данные взяты с сайта NASA. Все значения представлены в СИ.

# Радиусы в м. Все значения = const.
r_planet = {
    "Venus": 6051800,
    "Earth": 6371e3,
    "Mars": 339e4,
    "Jupiter": 69911e3,
    "Saturn": 58232e3,
    "Uranus": 25362e3,
    "Neptune": 24622e3
}
# Массы Солнца и планет в кг. Все значения = const.
m_planets = {
    "Venus": 4.9e24,
    "Earth": 5.97e24,
    "Mars": 6.42e23,
    "Jupiter": 1.89e27,
    "Saturn": 5.68e26,
    "Uranus": 8.68e25,
    "Neptune": 1.02e26
}
# Дистанция от Солнца до планеты в м. Задаётся только в начале и дальше значения меняются.
dist_Venus = 1082e5
dist_Earth = 1496e5
dist_Mars = 2279e5
dist_Jupiter = 7786e5
dist_Saturn = 14335e5
dist_Uranus = 28725e5
dist_Neptune = 44951e5
# Начальные скорости планет в м/c. Задаётся только в начале и дальше значения меняются.
spd_Venus = 35020
spd_Earth = 29780
spd_Mars = 24130
spd_Jupiter = 13070
spd_Saturn = 9690
spd_Uranus = 6810
spd_Neptune = 5430




# Параметры планет
# name: (radius, mass, distanceFromSun, speed, color)
planets_data = {
    "Sun": {
        "radius": 7e8,
        "mass": 1.989e30,
        "distanceFromSun": 0,
        "speed": 0,
        "color": "yellow"
    },
    "Mercurian": {
        "radius": 2440000,  # 244e4
        "mass": 3.3e23,
        "distanceFromSun": 57900000,  # 579e5
        "speed": 47870,
        "color": "gray"
    },
    "Venus": {
        "radius": 6051800,
        "mass": 4.9e24,
        "distanceFromSun": 108200000,  # dist_Venus = 1082e5
        "speed": 35020,
        "color": "orange"
    },
    "Earth": {
        "radius": 6371000,  # 6371e3
        "mass": 5.97e24,
        "distanceFromSun": 149600000,  # dist_Earth = 1496e5
        "speed": 29780,
        "color": "blue"
    },
    "Mars": {
        "radius": 3390000,  # 339e4
        "mass": 6.42e23,
        "distanceFromSun": 227900000,  # dist_Mars = 2279e5
        "speed": 24130,
        "color": "red"
    },
    "Jupiter": {
        "radius": 69911000,  # 69911e3
        "mass": 1.89e27,
        "distanceFromSun": 778600000,  # dist_Jupiter = 7786e5
        "speed": 13070,
        "color": "brown"
    },
    "Saturn": {
        "radius": 58232000,  # 58232e3
        "mass": 5.68e26,
        "distanceFromSun": 1433500000,  # dist_Saturn = 14335e5
        "speed": 9690,
        "color": "green"
    },
    "Uranus": {
        "radius": 25362000,  # 25362e3
        "mass": 8.68e25,
        "distanceFromSun": 2872500000,  # dist_Uranus = 28725e5
        "speed": 6810,
        "color": "yellow"
    },
    "Neptune": {
        "radius": 24622000,  # 24622e3
        "mass": 1.02e26,
        "distanceFromSun": 4495100000,  # dist_Neptune = 44951e5
        "speed": 5430,
        "color": "orange"
    }
}



# Гравитационная постоянная. Данные взяты с журнала Nature: https://www.nature.com/articles/s41586-018-0431-5
# G = const
G = 6.674334e-11
