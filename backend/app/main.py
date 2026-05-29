from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import engine, Base
from app.api import auth, market, signals, users, admin
from app.core.config import settings

app = FastAPI(title="AI Trading Signals MVP")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(market.router, prefix="/market", tags=["market"])
app.include_router(signals.router, prefix="/signals", tags=["signals"])
app.include_router(users.router, tags=["users"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}
