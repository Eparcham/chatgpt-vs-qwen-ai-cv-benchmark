#!/usr/bin/env python3
from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
cross = pd.read_csv(ROOT / "evaluation" / "cross_eval_task_scores.csv")

for model, group in cross.groupby("answering_system"):
    print(f"{model}: {group['overall_score'].mean():.3f}/100 over {len(group)} tasks")

phase1 = json.loads((ROOT / "evaluation" / "phase1_summary.json").read_text(encoding="utf-8"))
for model, values in phase1["models"].items():
    print(f"{model}: {values['overall_expert_adjusted_score_pct']:.1f}% (Phase 1 archived score)")
