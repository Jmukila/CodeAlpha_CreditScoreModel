# -*- coding: utf-8 -*-
"""CodeAlpha_CreditScore.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DMlW2n955fE2r88oWR0kLwy_LsZ7bZ09
"""
"""
import kagglehub

# Download latest version
path = kagglehub.dataset_download("parisrohan/credit-score-classification")

print("Path to dataset files:", path)

import shutil
import os

# Define the target folder in your Google Drive
drive_path = "E:\Cse 2021-2025\CodeAlpha\Task1\credit-score-classification"

# Copy the dataset folder to Google Drive
if os.path.exists(path):
    shutil.copytree(path, drive_path)
    print(f"Dataset successfully saved to: {drive_path}")
else:
    print("Dataset path does not exist. Please check the path.")

"""
import numpy as np
import pandas as pd
df = pd.read_csv('E:/Cse 2021-2025/CodeAlpha/Task1/credit-score-classification/train.csv')
print(df.head())

from wolta.data_tools import col_types

types = col_types(df, print_columns=True)

from wolta.data_tools import seek_null

seeked = seek_null(df, print_columns=True)

from wolta.data_tools import unique_amounts

unique_amounts(df)

from wolta.feature_tools import list_deletings

df = list_deletings(df, extra=[
    'ID',
    'Customer_ID',
    'Name',
    'SSN',
    'Type_of_Loan',
])

from wolta.data_tools import find_broke

indexes = find_broke(df['Annual_Income'])

for index in indexes:
    df['Annual_Income'].values[index] = df['Annual_Income'].values[index][:-1]
df['Annual_Income'] = df['Annual_Income'].astype(float)

indexes = find_broke(df['Outstanding_Debt'])

for index in indexes:
    df['Outstanding_Debt'].values[index] = df['Outstanding_Debt'].values[index][:-1]
df['Outstanding_Debt'] = df['Outstanding_Debt'].astype(float)
indexes = find_broke(df['Monthly_Balance'])

for index in indexes:
    df['Monthly_Balance'].values[index] = df['Monthly_Balance'].values[index][2:-2]
df['Monthly_Balance'] = df['Monthly_Balance'].astype(float)
indexes = find_broke(df['Num_of_Delayed_Payment'])

for index in indexes:
    df['Num_of_Delayed_Payment'].values[index] = df['Num_of_Delayed_Payment'].values[index][:-1]
df['Num_of_Delayed_Payment'] = df['Num_of_Delayed_Payment'].astype(float)
indexes = find_broke(df['Num_of_Loan'])

for index in indexes:
    df['Num_of_Loan'].values[index] = df['Num_of_Loan'].values[index][:-1]
df['Num_of_Loan'] = df['Num_of_Loan'].astype(float)
indexes = find_broke(df['Changed_Credit_Limit'])

for index in indexes:
    df['Changed_Credit_Limit'].values[index] = '0'
df['Changed_Credit_Limit'] = df['Changed_Credit_Limit'].astype(float)
indexes = find_broke(df['Amount_invested_monthly'])

for index in indexes:
    df['Amount_invested_monthly'].values[index] = df['Amount_invested_monthly'].values[index][2:-2]
df['Amount_invested_monthly'] = df['Amount_invested_monthly'].astype(float)
types = col_types(df, print_columns=True)

seeked = seek_null(df, print_columns=True)

df['Credit_History_Age'] = df['Credit_History_Age'].fillna('unknown')
seeked.remove('Credit_History_Age')
for seek in seeked:
    df[seek] = df[seek].fillna(np.nanmean(df[seek].values))
history_age = []

for i in range(df.shape[0]):
    if df['Credit_History_Age'].values[i].__contains__('Years and'):
        splitted = df['Credit_History_Age'].values[i].split('Years and')

        years = int(splitted[0].strip())
        months = int(splitted[1].replace('Months', ''))
        history_age.append((years * 12) + months)
    else:
        history_age.append(0)

df['Credit_History_Age'] = history_age
from wolta.data_tools import make_numerics

df['Credit_Score'], outs = make_numerics(df['Credit_Score'], space_requested=True)

print(outs)
outs = list(outs)
print(outs)

types = col_types(df)
loc = 0

for col in df.columns:
    if types[loc] == 'str':
        df[col] = make_numerics(df[col])

    loc += 1

df.head()

df.describe()

from wolta.data_tools import stat_sumls

stat_sum(df,
        ['max', 'min', 'width', 'var', 'med'])

df['Credit_Score'].value_counts().plot(kind='pie')

y = df['Credit_Score'].values
del df['Credit_Score']
X = df.values
del df
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
del X, y

from collections import Counter

print(Counter(y_train))
print(Counter(y_test))

from wolta.model_tools import compare_models

results = compare_models('clf',
                        ['ada', 'cat', 'raf', 'lbm', 'dtr', 'ext', 'per', 'rdg'],
                        ['acc', 'precision', 'f1', 'recall'],
                        X_train, y_train, X_test, y_test,
                        get_result=True)

from wolta.model_tools import get_best_model

model = get_best_model(results, 'acc', 'clf', X_train, y_train, behavior='max-best')
y_pred = model.predict(X_test)

from sklearn.metrics import classification_report as rep

print(rep(y_test, y_pred))

from sklearn.metrics import confusion_matrix as conf
from sklearn.metrics import ConfusionMatrixDisplay as cmd

cm = conf(y_test, y_pred)
disp = cmd(confusion_matrix=cm, display_labels=outs)
disp.plot()