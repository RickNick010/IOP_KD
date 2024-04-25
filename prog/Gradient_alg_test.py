import numpy as np
# Функция, которую мы хотим оптимизировать
def function_to_optimize(x1, x2, x3):
    return 0*x1**4-x1*x2**2+2*x2**2*x3**2-2*x3**3+10*x1+4*x2+np.exp(x3)-np.log(x1**2+x2**2+1)

# Градиент функции
def gradient(x1, x2, x3):
    grad_x1 = -4 * x1**3 - (2 * x1) / (x1**2 + x2**2 + 1) + 10
    grad_x2 = -2 * x1 * x2 - (2 * x2) / (x1**2 + x2**2 + 1) + 4
    grad_x3 = 4 * x2**2 * x3**2 - 6 * x3 + np.exp(x3)
    return grad_x1, grad_x2, grad_x3

# Начальные значения переменных
x1 = 0
x2 = 0
x3 = 0

# Скорость обучения (learning rate)
learning_rate = 0.1

# Количество итераций
num_iterations = 100

# Градиентный спуск
for i in range(num_iterations):
    grad_x1, grad_x2, grad_x3 = gradient(x1, x2, x3)
    # Обновление переменных
    x1 -= learning_rate * grad_x1
    x2 -= learning_rate * grad_x2
    x3 -= learning_rate * grad_x3
    # Вывод каждой итерации
    print(f"Iteration {i+1}: x1 = {x1}, x2 = {x2}, x3 = {x3}, value = {function_to_optimize(x1, x2, x3)}")
