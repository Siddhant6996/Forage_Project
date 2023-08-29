'''import pandas as pd

df=pd.read_csv('E:/data/BA_reviews.csv')


for i in range(0,1000):
    row = df.loc[i]  
    split= row.str.split('|')
    output=split.str[1]
    
    print(output)
    
    print("--------------------------------------")
    
'''
import pandas as pd

df = pd.read_csv('E:/data/BA_reviews.csv')

output_data=[]
for i in range(0, min(1000, len(df))):
    row = df.iloc[i]  # Use iloc instead of loc
    split = row['reviews'].split('|')  # Replace 'column_name' with the actual column name containing the '|' separated values
    output = split[1] if len(split) > 1 else ''  # Extract the second element from split, handling missing values
    output_data.append(output)
    
    # Create a new DataFrame with the extracted data
    new_df = pd.DataFrame({'Extracted Column': output_data})

    # Save the new DataFrame to a CSV file
    new_df.to_csv('E:/data/extracted_data.csv', index=False)
    print(output_data)
