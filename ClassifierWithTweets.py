import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

Stock_Data = pd.read_csv('..\\faangStockTweets\\netflix.csv',usecols=['Stock_Date','open','high',
                                                  'low', 'close','volume','Positive','Negative','Total','Tweet_Date'])
def amount_change (row):
    '''
    if ((row['close'] - row['open'])/row['open']) > .025:
        return 2
    if ((row['close'] - row['open'])/row['open']) > .005:
        return 1
    if ((row['close'] - row['open'])/row['open']) > -.005:
        return 0
    if ((row['close'] - row['open'])/row['open']) > -.025:
        return -1
    if ((row['close'] - row['open'])/row['open']) < -.025:
        return -2
    '''
    if ((row['close'] - row['open'])/row['open']) > 0:
        return 1
    if ((row['close'] - row['open'])/row['open']) <= 0:
        return 0

Stock_Data['change'] = Stock_Data.apply(lambda row: amount_change (row),axis=1)

Stock_Data.to_csv(r'FinalNE1.csv',index=None,header=True)





'''
Stock_Prediction = pd.read_csv('FinalAM.csv')
Stock_Prediction = pd.DataFrame(Stock_Prediction).head(30)
print(Stock_Prediction)

X = Stock_Prediction.drop(['date','change'],axis=1)
y = Stock_Prediction['change']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15,random_state=109)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators = 4, criterion = 'entropy', random_state = 42)
model.fit(X_train,y_train)
print(model.score(X_train,y_train))
y_pred = model.predict(X_test)

print("Accuracy: ",metrics.accuracy_score(y_test,y_pred))
metrics.confusion_matrix(y_test,y_pred)
'''
