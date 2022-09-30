import datetime
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
sns.set_style('darkgrid')
sns.set_palette("RdBu")
df = pd.read_csv('Suicides.csv')
df.rename({'sex':'gender' , 'suicides_no':'suicides'} , inplace = True , axis = 1)
plt.figure(figsize=(14,9))
g = sns.relplot(x='year', y='suicides' ,data=df, ci=None, col='gender', kind = "line",)
g.fig.suptitle('Suicides tendensy across the world from 2000', x=0.53)
fig, ax = plt.subplots()
population = df.groupby(['country']).population.max()
df = df.groupby(['country']).suicides.agg(['sum', lambda x: x.sum()>25000]).sort_values(by ="sum")
df['num'] = df['sum']
df = df[df.num > 25000]
ax.bar(df.index, df["sum"])
ax.set_xticklabels(df.index, rotation = 90)
ax.legend()
print(df)
plt.show()