"""
Interpreter for GLM
"""
from ..interpreter import Interpreter


class LinearInterpreter(Interpreter):
    def __init__(self, model, X_train, y_train, y_test, X_test=None, validation=None, *args):
        super().__init__(model, X_train, X_test, validation)
        self.y_train = y_train
        self.y_test = y_test
        self.rsquare = None

    def compute_ci(self):

        return NotImplementedError

    def plot_weights(self, nb_features=20):
        """
        Plot weights of self.features, according to self.model.coef_
        :param nb_features: Number of most important features to keep.
        :return: matplotlib.pyplot.plt figures
        """

        df_plot = pd.DataFrame(np.column_stack((self.features, self.model.coef_)), columns=['feature', 'coef'],
                               index=None)
        df_plot['coef_abs'] = df_plot.coef.abs()
        df_plot = df_plot.sort_values(by=['coef_abs'], ascending=False).head(nb_features)
        df_plot.sort_values(by=['coef'], inplace=True)

        fig = self.init_plt_fig(1, 1)
        sns.barplot(data=df_plot, x='feature', y='coef', palette="rocket", ax=fig[1])
        fig[1].axhline(0, color="k", clip_on=False)
        fig[1].set_ylabel("Sequential")

        plt.tight_layout(h_pad=2)
        plt.plot()

        return None

    def compute_rsquare(self):

        return NotImplementedError




