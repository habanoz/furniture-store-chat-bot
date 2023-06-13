from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

index_name = "mobilya1"


class Index:
    def __init__(self):
        self.docsearch = Chroma(persist_directory="../langchaindemo/db", embedding_function=OpenAIEmbeddings())

    def find_context(self, query):
        docs = self.docsearch.similarity_search(query, k=4)

        return "--\n".join(doc.page_content for doc in docs)
