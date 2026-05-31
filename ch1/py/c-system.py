from langchain_core.messages import HumanMessage, SystemMessage
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model="claude-haiku-4-5")
system_msg = SystemMessage(
    "You are a helpful assistant that responds to questions with three exclamation marks."
)
human_msg = HumanMessage("What is the capital of France?")

response = model.invoke([system_msg, human_msg])
print(response.content)
