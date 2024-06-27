from  fastapi import FastAPI

#instala  FastAPI : pip install "fastapi[all]"
app = FastAPI()
@app.get("/")
async def root():
    return"hola fast api!"
#url local: http: http://127.0.01:8000



app = FastAPI()
@app.get("/url")
async def url():
    return {"url":"https://mouredev.com"}
#url local: http://127.001:8000/url

#inicia el server :uvicorn main:app --reload
#detener server : CRTL +C
#documentacion swagger: http://127.0.0.1:800/docs
#documentacion con Redocly: http://127.0.0.1:8000/redo