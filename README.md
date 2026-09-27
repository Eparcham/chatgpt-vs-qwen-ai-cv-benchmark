# AI-CV Programming Benchmark: ChatGPT 5.6 Instant vs Qwen 3.8 120B

This repository contains a reproducible comparison of two language models on 30 programming challenges focused on artificial intelligence and computer vision.

## Models

| Model | Configuration used in this benchmark |
|---|---|
| ChatGPT 5.6 Instant | ChatGPT 5.6, Instant mode |
| Qwen 3.8 120B | Qwen 3.8, 120B parameters |

The benchmark does not claim that these scores represent universal model quality. They are specific to the tasks, scoring method, prompts, and evaluation conditions included in this repository.

## Benchmark scope

The benchmark contains 30 English programming challenges covering:

- NumPy
- OpenCV
- PyTorch
- Object detection
- Segmentation
- 3D vision
- Depth and stereo vision
- Camera geometry
- Transformer components
- Metric learning
- Training utilities
- Tracking
- LoRA

The benchmark source is available in:

`benchmark_ai_cv_clean.json`

Each challenge contains the problem statement, requirements, expected API, public examples, reference implementation, and grader-test descriptions.

## Evaluation methodology

The final comparison is not based only on literal similarity to a reference answer or on a simple pass/fail count.

The revised evaluation uses six dimensions:

| Dimension | Weight |
|---|---:|
| Functional correctness | 50% |
| Robustness / edge cases | 15% |
| API / specification compliance | 10% |
| Algorithmic flow / design | 10% |
| Generated-code runtime efficiency | 5% |
| Code clarity / maintainability | 10% |

Reference implementations were audited independently and were not treated as infallible.

For example, the review identified a practical issue in the original letterbox reference implementation: using a scalar OpenCV border value for a multi-channel image does not necessarily produce the intended equal padding value on every channel. This is one reason the final evaluation does not assign a perfect score simply because a solution matches the reference implementation.

## Final results

| Metric | ChatGPT 5.6 Instant | Qwen 3.8 120B |
|---|---:|---:|
| Functional correctness | 98.8% | 86.4% |
| Robustness / edge cases | 92.0% | 55.0% |
| API / specification compliance | 98.0% | 78.0% |
| Algorithmic flow / design | 97.0% | 82.0% |
| Generated-code runtime efficiency | 80.2% | 85.2% |
| Code clarity / maintainability | 95.0% | 82.0% |
| **Overall expert-adjusted score** | **96.2%** | **79.9%** |
| Average challenge-level quality | 96.7% | 81.1% |

### Overall score

![Overall score](overall_expert_score.png)

### Score by evaluation dimension

![Evaluation dimensions](dimension_scores.png)

### Challenge-by-challenge comparison

![Challenge scores](challenge_scores.png)

### Generated-code runtime

![Runtime benchmark](runtime_benchmark.png)

The runtime chart measures the execution speed of generated code on representative workloads. It does **not** measure how quickly the language model generated its answer.

Matched response-generation latency logs were not available for both models, so model response latency is intentionally not included as a numeric score.

## Important findings

### ChatGPT 5.6 Instant

The strongest results were observed in functional correctness, API compliance, and algorithmic consistency.

Identified weaknesses include:

- `AICV-02`: the OpenCV letterbox padding implementation uses a scalar border value, which is not fully robust for multi-channel images.
- `AICV-21`: fractional class IDs may be silently converted to integers instead of being rejected.
- `AICV-28`: NaN confidence values are not explicitly rejected.

These issues are the main reason the model was not assigned a perfect score.

### Qwen 3.8 120B

Qwen produced many valid normal-path solutions and was competitive in generated-code execution speed on several workloads.

The largest score reductions came from specification mismatches and edge cases, including:

- `AICV-04`: NMS uses inclusive-coordinate `+1` geometry although the benchmark defines continuous coordinates.
- `AICV-05`: background handling does not fully match the requested foreground definition.
- `AICV-06`: largest-component output uses `255` rather than the required binary `{0,1}` representation.
- `AICV-07`: negative non-zero mask values are not treated as foreground.
- `AICV-09`: returns a homography matrix instead of the required ordered source points.
- `AICV-20`: zero-distance same-class positives can be incorrectly discarded.
- `AICV-22`: validation of parameter/buffer matching and decay range is incomplete.
- `AICV-23`: gradient accumulation retains multiple computation graphs and can use more memory.
- `AICV-29`: validation of `max_distance` and detection shapes is incomplete.

## Repository contents

```text
.
├── README.md
├── benchmark_ai_cv_clean.json
├── chatgpt_5_6_instant_answers.json
├── qwen_3_8_120b_answers.json
├── evaluation_summary_revised.json
├── challenge_level_expert_scores.csv
├── comparison_report_revised.html
├── overall_expert_score.png
├── dimension_scores.png
├── challenge_scores.png
├── runtime_benchmark.png
├── evaluation_flowchart.png
└── GITHUB_UPLOAD_COMMANDS.txt
```

### Main files

- `benchmark_ai_cv_clean.json`  
  Full benchmark definition.

- `chatgpt_5_6_instant_answers.json`  
  Complete answer set produced for ChatGPT 5.6 Instant.

- `qwen_3_8_120b_answers.json`  
  Complete answer set produced for Qwen 3.8 120B.

- `evaluation_summary_revised.json`  
  Machine-readable final scores and scoring methodology.

- `challenge_level_expert_scores.csv`  
  Per-challenge expert scores for both models.

- `comparison_report_revised.html`  
  Full human-readable report.

- `evaluation_flowchart.png`  
  Evaluation process overview.

## Evaluation flow

![Evaluation flowchart](evaluation_flowchart.png)

The evaluation follows this sequence:

1. The same 30 benchmark tasks are presented to both models.
2. Solutions are checked using executable and adversarial cases.
3. Requirements and API behavior are independently audited.
4. Code quality and generated-code runtime are reviewed.
5. Scores are combined using the published weights.

## Reproducibility notes

The answer files preserve the generated implementations used in this comparison.

The final scores include expert review in addition to deterministic checks. Therefore, exact reproduction of the final percentage requires using the same review rubric, not only executing the code.

This repository should be interpreted as a benchmark-specific engineering comparison rather than a universal ranking of the models.

## Limitations

- Only 30 AI/CV programming tasks are included.
- The benchmark emphasizes Python, NumPy, OpenCV, and PyTorch.
- Model response latency is not directly compared because equivalent timing logs were not available.
- Runtime benchmarks measure the generated programs, not the underlying inference engines.
- The expert-adjusted dimensions contain human review and are therefore not equivalent to a fully automatic benchmark.
- Results may change with different prompts, sampling parameters, serving engines, quantization, or model versions.

## Viewing the full report

Open:

`comparison_report_revised.html`

in a web browser.

It contains the detailed score table, charts, runtime results, important findings, and challenge-by-challenge comparison.

## Citation / sharing

When sharing these results, please describe them as:

> AI-CV Programming Benchmark — a 30-task engineering comparison of ChatGPT 5.6 Instant and Qwen 3.8 120B using functional correctness, robustness, specification compliance, algorithmic design, generated-code runtime, and maintainability.

Avoid presenting the percentages as universal model accuracy. They are specific to this benchmark and evaluation methodology.
