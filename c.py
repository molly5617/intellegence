import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline


from sklearn import preprocessing, tree
#from sklearn.cross_validation import train_test_split #舊版
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
clf = tree.DecisionTreeClassifier(random_state=0)

ordering = pd.read_csv("order_train.csv")
#Age中有NaN資料
ordering["alt"].replace(['No','Yes'],[0,1],inplace=True)
ordering["bar"].replace(['No','Yes'],[0,1],inplace=True)
ordering["fri"].replace(['No','Yes'],[0,1],inplace=True)
ordering["hun"].replace(['No','Yes'],[0,1],inplace=True)
ordering["pat"].replace(['none','some','full'],[0,1,2],inplace=True)
ordering["price"].replace(['$','$$','$$$'],[0,1,2],inplace=True)
ordering["rain"].replace(['No','Yes'],[0,1],inplace=True)
ordering["res"].replace(['No','Yes'],[0,1],inplace=True)
ordering["type"].replace(['french','thai','burger','italian'],[0,1,2,3],inplace=True)
ordering["est"].replace(['0-10','10-30','30-60','>60'],[0,1,2,3],inplace=True)


y=pd.DataFrame(ordering["willWait"])
ordering.drop('willWait',inplace=True,axis=1)
X=pd.DataFrame(ordering)

print(y)

Xtrain, XTest, yTrain, yTest = \
train_test_split(X, y, test_size=1, random_state=1)
dtree =tree.DecisionTreeClassifier()
dtree.fit(Xtrain, yTrain)
print("準確率 :", dtree.score(XTest, yTest))
preds= dtree.predict_proba(X=XTest)
print(pd.crosstab(preds[:,0], columns=[X["bar"],XTest["hun"]]))

preds= dtree.predict_proba(X=XTest)
print(pd.crosstab(preds[:,0], columns=[X["bar"],XTest["hun"]]))

plt.figure()
plot_tree(dtree, filled=True)
plt.show()
