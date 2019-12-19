import sklearn
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import linear_model

xl=pd.read_excel('New_Data_Set1.xlsx')
x=xl.iloc[:,0:4].values
y=xl.iloc[:,5].values

X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=.30,random_state=10)
svm = SVC(gamma='auto')
svm.fit(X_train,Y_train)
y_pred=svm.predict(X_test)
accuracy=accuracy_score(Y_test,y_pred)
print("Test Accuracy: ",accuracy*100)