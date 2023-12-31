import numpy as np

def pearson_correlation(x, y):
    # Вычисляем среднее значение для каждого массива
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    # Вычисляем среднеквадратичное отклонение для каждого массива
    std_x = np.std(x)
    std_y = np.std(y)

    # Вычисляем ковариацию между массивами
    covariance = np.cov(x, y)[0, 1]

    # Вычисляем коэффициент корреляции Пирсона
    correlation = covariance / (std_x * std_y)

    return correlation

# Пример использования
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

correlation = pearson_correlation(x, y)
print("Коэффициент корреляции Пирсона:", correlation)



# В предложенном скрипте была использована функциональная парадигма программирования.
# Помимо функциональной парадигмы, в этом скрипте также применяется императивный стиль
# программирования, когда мы вызываем функцию print для вывода результата на экран.