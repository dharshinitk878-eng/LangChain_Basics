
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import pandas as pd
import os

# Connect to Ollama model
llm = ChatOllama(
    model="gemma3:1b",
    temperature=0.3
)

# Five prompt templates
prompts = {
    "College Information": "You are a helpful college assistant. Explain in simple words: {question}",
    "Admission": "You are an admission assistant. Explain the admission process: {question}",
    "Library": "You are a library assistant. Answer library questions: {question}",
    "Examination": "You are an exam assistant. Explain exam details: {question}",
    "Courses": "You are a course assistant. Explain course details: {question}"
}

# Select prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template=prompts["College Information"]
)

# Create LangChain
chain = prompt | llm | StrOutputParser()

# Additional chain 1: Summarization
summary_prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in simple words: {text}"
)

summary_chain = summary_prompt | llm | StrOutputParser()

# Additional chain 2: Question Answering
qa_prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer the following question clearly and simply: {question}"
)

qa_chain = qa_prompt | llm | StrOutputParser()

# Create dataset folder if missing
os.makedirs("dataset", exist_ok=True)

# Start chatbot
print("\n===== COLLEGE ASSISTANT CHATBOT =====")
print("Type 'exit' to stop the chatbot.")

while True:
    question = input("\nEnter your college question: ")

    if question.lower() == "exit":
        print("Thank you for using College Assistant!")
        break

    # Generate response
    response = chain.invoke({"question": question})

    print("\nChatbot:", response)

    # Save query and response
    file_path = "dataset/chatbot_responses.csv"

    data = pd.DataFrame(
        [[question, response]],
        columns=["query", "response"]
    )

    data.to_csv(
        file_path,
        mode="a",
        header=not os.path.exists(file_path),
        index=False
    )

    print("Response saved successfully!")
