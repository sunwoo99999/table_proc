import pandas as pd

df = pd.read_csv('input.csv')

df.loc[100] = ['AVR', df['B'].mean(), df['C'].mean(), df['D'].mean(), df['E'].mean(), df['F'].mean()]
df.loc[101] = ['STD', df['B'].std(), df['C'].std(), df['D'].std(), df['E'].std(), df['F'].std()]
df.loc[102] = ['MIN', df['B'].min(), df['C'].min(), df['D'].min(), df['E'].min(), df['F'].min()]
df.loc[103] = ['MAX', df['B'].max(), df['C'].max(), df['D'].max(), df['E'].max(), df['F'].max()]
df.loc[104] = ['SUM', df['B'].sum(), df['C'].sum(), df['D'].sum(), df['E'].sum(), df['F'].sum()]

df.to_csv('output2.csv', index=False)

print(df.tail(10))
