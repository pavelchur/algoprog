import pandas as pd
df = pd.read_csv('StudentsPerformance .csv')
print(df.info())
print(df.head())
def degree(lvl):
    l = lvl.split(' ')
    return l[-1]
df['parental level of education'] = df['parental level of education'].apply(degree)
print(df['parental level of education'])
df['overall score'] = df['math score']+df['reading score']+df['writing score']
print(df.head())
pf = df.pivot_table(
    values='overall score',
    index='test preparation course',
    columns='parental level of education',
    aggfunc='median'
)
print(pf)
#not changing