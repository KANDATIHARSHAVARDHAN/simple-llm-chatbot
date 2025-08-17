import getpass
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

#Now we instantiate our model object and generate chat completions:
llm=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    max_tokens=None,
    max_retries=2,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a chatbot"),
        ("human","Question:{question}")
    ]
)

st.title('Langchain Demo with Gemini')
input_text=st.text_input("Enter your question here")

output_parser=StrOutputParser()

chain=prompt|llm|output_parser## chain-means the processing step by step manner-means first prompt,then llm,then output parser 

if input_text:
    st.write(chain.invoke({'question':input_text}))

#to run this code,write- streamlit run gemini_app.py