# Repository Working Agreement

This repository is a daily AI-engineering practice environment.

## Daily scope

- Advance one exercise at a time. Do not prebuild future exercises.
- Begin with the next incomplete row in `PROGRESS.md` unless the user chooses another topic.
- Keep each session small enough to understand, test, and explain in 30-45 minutes.
- Prefer a direct implementation over a framework until the framework closes a demonstrated gap.
- Use public or synthetic data. Never commit secrets, tokens, private documents, or personal data.

## Definition of done

A daily exercise is done only when:

1. the relevant automated checks pass;
2. the learner can explain the concept without reading the source;
3. one limitation or failure case has been recorded;
4. `PROGRESS.md` links to the resulting code or note.

## Changes

- Preserve the dependency-free baseline until a specific exercise requires a dependency.
- Add tests in proportion to each behavior change.
- For bug fixes, establish a failing regression test before changing the implementation.
- Keep generated output, downloaded models, local indexes, and credentials out of Git.
