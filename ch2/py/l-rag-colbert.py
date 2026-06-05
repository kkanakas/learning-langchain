"""
PyLate implementation of ColBERT RAG.
- Supports macOS, Linux, and Windows (unlike RAGatouille).

- To install run:

```bash
pip install pylate
```
"""
from typing import Any, List

import requests
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pydantic import ConfigDict
from pylate import indexes, models, retrieve


def get_wikipedia_page(title: str):
    """
    Retrieve the full text content of a Wikipedia page.
    :param title: str - Title of the Wikipedia page.
    :return: str - Full text content of the page as raw string.
    """
    URL = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "extracts",
        "explaintext": True,
    }
    headers = {"User-Agent": "PyLate_tutorial/0.0.1"}
    response = requests.get(URL, params=params, headers=headers)
    data = response.json()
    page = next(iter(data["query"]["pages"].values()))
    return page["extract"] if "extract" in page else None


full_document = get_wikipedia_page("Hayao_Miyazaki")

# Split into passages — RAGatouille used max_document_length=180 tokens (~720 chars)
splitter = RecursiveCharacterTextSplitter(chunk_size=720, chunk_overlap=0)
passages = splitter.split_text(full_document)

# Load ColBERT model
model = models.ColBERT(model_name_or_path="colbert-ir/colbertv2.0")

# Encode documents
documents_embeddings = model.encode(
    passages,
    batch_size=32,
    is_query=False,
    show_progress_bar=True,
)

# Create PLAID index and add documents
index = indexes.PLAID(
    index_folder="./pylate-index",
    index_name="Miyazaki-123",
    model=model,
    override=True,
)
index.add_documents(
    documents_ids=list(range(len(passages))),
    documents_embeddings=documents_embeddings,
)

# Direct retrieval
retriever_engine = retrieve.ColBERT(index=index)
query = "What animation studio did Miyazaki found?"
query_embeddings = model.encode(
    [query],
    batch_size=1,
    is_query=True,
    show_progress_bar=True,
)
results = retriever_engine.retrieve(queries_embeddings=query_embeddings, k=3)
print(results)


# LangChain retriever wrapper
class PyLateRetriever(BaseRetriever):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    colbert_model: Any
    colbert_retriever: Any
    passages: List[str]
    k: int = 3

    def _get_relevant_documents(self, query: str) -> List[Document]:
        query_embeddings = self.colbert_model.encode(
            [query], batch_size=1, is_query=True, show_progress_bar=False
        )
        results = self.colbert_retriever.retrieve(
            queries_embeddings=query_embeddings, k=self.k
        )
        return [
            Document(
                page_content=self.passages[r["id"]],
                metadata={"score": r["score"]},
            )
            for r in results[0]
        ]


langchain_retriever = PyLateRetriever(
    colbert_model=model,
    colbert_retriever=retriever_engine,
    passages=passages,
    k=3,
)
docs = langchain_retriever.invoke("What animation studio did Miyazaki found?")
print(docs)
