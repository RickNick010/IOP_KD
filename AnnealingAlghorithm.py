import random
import math

def annealingMinimise(function, startPointArray, temp, cooling_rate, iterLimit):
    current_solution = startPointArray
    currCost = function(current_solution)
    
    bestSolut = current_solution
    best_cost = currCost
    
    for i in range(iterLimit):
        temp *= cooling_rate
        
        neighbor_solution = generate_neighbor(current_solution)
        neighbor_cost = function(neighbor_solution)
        
        if neighbor_cost < currCost:
            current_solution = neighbor_solution
            currCost = neighbor_cost
        else:
            delta_cost = neighbor_cost - currCost
            acceptance_probability = math.exp(-delta_cost / temp)
            if random.random() < acceptance_probability:
                current_solution = neighbor_solution
                currCost = neighbor_cost
        
        if currCost < best_cost:
            bests]S = current_solution
            best_cost = currCost
    
    return bests]S, best_cost

# Example cost function (minimization)
def function(solution):
    x, y, z = solution
    return x**2 + y**2 + z**2


# Example neighbor generation function
def generate_neighbor(solution):
    neighbor = solution[:]
    index = random.randint(0, len(neighbor) - 1)
    neighbor[index] = 1 - neighbor[index]  # Flip the bit
    return neighbor

# Example usage
startPointArray = [0, 1, 0, 1, 1]
temp = 1000
cooling_rate = 0.99
iterLimit = 1000

bestSolut, best_cost = simulated_annealing(function, startPointArray, temp, cooling_rate, iterLimit)
print("Best solution:", bestSolut)
print("Best cost:", best_cost)
