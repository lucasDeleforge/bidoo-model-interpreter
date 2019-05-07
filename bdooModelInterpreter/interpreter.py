"""
Main interpreter
"""
import logging
import seaborn as sns

class Interpreter:
    """
    Parent class for all interpreter.
    """
    def __init__(self, model, X_train, X_test=None, validation=None):
        logging.info('Initialise : %s', type(self))
        self.model = model
        self.X_train = X_train
        self.X_test = X_test
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

    def summarise(self):
        """

        :return:
        """

        return None


