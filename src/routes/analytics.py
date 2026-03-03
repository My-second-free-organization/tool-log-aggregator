from fastapi import APIRouter

router = APIRouter()

@router.get("/workflows/summary")
def workflow_summary(tenant_id: str): return {"tenant_id": tenant_id, "total_workflows": 42, "active": 28, "avg_completion_time_hours": 4.5}

@router.get("/tasks/summary")
def task_summary(tenant_id: str): return {"tenant_id": tenant_id, "total_tasks": 1250, "completed": 980, "pending": 270}

@router.get("/performance")
def performance(tenant_id: str, period: str = "7d"): return {"tenant_id": tenant_id, "period": period, "throughput": 150, "error_rate": 0.02}
