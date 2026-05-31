import { ChatAnthropic } from '@langchain/anthropic';

const model = new ChatAnthropic({ model: 'claude-haiku-4-5' });

const response = await model.invoke('Hi there!');
console.log(response);
// Hi!

const completions = await model.batch(['Hi there!', 'Bye!']);
// ['Hi!', 'See you!']

for await (const token of await model.stream('Bye!')) {
  console.log(token);
  // Good
  // bye
  // !
}
