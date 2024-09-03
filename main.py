from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from deep_translator import GoogleTranslator

app = FastAPI()

class TranslationRequest(BaseModel):
    text: str
    source_language: str = 'auto'

def translate_to_english(text: str, source_language: str = 'auto') -> str:
    try:
        translator = GoogleTranslator(source=source_language, target='en')
        translation = translator.translate(text)
        return translation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/translate")
def translate(request: TranslationRequest):
    translated_text = translate_to_english(request.text, request.source_language)
    return {"translated_text": translated_text}
@app.get("/")
def read_root():
    return {"message": "Welcome to the translation API!"}
