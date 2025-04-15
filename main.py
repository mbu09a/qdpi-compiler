from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CompileInput(BaseModel):
    input: str

@app.post("/compile")
async def compile(input_data: CompileInput):
    user_input = input_data.input
    # Simulate symbolic transformation logic
    return {
        "response": f"🜂 Dream Refraction: You gave \"{user_input}\" and the mirror spoke back."
    }

@app.get("/")
def root():
    return {"message": "QDPI Compiler is running."}
