from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-3.5-turbo-16k")

from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="Translate the following from English into Gujarati"),
    HumanMessage(content="How are you?"),
]

print(model.invoke(messages))