
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
class classifiers:
    def naive_bayes(self,features_train,labels_train,features_test,labels_test):
        clf=GaussianNB()
        clf.fit(features_train,labels_train)
        pred=clf.predict(features_test)
        accuracy = accuracy_score(labels_test, pred)
        print(pred)
        print(accuracy)


    def svm(self,features_train,labels_train,features_test,labels_test):
         clf=svm.SVC(class_weight='balanced')
         clf.fit(features_train, labels_train)
         pred = clf.predict(features_test)
         accuracy = accuracy_score(labels_test,pred)
         print(pred)
         print(accuracy)

    def decision_tree(self,features_train,labels_train,features_test,labels_test):
        clf=DecisionTreeClassifier(random_state=0)
        clf.fit(features_train, labels_train)
        pred = clf.predict(features_test)
        print(pred)
        print(accuracy_score(labels_test,pred))
        print(cross_val_score(clf, features_test, labels_test,cv=10))