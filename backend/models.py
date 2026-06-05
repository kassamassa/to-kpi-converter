from pydantic import BaseModel, Field
from typing import List

class KPI:
  metric_name: str = Field(description="評価される指標名（例：APIレスポンスタイム）")
  target_value: str = Field(description="具体的な目標数値（例：200ms以内）")
  verification_method: str = Field(description="GitHub等での証明方法（例：該当PRのリンク）")

# LLMに最終的に出力させるJSON全体の構造を定義
class JDAnalysisResult(BaseModel):
  kpis: List[KPI] = Field(description="抽出されたKPIのリスト")
  unmeasurable_items: List[str] = Field(description="数値化が困難な定性的な要件のリスト")
