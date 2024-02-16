from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.endpoints.agent import router as agent_router
from src.app.endpoints.conversation import router as conversation_router
from src.app.endpoints.instant_agent import router as instant_agent_router
from src.app.endpoints.internal import router as internal_router

app = FastAPI(
    title="Amigo API",
    version="1.0",
    timeout=360,  # 6 minutes
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agent_router, prefix="/agents", tags=["agents"])
app.include_router(
    instant_agent_router, prefix="/instant/agents", tags=["instant/agents"]
)
app.include_router(internal_router, prefix="/internal", tags=["internal"])
app.include_router(conversation_router, prefix="/conversations", tags=["conversations"])
