from fastapi import FastAPI

from form_scrapper.server.routes.forms import router as FormsRouter

app = FastAPI()


app.include_router(FormsRouter, tags=["Forms"], prefix="/forms")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this form scrapper!"}
