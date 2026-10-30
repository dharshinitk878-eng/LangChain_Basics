from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import pandas as pd

llm = ChatOllama(
    model="gemma3:1b",
    temperature=0.3
)

print("College Assistant Chatbot")
prompt = PromptTemplate(
    input_variables=["question"],
    template="You are a helpful college assistant. Answer this question in simple words: {question}"
)

chain = prompt | llm | StrOutputParser()