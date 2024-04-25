import numpy as np
import matplotlib.pyplot as plt
class GradientAlg:
    
    def __init__(self, startPointArray, iterLimit, tolerance, learningRate):
        self.startPointArray = startPointArray
        self.iteration_limit = iterLimit
        self.tolerance = tolerance
        self.learningRate = learningRate
        self.diagFuncHistory = []
        self.iterPerLr = {}
        self.x = self.startPointArray

    
    def function(self):
        return 0*self.x[0]**4-self.x[0]*self.x[1]**2+2*self.x[1]**2*self.x[2]**2-2*self.x[2]**3+10*self.x[0]+4*self.x[1]+np.exp(self.x[2])-np.log(self.x[0]**2+self.x[1]**2+1)
    
    def gradFunction(self):
        grad_x0 = -4 * self.x[0]**3 - (2 * self.x[0]) / (self.x[0]**2 + self.x[1]**2 + 1) + 10
        grad_x1 = -2 * self.x[0] * self.x[1] - (2 * self.x[1]) / (self.x[0]**2 + self.x[1]**2 + 1) + 4
        grad_x2 = 4 * self.x[1]**2 * self.x[2]**2 - 6 * self.x[2] + np.exp(self.x[2])
        return np.array([grad_x0,
                         grad_x1,
                         grad_x2])
        
    def gradientOpt(self):
        for lr in self.learningRate:
            for i in range(self.iteration_limit):
                gradient = self.gradFunction()
                flag = np.linalg.norm(self.x)
                if flag < self.tolerance:
                    self.iterPerLr[lr] = i
                    break
                self.x[0] -= lr * gradient[0]
                self.x[1] -= lr * gradient[1]
                self.x[2] -= lr * gradient[2]
                self.diagFuncHistory.append(self.function())

 
    
    def diagPlot(self):
        iterations = range(1, len(self.diagFuncHistory) + 1)
        plt.plot(iterations, self.diagFuncHistory, marker='o', linestyle='-')
        plt.xlabel('Iteraciju Skaits')
        plt.ylabel('Funkcijas Vērtiba')
        plt.title('Funkcijas vērtības atšķirība no optimuma')
        plt.grid(True)
        plt.show()
    
    def diagPlotAdv(self):
        plt.bar(self.iterPerLr.keys(), self.iterPerLr.values(), color='skyblue')
        plt.xlabel('Learning Rate')
        plt.ylabel('Number of Iterations')
        plt.title('Number of Iterations vs Learning Rate')
        plt.xticks(list(self.iterPerLr.keys()))
        plt.grid(axis='y')
        plt.show()        
        
    def Print(self):
        print("Minimum:", self.x)
        print("Function value at minimum:", self.function())    