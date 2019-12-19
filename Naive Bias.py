import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

xl=pd.read_excel('New_Data_Set1.xlsx')
x=xl.iloc[:,0:4].values
y=xl.iloc[:,5].values

X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=.30,random_state=17)
logreg = GaussianNB()
logreg.fit(X_train,Y_train)
y_pred=logreg.predict(X_test)
accuracy=accuracy_score(Y_test,y_pred)
print("Test Accuracy: ",accuracy*100)
