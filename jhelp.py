from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import VarianceThreshold
import pandas as pd

data = pd.read_csv("data.csv", nrows=40000)
data.shape

train_features, test_features, train_labels, test_labels=train_test_split(
    data.drop(labels=['price_range'], axis=1),
    data['price_range'],
    test_size=0.2,
    random_state=41)

reg = LassoCV()
reg.fit(train_features, train_labels)
print("Best alpha using built-in LassoCV: %f" % reg.alpha_)
print("Best score using built-in LassoCV: %f" %reg.score(train_features, train_labels))
coef = pd.Series(reg.coef_, index = train_features.columns)

print(train_features.columns)

