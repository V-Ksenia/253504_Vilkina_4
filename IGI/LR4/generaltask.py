from abc import ABC, abstractmethod

class GeneralTask(ABC):
    @staticmethod
    @abstractmethod
    def __call__():
        pass