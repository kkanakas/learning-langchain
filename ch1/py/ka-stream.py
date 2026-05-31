from langchain_core.runnables import chain
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate


model = ChatAnthropic(model="claude-haiku-4-5")


template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "{question}"),
    ]
)


@chain
def chatbot(values):
    prompt = template.invoke(values)
    for token in model.stream(prompt):
        yield token


for part in chatbot.stream({"question": "Which model providers offer LLMs?"}):
    print(part)
