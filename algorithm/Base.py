import abc as ABC
from abc import ABC, abstractmethod, abstractproperty


class Algorithm(ABC):

    @abstractmethod
    def solve(self):
        pass

    @abstractmethod
    def eval(self):
        pass

    @abstractproperty
    def name(self):
        pass
