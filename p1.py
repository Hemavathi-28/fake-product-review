import numpy as np #importing the numpy module which we will be using in this project
import pandas as pd #importing the pandas module which will be used in this porject
import string#importing the pandas module which will be used in this porject
from sklearn.model_selection import train_test_split, GridSearchCV#importing the test_train_split module which will be used in this porject
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score #importing the classification report adn the confusion matrix module which will be used in this porject
import nltk#importing the nltk module which will be used in this porject
from nltk.corpus import stopwords#importing the nltk.corpus.stopwords module which will be used in this porject
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer#importing the extraction.text.CountVectorizer and TfidfTransformer module which will be used in this porject
from sklearn.pipeline import Pipeline#importing the sklearn.pipeline.Pipeline module which will be used in this porject
from sklearn.ensemble import RandomForestClassifier#importing the sklearn.ensemble.RandomForestClassifier module which will be used in this porject
from sklearn.svm import SVC#importing the sklearn.svm.SVC module which will be used in this porject
from sklearn.linear_model import LogisticRegression#importing the sklearn.linear_model.LogisticRegression module which will be used in this porject
dataframe = pd.read_csv('datasest.csv') #reading our dataset which contains text and a label whether it is fake or real
dataframe.head() #printing the first 5 column in our dataset
dataframe.drop('Unnamed: 0',axis=1,inplace=True)## dropping the unnecessary column 'UNAMED'
dataframe.head() #printing the dataset again after dropping the column
dataframe.dropna(inplace=True) #dropping alll the null rows in the dataset
dataframe['length'] = dataframe['text_'].apply(len) #storing the length of all the text into a separate column called 'length'

dataframe[dataframe['label']=='OR'][['text_','length']].sort_values(by='length',ascending=False).head().iloc[0].text_ ##so here we are just collecting the words which are most common in the fake reviews so that we can identify these wrods to detect for future text


def convertmyTxt(rv):  # here we are defining a function
    np = [c for c in rv if
          c not in string.punctuation]  # this function is checking if it is present in punctuation or not.
    np = ''.join(np)  # the character which are not in punctuation, we are storing them in a separate string
    return [w for w in np.split() if w.lower() not in stopwords.words(
        'english')]  # here we are returning a list of words from the sentences we just made in above line and checking if it is not a stopword


x_train, x_test, y_train, y_test = train_test_split(dataframe['text_'], dataframe['label'], test_size=0.25)
pip = Pipeline([
    ('bow',CountVectorizer(analyzer=convertmyTxt)),
    ('tfidf',TfidfTransformer()),
    ('classifier',RandomForestClassifier())
]) #here we are defining our Random Forest Classifier model in which we will pass the training and testing data
pip.fit(x_train,y_train) #here we are passing the testing and training data into Random Forest Classifier
randomForestClassifier = pip.predict(
    x_test)  # here we are predicting the accuracy of the Random Forest Classifier model
randomForestClassifier

print('Accuracy of the model: ', str(np.round(accuracy_score(y_test, randomForestClassifier) * 100,
                                              2)) + '%')  # here we are predicting the accuracy of the Random Forest Classifier model
pip = Pipeline([
    ('bow',CountVectorizer(analyzer=convertmyTxt)),
    ('tfidf',TfidfTransformer()),
    ('classifier',SVC())
])#here we are defining our Support Vector Classifier model in which we will pass the training and testing data
pip.fit(x_train,y_train)#here we are passing the testing and training data into Random Forest Classifier
supportVectorClassifier = pip.predict(x_test)#here we are predicting the accuracy of the Random Forest Classifier model
supportVectorClassifier
print('accuracy of the model:',str(np.round(accuracy_score(y_test,supportVectorClassifier)*100,2)) + '%')#here we are predicting the accuracy of the Random Forest Classifier model
pip = Pipeline([
    ('bow',CountVectorizer(analyzer=text_process)),
    ('tfidf',TfidfTransformer()),
    ('classifier',LogisticRegression())
])#here we are defining our Logistic Regression model in which we will pass the training and testing data
pip.fit(x_train,y_train)#here we are passing the testing and training data into Random Forest Classifier
logisticRegression = pip.predict(x_test)#here we are predicting the accuracy of the Random Forest Classifier model
logisticRegression
print('accuracy of the model:',str(np.round(accuracy_score(y_test,logisticRegression)*100,2)) + '%')#here we are predicting the accuracy of t
