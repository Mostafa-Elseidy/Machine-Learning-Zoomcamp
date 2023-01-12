import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

# Load data
df = pd.read_csv('online_shoppers_intention.csv')

# data preparation
df.Month = df.Month.replace({'Feb': 2, 'Mar': 3, 'May': 5, 'June': 6, 'Jul': 7,
                             'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12})
df.VisitorType = df.VisitorType.replace(
    {"Returning_Visitor": 0, 'New_Visitor': 1, 'Other': 2})
df.Weekend = df.Weekend.astype('int')
df.Revenue = df.Revenue.astype('int')
df.drop_duplicates(inplace=True)
df.SpecialDay = (df.SpecialDay * 10).astype("int")

# split data
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# train and val 80,  test 20
X_full_train, X_test, y_full_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1)


# parameters
max_iter = 5000
C = 0.5005
solver = 'lbfgs'

# training


def train(df_train, y_train, C=1.0):
    dicts = df_train.to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)

    model = LogisticRegression(C=C, max_iter=max_iter, solver=solver)
    model.fit(X_train, y_train)

    return dv, model


def predict(df, dv, model):
    dicts = df.to_dict(orient='records')

    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:, 1]

    return y_pred


# training the final model
print('training the final model')

dv, model = train(X_full_train, y_full_train, C=C)
y_pred = predict(X_test, dv, model)
auc = roc_auc_score(y_test, y_pred)

print(f'auc={auc}')


# Save the model

with open("lr_model.bin", 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print('model saved.')
