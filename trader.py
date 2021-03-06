# -*- coding: utf-8 -*-
"""datascience_hw2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y1c0AV8kn-3yWlMI78nveQrvdamk4-yr
"""

'''from google.colab import drive
import os
drive.mount('/content/drive')

os.chdir('/content/drive/MyDrive/資料競程/hw2') #切換該目錄
os.listdir() #確認目錄內容'''

# Commented out IPython magic to ensure Python compatibility.
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
from fbprophet import Prophet
from sklearn import metrics
from sklearn.metrics import mean_squared_error
from math import sqrt
from matplotlib import pyplot

# %matplotlib inline

def load_training_data(path):
    train_data = pd.read_csv(path,names=['open','high','low','close'])
    return train_data
def load_testing_data(path):
    test_data = pd.read_csv(path,names=['open','high','low','close'])
    return test_data
def plot_series(df=None, column=None, series=pd.Series([]), 
                label=None, ylabel=None, title=None, start=0, end=None):
    """
    Plots a certain time-series which has either been loaded in a dataframe
    and which constitutes one of its columns or it a custom pandas series 
    created by the user. The user can define either the 'df' and the 'column' 
    or the 'series' and additionally, can also define the 'label', the 
    'ylabel', the 'title', the 'start' and the 'end' of the plot.
    """
    sns.set()
    fig, ax = plt.subplots(figsize=(30, 12))
    ax.set_xlabel('Time', fontsize=16)
    if column:
        ax.plot(df[column][start:end], label=label)
        ax.set_ylabel(ylabel, fontsize=16)
    if series.any():
        ax.plot(series, label=label)
        ax.set_ylabel(ylabel, fontsize=16)
    if label:
        ax.legend(fontsize=16)
    if title:
        ax.set_title(title, fontsize=24)
    ax.grid(True)
    return ax

if __name__ == '__main__':
    # You should not modify this part.
    import argparse


    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                       default='training_data.csv',
                       help='input training data file name')
    parser.add_argument('--testing',
                        default='testing_data.csv',
                        help='input testing data file name')
    parser.add_argument('--output',
                        default='output.csv',
                        help='output file name')
    args = parser.parse_args()
    
    # The following part is an example.
    # You can modify it at will.
    #training_data = load_data(args.training)
    #trader = Trader()
    #trader.train(training_data)
    
    #testing_data = load_data(args.testing)
    training_data = load_training_data(args.training)
    testing_data = load_testing_data(args.testing)
    '''training_data = load_training_data("training.csv")
    testing_data = load_testing_data("testing.csv")'''
    from pandas.core.indexes.datetimes import date_range

    dr = pd.date_range('1/1/2015', periods=len(training_data['open']), freq='D')
    df = pd.Series(training_data['open'].to_numpy(),index=dr)
    df_train=df.to_frame(name='open')
    print(df_train)

    dr = pd.date_range('1/1/2015', periods=len(testing_data['open']), freq='D')
    df = pd.Series(testing_data['open'].to_numpy(),index=dr)
    df_test=df.to_frame(name='open')

    '''from pandas.core.indexes.datetimes import date_range
    test_data_size = len(testing_data['open'])

    training_data = pd.concat([training_data,testing_data])

    dr = pd.date_range('1/1/2015', periods=len(training_data['open']), freq='D')
    df = pd.Series(training_data['open'].to_numpy(),index=dr)
    df_train=df.to_frame(name='open')
    #print(df_train)

    dr = pd.date_range('1/1/2015', periods=len(testing_data['open']), freq='D')
    df = pd.Series(testing_data['open'].to_numpy(),index=dr)
    df_test=df.to_frame(name='open')
    df_train.tail(20)

    df_testing = df_train.iloc[len(df_train)-test_data_size:,:]'''

    ax = plot_series(df=df_train, column='open', ylabel='open',
                 title='open curve', end=len(training_data['open']))
    plt.show()

    '''def relative_strength_idx(df, n=14):
    open = df['open']
    delta = open.diff()
    delta = delta[1:]
    pricesUp = delta.copy()
    pricesDown = delta.copy()
    pricesUp[pricesUp < 0] = 0
    pricesDown[pricesDown > 0] = 0
    rollUp = pricesUp.rolling(n).mean()
    rollDown = pricesDown.abs().rolling(n).mean()
    rs = rollUp / rollDown
    rsi = 100.0 - (100.0 / (1.0 + rs))
    return rsi

    # SMA
    df_train['EMA_3'] = df_train['open'].ewm(3).mean()
    df_train['EMA_7'] = df_train['open'].ewm(7).mean()
    df_train['EMA_30'] = df_train['open'].ewm(30).mean()

    # EMA
    df_train['SMA_3'] = df_train['open'].rolling(3).mean().shift()
    df_train['SMA_7'] = df_train['open'].rolling(7).mean().shift()
    df_train['SMA_30'] = df_train['open'].rolling(30).mean().shift()

    # RSI
    df_train['RSI'] = relative_strength_idx(df_train).fillna(0)

    # MACD
    EMA_12 = pd.Series(df_train['open'].ewm(span=12, min_periods=12).mean())
    EMA_26 = pd.Series(df_train['open'].ewm(span=26, min_periods=26).mean())
    df_train['MACD'] = pd.Series(EMA_12 - EMA_26)
    df_train['MACD_signal'] = pd.Series(df_train.MACD.ewm(span=9, min_periods=9).mean())'''

    '''df_train['y'] = df_train['open'].shift(-1)
    #df_train['y'] = df_train['open']
    df_train = df_train.dropna(axis=0)'''

    '''new_df_train = df_train.iloc[:-test_data_size,:]
    df_valid = df_train.iloc[len(df_train)-test_data_size:,:]
    new_df_train'''

    '''new_df_train = new_df_train.reset_index()
    new_df_train.columns = ['date','open','EMA_3','EMA_7','EMA_30','SMA_3','SMA_7','SMA_30','RSI','MACD','MACD_signal','y']

    df_valid = df_valid.reset_index()
    df_valid.columns = ['date','open','EMA_3','EMA_7','EMA_30','SMA_3','SMA_7','SMA_30','RSI','MACD','MACD_signal','y']'''

    '''features = ['SMA_3','SMA_7','SMA_30','EMA_3','EMA_7','EMA_30','RSI','MACD','MACD_signal']

    model_fbp = Prophet()
    for feature in features:
        model_fbp.add_regressor(feature)

    model_fbp.fit(new_df_train[["date", "y"] + features].rename(columns={"date": "ds", "y": "y"}))
    forecast = model_fbp.predict(df_valid[["date", "y"] + features].rename(columns={"date": "ds"}))
    df_valid["Forecast_Prophet"] = forecast.yhat.values'''

    '''future = model_fbp.make_future_dataframe(periods=test_data_size)
    forecast = model_fbp.predict(df_valid[["date", "y"] + features].rename(columns={"date": "ds"}),future)'''

    '''from sklearn.metrics import mean_absolute_error, mean_squared_error
    import plotly.graph_objects as go

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_valid.date, y=df_valid.y, name='open'))
    fig.add_trace(go.Scatter(x=df_valid.date, y=df_valid.Forecast_Prophet, name='Forecast_Prophet'))
    fig.show()

    print("RMSE of Prophet:", np.sqrt(mean_squared_error(df_valid.y, df_valid.Forecast_Prophet)))
    print("MAE of Prophet:", mean_absolute_error(df_valid.y, df_valid.Forecast_Prophet))'''

    '''from sklearn.metrics import mean_absolute_error, mean_squared_error
    import plotly.graph_objects as go
    df_testing = df_testing.reset_index()
    fig = go.Figure()
    #fig.add_trace(go.Scatter(x=df_testing['index'], y=df_testing['open'], name='open'))
    fig.add_trace(go.Scatter(x=df_valid.date, y=df_valid.open, name='open'))
    fig.add_trace(go.Scatter(x=df_valid.date, y=df_valid.Forecast_Prophet, name='Forecast_Prophet'))
    fig.show()

    print("RMSE of Prophet:", np.sqrt(mean_squared_error(df_valid.y, df_valid.Forecast_Prophet)))
    print("MAE of Prophet:", mean_absolute_error(df_valid.y, df_valid.Forecast_Prophet))'''

    new_df_train = pd.DataFrame(df_train['open']).reset_index().rename(columns={'index':'ds', 'open':'y'})

    import pickle
    # 定義模型
    model = Prophet(daily_seasonality=True)

    # 訓練模型
    model.fit(new_df_train)

    #pickle.dump(model, open('model.h5', 'wb'))

    # 建構預測集
    future = model.make_future_dataframe(periods=len(testing_data)+1) #forecasting for 1 year from now.

    # 進行預測
    forecast = model.predict(future)

    #forecast.head()

    forecast.tail(len(testing_data)+1)

    figure=model.plot(forecast)

    '''ax = plot_series(df=df_test, column='open', ylabel='open',
                     title='open curve', end=len(training_data['open']))
    plt.show()'''

    output = pd.DataFrame(columns=['ds','yhat'])
    output = forecast[['ds','yhat']].tail((len(testing_data)+1))
    output.columns = ['date','open']
    #print(output)
    output = output.set_index('date')
    ax = plot_series(df=output, column='open', ylabel='open',
                    title='open curve', end=len(training_data['open']))
    plt.show()

    plt.figure(figsize = (8, 6))
    plt.plot(output['open'].values, color = 'blue')
    plt.plot(df_test['open'].values, color = 'red')

    df_test['strategy'] = 0
    for i in range(2, output.shape[0]):
        if output.iloc[i, 0] >= output.iloc[i - 1, 0]:
            df_test.iloc[i - 2, 1] = 1
        else:
            df_test.iloc[i - 2 , 1] = -1
    #output['strategy'] = output['strategy'].shift(-1)
    df_test.iloc[output.shape[0]-2, 1] = 0


    #strategy = output['strategy'].values

    #df_test['strategy'] = strategy
    plt.figure(figsize = (15, 9))
    plt.plot(df_test['open'], color = 'blue')
    plt.scatter(df_test[df_test['strategy'] == 1].index ,df_test[df_test['strategy'] == 1]['open'].values, marker = '^')
    plt.scatter(df_test[df_test['strategy'] == -1].index ,df_test[df_test['strategy'] == -1]['open'].values, marker = 'v')

    strategy = df_test['strategy'].squeeze()
    output_strategy = []
    unit = 0
    for i in range(0,len(strategy)):
        if strategy[i] == 1:
            if unit==0 or unit==-1:
                unit = unit + 1
                output_strategy.append(1)
            else:
                output_strategy.append(0)
        if strategy[i] == -1:
            if unit==1 or unit==0:
                unit = unit - 1
                output_strategy.append(-1)
            else:
                output_strategy.append(0)
      #output_strategy.append(0)
    #print(output_strategy)
    pd_output = pd.DataFrame(data=output_strategy)
    pd_output.to_csv('output.csv',index=False)

    open = testing_data["open"].squeeze()
    the_last_day_close = testing_data.at[len(testing_data)-1,"close"]
    unit = 0
    profit = 0
    for i in range(0,len(output_strategy)):
        if output_strategy[i] == 1:
            if unit==0 or unit==-1:
                unit = unit + 1
                profit = profit - open[i+1]
        if output_strategy[i] == -1:
            if unit==1 or unit==0:
                unit = unit - 1
                profit = profit + open[i+1]
        else:
            continue
    if unit!=0:
        if unit == 1:
            unit = unit-1
            profit = profit + the_last_day_close
        if unit == -1:
            unit = unit+1
            profit = profit - the_last_day_close
    #print(profit)

# You can write code above the if-main block.