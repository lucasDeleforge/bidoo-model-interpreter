"""
Main interpreter
"""
import logging
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", context="talk")


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
        self.features = self.X_train.columns.values

    def plot_feature_importance(self):

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

    def init_plt_fig(self, rows, cols):
        """
        Standardization of figure creation.
        :param rows: Number of axis in rows
        :param cols: Number of axis in columns
        :return: matplotlib.pyplot.plt figures with rows*columns shape
        """
        fig = plt.subplots(rows, cols, figsize=(7, 5), sharex=True)

        return fig


