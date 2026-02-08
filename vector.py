from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("cleaned.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

# Prepare data in documents format and add to vector store
if add_documents:
    documents = []
    ids = []
    for i, row in df.iterrows():
        document = Document(
            page_content=row["food"],
            metadata={"calories": row["Caloric Value"], "carbohydrates": row["Carbohydrates"], "protein": row["Protein"], "fats": row["Fat"], "sugars": row["Sugars"], "fiber": row["Dietary Fiber"], "sodium": row["Sodium"], "cholesterol": row["Cholesterol"], "nutrition_density": row["Nutrition Density"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)
        
# Initialize Chroma vector store
vector_store = Chroma(
    collection_name="nutritional_values",
    persist_directory=db_location,
    embedding_function=embeddings
)

# Add documents to vector store if not already present
if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)
    
# Create a retriever from the vector store to perform similarity search
retriever = vector_store.as_retriever(search_kwargs={"k": 5}) # Retrieve top 5 similar documents