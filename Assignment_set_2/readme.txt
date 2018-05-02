Assignment2 program files:
---------------------------
* main.py: project execution starts here, calls functions in other files.
* preprocessing.py: preprocessing of the dataset is done in this file.
* classifier.py: different classifiers and performance measures are coded.

Dataset:
---------
The dataset folder contains train.csv file, which is used for training, testing and validating.
The file contains the subset of original train.csv, with over 40k instances.

project flow:
--------------
1. The project starts at main, which calls 'preprocess' function in 'preprocessing.py'.
2. The datset is read using pandas.
3. Rows with missing values are eliminated.
4. Target data is separated.
5. ID column is droppped.
6. Other columns are formatted using 'ormat_columns' function.
    6.1 'format_broswer' function finds aliases in browser classes like, 'MOzilla' and 'Firefox' and gives a
    common class name.
    6.2  'decompose_datetime' function separates the 'time' and 'date' from 'datetime' and gives divisions like
    'morning','afternoon','evening' for time and 'month_first_half' and 'month_second_half' for date.
7. 'One hot encoding' is done on all categorical data.
8. Important features are found out by using 'ExtraTreesClassifier.feature_importances_'.
9. Unimportant columns are deleted.
10. Training data is divided into train and test in 70:30 ratio.
11. Training data is again divided into train and validate in 80:20 ratio.
12. Dataset is trained using 'Naive Bayes', 'svm' and 'Decision Tree' models.
13. The data imbalance is handled by applying weight='balanced' for svm and using skew insensitive models like naive bayes and Decision tree.
14. Performance measures are calculated with validation data.
15. Accuracy of test set is found.