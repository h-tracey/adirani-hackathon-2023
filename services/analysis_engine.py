# pylint: disable=no-member, import-error
from repos.data_driver import DataRepo
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn import svm
from sklearn.model_selection import cross_val_score
from joblib import dump, load


class AnalysisEngine:
    def __init__(self, repo=DataRepo) -> None:
        self.repo = repo

    def calculate_page_conversions(self):
        page_data = self.repo.get_conversions_per_page
        agg_data = self.repo.get_conversions_per_type_agg

        return agg_data

    def get_agg_data(self):
        agg_data = self.repo.get_conversions_per_page
        agg_data['ptype'] = pd.Categorical(agg_data['ptype'])
        return agg_data.dropna(subset=['ptype']).reset_index(drop=True)

    def hexbin_conversion_rate(self, plot=True):
        data = self.get_agg_data()
        if plot:
            os.remove("temp/image.png")
            data.plot.hexbin('conversion_rate_per_user',
                             'views_per_user', gridsize=40)
            plt.savefig("temp/image.png", format='png')
            return "temp/image.png"
        else:
            return data

    def scatter_conversion_rate_type(self, plot=True):
        data = self.get_agg_data()
        if plot:
            os.remove("temp/image.png")
            data.plot.scatter('conversion_rate_per_user',
                              'views_per_user', c='ptype', cmap='viridis')
            plt.savefig("temp/image.png", format='png')
            return "temp/image.png"
        else:
            return data

    def views_boxplot(self, plot=True):
        data = self.get_agg_data()
        if plot:
            os.remove("temp/image.png")
            data.boxplot(['views_per_user'], by='ptype')
            plt.savefig("temp/image.png", format='png')
            return "temp/image.png"
        else:
            return data

    def conv_rate_boxplot(self, plot=True):
        data = self.get_agg_data()
        if plot:
            os.remove("temp/image.png")
            data.boxplot('conversion_rate_total', by='ptype')
            plt.savefig("temp/image.png", format='png')
            return "temp/image.png"
        else:
            return data

    def touchpoints_count(self, plot=True):
        data = self.repo.get_conversions_per_num_touchpoints
        if plot:
            os.remove("temp/image.png")
            data.plot.scatter('num_touchpoints', 'num_conversions')
            plt.savefig("temp/image.png", format='png')
            return "temp/image.png"
        else:
            return data

    def conversions_by_channel(self, plot=True):
        data = self.repo.get_conversions_per_channel
        if plot:
            os.remove("temp/image.png")
            data.plot.bar(y='conversions', x='default_channel_group')
            plt.savefig("temp/image.png", format='png')
            return "temp/image.png"
        else:
            return data
            #

    def conversions_by_month(self):
        data = self.repo.get_conversions_per_month
        return data

    def conversions_by_week(self):
        data = self.repo.get_conversions_per_weekday
        return data

    def conversions_by_product(self):
        data = self.repo.get_conversions_per_product
        return data

    def train_svm(self):
        df = self.get_agg_data()
        bins = np.histogram(df['conversion_rate_total'], 3)[1]
        bins.tolist() + [np.inf]
        bins[-1] = 1
        bins[0] = -0.01
        df['conversion_intent'] = pd.cut(
            df['conversion_rate_total'], bins.tolist(), labels=['Low', 'Medium', 'High'])

        x = df.loc[:, ['ptype', 'views_per_user']]
        x = pd.concat([pd.get_dummies(df.ptype), df.views_per_user], axis=1)
        y = df['conversion_intent']
        clf = svm.LinearSVC()
        scores = clf.fit(x,  y)
        os.remove("model/classifier.joblib")
        dump(scores, 'model/classifier.joblib')

    def post_svm(self, page_type, views_per_user):
        unfrozen = load('model/classifier.joblib')
        df = pd.DataFrame({'DINING': 0,
                           'HOTEL': 0,
                           'OFFERS': 0,
                           'RESORT': 0,
                           'views_per_user': views_per_user}, index=[0])
        df[page_type] = 1
        x = pd.concat([pd.get_dummies([page_type]),
                      pd.Series(views_per_user)], axis=1)
        for label in ['DINING', 'HOTEL', 'OFFERS', 'RESORT']:
            if label not in x:
                x[label] = 0
        prediction = unfrozen.predict(df)
        return prediction[0]
