# Four-Week Roadmap

The roadmap contains 24 practice days. Sundays are intentionally left open for rest or catch-up.

Each practice day has two coordinated tracks:

1. a cold-recall question selected from the focused rotation in `questions/README.md`;
2. the cumulative document-assistant build step below.

The question and build should align when practical. The focused question rotation continues after this 24-day build is complete, so all 246 selected prompts remain available without forcing the project roadmap to become 246 days long.

## Week 1: Understand the basic loop

| Day | Question | Build | Proof |
| --- | --- | --- | --- |
| 1 | What does RAG solve? | Run a lexical retrieval baseline | Explain one success and one failure |
| 2 | What are embeddings? | Add an embedding interface and local implementation | Compare results with Day 1 |
| 3 | How does chunking affect retrieval? | Implement fixed-size and paragraph chunking | Show a query whose ranking changes |
| 4 | How do structured outputs work? | Validate a typed answer-and-citations response | Reject malformed output in a test |
| 5 | Why do context limits matter? | Add a context-budget selector | Prove the budget is never exceeded |
| 6 | How should a RAG answer cite evidence? | Format grounded answers with source IDs | Demo an answer and an abstention |

**Weekly milestone:** explain the retrieval-to-answer path and demonstrate a small grounded answer without hidden steps.

## Week 2: Improve retrieval with evidence

| Day | Question | Build | Proof |
| --- | --- | --- | --- |
| 7 | How should documents be ingested? | Add validation and normalized metadata | Reject a malformed document |
| 8 | How is vector search indexed? | Persist and reload a small local index | Results survive a restart |
| 9 | Why use hybrid retrieval? | Combine lexical and embedding ranks | Beat each baseline on a chosen query set |
| 10 | What does a reranker do? | Rerank top candidates | Record before-and-after ranking |
| 11 | How do updates stay fresh? | Add document versions and replacement | Old content no longer appears |
| 12 | How is retrieval evaluated? | Create a small labeled query set | Report recall at k and failure cases |

**Weekly milestone:** a repeatable retrieval evaluation shows whether each new component helps.

## Week 3: Make the system dependable

| Day | Question | Build | Proof |
| --- | --- | --- | --- |
| 13 | How does tool calling work? | Add one typed, read-only tool | Invalid arguments fail safely |
| 14 | When should an agent stop? | Implement a bounded agent loop | The loop cannot run forever |
| 15 | How should transient failures be handled? | Add retry with exponential backoff | Deterministic failure test passes |
| 16 | When is caching safe? | Add exact request caching | Show hit, miss, and invalidation |
| 17 | What should be observable? | Record latency, steps, and result status | Inspect one trace without secrets |
| 18 | How should provider failure degrade? | Add a fallback or clear abstention path | Simulated outage stays controlled |

**Weekly milestone:** the assistant handles expected failures without looping, leaking data, or silently inventing success.

## Week 4: Evaluate, secure, and explain

| Day | Question | Build | Proof |
| --- | --- | --- | --- |
| 19 | How are generated answers evaluated? | Add groundedness and relevance checks | Evaluate the labeled set |
| 20 | How should hallucinations be handled? | Require claim-to-source support | Unsupported answer abstains or fails |
| 21 | What is prompt injection? | Add adversarial retrieval cases | Demonstrate the trust boundary |
| 22 | How should sensitive data be handled? | Add input and log redaction | Redaction regression tests pass |
| 23 | How would this system scale? | Write a system-design brief | Cover latency, cost, reliability, and safety |
| 24 | Can you defend the design? | Record a five-minute demo and mock interview | Answer unfamiliar follow-ups clearly |

**Final milestone:** a tested document assistant, evaluation report, system-design brief, and short demonstration.
