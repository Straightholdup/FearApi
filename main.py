from typing import List

from fastapi import FastAPI, UploadFile

import aiofiles

from db.config import async_session
from db.dals.entity_dal import BookDAL
from db.models.entity import Entity

app = FastAPI()

@app.post("/audio")
async def create_audio(audio: UploadFile):
    async with aiofiles.open("./audio.wav", 'wb') as out_file:
        content = await audio.read()  # async read
        await out_file.write(content)  # async write
    return {"message": "Hello World"}

@app.get("/books")
async def get_all_books() -> List[Entity]:
    async with async_session() as session:
        async with session.begin():
            book_dal = BookDAL(session)
            return await book_dal.get_all_entities()

@app.get("/emotion")
async def get_emotion(audio: UploadFile):
    return {"emotion": "fear"}
