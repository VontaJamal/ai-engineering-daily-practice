# Focused Question Catalog

This catalog contains every top-level question from the six source sections selected for daily practice.

| Domain | IDs | Questions |
| --- | --- | ---: |
| LLM fundamentals | `LLM-001` onward | 66 |
| Prompt engineering | `PROMPT-001` onward | 30 |
| Retrieval-augmented generation | `RAG-001` onward | 37 |
| AI agents and agentic systems | `AGENT-001` onward | 45 |
| AI system design | `DESIGN-001` onward | 46 |
| Coding and practical implementation | `CODE-001` onward | 22 |
| **Total** |  | **246** |

## Selection rule

Daily interview questions must come from these files. Rotate through the domains in this order:

`LLM → PROMPT → RAG → AGENT → DESIGN → CODE`

Within each domain, choose the lowest-numbered question that is not recorded in `QUESTION_LOG.md`. After `CODE`, begin the next rotation at `LLM`.

Coding is both a source-question domain and the applied layer for every session. Even on a concept day, finish with a small implementation, test, trace, calculation, or design artifact.

Supporting concerns such as evaluation, safety, latency, cost, infrastructure, embeddings, and observability may appear inside answers and builds when they affect the selected domain. Do not use them as standalone interview-question categories.

## Material rule

Before cold recall, surface:

1. the selected question ID and local catalog file;
2. any answer or learning links stored beneath it;
3. the matching local implementation, test, or roadmap material;
4. a current primary source when the catalog has no supporting link.

Do not reveal the answer before the learner responds.
