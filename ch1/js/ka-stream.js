import { ChatAnthropic } from '@langchain/anthropic';
import { ChatPromptTemplate } from '@langchain/core/prompts';
import { RunnableLambda } from '@langchain/core/runnables';

const template = ChatPromptTemplate.fromMessages([
  ['system', 'You are a helpful assistant.'],
  ['human', '{question}'],
]);

const model = new ChatAnthropic({
  model: 'claude-haiku-4-5',
});

const chatbot = RunnableLambda.from(async function* (values) {
  const prompt = await template.invoke(values);
  for await (const token of await model.stream(prompt)) {
    yield token;
  }
});

for await (const token of await chatbot.stream({
  question: 'Which model providers offer LLMs?',
})) {
  console.log(token);
}
