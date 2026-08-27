# AI Engineering Daily Practice

A small, cumulative practice repository for building applied AI-engineering skills through explanation, implementation, testing, and review.

The topic bank comes from Outcome School's [AI Engineering Interview Questions](https://github.com/amitshekhariitbhu/ai-engineering-interview-questions). This repository turns selected questions into hands-on work rather than attempting to memorize the entire list.

## The daily loop

Use one 30-45 minute session:

1. **Recall (5 minutes):** answer the day's question without notes.
2. **Learn (10 minutes):** inspect a source and correct the answer.
3. **Build (15-25 minutes):** implement or test one small capability.
4. **Record (5 minutes):** capture what worked, what failed, and what you can now explain.

Use the [answer framework](docs/answer-framework.md) for the recall step. Update [PROGRESS.md](PROGRESS.md) only after the day's done condition is met.

## Focused question bank

Daily interview questions come from a local catalog of all **246** top-level source prompts in six selected domains:

- LLM fundamentals;
- prompt engineering;
- retrieval-augmented generation;
- AI agents and agentic systems;
- AI system design;
- coding and practical implementation.

See [questions/README.md](questions/README.md) for counts, source files, and the round-robin selection rule. Coding is also the applied layer for every session, so concept questions still end with implementation, testing, measurement, or design work. Completed questions are recorded in [QUESTION_LOG.md](QUESTION_LOG.md).

## Start here: Day 1

**Question:** What is retrieval-augmented generation (RAG), and what problem does it solve?

**Build:** Run and investigate a deterministic text-retrieval baseline over ten short documents.

```bash
python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m ai_practice.day01 --query "vector search embeddings"
```

Then follow [Exercise 001](exercises/001-retrieval-baseline/README.md). The code intentionally uses lexical TF-IDF retrieval rather than model embeddings. That gives the next exercise a baseline whose failure can be measured.

## One cumulative project

Across four weeks, the baseline becomes a small document assistant with:

- document ingestion and chunking;
- embedding and hybrid retrieval;
- reranking and grounded citations;
- evaluation cases and regression checks;
- tool use, retries, caching, and observability;
- safety boundaries and a final system-design explanation.

The detailed sequence and weekly proof points are in [ROADMAP.md](ROADMAP.md).

## Repository layout

```text
data/        Synthetic learning corpus
docs/        Explanation and design frameworks
exercises/   Daily briefs and done conditions
questions/   Focused interview-question catalog and source manifest
src/         Implementations that accumulate over time
tests/       Deterministic regression checks
```

## Practice rules

- Predict before running the code.
- Measure before replacing a component.
- Keep examples public or synthetic.
- Treat a generated answer as a hypothesis until code, tests, or a reliable source supports it.
- Prefer a small working system you can explain over a large system you only assembled.

## License and attribution

The repository is licensed under the [Apache License 2.0](LICENSE). The curriculum topic bank is adapted from Outcome School's Apache-2.0-licensed repository; see [NOTICE](NOTICE) for attribution.
