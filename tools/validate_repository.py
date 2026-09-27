#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

initial = load(ROOT / "initial_benchmark" / "benchmark_30_tasks_with_reference.json")
assert len(initial["challenges"]) == 30

chat_public = load(ROOT / "chatgpt" / "authored_cross_eval" / "questions_only.json")
qwen_public = load(ROOT / "qwen" / "authored_cross_eval" / "questions_only.json")
assert len(chat_public["challenges"]) == 15
assert len(qwen_public["challenges"]) == 15

for label, obj in [("ChatGPT public", chat_public), ("Qwen public", qwen_public)]:
    for task in obj["challenges"]:
        assert "reference_answer" not in task, f"{label}: leaked reference in {task.get('id')}"
        assert "grader_tests" not in task, f"{label}: leaked grader tests in {task.get('id')}"

qwen_answers = load(ROOT / "qwen" / "answers" / "cross_eval_answers_on_chatgpt_authored_questions.json")
gpt_answers = load(ROOT / "chatgpt" / "answers" / "cross_eval_gpt_5_6_sol_answers_on_qwen_questions.json")
assert len(qwen_answers["answers"]) == 15
assert len(gpt_answers["answers"]) == 15

for obj in [qwen_answers, gpt_answers]:
    for answer in obj["answers"]:
        compile(answer["solution_code"], answer["challenge_id"], "exec")

print("Repository validation passed.")
print("Initial benchmark: 30 tasks")
print("ChatGPT-authored public cross set: 15 tasks, no private fields")
print("Qwen-authored public cross set: 15 tasks, no private fields")
print("Cross answers: 15 + 15, all Python solution_code blocks compile")
