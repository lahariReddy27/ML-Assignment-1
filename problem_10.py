#The diagram below shows a dataset with 2 classes and 8 data points, each with only one feature value, labeled f.
#  Note that there are two data points with the same feature value of 6. These are shown as two x’s one above the other.
#1. Divide this data equally into two parts. Use first part as training and second part as testing.
#  Using KNN classifier, for K=3, what would be the predicted outputs for the test samples? Show how you arrived at your answer.
#2. Compute the confusion matrix for this and calculate accuracy, sensitivity and specificity values.


# dot - girl
# cross - boy

# 1 - girl
# 2 - boy
# 3 - boy
# 4 - nothing
# 5 - nothing
# 6 - boy
# 6 - boy
# 7 - girl
# 8 - nothing
# 9 - nothing
# 10 - girl
# 11 - girl
# 12 - nothing
# 13 - nothing


# assume each output class as boy or girl, say dot means girl, cross means boy
# The dataset that I decided from the diagram is on dataset variable defined below.
# lets seperate the features and outputs into 2 different arrays
# X = [[1], [2] ,[3], [6], [6], [7], [10], [11]] represents features for the given dataset
# y = [0, 1, 1, 1, 1, 0, 0, 0] represents classes for these features
# Then I applied a simple KNN algorithm
# Created the confusion matrix with the predicted values and ofc inbuilt methods
# Then I defined accuracy and specificity, sensitivity values as follows (inbuilt methods)

 

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics


dataset = [[1, 0], [2, 1], [3, 1], [6, 1], [6, 1], [7, 0], [10, 0], [11, 0]]
X = [[1], [2] ,[3], [6], [6], [7], [10], [11]]
y = [0, 1, 1, 1, 1, 0, 0, 0]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state=42)


# print(X_train)
# print(X_test)
# print(y_train)
# print(y_test)


knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
predicted = knn.predict(X_test)
confusion_matrix = metrics.confusion_matrix(y_test, predicted)

TP = confusion_matrix[0][0]
FP = confusion_matrix[0][1]
FN = confusion_matrix[1][0]
TN = confusion_matrix[1][1]



print(f'testing inputs: {X_test}')
print(f'predicted outputs: {predicted}')
print(f'confusion matrix: \n{confusion_matrix}')
print(f'accuracy: \n {metrics.accuracy_score(y_test, predicted)}')
# print(f'sensitivity: \n {TP/(TP + FN)}') # Getting 0 / 0
print(f'specificity: \n {TN/(TN + FN)}')