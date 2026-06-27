from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from routers import categories, customers, products

app = FastAPI(
    title="Northwind API",
    description="Northwind veritabani icin basit CRUD API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(customers.router)
app.include_router(categories.router)
app.include_router(products.router)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return FileResponse("static/index.html")


@app.get("/api")
def api_info():
    return {
        "message": "Northwind API",
        "docs": "/docs",
        "ui": "/",
        "endpoints": {
            "customers": "/customers",
            "categories": "/categories",
            "products": "/products",
        },
    }
