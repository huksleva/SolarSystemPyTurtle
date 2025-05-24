
# Гравитационная постоянная. Данные взяты из статьи журнала Nature: https://www.nature.com/articles/s41586-018-0431-5
# G = const
G = 6.674334e-11

# Все данные взяты с сайта NASA. Все значения представлены в СИ.
# Радиусы в м. Все значения = const.
# Массы Солнца и планет в кг. Все значения = const.
# Дистанция от Солнца до планеты в м. Задаётся только в начале и дальше значения меняются.
# Начальные скорости планет в м/c. Задаётся только в начале и дальше значения меняются.

planets_data = {
    "Sun": {
        "radius": 7e8,
        "mass": 1.989e30,
        "distanceFromSun": 0,
        "speed": 0,
        "color": "yellow"
    },
    "Mercurian": {
        "radius": 244e4,
        "mass": 3.3e23,
        "distanceFromSun": 579e5,
        "speed": 47870,
        "color": "gray"
    },
    "Venus": {
        "radius": 6051800,
        "mass": 4.9e24,
        "distanceFromSun": 1082e5,
        "speed": 35020,
        "color": "orange"
    },
    "Earth": {
        "radius": 6371e3,
        "mass": 5.97e24,
        "distanceFromSun": 1496e5,
        "speed": 29780,
        "color": "blue"
    },
    "Mars": {
        "radius": 339e4,
        "mass": 6.42e23,
        "distanceFromSun": 2279e5,
        "speed": 24130,
        "color": "red"
    },
    "Jupiter": {
        "radius": 69911e3,
        "mass": 1.89e27,
        "distanceFromSun": 7786e5,
        "speed": 13070,
        "color": "brown"
    },
    "Saturn": {
        "radius": 58232e3,
        "mass": 5.68e26,
        "distanceFromSun": 14335e5,
        "speed": 9690,
        "color": "green"
    },
    "Uranus": {
        "radius": 25362e3,
        "mass": 8.68e25,
        "distanceFromSun": 28725e5,
        "speed": 6810,
        "color": "yellow"
    },
    "Neptune": {
        "radius": 24622e3,
        "mass": 1.02e26,
        "distanceFromSun": 44951e5,
        "speed": 5430,
        "color": "orange"
    }
}



