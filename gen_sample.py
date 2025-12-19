import pandas as pd
import numpy as np

np.random.seed(42)  
data = {
    'A': range(1, 101),  
    'B': np.random.uniform(0, 100.0, 100), 
    'C': np.random.uniform(0, 100.0, 100),
    'D': np.random.uniform(0, 100.0, 100),
    'E': np.random.uniform(0, 100.0, 100),
    'F': np.random.uniform(0, 100.0, 100)
}

df = pd.DataFrame(data)

df.to_csv('input.csv', index=False, encoding='utf-8-sig')

print("파일이 'input.csv'로 저장되었습니다.")
print(df.head()) 