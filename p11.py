import pandas as pd
import nltk
import streamlit as st
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

def get_wordnet_pos(treebank_tag):
    """Convert POS tag from nltk to WordNet format."""
    if treebank_tag.startswith('J'):
        return nltk.corpus.wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return nltk.corpus.wordnet.VERB
    elif treebank_tag.startswith('N'):
        return nltk.corpus.wordnet.NOUN
    # elif treebank_tag.startswith('R')
        return nltk.corpus.wordnet.ADV
    else:
        return nltk.corpus.wordnet.NOUN  # Default to noun

def preprocess_question(question):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(question)
    tokens = [word.lower() for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stop_words]
    pos_tags = pos_tag(tokens)
    lemmatized_tokens = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in pos_tags]
    return "-".join(lemmatized_tokens)

# Load data from CSV
csv_file_path = "git_github_qa_dataset.csv"  # Replace with your CSV file path

try:
    df = pd.read_csv(csv_file_path)
    # Ensure correct column names
    if 'Question' not in df.columns or 'Answer' not in df.columns:
        raise ValueError("CSV file must have 'Question' and 'Answer' columns.")

    # Preprocess questions and create a dictionary
    processed_qa_data = {preprocess_question(str(q)): a for q, a in zip(df['Question'], df['Answer'])}
except FileNotFoundError:
    st.error(f"Error: File '{csv_file_path}' not found. Please ensure the file exists.")
    processed_qa_data = {}  # Empty dictionary if file not found
except ValueError as e:
    st.error(f"Error: {e}")
    processed_qa_data = {}

# Streamlit App
st.title("Git&GithubDetails Question Answering System")

user_input = st.text_input("Enter your question:")

if st.button("Submit"):
    if user_input:
        processed_input = preprocess_question(user_input)
        answer = processed_qa_data.get(processed_input, "Sorry, I don't have an answer for that question.")
        st.write("Your Question:")
        st.write(user_input)
        st.write("Answer:")
        st.write(answer)
    else:
        st.warning("Please enter a question.")