"""
Interpreter for GLM
"""
from ..interpreter import Interpreter


class LinearInterpreter(Interpreter):
    def __init__(self, y_train, x_test,*args):
        super().__init__(*args)
        self.y_train = y_train
        self.y_test = x_test


