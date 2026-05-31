import { TextLoader } from 'langchain/document_loaders/fs/text';
import { RecursiveCharacterTextSplitter } from '@langchain/textsplitters';
import { HuggingFaceTransformersEmbeddings } from "@langchain/community/embeddings/huggingface_transformers";

const loader = new TextLoader('./test.txt');
const docs = await loader.load();

// Split the document
const splitter = new RecursiveCharacterTextSplitter({
  chunkSize: 1000,
  chunkOverlap: 200,
});
const chunks = await splitter.splitDocuments(docs);

console.log(chunks);

// Generate embeddings
const model = new HuggingFaceTransformersEmbeddings({ model: "Xenova/all-MiniLM-L6-v2" });
const embeddings = await model.embedDocuments(chunks.map((c) => c.pageContent));

console.log(embeddings);
