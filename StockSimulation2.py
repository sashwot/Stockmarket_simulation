import numpy as np
import pandas as ad
from pandas_datareder import data as wb
import matplotlib as mpl
import mathplotlib.pyplot as plt
from scipy.stats import norm

def get_simulation(ticker,name):
data=pd.DataFrame()
data[ticker]=wb.DataReader(ticker,data_source='yahoo',start='2020-1-1')['Adj Close']
log_return =np.log(1+data.pct_change())
u=log_return.mean()
var=log_return.var()

drift=u-(0.5*var)
stdev=log_returns.std()

t_intervals=365
iteration =10

daily_returns =np.exp(drift.value+ stdev.values*norm.ppf(np.random.rand(t_intervals,iterations))
S0=data.iloc[-1]
price_list=np.zeros_like(daily_returns)
price_list[0]=S0

for t in range(1,t_intervals):
price_list[t]=price_list[t-1]+daily_returns[t]

plt.figure(figsize=(10,6))
plt.title("1 year Monte Carlo Simulation"+name)
plt.ylabe("Price(P)")
plt.xlab("Time (Day)")
plt.plot(price_list)
plt.show()
get_simulation("MSFT","Microsoft Coperation")
