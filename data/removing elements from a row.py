import pandas as pd

df=pd.read_csv('E:/data/BA_reviews.csv')
'''
list=[]
cv= df['reviews']
split=cv[0].split('|')
#print(split[1])

'''

for i in range(0,1000):
    row = df.loc[i]  
    split= row.str.split('|')
    output=split.str[1]
    
    print(output)
   
    print("--------------------------------------")
    
    
    
    
