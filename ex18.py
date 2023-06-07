from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt


iris = datasets.load_iris()
print(iris)

answer = iris['target']
print(answer, end = '\n\n')

(X_train, X_test, y_train, y_test) = train_test_split(iris['data'], iris['target'], random_state=2023)

print(X_train)
print(X_train.shape)
print(X_test.shape)

knn:KNeighborsClassifier = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)

result = knn.predict(X_test)
print(result)
print(y_test)

scores = metrics.accuracy_score(y_test, result)
print(scores)

digits = datasets.load_digits()
plt.imshow(digits.images[0], cmap=plt.cm.gray_r, interpolation='nearest')