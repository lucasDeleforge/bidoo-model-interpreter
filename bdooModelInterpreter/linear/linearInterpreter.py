"""
Interpreter for GLM
"""
from ..interpreter import Interpreter


class LinearInterpreter(Interpreter):
    def __init__(self, model, X_train, y_train, y_test, X_test=None, validation=None, nb_features_max=20, *args):
        super().__init__(model, X_train, X_test, validation)
        self.y_train = y_train
        self.y_test = y_test
        self.rsquare = None
        self.nb_features_max = nb_features_max

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

        df_plot = pd.DataFrame(np.column_stack((self.features, self.model.coef_)), columns=['feature', 'coef'],
                               index=None)
        df_plot['coef_abs'] = df_plot.coef.abs()
        df_plot = df_plot.sort_values(by=['coef_abs'], ascending=False).head(self.nb_features)
        df_plot.sort_values(by=['coef'], inplace=True)

        fig = self.init_plt_fig(1, 1)
        sns.barplot(data=df_plot, x='feature', y='coef', palette="rocket", ax=fig[1])
        fig[1].axhline(0, color="k", clip_on=False)
        fig[1].set_ylabel("Sequential")

        plt.tight_layout(h_pad=2)
        plt.plot()

        return None

    def plot_effects(self):
        """
        Plot a boxplot (effect distriburion) of each feature.
        Effect(i) = weight(Feature)*Value(i).
        Not meaningful on well scaled data
        :return: matplotlib.pyplot.plt figures
        """
        return NotImplementedError

    def compute_rsquare(self):

        return NotImplementedError




