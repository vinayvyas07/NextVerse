
import streamlit as st
from transformers import pipeline, set_seed
from utils.feedback import save_feedback

# Custom CSS styling
st.markdown("""
    <style>
        .main { background-color: #f5f5f5; }
        h1 { color: #4B8BBE; text-align: center; }
        .stTextInput>div>div>input { background-color: #ffffff; }
    </style>
""", unsafe_allow_html=True)

st.title("NextVerse: Next Sentence Prediction using Generative AI")
st.write("Enter a sentence and view predicted next sentences.")

generator = pipeline("text-generation", model="gpt2")
set_seed(42)

input_text = st.text_input("Enter your sentence:")

if input_text:
    st.subheader("Generated Next Sentences:")
    outputs = generator(input_text, max_length=50, num_return_sequences=3)
    for i, output in enumerate(outputs):
        st.write(f"{i+1}. {output['generated_text']}")
        rating = st.slider(f"Rate Sentence {i+1}", 1, 5, 3, key=f"rating_{i}")
        save_feedback(input_text, output['generated_text'], rating)
