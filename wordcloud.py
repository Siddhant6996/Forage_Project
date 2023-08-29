import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import  WordCloud 


# Read the CSV file
df = pd.read_csv('E:\data\extracted_data.csv')

# Concatenate the text from all rows
text = ' '.join(df['Extracted Column'])  # Replace 'text_column' with the actual column name containing the text data

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400).generate(text)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
