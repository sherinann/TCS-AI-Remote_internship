
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
class classifiers:
    #naive bayes training, prediction, accuracy

    def performance_measures(self,clf,labels_test,pred,features_test):
        cm = confusion_matrix(y_true=labels_test, y_pred=pred)
        print('confusion matrix:')
        print(cm)
        print('cross validation score')
        print(cross_val_score(clf, features_test, labels_test, cv=10))
        print('precision, recall, fscore, support')
        print(precision_recall_fscore_support(labels_test, pred))

    def naive_bayes(self,features_train,labels_train,features_test,labels_test,flag,labels):
        clf=GaussianNB()
        clf.fit(features_train, labels_train)
        pred = clf.predict(features_test)
        accuracy = accuracy_score(labels_test, pred)
        print('naive bayes accuracy :', accuracy)
        if flag == 1:
            self.performance_measures(clf,labels_test,pred,features_test)

    # svm training, prediction, accuracy
    def svm(self,features_train,labels_train,features_test,labels_test,flag,labels):
        clf=svm.SVC(class_weight='balanced')
        clf.fit(features_train, labels_train)
        pred = clf.predict(features_test)
        accuracy = accuracy_score(labels_test,pred)
        print('svm accuracy',accuracy)
        if flag == 1:
            self.performance_measures(clf, labels_test, pred, features_test)

    # decision tree training, prediction, accuracy
    def decision_tree(self,features_train,labels_train,features_test,labels_test,flag,labels):
        clf=DecisionTreeClassifier(random_state=0)
        clf.fit(features_train, labels_train)
        pred = clf.predict(features_test)
        print('decision tree accuracy',accuracy_score(labels_test,pred))
        if flag==1:
            self.performance_measures(clf, labels_test, pred, features_test)

