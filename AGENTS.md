# Repository Working Agreement

This repository is a daily AI-engineering practice environment.

## Daily scope

- Advance one exercise at a time. Do not prebuild future exercises.
- Begin with the next incomplete row in `PROGRESS.md` unless the user chooses another topic.
- Select interview questions only from the six domains in `questions/README.md`.
- Follow the focused round-robin rotation and choose the lowest-numbered unlogged question in that domain.
- Treat coding as the applied layer for every session, not only as a separate question category.
- Record completed cold-recall questions in `QUESTION_LOG.md`.
- Keep each session small enough to understand, test, and explain in 30-45 minutes.
- Prefer a direct implementation over a framework until the framework closes a demonstrated gap.
- Use public or synthetic data. Never commit secrets, tokens, private documents, or personal data.

## Learning materials

- Before cold recall, identify the selected question ID, its catalog file, its linked learning material, and the relevant local code or roadmap files.
- Do not reveal the answer before the learner responds.
- If the catalog does not link supporting material, use a current primary source.
- Evaluation, safety, latency, cost, infrastructure, embeddings, and observability may appear as constraints within the six selected domains, but not as standalone interview-question categories.

## Definition of done

A daily exercise is done only when:

1. the relevant automated checks pass;
2. the learner can explain the concept without reading the source;
3. one limitation or failure case has been recorded;
4. `PROGRESS.md` links to the resulting code or note;
5. `QUESTION_LOG.md` records the selected question and result.

## Changes

- Preserve the dependency-free baseline until a specific exercise requires a dependency.
- Add tests in proportion to each behavior change.
- For bug fixes, establish a failing regression test before changing the implementation.
- Keep generated output, downloaded models, local indexes, and credentials out of Git.
