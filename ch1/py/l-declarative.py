from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
import asyncio

# the building blocks

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "{question}"),
    ]
)

model = ChatAnthropic(model="claude-haiku-4-5")

# combine them with the | operator

chatbot = template | model

# use it

response = chatbot.invoke({"question": "Which model providers offer LLMs?"})
print(response.content)

# streaming

for part in chatbot.stream({"question": "Which model providers offer LLMs?"}):
    print(part)

# asynchronous method

async def main():
    response = await chatbot.ainvoke({"question": "Which model providers offer LLMs?"})
    print(response.content)

asyncio.run(main())