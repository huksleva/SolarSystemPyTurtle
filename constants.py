
# Гравитационная постоянная. Данные взяты из статьи журнала Nature: https://www.nature.com/articles/s41586-018-0431-5
# G = const
G = 6.674334e-11



# Данные взяты с сайта NASA. Все значения представлены в СИ. Все значения = const.
# Радиусы - м.
# Массы - кг.
# Дистанция - м.
# Скорости - м/c.
# Орбитальный период - с.


# Реальные данные о Солнечной системе
planets_data = {
    "Sun": {
        "radius": 7e8,
        "mass": 1.989e30,
        "distanceFromSun": 0,
        "speed": 0,
        "color": "yellow", # Жёлтый
        "orbitalPeriod": 0,
        "eccentricity": 0
    },
    "Mercurian": {
        "radius": 244e4,
        "mass": 3.3e23,
        "distanceFromSun": 579e8,
        "speed": 47870,
        "color": "#A9A9A9", # Темно-серый, скалистый
        "orbitalPeriod": 7600688,
        "eccentricity": 0.206
    },
    "Venus": {
        "radius": 6051800,
        "mass": 4.9e24,
        "distanceFromSun": 1082e8,
        "speed": 35020,
        "color": "#FFFFCC", # Белесовато-желтый
        "orbitalPeriod": 19410240,
        "eccentricity": 0.007
    },
    "Earth": {
        "radius": 6371e3,
        "mass": 5.97e24,
        "distanceFromSun": 1496e8,
        "speed": 29780,
        "color": "#3D85C6", #
        "orbitalPeriod": 31558151,
        "eccentricity": 0.017
    },
    "Mars": {
        "radius": 339e4,
        "mass": 6.42e23,
        "distanceFromSun": 2279e8,
        "speed": 24130,
        "color": "#CC6600", #
        "orbitalPeriod": 59353728,
        "eccentricity": 0.093
    },
    "Jupiter": {
        "radius": 69911e3,
        "mass": 1.89e27,
        "distanceFromSun": 7786e8,
        "speed": 13070,
        "color": "#F2D4A2", #
        "orbitalPeriod": 374434176,
        "eccentricity": 0.048
    },
    "Saturn": {
        "radius": 58232e3,
        "mass": 5.68e26,
        "distanceFromSun": 14335e8,
        "speed": 9690,
        "color": "#E3C891", #
        "orbitalPeriod": 930752640,
        "eccentricity": 0.056
    },
    "Uranus": {
        "radius": 25362e3,
        "mass": 8.68e25,
        "distanceFromSun": 28725e8,
        "speed": 6810,
        "color": "#B2FFFF", #
        "orbitalPeriod": 2659213440,
        "eccentricity": 0.047
    },
    "Neptune": {
        "radius": 24622e3,
        "mass": 1.02e26,
        "distanceFromSun": 44951e8,
        "speed": 5430,
        "color": "#3D66FF", #
        "orbitalPeriod": 5202620160,
        "eccentricity": 0.009
    }
}




# Множители масштаба всей симуляции, подгонял вручную.
smaller_dist = 1 / 4e9
bigger_size = 9e-8



# Числа, множители для значений свойств объектов в planets_data.
# Нужны для нормального отображения объектов, чтобы их было видно на экране
planets_data_multipliers = {
    "Sun": {
        "radius": 1 / 25 * bigger_size,
        "distanceFromSun": 1,
    },
    "Mercurian": {
        "radius": 3 * bigger_size,
        "distanceFromSun": 3 * smaller_dist,
    },
    "Venus": {
        "radius": 1.8 * bigger_size,
        "distanceFromSun": 3 * smaller_dist,
    },
    "Earth": {
        "radius": 2 * bigger_size,
        "distanceFromSun": 3.5 * smaller_dist,
    },
    "Mars": {
        "radius": 2.5 * bigger_size,
        "distanceFromSun": 3.5 * smaller_dist,
    },
    "Jupiter": {
        "radius": 1 / 4 * bigger_size,
        "distanceFromSun": 1.5 * smaller_dist,
    },
    "Saturn": {
        "radius": 1 / 4 * bigger_size,
        "distanceFromSun": 1 * smaller_dist,
    },
    "Uranus": {
        "radius": 1 / 2.5 * bigger_size,
        "distanceFromSun": 1 / 1.8 * smaller_dist,
    },
    "Neptune": {
        "radius": 1 / 2.5 * bigger_size,
        "distanceFromSun": 1 / 2.5 * smaller_dist,
    }
}


