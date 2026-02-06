from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

llm = OllamaLLM(model="llama3.1")

template = """
You are a helpful assistant that translates English to French. Translate the user sentence.

User sentence: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | llm

q = input("What would you like to translate?\n")

res = chain.invoke({"question": q})
print(res)