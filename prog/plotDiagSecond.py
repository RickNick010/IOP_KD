import matplotlib.pyplot as plt
def gradient_descent_iterations(func, grad_func, initial_guess, learning_rates, tol=1e-6, max_iter=1000):
    """
    Gradient Descent optimization algorithm with history.

    Parameters:
        func (function): The objective function to minimize.
        grad_func (function): The gradient of the objective function.
        initial_guess (float): Initial guess for the minimum.
        learning_rates (list): List of learning rates to try.
        tol (float): Tolerance for stopping criteria (default=1e-6).
        max_iter (int): Maximum number of iterations (default=1000).

    Returns:
        Dict: Dictionary containing the number of iterations for each learning rate.
    """
    iterations_per_lr = {}
    for lr in learning_rates:
        x = initial_guess
        for i in range(max_iter):
            gradient = grad_func(x)
            if abs(gradient) < tol:
                iterations_per_lr[lr] = i
                break
            x -= lr * gradient

    return iterations_per_lr

# Пример использования:
initial_guess = 0  # Начальное предположение
learning_rates = [0.001, 0.01, 0.1, 0.5, 1.0]  # Размеры шага для тестирования
iterations_per_lr = gradient_descent_iterations(func, grad_func, initial_guess, learning_rates)

# Построение диаграммы
plt.bar(iterations_per_lr.keys(), iterations_per_lr.values(), color='skyblue')
plt.xlabel('Learning Rate')
plt.ylabel('Number of Iterations')
plt.title('Number of Iterations vs Learning Rate')
plt.xticks(list(iterations_per_lr.keys()))
plt.grid(axis='y')
plt.show()