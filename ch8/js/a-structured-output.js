import { z } from "zod";
import { ChatAnthropic } from '@langchain/anthropic';

const joke = z.object({
  setup: z.string().describe("The setup of the joke"),
  punchline: z.string().describe("The punchline to the joke"),
});

let model = new ChatAnthropic({
  model: "claude-haiku-4-5",
  temperature: 0,
});

model = model.withStructuredOutput(joke);

const result = await model.invoke("Tell me a joke about cats");
console.log(result);
