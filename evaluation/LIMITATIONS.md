# Limitations and interpretation

1. The initial experiment contains only 30 tasks; the cross-authored experiment contains 15 tasks per direction.
2. The benchmark is concentrated in Python, NumPy, OpenCV and PyTorch AI/CV engineering.
3. The initial question pool was prepared with assistance from multiple cloud chatbots and DeepSeek, then reviewed.
4. Question-author bias, reference bias and judge/review bias can still remain.
5. The cross-authored task sets are not identical, so the Phase-2 directional scores are not a same-task head-to-head measurement.
6. Phase 1 used the historical GPT-5.6 Sol artifact; the new blind cross-eval ChatGPT answers were generated with GPT-5.6 Sol.
7. Qwen and ChatGPT were not served on matched hardware. Model response latency is therefore not given a numeric head-to-head score.
8. Exact provider tokenizer usage was not logged comparably. Output analyses therefore report exact characters/whitespace/code metrics plus a clearly labeled common estimate of `ceil(characters/4)`; this is not API billing token usage.
9. The Qwen-authored benchmark contains multiple documented conflicts among prompt text, public examples, private graders and references. These are reported rather than silently corrected.
10. Scores should be read as engineering-benchmark results, not universal measures of model intelligence, general coding ability or population-level accuracy.

## Operational workflow interpretation

The self-hosted Qwen run required explicit serving and recovery work, including worker management, retries, resumable generation, malformed-JSON handling and output-budget control. This is part of the real engineering cost of the evaluated workflow.

However, the experiment did not run GPT-5.6 Sol and Qwen on identical hardware with identical serving software. Therefore the repository does not convert this experience into a numeric inference-latency comparison. The operational conclusion is about end-to-end researcher workflow, not intrinsic per-token model speed.

11. The Phase-1 Qwen answer set includes recovery runs produced with a tighter output budget and reduced/disabled thinking. It should not be treated as a single frozen-generation-configuration run.
12. `Qwen 3.8 120B` is the deployment/operator-provided label; exact checkpoint/build identity was not independently established from the archived API responses.
