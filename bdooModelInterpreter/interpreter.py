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

    def plot_feature_importance(self, nb_features=20):
        """
        Plot importances of self.features, according to self.model.coef_
        :param nb_features: Number of most important features to keep.
        :return: matplotlib.pyplot.plt figures
        """

        df_plot = pd.DataFrame(np.column_stack((self.features, self.model.coef_)), columns=['feature', 'coef'],
                               index=None)
        df_plot['coef_abs'] = df_plot.coef.abs()
        df_plot = df_plot.sort_values(by=['coef_abs'], ascending=False).head(nb_features)
        df_plot.sort_values(by=['coef'], inplace=True)

        fig = self.init_plt_fig(1,1)
        sns.barplot(data=df_plot, x='feature', y='coef', palette="rocket", ax=fig[1])
        fig[1].axhline(0, color="k", clip_on=False)
        fig[1].set_ylabel("Sequential")

        plt.tight_layout(h_pad=2)
        plt.plot()

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


