from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)

from index import Index


class Chat:
    def __init__(self):
        template = """Answer the question as truthfully as possible using the provided context, and if the answer is not contained within the text below, say 'I don't know'"""
        system_msg_template = SystemMessagePromptTemplate.from_template(template=template)

        human_msg_template = HumanMessagePromptTemplate.from_template(template="{input}")

        prompt_template = ChatPromptTemplate.from_messages(
            [system_msg_template, MessagesPlaceholder(variable_name="history"), human_msg_template])

        self.memory = ConversationBufferWindowMemory(k=3, return_messages=True)
        self.llm = OpenAI(model_name="gpt-3.5-turbo")

        self.conversation = ConversationChain(memory=self.memory, prompt=prompt_template, llm=self.llm, verbose=True)
        self.index = Index()

    def predict(self, query):
        context = self.index.find_context(query)
        input = f"Context:\n {context} \n\n Query:\n{query}"

        print("Input is:", input)

        return self.llm.predict(input)
