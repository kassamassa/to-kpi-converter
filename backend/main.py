from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services import analyze_jd_and_generate_kpi
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # Next.jsのURLを許可
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Next.jsから送られてくるリクエストの型
class JDRequest(BaseModel):
    text: str

@app.post("/api/analyze-jd")
# あくまで例
def api_analyze_jd(request: JDRequest):
    # services.pyの関数を呼び出すだけ！ロジックが分離されていて綺麗です。
    result = analyze_jd_and_generate_kpi(request.text)
    return result
