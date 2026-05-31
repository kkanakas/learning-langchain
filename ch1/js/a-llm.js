import { ChatAnthropic } from '@langchain/anthropic';

const model = new ChatAnthropic({ model: 'claude-haiku-4-5' });

const response = await model.invoke('The sky is');
console.log(response);
