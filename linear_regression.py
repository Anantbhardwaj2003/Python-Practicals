import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
df=pd.read_csv('D:/data.csv')
df

X=df[['Temperature']]
y=df['Pressure']

model=LinearRegression()
model.fit(X,y)

y_pred=model.predict(X)

# intercept
intercept=model.intercept_
print(f"Intercept:{intercept:.2f}")

# Slope
slope=model.coef_[0]
print(f"slope:{slope:.2f}")

# Original Data
plt.scatter(X,y,color='blue',label='Original Points')

# Best fit line
plt.plot(X,y_pred,color='red',label='Regression Line')
plt.xlabel('Temperature')
plt.ylabel('Pressure')
plt.title('Linear Regression')
plt.legend()
plt.show()

# find the particular pressure using temperature
def predict_pressure(temperature):
    predict_pressure=model.predict([[temperature]])
    return predict_pressure

temperature_to_predict=30
predicted_pressure=predict_pressure(temperature_to_predict)
print(f"Predicted Pressure at{temperature_to_predict}°C: {predict_pressure:.2f}")

