from pydantic import BaseModel, Field
from langchain_anthropic import ChatAnthropic


class Joke(BaseModel):
    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline to the joke")


model = ChatAnthropic(model="claude-sonnet-4-6", temperature=0)
model = model.with_structured_output(Joke)

result = model.invoke("Tell me a joke about cats")
print(result)
