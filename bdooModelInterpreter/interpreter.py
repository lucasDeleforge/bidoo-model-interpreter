"""
Main interpreter
"""
import seaborn as sns

class Interpreter:
    """
    Parent class for all interpreter.
    """
    def __init__(self, model, train, test, validation=None):
        self.model = model
        self.train = train
        self.test = test
        self.validation = validation

    def plot_feature_importance(self):
        """

        :return:
        """

        return None

    def plot_data(self):
        """

        :return:
        """

        return None

    def plot_performance(self):
        """

        :return:
        """

        return None


