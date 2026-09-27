#!/usr/bin/env python3
"""Recompute descriptive output-length metrics from the archived answer JSON files."""
from pathlib import Path
import json, re, math, io, tokenize, pandas as pd

ROOT=Path(__file__).resolve().parents[1]
runs=[
("Phase 1","GPT-5.6 Sol",ROOT/"chatgpt/answers/phase1_chatgpt_5_6_sol_answers.json"),
("Phase 1","Qwen 3.8 120B",ROOT/"qwen/answers/phase1_qwen_3_8_120b_answers.json"),
("Cross-Evaluation","GPT-5.6 Sol",ROOT/"chatgpt/answers/cross_eval_gpt_5_6_sol_answers_on_qwen_questions.json"),
("Cross-Evaluation","Qwen 3.8 120B",ROOT/"qwen/answers/cross_eval_answers_on_chatgpt_authored_questions.json"),
]
def full(a):
    assumptions=a.get("assumptions",[])
    if not isinstance(assumptions,list): assumptions=[assumptions]
    return "\n".join([str(a.get("solution_code","")),str(a.get("explanation","")),
                      str(a.get("time_complexity","")),str(a.get("space_complexity","")),
                      "\n".join(map(str,assumptions))])
rows=[]
for phase,system,path in runs:
    obj=json.loads(path.read_text(encoding="utf-8"))
    for a in obj["answers"]:
        t=full(a); code=str(a.get("solution_code",""))
        rows.append({"phase":phase,"system":system,"challenge_id":a["challenge_id"],
                     "characters":len(t),"estimated_tokens_char4":math.ceil(len(t)/4),
                     "whitespace_units":len(re.findall(r"\S+",t)),
                     "code_lines":len(code.splitlines())})
df=pd.DataFrame(rows)
print(df.groupby(["phase","system"]).agg(
    answers=("challenge_id","count"),
    mean_characters=("characters","mean"),
    mean_estimated_tokens=("estimated_tokens_char4","mean"),
    mean_whitespace_units=("whitespace_units","mean"),
    mean_code_lines=("code_lines","mean")
).round(1))
print("\nNOTE: estimated_tokens_char4 is a common output-length proxy, not provider-reported API token usage.")
