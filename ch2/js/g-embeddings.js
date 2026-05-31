import { HuggingFaceTransformersEmbeddings } from "@langchain/community/embeddings/huggingface_transformers";

const model = new HuggingFaceTransformersEmbeddings({ model: "Xenova/all-MiniLM-L6-v2" });
const embeddings = await model.embedDocuments([
  'Hi there!',
  'Oh, hello!',
  "What's your name?",
  'My friends call me World',
  'Hello World!',
]);

console.log(embeddings);
