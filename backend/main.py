from fastapi import FastAPI
from pydantic import BaseModel
from services import analyze_jd_and_generate_kpi

app = FastAPI()

# Next.jsから送られてくるリクエストの型
class JDRequest(BaseModel):
    text: str

@app.post("/api/analyze-jd")　
#あくまで例
def api_analyze_jd(request: JDRequest):
    # services.pyの関数を呼び出すだけ！ロジックが分離されていて綺麗です。
    result = analyze_jd_and_generate_kpi(request.text)
    return result
