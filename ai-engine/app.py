
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from fastapi import FastAPI
from context import analyze_context
from prompt_injection import detect_prompt_injection
from risk_detection import detect_risk
from trust_score import calculate_trust_score
from ai_decision import make_ai_decision
from llm import analyze_with_llm

app = FastAPI()


@app.post("/analyze-context")
def analyze_user_context(text: str):
    result = analyze_context(text)
    injection_result = detect_prompt_injection(text)

    risk_result = detect_risk(
        text,
        result,
        injection_result
    )

    trust_result = calculate_trust_score(
        risk_result["risk_score"]
    )

    decision_result = make_ai_decision(
        risk_result["risk_level"],
        trust_result["trust_level"]
    )

    llm_result = analyze_with_llm(
        text,
        result,
        risk_result
    )

    return {
        **result,
        **injection_result,
        **risk_result,
        **trust_result,
        **decision_result,
        "llm_analysis": llm_result
    }