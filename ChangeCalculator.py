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
