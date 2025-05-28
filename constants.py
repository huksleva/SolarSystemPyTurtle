
# Гравитационная постоянная. Данные взяты из статьи журнала Nature: https://www.nature.com/articles/s41586-018-0431-5
# G = const
G = 6.674334e-11

# Константы времени
SECONDS_IN_DAY = 86400
DAYS_IN_YEAR = 365.25  # Учёт високосных годов
YEARS_IN_CENTURY = 100
WEEKS_IN_YEAR = 52
DAYS_IN_WEEK = 7
MONTHS_IN_YEAR = 12



# Множители масштаба всей симуляции, подгонял вручную.
smaller_dist = 4e9
bigger_size = 9e-8




# Все данные взяты с сайта NASA. Все значения представлены в СИ. Все значения = const.
# Радиусы - м.
# Массы - кг.
# Дистанция - м.
# Скорости - м/c.
# Орбитальный период - с.

# Реальные данные о Солнечной системе
# Числа, на которые делятся или умножаются значения в planets_data, нужны для нормального отображения объектов, чтобы их было видно на экране

planets_data = {
    "Sun": {
        "radius": 7e8 / 25,
        "mass": 1.989e30,
        "distanceFromSun": 0,
        "speed": 0,
        "color": "yellow", # Жёлтый
        "orbitalPeriod": 0
    },
    "Mercurian": {
        "radius": 244e4 * 3,
        "mass": 3.3e23,
        "distanceFromSun": 579e8 * 3,
        "speed": 47870,
        "color": "#A9A9A9", # Темно-серый, скалистый
        "orbitalPeriod": 7600688
    },
    "Venus": {
        "radius": 6051800 * 1.8,
        "mass": 4.9e24,
        "distanceFromSun": 1082e8 * 3,
        "speed": 35020,
        "color": "#FFFFCC", # Белесовато-желтый
        "orbitalPeriod": 19410240
    },
    "Earth": {
        "radius": 6371e3 * 2,
        "mass": 5.97e24,
        "distanceFromSun": 1496e8 * 3.5,
        "speed": 29780,
        "color": "#3D85C6", #
        "orbitalPeriod": 31558151
    },
    "Mars": {
        "radius": 339e4 * 2.5,
        "mass": 6.42e23,
        "distanceFromSun": 2279e8 * 3.5,
        "speed": 24130,
        "color": "#CC6600", #
        "orbitalPeriod": 59353728
    },
    "Jupiter": {
        "radius": 69911e3 / 4,
        "mass": 1.89e27,
        "distanceFromSun": 7786e8 * 1.5,
        "speed": 13070,
        "color": "#F2D4A2", #
        "orbitalPeriod": 374434176
    },
    "Saturn": {
        "radius": 58232e3 / 4,
        "mass": 5.68e26,
        "distanceFromSun": 14335e8,
        "speed": 9690,
        "color": "#E3C891", #
        "orbitalPeriod": 930752640
    },
    "Uranus": {
        "radius": 25362e3 / 2.5,
        "mass": 8.68e25,
        "distanceFromSun": 28725e8 / 1.8,
        "speed": 6810,
        "color": "#B2FFFF", #
        "orbitalPeriod": 2659213440
    },
    "Neptune": {
        "radius": 24622e3 / 2.5,
        "mass": 1.02e26,
        "distanceFromSun": 44951e8 / 2.5,
        "speed": 5430,
        "color": "#3D66FF", #
        "orbitalPeriod": 5202620160
    }
}



