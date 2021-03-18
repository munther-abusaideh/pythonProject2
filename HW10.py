
#HW10A
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
from sklearn.datasets import fetch_california_housing


housing = fetch_california_housing()

X_train_full, X_test, y_train_full, y_test = \
    train_test_split(housing.data, housing.target, test_size=0.33, random_state=42)

X_train, X_valid, y_train, y_valid = \
    train_test_split(X_train_full, y_train_full, test_size=0.33, random_state= 42)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_valid = scaler.transform(X_valid)
X_test = scaler.transform(X_test)

print(X_train, X_valid , X_test, y_train ,y_valid,y_test)

reg = LinearRegression
reg.fit(X_train, y_train)

reg = MLPRegressor ()
reg.fit(X_train, y_train)





#print('\nTesting regressers')
#regressers = []
#regressers.append(LinearRegression())
#for reg in regressers:
    ##reg.fit(X, y)




#print(X_train, y_train, X_test, y_test)


