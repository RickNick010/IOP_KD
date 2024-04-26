import GradientAlgorithm as ga

startPointArray = [1.0, 2.0, 3.0]
learningRate = [0.0001, 0.001, 0.000001]  
iterLimit = 10000
tolerance = 0.0000000001
minimum = ga.GradientAlg()
for lr in learningRate:
    minimum.gradientOpt(startPointArray, iterLimit, tolerance, lr)
minimum.diagPlot(0)
minimum.diagPlot1()

