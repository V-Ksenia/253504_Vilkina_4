import numpy as np 
import matplotlib.pyplot as plt
from math import fabs, log, sqrt
from statistics import median, mode, mean
from inputvalidator import *
from generaltask import GeneralTask

class Series:
    def __init__(self, x, eps):
        self._x = x
        self._eps = eps
        self._additionalCalculator = AdditionalCalculations()

    def calculateSeries(self):
        result = 0.0
        seriesList = []
        for n in range(1, 500):
            seriesList.append((-1) * self._x**n / n)
            result += (-1) * self._x**n / n
            if fabs(result - log(1 - self._x)) <= self._eps:
                print(f"\033[92m x = {self._x}, n = {n}, ln(1-x) = {round(result, 3)}, math ln(1-x) = {round(log(1 - self._x), 3)}, eps = {self._eps} \033[00m")
                
                print(f"\033[92m Average of elements: \033[00m {self._additionalCalculator.calculateAverage(seriesList)}")
                print(f"\033[92m Mode: \033[00m {self._additionalCalculator.calculateMode(seriesList)}")
                print(f"\033[92m Median: \033[00m {self._additionalCalculator.calculateMedian(seriesList)}")

                dispersion = self._additionalCalculator.calculateDispersion(seriesList)
                print(f"\033[92m Dispersion: \033[00m {dispersion}")
                print(f"\033[92m Mean deviation: \033[00m {self._additionalCalculator.calculateMeanDeviation(dispersion)}")
                return n
        print("iterations > 500")
        return None 

class AdditionalCalculations:
    @staticmethod
    def calculateDispersion(series):
        return round(np.var(series), 4) 
    
    @staticmethod
    def calculateMode(series):
        return round(mode(series), 4)

    @staticmethod
    def calculateMedian(series):
        return round(median(series), 4)
    
    @staticmethod
    def calculateMeanDeviation(dispertion):
        return round(sqrt(dispertion), 4)

    @staticmethod
    def calculateAverage(series):
        return round(mean(series), 4)

class PlotBuilder:
    def buildPlot(self, n):
        x = np.linspace(-0.99, 0.99, 100)

        func1 = np.log(1 - x)
        func2 = sum((-1) * x**i / i for i in range(1, n))

        plt.plot(x, func1, color='g')
        plt.plot(x, func2, color='y')
        
        plt.legend(['log(1 - x)', '(-1) * x**n / n'])
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Series plots')
        plt.annotate('Some annotation here', xy=(0.0, 0.0), xytext=(-0.25, -1), arrowprops=dict(facecolor="black"))
        plt.text(-0.95, -4, 'And a little bit of text\nright here')
    
        plt.grid(True)
        figure = plt.gcf()
        figure.set_size_inches(9, 5)
        plt.savefig(r'C:\253504_Vilkina_4\IGI\LR4\task3\plots.png')
        plt.show()

class TaskThird(GeneralTask):
    @staticmethod
    def __call__():

        while True:        
            x = inputValidate("\033[1m Enter x: \033[00m", TYPES.FLOAT)
            if fabs(x) > 1:
                print("\033[91m |x| > 1. Enter again. \033[00m")
            else:
                eps = inputValidate("\033[1m Enter eps: \033[00m", TYPES.FLOAT)

                series = Series(x, eps)
                iterations = series.calculateSeries()

                plotBuilder = PlotBuilder()
                plotBuilder.buildPlot(iterations)
                return
