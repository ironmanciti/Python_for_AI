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
# # 7. 타입 힌트, dataclass, Pydantic
#
# **학습 목표**: 
# - 타입 힌트로 코드 가독성을 높이고
# - dataclass로 데이터 모델을 간결하게 정의하며
# - Pydantic으로 자동 검증되는 스키마를 만듭니다.
#
# **소요 시간**: 1시간 30분
#
# ---

# %% [markdown]
# ## Part 1: 타입 힌트 (Type Hints)
# ---

# %% [markdown]
# ### 7.1 기본 타입 힌트
#
# Python 3.5+에서 도입된 타입 힌트는 코드의 가독성과 도구 지원을 향상시킵니다.

# %%
# 변수 타입 힌트
name: str = "홍길동"
age: int = 25
height: float = 175.5
is_student: bool = True

print(f"{name}({age}세, {height}cm, 학생: {is_student})")

# %%
# 함수 매개변수와 반환값 타입 힌트
def greet(name: str) -> str:
    return f"안녕하세요, {name}님!"

def add(a: int, b: int) -> int:
    return a + b

def divide(a: float, b: float) -> float:
    return a / b

print(greet("파이썬"))
print(add(3, 5))
print(divide(10.0, 3.0))

# %% [markdown]
# ### 7.2 컬렉션 타입 힌트

# %%
# 리스트
scores: list[int] = [85, 92, 78, 90]
names: list[str] = ["홍길동", "김철수", "이영희"]

# 딕셔너리
person: dict[str, str] = {"name": "홍길동", "city": "서울"}
scores_map: dict[str, int] = {"math": 90, "english": 85}

# 튜플
point: tuple[int, int] = (10, 20)
rgb: tuple[int, int, int] = (255, 128, 0)

# 셋
unique_ids: set[int] = {1, 2, 3, 4, 5}

print(f"점수: {scores}")
print(f"좌표: {point}")

# %% [markdown]
# ### 7.3 Optional과 Union

# %%
from typing import Optional, Union

# Optional: None일 수 있는 값
def find_user(user_id: int) -> Optional[str]:
    """사용자를 찾아 이름 반환, 없으면 None"""
    users = {1: "홍길동", 2: "김철수"}
    return users.get(user_id)

print(find_user(1))   # 홍길동
print(find_user(99))  # None

# %%
# Union: 여러 타입 중 하나
def process_input(value: Union[int, str]) -> str:
    """정수 또는 문자열을 받아 처리"""
    if isinstance(value, int):
        return f"숫자: {value}"
    else:
        return f"문자열: {value}"

print(process_input(42))
print(process_input("hello"))

# %%
# Python 3.10+에서는 | 연산자 사용 가능
def process_v2(value: int | str) -> str:
    return str(value)

# %% [markdown]
# ### 7.4 함수 시그니처 예시

# %%
def analyze_survey(
    responses: list[dict],
    category: Optional[str] = None,
    min_score: int = 0
) -> dict:
    """
    설문 응답 분석
    
    Args:
        responses: 응답 리스트
        category: 필터링할 카테고리 (선택)
        min_score: 최소 점수 필터 (기본값: 0)
    
    Returns:
        분석 결과 딕셔너리
    """
    filtered = responses
    if category:
        filtered = [r for r in filtered if r.get("category") == category]
    filtered = [r for r in filtered if r.get("score", 0) >= min_score]
    
    total = len(filtered)
    avg_score = sum(r.get("score", 0) for r in filtered) / total if total > 0 else 0
    
    return {
        "total": total,
        "average_score": round(avg_score, 2),
        "filter": {"category": category, "min_score": min_score}
    }

# %%
data = [
    {"category": "제품", "score": 5},
    {"category": "서비스", "score": 3},
    {"category": "제품", "score": 4},
]

print(analyze_survey(data))
print(analyze_survey(data, category="제품"))
print(analyze_survey(data, min_score=4))

# %% [markdown]
# ---
# ## Part 2: dataclass
# ---

# %% [markdown]
# ### 7.5 기본 dataclass
#
# `dataclass`는 데이터를 담는 클래스를 간결하게 정의하는 데코레이터입니다.

# %%
from dataclasses import dataclass, field, asdict

@dataclass
class Person:
    name: str
    age: int
    city: str = "서울"  # 기본값

# %%
# 인스턴스 생성
person1 = Person("홍길동", 25)
person2 = Person("김철수", 30, "부산")

print(person1)
print(person2)

# %%
# 속성 접근
print(person1.name)
print(person1.age)

# %%
# 자동 생성되는 메서드들
print(person1 == Person("홍길동", 25))  # __eq__ 자동 생성

# %% [markdown]
# ### 7.6 dataclass 옵션

# %%
@dataclass(frozen=True)  # 불변(immutable) 객체
class Point:
    x: int
    y: int

point = Point(10, 20)
print(point)
# point.x = 30  # 에러! frozen이므로 수정 불가

# %%
@dataclass
class Student:
    name: str
    scores: list[int] = field(default_factory=list)  # 가변 기본값
    
    def average(self) -> float:
        return sum(self.scores) / len(self.scores) if self.scores else 0.0

student = Student("홍길동")
student.scores.append(90)
student.scores.append(85)
print(f"{student.name}: 평균 {student.average()}")

# %% [markdown]
# ### 7.7 설문 분석 데이터 모델

# %%
from datetime import datetime
import json

@dataclass
class SurveyResponse:
    """개별 설문 응답"""
    id: int
    category: str
    text: str
    score: int
    timestamp: Optional[str] = None
    
    def is_positive(self) -> bool:
        """긍정 응답 여부"""
        return self.score >= 4
    
    def to_dict(self) -> dict:
        """딕셔너리로 변환"""
        return asdict(self)

# %%
response = SurveyResponse(
    id=1,
    category="제품",
    text="품질이 좋습니다",
    score=5,
    timestamp="2024-01-15"
)

print(response)
print(f"긍정 여부: {response.is_positive()}")
print(f"딕셔너리: {response.to_dict()}")

# %%
@dataclass
class CategoryStats:
    """카테고리별 통계"""
    name: str
    count: int
    avg_score: float
    positive_ratio: float
    
    def summary(self) -> str:
        return f"{self.name}: {self.count}건, 평균 {self.avg_score:.2f}, 긍정 {self.positive_ratio:.1%}"

# %%
stats = CategoryStats("제품", 24, 3.83, 0.625)
print(stats.summary())

# %%
@dataclass
class SurveyStats:
    """설문 분석 종합 통계"""
    total_responses: int
    average_score: float
    category_stats: list[CategoryStats] = field(default_factory=list)
    generated_at: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def to_json(self, indent: int = 2) -> str:
        """JSON 문자열로 변환"""
        data = {
            "total_responses": self.total_responses,
            "average_score": self.average_score,
            "category_stats": [asdict(cs) for cs in self.category_stats],
            "generated_at": self.generated_at
        }
        return json.dumps(data, ensure_ascii=False, indent=indent)

# %%
survey_stats = SurveyStats(total_responses=50, average_score=3.74)
survey_stats.category_stats.append(CategoryStats("제품", 24, 3.83, 0.625))
survey_stats.category_stats.append(CategoryStats("배송", 14, 3.79, 0.571))

print(survey_stats.to_json())

# %% [markdown]
# ---
# ## Part 3: Pydantic (검증 기능이 추가된 dataclass)
# ---

# %% [markdown]
# ### 7.8 Pydantic이란?
#
# - Python 타입 힌트를 사용한 **데이터 검증** 라이브러리
# - dataclass처럼 간결하지만 **자동 타입 검증** 추가
# - FastAPI, LangChain 등 주요 AI/웹 프레임워크에서 사용
# - JSON 직렬화/역직렬화 자동 지원
# - **AI 구조화 출력**: LLM 응답을 Pydantic 모델로 검증!

# %%
from pydantic import BaseModel, Field, field_validator, model_validator
from pydantic import ValidationError
from typing import Literal

# %% [markdown]
# ### 7.9 첫 번째 Pydantic 모델

# %%
class User(BaseModel):
    """사용자 모델"""
    name: str
    age: int
    email: str
    is_active: bool = True  # 기본값

# %%
# 인스턴스 생성
user = User(name="홍길동", age=25, email="hong@example.com")
print(user)
print(user.name)
print(user.age)

# %%
# 자동 타입 변환
user2 = User(name="김철수", age="30", email="kim@example.com")  # age는 문자열이지만...
print(user2.age)
print(type(user2.age))  # int로 자동 변환!

# %%
# 잘못된 타입 → 에러
try:
    invalid_user = User(name="이영희", age="서른", email="lee@example.com")
except ValidationError as e:
    print("유효성 검사 실패!")
    print(e)

# %% [markdown]
# ### 7.10 dataclass vs Pydantic 비교
#
# | 특성 | dataclass | Pydantic |
# |------|-----------|----------|
# | 타입 검증 | ❌ 없음 | ✅ 자동 검증 |
# | 타입 변환 | ❌ 없음 | ✅ 자동 변환 |
# | JSON 직렬화 | 수동 구현 | ✅ 내장 |
# | 커스텀 검증 | 수동 구현 | ✅ validator 데코레이터 |

# %%
# dataclass는 검증 안함
@dataclass
class UserDataclass:
    name: str
    age: int

dc_user = UserDataclass(name="홍길동", age="서른")  # 에러 없음!
print(dc_user.age)  # 그냥 문자열 "서른"

# %%
# Pydantic은 검증함
try:
    pydantic_user = User(name="홍길동", age="서른", email="test")
except ValidationError as e:
    print("Pydantic은 잘못된 값을 거부합니다:")
    print(e)

# %% [markdown]
# ### 7.11 Field로 상세 설정

# %%
class SurveyResponseModel(BaseModel):
    id: int = Field(..., description="응답 고유 ID")  # ... = 필수
    category: str = Field(..., min_length=1, max_length=50)
    text: str = Field(default="", max_length=1000)
    score: int = Field(..., ge=1, le=5, description="1-5점 만족도")
    
    # Field 옵션:
    # ge: greater than or equal (이상)
    # le: less than or equal (이하)
    # gt: greater than (초과)
    # lt: less than (미만)
    # min_length, max_length: 문자열 길이

# %%
# 유효한 응답
response = SurveyResponseModel(id=1, category="제품", text="좋아요", score=5)
print(response)

# %%
# 범위 벗어난 점수
try:
    invalid = SurveyResponseModel(id=2, category="서비스", score=10)
except ValidationError as e:
    print("점수 검증 실패:")
    print(e)

# %% [markdown]
# ### 7.12 중첩 모델 (Nested Models)

# %%
class CategoryStatsModel(BaseModel):
    """카테고리 통계"""
    name: str
    count: int
    avg_score: float

class ReportModel(BaseModel):
    """분석 보고서"""
    title: str
    summary: str
    total_responses: int
    average_score: float
    category_stats: list[CategoryStatsModel]
    insights: list[str] = []

# %%
# 중첩 모델 인스턴스 생성
report = ReportModel(
    title="2024년 1월 고객 만족도 분석",
    summary="전반적으로 만족도가 높음",
    total_responses=50,
    average_score=3.74,
    category_stats=[
        CategoryStatsModel(name="제품", count=24, avg_score=3.83),
        CategoryStatsModel(name="배송", count=14, avg_score=3.79),
    ],
    insights=["제품 만족도가 가장 높음"]
)

print(report.title)
print(f"카테고리 수: {len(report.category_stats)}")

# %% [markdown]
# ### 7.13 Validator (검증기)

# %%
class StrictSurveyResponse(BaseModel):
    id: int
    category: str
    text: str
    score: int
    
    @field_validator("category")
    @classmethod
    def validate_category(cls, v):
        """카테고리는 특정 값만 허용"""
        allowed = ["제품", "배송", "서비스", "기타"]
        if v not in allowed:
            raise ValueError(f"카테고리는 {allowed} 중 하나여야 합니다")
        return v
    
    @field_validator("text")
    @classmethod
    def validate_text(cls, v):
        """텍스트 정규화"""
        return v.strip()  # 앞뒤 공백 제거
    
    @field_validator("score")
    @classmethod
    def validate_score(cls, v):
        """점수 범위 체크"""
        if not 1 <= v <= 5:
            raise ValueError("점수는 1-5 사이여야 합니다")
        return v

# %%
# 유효한 응답
valid = StrictSurveyResponse(id=1, category="제품", text="  좋아요  ", score=5)
print(f"정규화된 텍스트: '{valid.text}'")  # 공백 제거됨

# %%
# 잘못된 카테고리
try:
    invalid = StrictSurveyResponse(id=2, category="잘못됨", text="테스트", score=3)
except ValidationError as e:
    print(e)

# %% [markdown]
# ### 7.14 model_validator (모델 전체 검증)

# %%
class DateRange(BaseModel):
    start_date: str
    end_date: str
    
    @model_validator(mode="after")
    def validate_dates(self):
        """시작일이 종료일보다 앞인지 검증"""
        if self.start_date > self.end_date:
            raise ValueError("시작일은 종료일보다 앞이어야 합니다")
        return self

# %%
# 유효한 범위
valid_range = DateRange(start_date="2024-01-01", end_date="2024-01-31")
print(valid_range)

# %%
# 잘못된 범위
try:
    invalid_range = DateRange(start_date="2024-02-01", end_date="2024-01-01")
except ValidationError as e:
    print(e)

# %% [markdown]
# ### 7.15 모델 직렬화/역직렬화

# %%
# 딕셔너리로 변환
report_dict = report.model_dump()
print(type(report_dict))
print(json.dumps(report_dict, ensure_ascii=False, indent=2))

# %%
# 특정 필드만 포함/제외
partial = report.model_dump(include={"title", "summary", "average_score"})
print(partial)

# %%
# JSON 문자열로 변환
json_str = report.model_dump_json(indent=2)
print(json_str[:300])

# %%
# 딕셔너리에서 모델 생성
data = {
    "title": "테스트 보고서",
    "summary": "테스트입니다",
    "total_responses": 10,
    "average_score": 4.0,
    "category_stats": [{"name": "A", "count": 5, "avg_score": 4.2}]
}

report_from_dict = ReportModel.model_validate(data)
print(report_from_dict.title)

# %%
# JSON 문자열에서 모델 생성
json_data = '{"title": "JSON 보고서", "summary": "...", "total_responses": 5, "average_score": 3.5, "category_stats": []}'
report_from_json = ReportModel.model_validate_json(json_data)
print(report_from_json.title)

# %% [markdown]
# ### 7.16 JSON 스키마 생성
#
# Pydantic 모델에서 JSON 스키마를 자동 생성할 수 있습니다.
# 이것이 **AI 구조화 출력**의 핵심입니다!

# %%
# Pydantic 모델에서 JSON 스키마 자동 생성
schema = ReportModel.model_json_schema()
print(json.dumps(schema, indent=2, ensure_ascii=False)[:800])

# %% [markdown]
# ### 7.17 Literal 타입 (특정 값만 허용)

# %%
class SentimentResult(BaseModel):
    """감성 분석 결과 스키마 - AI 구조화 출력에 사용"""
    sentiment: Literal["긍정", "부정", "중립"] = Field(description="감성 분류")
    confidence: float = Field(ge=0, le=1, description="신뢰도 0-1")
    keywords: list[str] = Field(default=[], description="핵심 키워드")
    summary: str = Field(description="한 줄 요약")

# %%
# 유효한 값
result = SentimentResult(
    sentiment="긍정",
    confidence=0.95,
    keywords=["좋음", "만족"],
    summary="전반적으로 긍정적입니다."
)
print(result)

# %%
# 잘못된 값
try:
    bad = SentimentResult(
        sentiment="매우좋음",  # Literal에 없는 값
        confidence=0.8,
        summary="테스트"
    )
except ValidationError as e:
    print(e)

# %% [markdown]
# ---
# ## 연습문제

# %% [markdown]
# ### 문제 1: Book dataclass
# 다음 속성을 가진 Book dataclass를 만드세요.
# - title: str
# - author: str
# - price: int
# - pages: int (기본값: 0)
# - is_ebook: bool (기본값: False)

# %%
# 여기에 코드 작성


# %% [markdown]
# ### 문제 2: UserProfile Pydantic 모델
# 다음 조건을 만족하는 UserProfile 모델을 만드세요.
# - name: 2-50자 문자열
# - email: 이메일 형식 (@포함 검증)
# - age: 0-150 정수
# - interests: 문자열 리스트 (선택)

# %%
class UserProfile(BaseModel):
    # 여기에 코드 작성
    pass


# %% [markdown]
# ### 문제 3: 주문 모델
# OrderItem과 Order 중첩 모델을 만드세요.
# - OrderItem: product_id, quantity, unit_price
# - Order: order_id, items(OrderItem 리스트), total_amount 자동 계산

# %%
class OrderItem(BaseModel):
    # 여기에 코드 작성
    pass

class Order(BaseModel):
    # 여기에 코드 작성
    pass


# %% [markdown]
# ### 문제 4: 상품 리뷰 분석 모델
# AI 구조화 출력용 상품 리뷰 분석 모델을 만드세요.
# - rating: 1-5 별점 예측
# - pros: 장점 리스트
# - cons: 단점 리스트
# - recommendation: 추천 여부 (bool)

# %%
class ReviewAnalysis(BaseModel):
    # 여기에 코드 작성
    pass



