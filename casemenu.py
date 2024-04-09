import pandas as pd
df = pd.read_csv('menu.csv')
print(df.info())
print(df.head())
df = df[('atte' not in df['Item'])&('appucino' not in df['Item'])&('Tea' not in df['Item'])&('Sprite' not in df['Item'])&('epper' not in df['Item'])&('Milk' not in df['Item'])&('Coke' not in df['Item'])&('Cola' not in df['Item'])('Fanta' not in df['Item'])]
def size(s):
    return float(s.split(' ')[0])*28.35
df['Serving Size'] = df['Serving Size'].apply(size)
breakfast = df[(df['Calories']*df['Serving Size']/100 <= 550)]['Item'].tolist
lunch = df[df['Calories']*df['Serving Size']/100 <= 700]['Item'].tolist
dinner = df[df['Calories']*df['Serving Size']/100 <= 500]['Item'].tolist
print(breakfast,lunch,dinner)
#not changing