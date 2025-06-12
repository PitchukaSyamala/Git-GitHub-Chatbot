# Git-GitHub-Chatbot
Chatbot-for-Git-GithubDetails
A Streamlit app that answers common Git and GitHub questions using a pre-loaded dataset. 
# Project Explanation: 
The Git & GitHub Chatbot is an AI-powered assistant designed to provide instant answers to frequently asked questions about Git and GitHub. Built using NLTK for Natural Language Processing and Streamlit for a web-based interface, this chatbot serves as a friendly guide for new users and beginners, helping them quickly grasp important commands, concepts, and workflows in Git and GitHub—without the need to sift through long and complex documentation. Whether you're just starting out with version control or trying to remember a specific Git command, this chatbot is here to support your learning journey.

Features: 
   * ✅ Answers common questions related to Git and GitHub. 
   *  ✅ Uses NLTK for text preprocessing (tokenization, stopword removal, lemmatization, POS tagging) . 
   * ✅ Employs a CSV-based Q&A dataset to handle dynamic queries. 
   * ✅ Built with Streamlit for a smooth and responsive UI.
   * ✅ Easily extendable by updating the dataset.

Requirements to Run the Project: 
  * Python 3.x . 
  * Required Libraries: pip install streamlit pandas nltk .
  * NLTK Downloads: The following NLTK resources are downloaded during runtime: punkt o stopwords o wordnet averaged_perceptron_tagger

How to Run the Project:
   * Step 1: Place your CSV Dataset Ensure your git_github_qa_dataset.csv is in the same folder as your Python script. It must contain two columns: Question and               Answer. 
   * Step 2: Run the Chatbot streamlit run app.py 
   * Step 3: Interact with the Chatbot Once launched in your browser: 
      • Enter a question about Git/GitHub in the textbox . 
      • Get a relevant answer based on the dataset .

How It Works:

  User Input is taken via a text field.
  The question is preprocessed using: o Tokenization o Lowercasing o Alphanumeric filtering o Stopword removal o Lemmatization based on POS tagging
  The processed question is compared with processed versions of questions in the dataset.
  If a match is found, the corresponding answer is returned.
