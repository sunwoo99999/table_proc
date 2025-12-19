import pandas as pd

pd.read_csv('input.csv').to_csv('output.csv', index=False)

# Read all rows from csv file and save to output.csv
df = pd.read_csv('input.csv')
df.to_csv('output.csv', index=False)


# Calculate average value for all columns B
avr_value_B = df['B'].mean()
avr_value_C = df['C'].mean()
avr_value_D = df['D'].mean()
avr_value_E = df['E'].mean()
avr_value_F = df['F'].mean()

# Create a new row named 'average' after row 100
df.loc['average'] = ['AVR', avr_value_B, avr_value_C, avr_value_D, avr_value_E, avr_value_F]
df.to_csv('output.csv', index=False)

# Print all rows with columns A, B, C, D, E, F
print(df.loc[:, ['A', 'B', 'C', 'D', 'E', 'F']])

# Save only the printed columns to output.csv
df.loc[:, ['A', 'B', 'C', 'D', 'E', 'F']].to_csv('output.csv', index=False)

# Calculate standard deviation for all columns B
std_value_B = df['B'].std()
std_value_C = df['C'].std()
std_value_D = df['D'].std()
std_value_E = df['E'].std()
std_value_F = df['F'].std()
# Create a new row named 'std_dev' after the average row
df.loc['std_dev'] = ['STD', std_value_B, std_value_C, std_value_D, std_value_E, std_value_F]
df.to_csv('output.csv', index=False)
# Print all rows with columns A, B, C, D, E, F
print(df.loc[:, ['A', 'B', 'C', 'D', 'E', 'F']])
# Save only the printed columns to output.csv
df.loc[:, ['A', 'B', 'C', 'D', 'E', 'F']].to_csv('output.csv', index=False)


# Calculate maximum value for all columns B
max_value_B = df['B'].max()
max_value_C = df['C'].max()
max_value_D = df['D'].max()
max_value_E = df['E'].max()
max_value_F = df['F'].max()
# Create a new row named 'max_value' after the std_dev row
df.loc['max_value'] = ['MAX', max_value_B, max_value_C, max_value_D, max_value_E, max_value_F]
df.to_csv('output.csv', index=False)
# Print all rows with columns A, B, C, D, E, F including average, std_dev, max_value rows
print(df.loc[:, ['A', 'B', 'C', 'D', 'E', 'F']])
# Save only the printed columns to output.csv
df.loc[:, ['A', 'B', 'C', 'D', 'E', 'F']].to_csv('output.csv', index=False)
# Calculate minimum value for all columns B
min_value_B = df['B'].min()
min_value_C = df['C'].min()
min_value_D = df['D'].min()
min_value_E = df['E'].min()
min_value_F = df['F'].min()
# Create a new row named 'min_value' after the max_value row
df.loc['min_value'] = ['MIN', min_value_B, min_value_C, min_value_D, min_value_E, min_value_F]
df.to_csv('output.csv', index=False)
# Print all rows with columns A, B, C, D, E, F
print(df.loc[:, ['A', 'B', 'C', 'D', 'E', 'F']])
# Save only the printed columns to output.csv
df.loc[[0, 1, 2, 3, 4, 'average', 'std_dev', 'max_value', 'min_value'], ['A', 'B', 'C', 'D', 'E', 'F']].to_csv('output.csv', index=False)

# Calculate sum for all columns B
sum_value_B = df['B'].sum()
sum_value_C = df['C'].sum()
sum_value_D = df['D'].sum()
sum_value_E = df['E'].sum()
sum_value_F = df['F'].sum()
# Create a new row named 'sum_value' after the min_value row
df.loc['sum_value'] = ['SUM', sum_value_B, sum_value_C, sum_value_D, sum_value_E, sum_value_F]
df.to_csv('output.csv', index=False)
# Print all rows with columns A, B, C, D, E, F including average, std_dev, max_value, min_value, sum_value rows
print(df.loc[:, ['A', 'B', 'C', 'D', 'E', 'F']])
# Save only the printed columns to output.csv
df.loc[:, ['A', 'B', 'C', 'D', 'E', 'F']].to_csv('output.csv', index=False)

# Create columns AVR, STD, MAX, MIN, SUM in rows 101, 102, 103, 104, 105 and assign values
df.loc[:, 'AVR'] = df.loc['average']
df.loc[:, 'STD'] = df.loc['std_dev']
df.loc[:, 'MAX'] = df.loc['max_value']
df.loc[:, 'MIN'] = df.loc['min_value']
df.loc[:, 'SUM'] = df.loc['sum_value']


df.to_csv('output.csv', index=False)
