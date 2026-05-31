import { ChatAnthropic } from '@langchain/anthropic';
import { HumanMessage } from '@langchain/core/messages';

const model = new ChatAnthropic({ model: 'claude-haiku-4-5' });
const prompt = [new HumanMessage('What is the capital of France?')];

const response = await model.invoke(prompt);
console.log(response);
