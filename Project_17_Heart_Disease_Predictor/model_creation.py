import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

df=pd.read_csv("data.csv")
df.replace('?', np.nan, inplace=True)
df = df.apply(pd.to_numeric, errors='coerce')
df.dropna(inplace=True)


X=df.drop('num',axis=1)
y=df['num']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model =LogisticRegression(max_iter=1000)

model.fit(X_train,y_train)

with open("model.pkl",'wb') as f:
  pickle.dump(model,f)
