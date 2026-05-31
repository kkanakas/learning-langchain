from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model="claude-haiku-4-5")

response = model.invoke("The sky is")
print(response.content)
