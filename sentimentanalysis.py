import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('E:\data\extracted_data.csv')

# Check if the specified column name exists in the DataFrame
if 'Extracted Column' not in df.columns:
    raise KeyError("Specified column name 'Extracted Column' not found in the CSV file.")

# Initialize the Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

# Create an empty list to store sentiment data
sentiment_data = []

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    text = row['Extracted Column']  # Replace 'Your_Column_Name' with the actual column name
    
    try:
        # Perform sentiment analysis on the text
        sentiment_scores = sia.polarity_scores(text)
        compound_score = sentiment_scores['compound']

        # Classify the text as positive, negative, or neutral based on the compound score
        if compound_score > 0.05:
            sentiment_data.append(('positive', text))
        elif compound_score < -0.05:
            sentiment_data.append(('negative', text))
        else:
            sentiment_data.append(('neutral', text))
    except Exception as e:
        print(f"Error processing row {index}: {e}")
        continue

# Create a new DataFrame for the extracted data
output_df = pd.DataFrame(sentiment_data, columns=['Sentiment', 'Text'])

# Save the DataFrame to a new CSV file
output_df.to_csv('E:/data/sentiment_output.csv', index=False)


# E:\data\extracted_data.csv    Extracted Column