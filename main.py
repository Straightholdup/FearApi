from fastapi import FastAPI, UploadFile
import aiofiles
app = FastAPI()


@app.post("/audio")
async def create_audio(audio: UploadFile):
    async with aiofiles.open("./audio.wav", 'wb') as out_file:
        content = await audio.read()  # async read
        await out_file.write(content)  # async write
    return {"message": "Hello World"}

@app.get("/emotion")
async def get_emotion(audio: UploadFile):
    return {"emotion": "fear"}