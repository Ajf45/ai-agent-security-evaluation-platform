from app.services.llm_service import get_llm_response
from app.services.evaluation_service import evaluate_response
from app.core.database import SessionLocal
from app.models.db_models import Evaluation

def process_prompt(job_id, prompt):
    db = SessionLocal()

    llm_output = get_llm_response(prompt)
    evaluation = evaluate_response(prompt, llm_output)

    record = db.query(Evaluation).filter(Evaluation.id == job_id).first()

    if record:
        record.response = llm_output
        record.risk_score = evaluation["risk_score"]
        record.risk_level = evaluation["risk_level"]
        record.status = "completed"

        db.commit()

    db.close()
    