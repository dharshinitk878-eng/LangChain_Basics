# Week 10 – LangChain Basics

## Project Title
College Assistant Chatbot Using LangChain and Ollama

## 1. Introduction
This project develops a College Assistant Chatbot using LangChain and a locally running Gemma model through Ollama.

The chatbot answers college-related questions in simple words. It helps students get information about college, admissions, library services, examinations, and courses.

## 2. Technologies Used
- Python
- LangChain
- Ollama
- Gemma 3:1b
- Pandas
- VS Code

## 3. Project Features
1. College information chatbot.
2. Five different prompt templates.
3. Dynamic user input.
4. Integration with local Ollama.
5. LLM chain implementation.
6. Summarization chain.
7. Question-answering chain.
8. Saving questions and responses in CSV files.
9. Displaying chatbot responses in the terminal.

## 4. Prompt Templates
The project uses five prompt templates:

- College Information
- Admission
- Library
- Examination
- Courses

These templates help the chatbot answer different types of college-related questions.

## 5. Additional Chains
### Summarization Chain
Summarizes the given text in simple words.

### Question Answering Chain
Answers user questions clearly and simply.

## 6. Dataset
The dataset folder contains:

- prompts.csv
- user_queries.csv
- chatbot_responses.csv
- chain_results.csv

The chatbot saves user questions and generated responses in chatbot_responses.csv.

## 7. How to Run the Project
1. Open the project in VS Code.
2. Activate