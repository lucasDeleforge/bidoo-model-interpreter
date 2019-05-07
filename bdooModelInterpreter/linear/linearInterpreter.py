"""
Interpreter for GLM
"""
from ..interpreter import Interpreter

class LinearInterpreter(Interpreter):
    def __init__(self, *args):
        super().__init__(*args)
