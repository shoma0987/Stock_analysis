from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.set_option("display.max_columns",10)
pd.set_option("display.max_rows",1000)

start = "2019-08-01"
end = "2020-08-01"
df = data.DataReader("^N225","yahoo",start,end)

date = df.index
price = df["Adj Close"]
span01=5
span02=25
span03=50

df["sma01-5weeks"] = price.rolling(window=span01).mean()
df["sma02-25weeks"] = price.rolling(window=span02).mean()
df["sma0350weeks"] = price.rolling(window=span03).mean()

plt.figure(figsize=(30,10))
plt.plot(date,price,label = "Nikkei225")

plt.plot(date,df["sma01-5weeks"],label="sma01-5weeks")
plt.plot(date,df["sma02-25weeks"],label="sma02-25weeks")
plt.plot(date,df["sma0350weeks"],label="sma03-50weeks")
plt.xlabel("date",color="black",size=20)
plt.ylabel("price",color="black",size=20)

plt.legend()
plt.show()


