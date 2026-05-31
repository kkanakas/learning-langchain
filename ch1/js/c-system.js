import { ChatAnthropic } from '@langchain/anthropic';
import { HumanMessage, SystemMessage } from '@langchain/core/messages';

const model = new ChatAnthropic({ model: 'claude-haiku-4-5' });
const prompt = [
  new SystemMessage(
    'You are a helpful assistant that responds to questions with three exclamation marks.'
  ),
  new HumanMessage('What is the capital of France?'),
];

const response = await model.invoke(prompt);
console.log(response);
