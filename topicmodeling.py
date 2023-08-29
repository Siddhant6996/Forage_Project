import pandas as pd
import gensim
from gensim import corpora
from gensim.models import LdaModel

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('E:\data\extracted_data.csv')

# Preprocess the text data
# Modify the preprocessing steps based on your requirements
df['preprocessed_text'] = df['Extracted Column'].apply(lambda x: x.split())  # Tokenization

# Create a dictionary from the preprocessed documents
dictionary = corpora.Dictionary(df['preprocessed_text'])

# Create a corpus (bag of words representation) from the dictionary
corpus = [dictionary.doc2bow(doc) for doc in df['preprocessed_text']]

# Build the LDA model
num_topics = 5  # Specify the number of topics to discover
lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=10)

# Assign topics to the documents in the corpus
df['topic'] = [lda_model.get_document_topics(doc) for doc in corpus]

# Create a new DataFrame for the topic modeling results
topic_modeling_results = pd.DataFrame(columns=['Document', 'Topic'])

# Populate the DataFrame with the document and topic data
for idx, row in df.iterrows():
    document = row['Extracted Column']  # Assuming 'text' is the column name containing the text data
    topic_distribution = row['topic']
    sorted_topics = sorted(topic_distribution, key=lambda x: x[1], reverse=True)
    top_topic = sorted_topics[0][0]

    topic_modeling_results = pd.concat([topic_modeling_results, pd.DataFrame({
        'Document': [document],
        'Topic': [top_topic]
    })], ignore_index=True)

# Save the topic modeling results to a new CSV file
topic_modeling_results.to_csv('E:/data/topic_modeling_results.csv', index=False)



     
