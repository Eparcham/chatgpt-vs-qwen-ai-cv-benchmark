# Publication audit

This repository was checked before public release for common benchmark-publication problems.

## Corrected before publication

1. **Conflicting scoring metadata**
   - The initial benchmark JSON still contained an older 70/15/10/5 draft rubric.
   - The public evaluation uses the six-dimension 50/15/10/10/5/10 rubric.
   - The JSON now labels the old rubric as a legacy draft and explicitly records the published rubric.

2. **Stale Cross-Evaluation status**
   - `phase1_summary.json` still described Cross-Evaluation as a future experiment.
   - It now records Cross-Evaluation as completed.

3. **Raw Qwen authoring trace**
   - Intermediate raw generations included discarded drafts, stale 14/15 status information, and model deliberation.
   - These traces were removed from the public package and replaced by the concise provenance description in `PROVENANCE.md`.

4. **XQWEN-13 editorial artifact**
   - A requirement contained the model's internal deliberation about whether SciPy should be allowed.
   - It was replaced by a short, explicit requirement without changing the intended solution space.

5. **Qwen model identity wording**
   - The public documentation now states that `Qwen 3.8 120B` is an operator/deployment-provided label and that the exact checkpoint/build was not independently verified from archived API outputs.

6. **Phase-1 Qwen generation regime**
   - Recovery of missing Phase-1 Qwen tasks used a tighter output budget and reduced/disabled thinking.
   - This is now explicitly disclosed; Phase 1 should not be described as a single fixed-generation-regime Qwen run.

7. **Cross-Evaluation gap wording**
   - The report now avoids treating the Phase-1 and Cross-Eval gap as a strict apples-to-apples reduction, because task sets and aggregation contexts differ.

## Intentionally retained and documented

Some Qwen-authored tasks contain substantive conflicts between the written specification, public examples, private graders, or generated references. These issues are part of what the benchmark audit discovered. They are documented in:

- `evaluation/benchmark_quality_audit.csv`
- `evaluation/regression_evidence.json`
- the HTML report

They are not silently rewritten after scoring.

## Public leakage checks

The two public Cross-Evaluation question files were verified to contain no `reference_answer` or `grader_tests` fields.

The repository was also scanned for API keys, bearer tokens, the private endpoint IP used during development, and identifying request headers. None are present in this public package.
