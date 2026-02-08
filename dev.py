from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

llm = OllamaLLM(model="llama3.1")

template = """
You are a helpful nutritionist assistant who helps users understand the nutritional value of ingredients provided by the user. 
You will receive a list of ingredients and provide information about their nutritional content, such as calories, macronutrients 
(carbohydrates, proteins, fats), vitamins, and minerals. You should provide your response in a table format for easy readability. 
Don't provide any additional information or explanations, just the nutritional content in a clear and concise manner.

User sentence: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | llm

while True:
    ingredients = list(input("Enter the ingredients(type bye to quit the agent): \n").lower().split(","))
    if "bye" in ingredients:
        break
    res = chain.invoke({"question": ingredients})
    print(res)