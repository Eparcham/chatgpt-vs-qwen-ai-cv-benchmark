# Benchmark provenance

## Phase 1 — 30-task shared benchmark

The initial 30-task AI/CV set was assembled with assistance from multiple cloud LLM/chatbot systems, including DeepSeek, and then manually reviewed and normalized into a common schema.

Per-question source provenance was **not retained**, so this repository does not claim that an individual task came from a specific external source or a specific model.

The answering models were only intended to receive the public task fields (problem, requirements, function signature, and public examples). Reference answers and grader descriptions were evaluation-side artifacts.

## Phase 2 — Cross-Evaluation

Two 15-task sets were used:

- a ChatGPT-side authored set answered by Qwen;
- a Qwen-authored set answered blindly by GPT-5.6 Sol.

The public question files exclude `reference_answer` and `grader_tests`.

The Qwen question-generation workflow included structural validation and recovery of an incomplete task. Discarded drafts and raw generation traces are intentionally **not included in the public repository**, because they are not part of the final benchmark and contained intermediate model deliberation that could be confused with the final task specification.

## Model identity

`GPT-5.6 Sol` is the ChatGPT-side model label used for this benchmark.

`Qwen 3.8 120B` is the **operator/deployment-provided label** for the internal endpoint used in this benchmark. The archived API responses do not independently identify the exact server-side checkpoint, quantization, or inference engine. Results should therefore be attributed to the tested deployment under that label, not generalized to every Qwen3.8 checkpoint.

## Post-publication editorial cleanup

One Qwen-authored task (`XQWEN-13`) contained a long piece of model deliberation inside a requirement about whether SciPy was allowed. For publication, that paragraph was replaced with a concise requirement that preserves the allowed solution space: SciPy is allowed but not required, and a pure NumPy/Python optimal implementation is also acceptable.

No model answer or score was changed by this editorial cleanup.

Known substantive prompt/example/reference conflicts are **not silently erased**. They remain documented in `evaluation/benchmark_quality_audit.csv` so the limitations of the as-run benchmark remain visible.
