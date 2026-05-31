from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model="claude-haiku-4-5")

completion = model.invoke("Hi there!")
# Hi!

completions = model.batch(["Hi there!", "Bye!"])
# ['Hi!', 'See you!']

for token in model.stream("Bye!"):
    print(token)
    # Good
    # bye
    # !
