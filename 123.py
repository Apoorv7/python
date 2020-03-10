import pandas as pd

df = pd.read_csv(r'C:\Users\HP\Downloads\1.csv')
pd.set_option("display.max.columns",None)
pd.set_option("display.max.rows",None)

print(df['Industry_name_NZSIOC'])

