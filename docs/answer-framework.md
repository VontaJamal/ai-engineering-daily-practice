# Answer Frameworks

## Concept question

Use five parts. A strong answer can usually fit in two minutes.

1. **Definition:** What is it?
2. **Mechanism:** How does it work?
3. **Purpose:** Which problem does it solve?
4. **Tradeoff:** What does it not solve, or what does it cost?
5. **Example and measurement:** Where would you use it, and how would you know it works?

### Example outline: RAG

- Definition: generation grounded by information retrieved at request time.
- Mechanism: retrieve candidate passages, place selected evidence in context, then generate an answer.
- Purpose: use current, private, or attributable knowledge without retraining model weights.
- Tradeoff: bad parsing or retrieval still produces bad context; grounding reduces but does not eliminate hallucinations.
- Measurement: evaluate retrieval and answer quality separately, including recall at k, citation support, relevance, latency, and cost.

## System-design question

Work through these in order:

1. clarify users, use cases, exclusions, and success measures;
2. estimate scale, latency, availability, privacy, and cost constraints;
3. draw the smallest end-to-end data and request flow;
4. identify evaluation data and release gates;
5. cover failures, fallbacks, observability, safety, and operations;
6. name the major tradeoff and what evidence would change the design.
