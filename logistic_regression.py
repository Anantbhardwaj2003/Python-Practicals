from sklearn.model_selection import train_test_split
from sklearn import datasets,linear_model,metrics
import pandas as pd

#Load the digit dataset
digits=datasets.load_digits()
df=pd.DataFrame(digits.data)
df

X=digits.data
y=digits.target
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.4,random_state=1)

# fit the model using Logistic Regression
model=linear_model.LogisticRegression()
model.fit(X_train,y_train)

# predict the model
y_pred=model.predict(X_test)

# calculate the accuracy
accuracy = metrics.accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy*100)
