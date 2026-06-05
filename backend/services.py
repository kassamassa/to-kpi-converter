from openai import OpenAI
from models import JDAnalysisResult  # models.pyで作ったPydanticモデル
from prompts import SYSTEM_PROMPT    # prompts.pyで作ったプロンプト

# OpenAIクライアントの初期化（環境変数にOPENAI_API_KEYが設定されている前提）
client = OpenAI()

def analyze_jd_and_generate_kpi(jd_text: str) -> JDAnalysisResult:
    """
    募集要項(JD)のテキストを受け取り、OpenAI APIを使ってKPIに変換する関数
    """
    
    # OpenAI APIを呼び出し、Pydanticモデルの形式でパースして受け取る
    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06", # Structured Outputs対応モデル推奨
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"以下の募集要項を分析し、具体的なKPIを生成してください。\n\n{jd_text}"}
        ],
        response_format=JDAnalysisResult, # ここでmodels.pyの型を指定！
        temperature=0.2 # 感情的バイアスを排除し、ロジカルな分析をさせるため低めに設定
    )

    # パースされた結果（JDAnalysisResultオブジェクト）を返す
    return response.choices[0].message.parsed
