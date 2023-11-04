import pandas as pd

data_info = {'first': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
             'second': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(data_info)
# To add new column third
df['third'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(df)
# To add new column fourth
df['fourth'] = df['first'] + df['third']
print(df)