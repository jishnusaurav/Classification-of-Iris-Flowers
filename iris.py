!pip install sklearn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np 
iris_dataset = load_iris()

xtrain, xtest, ytrain, ytest = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)


print("To check the ratio of training to testing datasets")
print("X_train shape:",xtrain.shape)
print("y_train shape:",xtrain.shape)
print("X_test shape:",xtest.shape)
print("y_test shape:",ytest.shape)


'''trains using our KNN algorithm'''
KNNALGO = KNeighborsClassifier(n_neighbors=1)
KNNALGO.fit(xtrain, ytrain)


sl=float(input("Enter sepal length:"))
sw=float(input("Enter sepal width:"))
pl=float(input("Enter petal length:"))
pw=float(input("Enter petal width:"))

new = np.array([[sl, sw, pl, pw]])
prediction = KNNALGO.predict(new)
'''to check the prediction print("Prediction:",prediction)'''
print("Predicted species:",end =" ")
for i in iris_dataset['target_names'][prediction]:
	print(i)
