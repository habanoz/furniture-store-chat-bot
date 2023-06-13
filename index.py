from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import os
import pinecone

index_name = "mobilya1"


class Index:
    def __init__(self):
        pinecone.init(api_key=os.environ['PINECONE_API_KEY'], environment=os.environ['PINECONE_ENV'])

        self.docsearch = Pinecone.from_existing_index(index_name, OpenAIEmbeddings())

    def find_context(self, query):
        docs = self.docsearch.similarity_search(query, k=4)

        return "--\n".join(doc.page_content for doc in docs)
