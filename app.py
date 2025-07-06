import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
import sklearn


tfidf=pickle.load(open("vectorizer.pk1","rb"))

import string
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:

        if i.isalnum():
            y.append(i)
            text = y[:]
            y.clear()
            for i in text:
                i = str(i)  # make sure it's a string
                if i not in stopwords.words("english") and i not in string.punctuation:
                    y.append(i)
            text = y[:]
            y.clear()
            for i in text:
                a = ps.stem(i)
                y.append(a)

    return " ".join(y)
model=pickle.load(open("model.pk1","rb"))
st.title("Email/SMS Spam Classifier")
input_sms=st.text_area("Enter the message")
if st.button("Predict"):#preprocess
 transform_sms=transform_text(input_sms)

# vectorize
 vector_input=tfidf.transform([transform_sms])
#predict
 prediction=model.predict(vector_input)
#display
 if prediction==1:
    st.header("Spam")
 else:
    st.header("Not Spam")