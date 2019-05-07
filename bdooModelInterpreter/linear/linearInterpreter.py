"""
Interpreter for GLM
"""
from ..interpreter import Interpreter


class LinearInterpreter(Interpreter):
    def __init__(self, model, X_train, y_train, y_test, X_test=None, validation=None, *args):
        super().__init__(model, X_train, X_test, validation)
        self.y_train = y_train
        self.y_test = y_test


