from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

import os


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

prompt = PromptTemplate(
    input_variables=["text"],
    template="Answer the following question: {text}",
)

chain = LLMChain(llm=llm, prompt=prompt)

print("Ask a question")
while True:
    question = input("Question: ")
    if question.lower() == "quit":
        break
    response = chain.run(question)
    print("Answer: ", response)