# Methodology and Limitations

This document adds methodological context to the original report while preserving its scoring structure and headline results.

## Benchmark construction

The initial question pool was prepared with assistance from multiple cloud chatbots and DeepSeek.
The questions were reviewed and filtered to retain broad AI/CV programming tasks.

This reduces, but does not eliminate:

- question-author bias,
- reference-answer bias,
- judge/evaluation bias,
- domain-selection bias.

## Evaluation dimensions

The published overall score uses the following dimensions:

- Functional correctness — 50%
- Robustness / edge cases — 15%
- API / specification compliance — 10%
- Algorithmic flow / design — 10%
- Generated-code runtime efficiency — 5%
- Code clarity / maintainability — 10%

The evaluation was not based only on textual similarity to reference solutions.

## Reference-answer policy

Reference implementations were treated as evaluation aids rather than absolute ground truth.
When a reference behavior appeared questionable, the task requirement and implementation behavior were reviewed separately.

## Serving-condition limitation

ChatGPT was accessed through cloud infrastructure.

Qwen 3.8 120B was served on constrained/self-hosted hardware.
Long reasoning substantially increased generation time, and some missing tasks required recovery under tighter output limits and reduced/disabled thinking.

Therefore model response-generation latency is not considered an apples-to-apples comparison.

## Runtime interpretation

The runtime dimension in the report refers to execution of generated programs on representative workloads.
It is not equivalent to model inference speed or response latency.

## Review subjectivity

Some dimensions—especially robustness, algorithmic design, and maintainability—require technical judgment.
The scores should therefore be read as a structured engineering evaluation, not as a purely automatic benchmark.

## Planned cross-evaluation

The next experiment will reverse question authorship:

- ChatGPT-side questions -> Qwen answers
- Qwen-side questions -> ChatGPT answers

The goal is to test whether the observed ranking is stable when the source of the benchmark questions changes.

## Appropriate interpretation

The current result is best interpreted as a benchmark-specific engineering comparison on 30 AI/CV code-generation tasks,
not a universal accuracy estimate or a definitive ranking of overall model intelligence.
