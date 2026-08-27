# Exercise 001: Retrieval Baseline

## Interview question

What is retrieval-augmented generation (RAG), and what problem does it solve?

Answer aloud before opening `docs/answer-framework.md`.

## Build target

Understand and test the retrieval stage that precedes generation. The starter uses TF-IDF and cosine similarity, so it matches shared words rather than meanings. This is a baseline, not a production RAG system.

## Run it

From the repository root:

```bash
python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m ai_practice.day01 --query "vector search embeddings"
PYTHONPATH=src python3 -m ai_practice.day01 --query "Locate conceptually equivalent snippets"
```

Before each search, predict the top result. Compare the two queries and inspect why the lexical baseline succeeds or fails.

## Your changes

1. Add a query to `tests/test_retrieval.py` that captures one result you expect.
2. Add or edit a synthetic document in `data/sample_documents.json`.
3. Rerun the tests and both searches.
4. Record one limitation in `PROGRESS.md`.

Do not add an LLM or embedding dependency today. Day 2 will replace the retrieval representation and compare it with this baseline.

## Done condition

- All tests pass.
- You can explain retrieval, augmentation, and generation without notes.
- You can explain why lexical similarity is not semantic similarity.
- `PROGRESS.md` links to the test or note and records one observed failure.
