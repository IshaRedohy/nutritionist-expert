# A nutrition expert chef AI agent

### Phase-1 (Initiate the prompt and model)

This is a local AI agent powered by [llama3.1](https://ollama.com/library/llama3.1) model and [langchain](https://docs.langchain.com/oss/python/integrations/chat/ollama). You input a list of food ingredients and the model replies with a table of its nutritional values. This is the phase 1 of the project. In next phase I will add documents containing nutrional facts of over thousands of ingredients so that the model can reply more precisely and fastly. The agent invocation happens in `dev.py` file.

### Phase-2 (connect model to vector database through langchain for RAG)

In this phase, we are using [ChromaDB](https://docs.trychroma.com/docs/overview/getting-started) as the vector database. Due to it being open-source, chroma is flexible for local agents. Over managed databases like pinecone or weaviate. For embedding, I am using [mxbai-embed-large](https://ollama.com/library/mxbai-embed-large) embedding model. For knowledge document I have found this [nutritional food dataset](https://www.kaggle.com/datasets/utsavdey1410/food-nutrition-dataset/data) from kaggle. It has almost 2400 ingredients and its nutritional info. In fact, it has way more info than I want for my agent. therefore, I have limited the columns to just calories, carbs, fats, protien, sugar, sodium, dietary fiber and nutritional density. The vector embedding and database storing is happening in `vector.py` file. 

Also, since there were multiple csv files, I have combined them and then trimmed off the unnecessary columns. Both codes can be found in `combine_csvs.py` and `trim_csv.py` files respectively.