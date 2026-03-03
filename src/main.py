from fastapi import FastAPI
from .routes import analytics, reports

app = FastAPI(title="FlowForge Analytics", version="2.4.0")
app.include_router(analytics.router, prefix="/api/v1/analytics")
app.include_router(reports.router, prefix="/api/v1/reports")

@app.get("/health")
def health(): return {"status": "healthy"}
