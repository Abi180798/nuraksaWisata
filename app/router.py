
from app.Wisata.router import wisataRouter
from app import app

app.include_router(wisataRouter, prefix="/wisata")