# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # 8. Gemini API + Pydantic 구조화 출력
#
# **학습 목표**: Gemini API로 Pydantic 스키마 기반의 구조화된 JSON 응답을 받습니다.
#
# **사전 준비**: 
# - `pip install google-genai pydantic python-dotenv`
# - GOOGLE_API_KEY 환경변수 설정
#
# **소요 시간**: 1시간
#
# ---

# %% [markdown]
# ## 8.1 API 키 설정

# %%
import os
from dotenv import load_dotenv

# .env 파일에서 환경변수 로드
load_dotenv()

# API 키 확인
api_key = os.environ.get("GOOGLE_API_KEY")
if api_key:
    print(f"API 키 로드됨: {api_key[:8]}...")
else:
    print("API 키가 설정되지 않았습니다.")
    print("1. https://aistudio.google.com/apikey 에서 API 키 발급")
    print("2. .env 파일에 GOOGLE_API_KEY=your-api-key 추가")

# %%
from google import genai

# 클라이언트 생성 (GOOGLE_API_KEY 환경변수 자동 사용)
client = genai.Client()

# %% [markdown]
# ---
# ## 8.2 기본 텍스트 생성

# %%
# 간단한 텍스트 생성
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="파이썬의 장점 3가지를 간단히 알려주세요."
)

print(response.text)

# %% [markdown]
# ---
# ## 8.3 Pydantic 스키마로 구조화 출력
#
# 핵심 포인트:
# - `response_mime_type`: "application/json" 으로 설정
# - `response_schema`: Pydantic 모델 클래스 전달
# - `model_validate_json()`: 응답을 Pydantic으로 검증

# %%
from pydantic import BaseModel, Field
from typing import Literal, Optional

# %% [markdown]
# ### 8.3.1 감성 분석

# %%
class SentimentResult(BaseModel):
    """감성 분석 결과"""
    sentiment: Literal["긍정", "부정", "중립"] = Field(description="감성 분류")
    confidence: float = Field(ge=0, le=1, description="신뢰도 0-1")
    keywords: list[str] = Field(default=[], description="핵심 키워드")
    summary: str = Field(description="한 줄 요약")

# %%
text = "이 제품은 정말 훌륭해요! 품질도 좋고 배송도 빨랐습니다. 다만 포장이 조금 아쉬웠어요."

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"다음 텍스트의 감성을 분석하세요:\n{text}",
    config={
        "response_mime_type": "application/json",
        "response_schema": SentimentResult,
    },
)

# Pydantic으로 검증
result = SentimentResult.model_validate_json(response.text)

print(f"감성: {result.sentiment}")
print(f"신뢰도: {result.confidence:.2f}")
print(f"키워드: {result.keywords}")
print(f"요약: {result.summary}")

# %%
# model_dump()로 딕셔너리 변환
import json
print(json.dumps(result.model_dump(), ensure_ascii=False, indent=2))

# %% [markdown]
# ### 8.3.2 레시피 추출 (중첩 모델)

# %%
class Ingredient(BaseModel):
    """재료"""
    name: str = Field(description="재료 이름")
    quantity: str = Field(description="수량 (단위 포함)")

class Recipe(BaseModel):
    """레시피"""
    recipe_name: str = Field(description="요리 이름")
    prep_time_minutes: Optional[int] = Field(description="준비 시간 (분)")
    ingredients: list[Ingredient] = Field(description="재료 목록")
    instructions: list[str] = Field(description="조리 순서")

# %%
recipe_text = """
간단 계란볶음밥 만들기
재료: 밥 1공기, 계란 2개, 파 1줄기, 간장 1스푼, 참기름 약간
1. 팬에 기름을 두르고 파를 볶습니다.
2. 풀어둔 계란을 넣고 스크램블합니다.
3. 밥을 넣고 간장으로 간을 합니다.
4. 참기름을 뿌려 마무리합니다.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"다음 텍스트에서 레시피를 추출하세요:\n{recipe_text}",
    config={
        "response_mime_type": "application/json",
        "response_schema": Recipe,
    },
)

recipe = Recipe.model_validate_json(response.text)

print(f"요리: {recipe.recipe_name}")
print(f"준비 시간: {recipe.prep_time_minutes}분")
print(f"\n재료:")
for ing in recipe.ingredients:
    print(f"  - {ing.name}: {ing.quantity}")
print(f"\n조리 순서:")
for i, step in enumerate(recipe.instructions, 1):
    print(f"  {i}. {step}")

# %% [markdown]
# ---
# ## 8.4 설문 분석 보고서 생성

# %%
class Insight(BaseModel):
    """인사이트 항목"""
    category: str = Field(description="관련 카테고리")
    finding: str = Field(description="발견 내용")
    importance: Literal["high", "medium", "low"] = Field(default="medium", description="중요도")

class ActionItem(BaseModel):
    """액션 아이템"""
    task: str = Field(description="수행할 작업")
    priority: int = Field(ge=1, le=5, description="우선순위 1-5")

class AnalysisReport(BaseModel):
    """분석 보고서"""
    title: str = Field(description="보고서 제목")
    summary: str = Field(description="전체 요약 (2-3문장)")
    insights: list[Insight] = Field(description="주요 인사이트 (최소 2개)")
    action_items: list[ActionItem] = Field(description="액션 아이템 (최소 2개)")

# %%
survey_data = {
    "period": "2024년 1월",
    "total_responses": 50,
    "average_score": 3.74,
    "categories": {
        "제품": {"count": 24, "avg_score": 3.83, "positive_pct": 62.5},
        "배송": {"count": 14, "avg_score": 3.79, "positive_pct": 57.1},
        "서비스": {"count": 12, "avg_score": 3.58, "positive_pct": 58.3}
    },
    "top_feedback": {
        "positive": ["품질 좋음", "빠른 배송", "친절한 서비스"],
        "negative": ["배송 지연", "포장 훼손", "앱 불편"]
    }
}

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""다음 설문 데이터를 분석하여 보고서를 작성하세요:

{json.dumps(survey_data, ensure_ascii=False, indent=2)}

- 인사이트 3개 이상 도출
- 액션 아이템 2개 이상 제안
""",
    config={
        "response_mime_type": "application/json",
        "response_schema": AnalysisReport,
    },
)

report = AnalysisReport.model_validate_json(response.text)

print(f"=== {report.title} ===")
print(f"\n요약: {report.summary}")
print(f"\n인사이트 ({len(report.insights)}개):")
for ins in report.insights:
    print(f"  [{ins.importance}] {ins.category}: {ins.finding}")
print(f"\n액션 아이템 ({len(report.action_items)}개):")
for act in report.action_items:
    print(f"  [P{act.priority}] {act.task}")

# %%
# JSON 파일로 저장
output_path = "data/analysis_report.json"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(report.model_dump_json(indent=2))
print(f"\n보고서 저장됨: {output_path}")

# %% [markdown]
# ---
# ## 8.5 배치 분석 함수

# %%
from pydantic import BaseModel
from typing import Type, TypeVar

T = TypeVar('T', bound=BaseModel)

def analyze_with_schema(
    text: str,
    schema: Type[T],
    instruction: str = "분석하세요"
) -> T:
    """
    Pydantic 스키마로 텍스트 분석
    
    Args:
        text: 분석할 텍스트
        schema: Pydantic 모델 클래스
        instruction: 지시사항
    
    Returns:
        검증된 Pydantic 모델 인스턴스
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{instruction}:\n{text}",
        config={
            "response_mime_type": "application/json",
            "response_schema": schema,
        },
    )
    return schema.model_validate_json(response.text)

# %%
# 함수 사용 예시
result = analyze_with_schema(
    text="배송이 예상보다 2일 늦게 왔어요. 제품 자체는 괜찮은데 기다리느라 힘들었습니다.",
    schema=SentimentResult,
    instruction="다음 리뷰의 감성을 분석하세요"
)

print(f"감성: {result.sentiment}")
print(f"키워드: {result.keywords}")

# %%
def analyze_batch(
    texts: list[str],
    schema: Type[T],
    instruction: str = "분석하세요"
) -> list[T]:
    """
    여러 텍스트를 배치로 분석
    
    Args:
        texts: 분석할 텍스트 리스트
        schema: Pydantic 모델 클래스
        instruction: 지시사항
    
    Returns:
        검증된 모델 인스턴스 리스트
    """
    results = []
    for i, text in enumerate(texts, 1):
        print(f"분석 중... {i}/{len(texts)}")
        result = analyze_with_schema(text, schema, instruction)
        results.append(result)
    return results

# %%
# 배치 테스트
sample_texts = [
    "제품 품질이 정말 좋습니다! 재구매 의사 있어요.",
    "배송이 너무 늦었어요. 3주나 걸렸습니다.",
    "가격 대비 괜찮은 것 같습니다. 보통이에요."
]

batch_results = analyze_batch(
    texts=sample_texts,
    schema=SentimentResult,
    instruction="다음 리뷰의 감성을 분석하세요"
)

print("\n=== 배치 분석 결과 ===")
for text, result in zip(sample_texts, batch_results):
    print(f"\n텍스트: {text[:30]}...")
    print(f"  감성: {result.sentiment} (신뢰도: {result.confidence:.2f})")

# %% [markdown]
# ---
# ## 8.6 FAQ 생성

# %%
class QAItem(BaseModel):
    """질문-답변 쌍"""
    question: str = Field(description="자주 묻는 질문")
    answer: str = Field(description="답변")

class FAQResult(BaseModel):
    """FAQ 목록"""
    topic: str = Field(description="주제")
    faqs: list[QAItem] = Field(description="FAQ 목록 (최소 3개)")

# %%
product_info = """
스마트 공기청정기 A100
- 가격: 299,000원
- 적용 면적: 30평
- 필터 교체 주기: 6개월
- 소비전력: 50W
- 스마트폰 앱 연동 가능
- 헤파 H13 필터 사용
- 소음: 최저 25dB
- 배송: 주문 후 2-3일 소요
- 반품: 7일 이내 무료 반품
"""

faq_result = analyze_with_schema(
    text=product_info,
    schema=FAQResult,
    instruction="다음 제품 정보를 바탕으로 고객이 자주 물을 FAQ 5개를 생성하세요"
)

print(f"=== {faq_result.topic} FAQ ===\n")
for i, qa in enumerate(faq_result.faqs, 1):
    print(f"Q{i}. {qa.question}")
    print(f"A{i}. {qa.answer}\n")

# %% [markdown]
# ---
# ## 8.7 요약 생성

# %%
class ArticleSummary(BaseModel):
    """기사 요약"""
    title: str = Field(description="요약 제목")
    summary: str = Field(description="3문장 이내 요약")
    key_points: list[str] = Field(description="핵심 포인트 3-5개")
    category: Literal["경제", "기술", "사회", "문화", "기타"] = Field(description="기사 카테고리")

# %%
article = """
인공지능(AI) 기술의 발전이 가속화되면서 기업들의 AI 투자가 급증하고 있다. 
최근 발표된 보고서에 따르면, 글로벌 AI 시장 규모는 2024년 5,000억 달러를 
돌파할 것으로 예상된다. 특히 생성형 AI 분야에서의 성장이 두드러지며, 
ChatGPT, Gemini 등의 대형 언어 모델이 기업 업무 자동화에 널리 활용되고 있다.
전문가들은 AI가 향후 10년간 전 산업 분야에 혁신을 가져올 것이라고 전망한다.
다만 AI 윤리와 일자리 대체 문제에 대한 사회적 논의도 필요하다는 목소리가 높다.
"""

summary = analyze_with_schema(
    text=article,
    schema=ArticleSummary,
    instruction="다음 기사를 요약하세요"
)

print(f"제목: {summary.title}")
print(f"카테고리: {summary.category}")
print(f"\n요약: {summary.summary}")
print(f"\n핵심 포인트:")
for point in summary.key_points:
    print(f"  • {point}")

# %% [markdown]
# ---
# ## 연습문제

# %% [markdown]
# ### 문제 1: 회의록 요약 모델
# 회의 내용을 요약하는 Pydantic 모델을 만들고 Gemini로 요약하세요.
# - participants: 참가자 리스트
# - main_topics: 주요 안건
# - decisions: 결정 사항
# - next_steps: 다음 단계

# %%
class MeetingSummary(BaseModel):
    # 여기에 코드 작성
    pass


# %% [markdown]
# ### 문제 2: 상품 리뷰 분석 모델
# 상품 리뷰를 분석하는 모델을 만드세요.
# - rating: 1-5 별점 예측
# - pros: 장점 리스트
# - cons: 단점 리스트
# - recommendation: 추천 여부 (bool)

# %%
class ReviewAnalysis(BaseModel):
    # 여기에 코드 작성
    pass


# %% [markdown]
# ### 문제 3: 이메일 분류 모델
# 이메일을 분류하는 모델을 만드세요.
# - category: 문의/불만/칭찬/기타
# - urgency: high/medium/low
# - summary: 한 줄 요약
# - suggested_response: 답변 제안

# %%
class EmailClassification(BaseModel):
    # 여기에 코드 작성
    pass


# %% [markdown]
# ### 문제 4: 다국어 번역 모델
# 텍스트를 여러 언어로 번역하는 모델을 만드세요.
# - original_text: 원문
# - translations: dict[언어코드, 번역문]
# - detected_language: 감지된 원문 언어

# %%
class MultilingualTranslation(BaseModel):
    # 여기에 코드 작성
    pass



