import numpy as np
import matplotlib.pyplot as plt
class GradientAlg:
    
    def __init__(self):
        self.diagFuncHistory = {}
        self.iterations_per_lr = {}
        self.x = []
        self.counter = 0

    
    def function(self, x):
        x1, x2, x3 = x
        return 0*x1**4-x1*x2**2+2*x2**2*x3**2-2*x3**3+10*x1+4*x2+np.exp(x3)-np.log(x1**2+x2**2+1)
    
    def gradFunction(self, x):
        x1, x2, x3 = x
        grad_x0 = -4 * x1**3 - (2 * x1) / (x1**2 + x2**2 + 1) + 10
        grad_x1 = -2 * x1 * x2 - (2 * x2) / (x1**2 + x2**2 + 1) + 4
        grad_x2 = 4 * x2**2 * x3**2 - 6 * x3 + np.exp(x3)
        return np.array([grad_x0, grad_x1, grad_x2])
        
    def gradientOpt(self, x, iterLimit, tolerance, learningRate):
        for i in range(iterLimit):
            gradient = self.gradFunction(x)
            norma = np.linalg.norm(x)
            if norma < tolerance:
                break
            x[0] -= learningRate * gradient[0]
            x[1] -= learningRate * gradient[1]
            x[2] -= learningRate * gradient[2]
            if self.diagFuncHistory.get(self.counter) is not None:
                self.diagFuncHistory[self.counter] = np.append(self.diagFuncHistory[self.counter], self.function(x))
            else:
                self.diagFuncHistory[self.counter] = self.function(x)    
        self.x.append(x)
        self.iterations_per_lr[learningRate] = i
        self.PrintResult(self.counter)
        self.counter += 1 
 
    
    def diagPlot(self, number):
        iterations = range(1, np.size(self.diagFuncHistory[number]) + 1)
        plt.plot(iterations, self.diagFuncHistory[number], marker='o', linestyle='-')
        plt.xlabel('Iteraciju Skaits')
        plt.ylabel('Funkcijas Vērtiba')
        plt.title('Funkcijas vērtība pec iteracijam')
        plt.grid(True)
        plt.show()
          

    def diagPlot1(self):
        plt.bar(self.iterations_per_lr.keys(), self.iterations_per_lr.values(), color='skyblue')
        plt.xlabel('Soļa lielums')
        plt.ylabel('Iteraciju skaits')
        plt.title('Iteraciju skaita atakrība no soļa lieluma')
        plt.xticks(list(self.iterations_per_lr.keys()))
        plt.grid(axis='y')
        plt.show()

    def PrintResult(self, number):
        print("Minimum:", self.x[number])
        print("Function value at minimum:", self.function(self.x[number]))    