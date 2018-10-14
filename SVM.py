# 将提取出的基因数据整理到一起
from sklearn import preprocessing
from sklearn import cross_validation, svm
import pandas as pd
from sklearn.metrics import precision_recall_fscore_support
from matplotlib import pyplot as plt
import random

# 读出分级基因数据
data = pd.read_csv('DataAfterProFive.csv', index_col='Keys')
# 读出筛选出的基因
gene_name = pd.read_csv('featureFive.csv').Name.values

data = data[gene_name]
target = pd.read_csv('newCombine.csv').Five.values
# data.to_csv('Step 2.csv')
print(target)

X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(data, target, test_size=0.2, random_state=0)
columns = X_train.columns.values

print(columns)

# -----------------------
# SVM
# -----------------------
X = range(1, 300)
Y1 = []
Y2 = []
Y3 = []
for i in range(1, 300):
    t = columns[0: i]
    X1 = X_train[t]
    X2 = X_test[t]
    print(X1.shape)
# 对数据进行归一化
    scale = preprocessing.StandardScaler().fit(X1)
    X1 = scale.transform(X1)
    X2 = scale.transform(X2)
    clf = svm.SVC()

    print(i)
    print(clf.fit(X1, Y_train).score(X2, Y_test))
    Y1.append(clf.fit(X1, Y_train).score(X2, Y_test))
    y_true = Y_test
    y_pred = clf.predict(X2)
    # print(y_true)
    # print(y_pred)
    # real = pd.Series(y_true)
    # pre = pd.Series(y_pred)
    # real.to_csv('112233.csv')
    # pre.to_csv('223344.csv')
    list = []
    list.append(precision_recall_fscore_support(y_true=y_true, y_pred=y_pred, average='macro'))
    print(list)
    Y2.append(list[0][0])
    Y3.append(list[0][1])

plt.plot(X, Y1, label='Accuracy')
plt.plot(X, Y2, label='Precision')
plt.plot(X, Y3, label='Recall')
APR = pd.DataFrame([Y1, Y2, Y3], index=['Accuracy', 'Precision', 'Recall'], columns=X)
APR = APR.T
APR.to_csv('HGG_Five_APR.CSV')
plt.legend()
plt.show()
