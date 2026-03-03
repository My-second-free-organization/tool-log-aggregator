from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class WorkflowMetric(BaseModel):
    workflow_id: str
    name: str
    executions: int
    avg_duration_seconds: float
    error_rate: float
    last_executed: Optional[datetime] = None

class TaskMetric(BaseModel):
    task_type: str
    total: int
    completed: int
    avg_duration_seconds: float
