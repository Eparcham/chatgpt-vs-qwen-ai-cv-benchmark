#!/usr/bin/env python3
from pathlib import Path
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

def load_namespace(code):
    ns = {}
    exec(compile(code, "<answer>", "exec"), ns)
    return ns

qwen_obj = json.loads((ROOT/"qwen"/"answers"/"cross_eval_answers_on_chatgpt_authored_questions.json").read_text(encoding="utf-8"))
answers = {a["challenge_id"]: a for a in qwen_obj["answers"]}

# XCHAT-13: unmatched semantics
ns = load_namespace(answers["XCHAT-13"]["solution_code"])
got = ns["greedy_cost_match"](np.array([[1.,2.],[2.,1.]]), 1.0)
expected = ([(0,0),(1,1)], [], [])
print("XCHAT-13 unmatched expected:", expected)
print("XCHAT-13 Qwen returned     :", got)
assert got != expected, "Archived behavior changed unexpectedly"

# XCHAT-11: compile-only integrity; exact frequency interpretation is documented separately
for cid, answer in answers.items():
    compile(answer["solution_code"], cid, "exec")

print("Known regression checks completed.")
