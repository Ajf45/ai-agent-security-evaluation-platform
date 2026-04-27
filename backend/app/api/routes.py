from fastapi import APIRouter
from app.models.schemas import PromptRequest
from app.core.queue import task_queue
from app.workers.tasks import process_prompt

from app.core.database import SessionLocal
from app.models.db_models import Evaluation

router = APIRouter()

@router.post("/evaluate")
async def evaluate_prompt(data: PromptRequest):
    db = SessionLocal()

    new_eval = Evaluation(
        prompt=data.prompt,
        response="",
        risk_score=0,
        risk_level="",
        status="pending"
    )

    db.add(new_eval)
    db.commit()
    db.refresh(new_eval)

    # Send job with ID
    task_queue.enqueue(process_prompt, new_eval.id, data.prompt)

    return {
        "message": "Task added",
        "job_id": new_eval.id
    }

@router.get("/result/{job_id}")
def get_result(job_id: int):
    db = SessionLocal()
    record = db.query(Evaluation).filter(Evaluation.id == job_id).first()

    if not record:
        return {"error": "Job not found"}

    return {
        "id": record.id,
        "prompt": record.prompt,
        "response": record.response,
        "risk_score": record.risk_score,
        "risk_level": record.risk_level,
        "status": record.status
    }