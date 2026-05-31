import { ChatAnthropic } from '@langchain/anthropic';
import { ChatPromptTemplate } from '@langchain/core/prompts';
import { RunnableLambda } from '@langchain/core/runnables';

// the building blocks

const template = ChatPromptTemplate.fromMessages([
  ['system', 'You are a helpful assistant.'],
  ['human', '{question}'],
]);

const model = new ChatAnthropic({
  model: 'claude-haiku-4-5',
});

// combine them in a function

const chatbot = template.pipe(model);

// use it

const response = await chatbot.invoke({
  question: 'Which model providers offer LLMs?',
});

console.log(response);

//streaming

for await (const part of chatbot.stream({
  question: 'Which model providers offer LLMs?',
})) {
  console.log(part);
}
