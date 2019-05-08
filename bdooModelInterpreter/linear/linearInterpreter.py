"""
Interpreter for GLM
"""
from ..interpreter import Interpreter
import logging
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", context="talk")


class LinearInterpreter(Interpreter):

    def __init_structure(self):
        df_features = pd.DataFrame(np.column_stack((self.features, self.model.coef_)), columns=['feature', 'coef'],
                               index=None)
        df_features['coef_abs'] = df_features.coef.abs()
        df_features = df_features.sort_values(by=['coef_abs'], ascending=False).head(self.nb_features_max)
        df_features.sort_values(by=['coef'], inplace=True)

        self.df_features = df_features


    def __init__(self, model, X_train, y_train, y_test, X_test=None, validation=None, nb_features_max=20, *args):
        super().__init__(model, X_train, X_test, validation)
        self.y_train = y_train
        self.y_test = y_test
        self.rsquare = None
        self.nb_features_max = min(len(self.features), nb_features_max)

        self.__init_structure()

    def compute_ci(self, ci=.95):
        """
        Compute the confidence interval for each coeff.
        P-value, ttest... Need more docs to compute it.
        :return:
        """

        return NotImplementedError

    def plot_weights(self):
        """
        Plot weights of self.features, according to self.model.coef_
        :return: matplotlib.pyplot.plt figures
        """

        fig = self.init_plt_fig(1, 1)
        sns.barplot(data=self.df_features, x='feature', y='coef', palette="rocket", ax=fig[1])

        plt.tight_layout(h_pad=2)
        plt.plot()

        return None

    def compute_effect(self, X, coef):
        """
        Compute the effect of coef on X instances
        :param X: vector of values
        :param coef: coef
        :return: numpy array (coef*X))
        """
        return np.dot(coef, X)

    def plot_effects(self):
        """
        Plot a boxplot (effect distribution) of each feature.
        Effect(i) = weight(Feature)*Value(i).
        Not meaningful on well scaled data
        :return: matplotlib.pyplot.plt figures
        """
        fig, ax = self.init_plt_fig(self.nb_features_max, 1, height=self.nb_features_max*.9)
        for i, t in enumerate(self.df_features[['feature', 'coef']].values):
            feature, coef = t
            X = self.compute_effect(self.X_train[feature], coef)
            sns.boxplot(x=X, palette="rocket", ax=ax[i])
            ax[i].set_ylabel(feature)

        plt.tight_layout(h_pad=2)
        plt.plot()


    def compute_rsquare(self):

        return NotImplementedError




