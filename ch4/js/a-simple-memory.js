import { ChatPromptTemplate } from '@langchain/core/prompts';
import { ChatAnthropic } from '@langchain/anthropic';

const prompt = ChatPromptTemplate.fromMessages([
  [
    'system',
    'You are a helpful assistant. Answer all questions to the best of your ability.',
  ],
  ['placeholder', '{messages}'],
]);
const model = new ChatAnthropic({ model: 'claude-haiku-4-5' });
const chain = prompt.pipe(model);

const response = await chain.invoke({
  messages: [
    [
      'human',
      'Translate this sentence from English to French: I love programming.',
    ],
    ['ai', "J'adore programmer."],
    ['human', 'What did you just say?'],
  ],
});

console.log(response.content);
