
import GradientAlgorithm as ga

startPointArray = [1, 2, 3]  # Начальное предположение
learningRate = [0.0001, 0.001, 0.000001]  # Размер шага градиентного спуска
iterLimit = 1000
tolerance = 0.000000000000001
minimum = ga.GradientAlg(startPointArray, iterLimit, tolerance, learningRate)
minimum.gradientOpt()
minimum.Print()
minimum.diagPlot()
minimum.diagPlotAdv()

