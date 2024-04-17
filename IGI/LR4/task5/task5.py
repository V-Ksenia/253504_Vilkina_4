import numpy as np
from inputvalidator import *
from generaltask import GeneralTask

class InputMatrixMixin:
    matrix : any
    def input_matrix(self):
        n = inputValidate("\033[1mEnter the number of rows:\033[00m ", TYPES.INT) 
        m = inputValidate("\033[1mEnter the number of columns:\033[00m ", TYPES.INT) 

        print("\033[1mEnter elements:\033[00m")  
        
        listmatrix = []
        for _ in range(n):  
            r = []  
            for __ in range(m): 
                r.append(inputValidate("", TYPES.INT))  
            listmatrix.append(r) 

        self.matrix = np.array(listmatrix).reshape(n, m) 

        return self.matrix

class MatrixHandler(InputMatrixMixin):
    

    @property
    def matrix_(self):
        return self.matrix
    
    @matrix_.setter
    def matrix_(self, matrix_):
        self.matrix = matrix_

    def find_even_odd(self):
        self.even_elements = self.matrix[self.matrix % 2 == 0]
        self.odd_elements = self.matrix[self.matrix % 2 != 0]
        return self.even_elements, self.odd_elements
    
    def calculate_corr_coeff(self):
        if len(self.even_elements) != len(self.odd_elements):
            min_length = min(len(self.even_elements), len(self.odd_elements))
            self.even_elements = self.even_elements[:min_length]
            self.odd_elements = self.odd_elements[:min_length]
            print(f"\033[1mCropped matrix:\033[00m\n \033[32mEven matrix:\033[00m {self.even_elements}\n \033[31mOdd matrix:\033[00m {self.odd_elements}")

        return round(np.corrcoef(self.even_elements, self.odd_elements)[0, 1], 4)
    

class TaskFifth(GeneralTask):
    @staticmethod
    def __call__():
        
        handler = MatrixHandler()

        while True:
            option = input("\033[92m\033[1mEnter 1(for random matrix), 2(for user's input) or any other symbol to leave: \033[00m")
            match option:
                case "1":          
                    n = np.random.randint(2, 6)
                    m = np.random.randint(2, 6)
                    matrix = np.random.randint(1, 10, (n, m))
                    
                    handler.matrix_ = matrix

                    print(f'\033[1mRandom generated matrix:\033[00m\n{handler.matrix_}')

                    even_elements, odd_elements = handler.find_even_odd()
                    print(f"\033[32m Even matrix:\033[00m {even_elements}\n \033[31mOdd matrix:\033[00m {odd_elements}")

                    print(f"\033[92mCoeff:\033[00m {handler.calculate_corr_coeff()}")

                case "2":
                    print(f"\033[1mUser's matrix:\033[00m {handler.input_matrix()}")

                    even_elements, odd_elements = handler.find_even_odd()
                    print(f"\033[32m Even matrix:\033[00m {even_elements}\n \033[31mOdd matrix:\033[00m {odd_elements}")

                    print(f"\033[92mCoeff:\033[00m {handler.calculate_corr_coeff()}")

                case _:
                    break