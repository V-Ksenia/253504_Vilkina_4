import numpy as np
from inputvalidator import *

class TaskFifth:
    @staticmethod
    def __call__():

        n = np.random.randint(2, 6)
        m = np.random.randint(2, 6)
        matrix = np.random.randint(1, 10, (n, m))
        print(f'Generated matrix:\n{matrix}')

        even_elements = matrix[matrix % 2 == 0]
        odd_elements = matrix[matrix % 2 != 0]

        print(f"Even matrix: {even_elements}\n Odd matrix: {odd_elements}")

        if len(even_elements) != len(odd_elements):
            min_length = min(len(even_elements), len(odd_elements))
            even_elements = even_elements[:min_length]
            odd_elements = odd_elements[:min_length]
            print(f"Cropped matrix:\n Even matrix: {even_elements}\n Odd matrix: {odd_elements}")

        correlation_coefficient = np.corrcoef(even_elements, odd_elements)[0, 1]

        print(f"Correlation coefficient: {round(correlation_coefficient, 4)}")