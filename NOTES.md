# Project Notes — Decisions & Thought Process

Running log of decisions made during the build. Raw material for the README.

## Scoping decisions

- **Bite-size commits over big-bang builds.** Got the API plumbing working with generic sample prompts first, then moved on. Separating plumbing from domain logic makes troubleshooting faster and produces cleaner commit history.
- **Caught a course-correction mid-stream.** Was about to build grading before I had real test cases — realized the generic "capital of France" samples weren't useful for a golf rules bot. Stepped back, did test cases first.
- **Evals before system prompt.** You can't know if a prompt is good without something to grade it against. Test cases → baseline prompt → grader → iterate.
- **Deferred URL citations to v1.x (RAG).** Bare API calls can't reliably cite sources — the model generates plausible-looking URLs from training data, not verified links. Rather than ship hallucinated citations in v0.1, dropped the field and scoped it to v1.x when RAG is in place.
- **Simplified output schema to `question | ruling`.** Briefly over-engineered with ruling/rule/procedure/format/options fields. Collapsed to a single `ruling` blob for v0.1. Let the evals tell us what's worth structuring later.
- **UI deferred to v1.0.** Eval harness and prompt iteration is the PM-rigor story. Building UI early dilutes that.

## Ground truth methodology

- **Did not let the model grade its own homework.** Rejected "have Claude generate both questions and expected answers" because the evaluator and the thing being evaluated would be the same model.
- **Real scenarios, reworded.** Sourced from r/golf via subagent to get real situations players ask about, then reworded so surface forms differ from anything in training data.
- **Top comment ≠ ground truth.** Captured what Reddit said separately from the verified answer, so disagreement in threads becomes signal (adversarial markers) rather than noise.
- **Every test case traces to a public source** — defensibility for the README.

## Subagent vs bare API (conceptual gap RAG closes)

- **Bare API call** = model generates text from training weights only. No tools, no retrieval. Citations hallucinate.
- **Subagent** = Claude + tools (WebFetch, WebSearch, filesystem). Actually retrieves real pages and returns real data.
- **RAG in v1.x** = tools at _query time_ for the production app. Closes the same gap, just live.

## App behavior vs eval behavior

- "Ask for clarification" works in the live app (there's a human to answer) but breaks in single-shot evals (no one to reply).
- Changed to **"flag what clarification you'd need"** — same intent, but the grader can score "did the model correctly identify the ambiguity?"

## Rubric = PM thinking (don't delegate)

- Writing code around the rubric → fine to delegate to a subagent.
- Designing _what_ the rubric measures and _how_ it's weighted → the actual PM work. Keep that.

## Test case structure (v0.1)

Fields: `id | difficulty | category | question | source URL | top comment | ground truth (blank) | format`

- **40 cases:** 10 easy / 10 medium / 10 hard / 10 adversarial
- **~25% match play** via active search, not passive filter
- **Adversarial signal:** threads with significant comment disagreement
- **Skip unclear posts** rather than force-fit

## v0.1 system prompt

- **Persona:** Experienced USGA rules official at a major tournament. Correct > fast. Direct and helpful.
- **Ruling first**, then explanation. No making the reader hunt for the answer.
- **Output:** `question | ruling` blob (options, procedures, citations all inside ruling for v0.1).
- **Guardrails:** No hallucinated rule numbers. Flag ambiguity instead of presuming. No swing advice. Don't guess — state when you can't conclude.

## Workflow observations worth surfacing in README

- **Stubbing + polishing is the expected vibe-coding workflow.** PM writes the structure and intent; Claude writes the prose.
- **Commit history is part of the artifact.** Each meaningful unit of work is its own commit.
- **Parallelization:** subagent researching cases while I draft the system prompt. Context stays clean.

## Roadmap (working)

- **v0.1** — eval harness, 40 test cases, baseline system prompt, grader, scorecard
- **v0.2–x** — iterate prompt based on failure clusters
- **v1.0** — mobile web app (Vercel)
- **v1.x** — RAG (retrieval at query time), match-play toggle, local rules via photo OCR
- **v2.x** — model routing (Haiku/Sonnet/Opus by complexity), cost optimization