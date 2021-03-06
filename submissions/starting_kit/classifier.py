from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import Imputer
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator

from imblearn.pipeline import make_pipeline as make_pipeline_imb
from imblearn.under_sampling import RandomUnderSampler


class Classifier(BaseEstimator):
    def __init__(self):
        self.clf = make_pipeline_imb(
        	Imputer(strategy='median'), 
        	RandomUnderSampler(), 
        	LogisticRegression(C=1e-3, penalty="l2"))

    def fit(self, X, y):
        self.clf.fit(X, y)
        

    def predict_proba(self, X):
        return self.clf.predict_proba(X)
