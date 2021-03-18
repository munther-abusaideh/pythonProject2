from sklearn import *
from sklearn import datasets, linear_model
from sklearn.ensemble.tests.test_bagging import diabetes
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score

from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import cross_val_score

diabetes= datasets.load_diabetes()

X = diabetes.data[:, np.newaxls, 3]
# print(X.shape)

y = diabetes.target
cross_val_score(reg, X, y, scoring="neg_mean_squared_error", cv=3)

X_train, X_test, y_train, y_test = cross_val_score.train_test_split(X, y, test_size=0.3)
reg = linear_model.LinearRegression()

reg.fit(X_train, y_train)

y_pred = reg.predict(X_test)
Coef = reg.coef_
print(Coef)

R2 = r2_score(y_test, y_pred)
MSE = mean_squared_error(y_test, y_pred)
print(R2.MSE)

style.use('ggplot')
plt.scatter(y_pred, y_test, color='green')
plt.title('Predected dara vs Real data')
plt.xlabel('y_pred')
plt.ylabel('y_test')
plt.show()
