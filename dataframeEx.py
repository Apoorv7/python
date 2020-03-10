#pip install pandas
import pandas as pd

df = pd.read_csv(r'C:\Users\vkumar15\Desktop\backup\Health data.csv')
'''
#print(df)
print(df.columns)
print(df.shape)

print(df.head(n=4)) #top 4 rows

print(df.tail(10))

print(df['AGE'])

print(df[4:10])

##sorting
print(df.sort_values('AGE',ascending=True))

##group by
print(df.groupby('AGE').size())
print(df.groupby('AGE').sum())
print(df.groupby('AGE').sum()['CODING_EXTRACT_ID'])
print(df.groupby('AGE').max())
print(df.groupby('AGE').min())

'''
####
data = df.values
for r in data:
     for c in r:
          print (c)







