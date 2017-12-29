import nltk
import os

# Downloading necessary NLTK datasets
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

# creating directory for storing chat logs
if not os.path.exists("logs"):
    os.makedirs("logs")