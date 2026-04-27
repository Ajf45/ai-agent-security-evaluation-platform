from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(Text)
    response = Column(Text)
    risk_score = Column(Integer)
    risk_level = Column(String)
    status = Column(String)  # pending / completed
    