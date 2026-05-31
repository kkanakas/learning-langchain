from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage

model = ChatAnthropic(model="claude-haiku-4-5")
prompt = [HumanMessage("What is the capital of France?")]

response = model.invoke(prompt)
print(response.content)
