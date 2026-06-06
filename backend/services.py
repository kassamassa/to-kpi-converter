from openai import OpenAI
from models import JDAnalysisResult  # models.pyで作ったPydanticモデル
import google.generativeai as genai
from prompts import SYSTEM_PROMPT    # prompts.pyで作ったプロンプト
from dotenv import load_dotenv  
import os

load_dotenv()
# OpenAIクライアントの初期化（環境変数にOPENAI_API_KEYが設定されている前提）
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config={"response_mime_type": "application/json"} # JSON出力を強制
)

print("=== あなたのキーで使えるモデル一覧 ===")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
print("======================================")


def analyze_jd_and_generate_kpi(jd_text: str) -> JDAnalysisResult:
    # プロンプトを構築
    prompt = f"""
    あなたはプロの採用コンサルタントです。以下の募集要項(JD)を分析し、KPIを抽出してください。
    必ず、以下のJSONスキーマに従って出力してください。
    
    {JDAnalysisResult.model_json_schema()}
    
    対象JD: 
    {jd_text}
    """
    
    # AIの呼び出し
    response = model.generate_content(prompt)
    
    # JSON文字列をPythonのモデルに変換して返す
    return JDAnalysisResult.model_validate_json(response.text)
