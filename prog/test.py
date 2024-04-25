import numpy as np

# Определение функции для минимизации
def f(x):
    return 0*x[0]**4-x[0]*x[1]**2+2*x[1]**2*x[2]**2-2*x[2]**3+10*x[0]+4*x[1]+np.exp(x[2])-np.log(x[0]**2+x[1]**2+1)

# Определение градиента функциисд
def gradient_f(x):
    return np.array([4*x[0]**3 + (2*x[0])/(x[0]**2 + x[1]**2 + 1) + 10,
                     -2*x[0]*x[1] - (2*x[1])/(x[0]**2 + x[1]**2 + 1) + 4,
                     4*x[1]**2*x[2] - 6*x[2]**2 + np.exp(x[2])])

# Начальная точка и скорость обучения
x = np.array([3.0, 4.0, 5.0])  # Начальная точка
learning_rate = 0.1

# Максимальное количество итераций
max_iterations = 1000

# Градиентный спуск
for i in range(max_iterations):
    grad = gradient_f(x)
    x = x - learning_rate * grad
    # Проверка на достижение минимума (заданного порога)
    
    flag = np.linalg.norm(grad)
    print(flag, i)
    if flag < 1e-6:
        break

print("Минимум достигается в точке:", x)
print("Значение функции в минимуме:", f(x))