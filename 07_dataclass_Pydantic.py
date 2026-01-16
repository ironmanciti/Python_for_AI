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
# ---

# %% [markdown]
# ## 문법 설명
#
# ### 1. 타입 힌트 (Type Hints)
#
# **정의**: 변수나 함수의 타입을 명시하여 코드 가독성을 높입니다.
#
# **문법**:
# ```python
# 변수명: 타입 = 값
# def 함수명(매개변수: 타입) -> 반환타입:
#     코드
# ```
#
# **기본 타입**:
# - `int`, `float`, `str`, `bool`
# - `list[타입]`, `dict[키타입, 값타입]`
# - `Optional[타입]`: `None` 가능
# - `Union[타입1, 타입2]`: 여러 타입 중 하나
#
# **타입 임포트**:
# ```python
# from typing import List, Dict, Optional, Union
# ```
#
# ---
#
# ### 2. dataclass
#
# **정의**: 데이터 클래스를 간결하게 정의하는 데코레이터입니다.
#
# **문법**:
# ```python
# from dataclasses import dataclass
#
# @dataclass
# class 클래스명:
#     속성1: 타입
#     속성2: 타입 = 기본값
# ```
#
# **특징**:
# - `__init__()`, `__repr__()`, `__eq__()` 자동 생성
# - 타입 힌트 필수
# - 기본값 지정 가능
# - `frozen=True`: 불변 객체 (수정 불가)
#
# **주요 함수**:
# - `asdict()`: 딕셔너리로 변환
# - `astuple()`: 튜플로 변환
# - `fields()`: 필드 정보 가져오기
#
# ---
#
# ### 3. Pydantic
#
# **정의**: 데이터 검증과 직렬화를 자동으로 처리하는 라이브러리입니다.
#
# **문법**:
# ```python
# from pydantic import BaseModel, Field
#
# class 모델명(BaseModel):
#     필드1: 타입 = Field(..., description="설명")
#     필드2: 타입 = 기본값
# ```
#
# **특징**:
# - 자동 타입 검증 및 변환
# - 필수 필드 검증 (`...` 또는 `Field(...)`)
# - JSON 직렬화/역직렬화 자동 지원
# - `model_dump()`: 딕셔너리로 변환
# - `model_dump_json()`: JSON 문자열로 변환
# - `model_validate()`: 딕셔너리에서 객체 생성
#
# **Field 옵션**:
# - `default`: 기본값
# - `description`: 필드 설명
# - `gt`, `lt`: 크기 제한 (greater than, less than)
# - `min_length`, `max_length`: 길이 제한
#
# ---
# ## 실습 시작
#
# 아래 실습을 통해 위 문법들을 직접 사용해봅니다.
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

# %% [markdown]
# ### 7.4 함수 시그니처 
# | 구성 요소      | 의미                                   |
# | ------- | ------------------------------------ |
# | 함수 이름   | `analyze_survey`                     |
# | 매개변수 이름 | `responses`, `category`, `min_score` |
# | 매개변수 개수 | 3개                                   |
# | 매개변수 순서 | responses → category → min_score     |
# | 기본값     | `category=None`, `min_score=0`       |
# | 타입 힌트   | `list[dict]`, `Optional[str]`, `int` |
# | 반환 타입   | `-> dict`                            |

# %%
from typing import Optional

def analyze_survey(
    responses: list[dict],
    category: Optional[str] = None,
    min_score: int = 0
) -> dict:
    """
    설문 응답 분석 함수
    - 설문 응답 리스트를 받아 조건에 따라 필터링하고
    - 응답 개수와 평균 점수를 계산
    
    Args:
        responses (list[dict]):
            설문 응답 데이터 리스트
            예: [{"category": "서비스", "score": 5}, {...}]
        
        category (Optional[str]):
            필터링할 카테고리
            - None이면 카테고리 필터링을 하지 않음
        
        min_score (int):
            최소 점수 기준
            - 이 점수 이상인 응답만 분석 대상에 포함
    
    Returns:
        dict:
            분석 결과를 담은 딕셔너리
    """
    
    # 초기에는 전체 응답 데이터를 분석 대상으로 설정
    filtered = responses
    
    # 카테고리가 지정된 경우 해당 카테고리만 필터링
    if category:
        filtered = [
            r for r in filtered if r.get("category") == category
        ]
    
    # 최소 점수 조건을 만족하는 응답만 필터링
    filtered = [
        r for r in filtered if r.get("score", 0) >= min_score
    ]
    
    # 필터링 후 전체 응답 개수
    total = len(filtered)
    
    # 평균 점수 계산
    # - 응답이 없을 경우 0으로 처리 (ZeroDivisionError 방지)
    avg_score = (
        sum(r.get("score", 0) for r in filtered) / total
        if total > 0 else 0
    )
    
    # 분석 결과를 딕셔너리 형태로 반환
    return {
        "total": total,                             # 최종 응답 개수
        "average_score": round(avg_score, 2),       # 평균 점수 (소수점 2자리)
        "filter": {                                 # 적용된 필터 정보
            "category": category,
            "min_score": min_score
        }
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
#
# | 구분         | 기존 `class`   | `@dataclass`    |
# | ---------- | ------------ | --------------- |
# | 도입 버전      | 초기부터 존재      | **Python 3.7+** |
# | 목적         | **동작 + 데이터** | **데이터 중심 객체**   |
# | `__init__` | 직접 작성        | **자동 생성**       |
# | 타입 힌트      | 선택           | **필수**      |
# | 코드 길이      | 김            | **매우 짧음**       |
# | `__repr__` | 직접 작성        | 자동              |
# | `__eq__`   | 직접 작성        | 자동              |

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
# | 구분       | `@dataclass` | Pydantic                 |
# | -------- | ------------ | ------------------------ |
# | 등장 시기    | Python 3.7   | Python 3.8 (v1), 2023 v2 |
# | 주 목적     | 데이터 묶음       | **검증 + 파싱**              |
# | 런타임 검증   | ❌ 없음         | ✅ 강력                     |
# | JSON 직렬화 | 수동           | 자동                       |
# | 외부 입력    | ❌ 비추천        | **최적**                   |
# | 성능       | **매우 빠름**    | 느린 편                     |
# | 의존성      | 없음           | 있음                       |

# %%
# dataclass는 런타임 검증 안함
@dataclass
class UserDataclass:
    name: str
    age: int

dc_user = UserDataclass(name="홍길동", age="서른")  # 에러 없음!
print(dc_user.age)  # 그냥 문자열 "서른"

# %%
# Pydantic은 런타임 검증함
try:
    pydantic_user = User(name="홍길동", age="서른", email="test")
except ValidationError as e:
    print("Pydantic은 잘못된 값을 거부합니다:")
    print(e)

# %% [markdown]
# ### 7.11 Field로 상세 설정
# ```
#     # Field 옵션:
#     # ge: greater than or equal (이상)
#     # le: less than or equal (이하)
#     # gt: greater than (초과)
#     # lt: less than (미만)
#     # min_length, max_length: 문자열 길이
# ```

# %%
class SurveyResponseModel(BaseModel):
    id: int = Field(..., description="응답 고유 ID")  # ... = 필수
    category: str = Field(..., min_length=1, max_length=50)
    text: str = Field(default="", max_length=1000)
    score: int = Field(..., ge=1, le=5, description="1-5점 만족도")

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
from pydantic import BaseModel

class CategoryStatsModel(BaseModel):
    """
    카테고리별 통계 정보를 표현하는 모델
    - 특정 카테고리에 대한 응답 수와 평균 점수를 담음
    """
    name: str    # 카테고리 이름 (예: "서비스", "가격", "디자인")
    count: int   # 해당 카테고리에 속한 응답 개수
    avg_score: float   # 해당 카테고리의 평균 점수
    
class ReportModel(BaseModel):
    """
    설문 분석 결과를 담는 보고서 모델
    - 전체 요약 정보와 카테고리별 통계, 인사이트를 포함
    """
    title: str   # 보고서 제목
    summary: str   # 분석 결과에 대한 요약 설명
    total_responses: int   # 전체 설문 응답 수
    average_score: float   # 전체 설문 평균 점수
    category_stats: list[CategoryStatsModel]   # 카테고리별 통계 목록
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
# ### 7.13 모델 직렬화

# %%
# 딕셔너리로 변환
report_dict = report.model_dump()
print(type(report_dict))
print(json.dumps(report_dict, ensure_ascii=False, indent=2))

# %%
# JSON 문자열로 변환
json_str = report.model_dump_json(indent=2)
print(json_str[:300])

# %% [markdown]
# ### 7.14 Validator (검증기)
#
# | 구분    | `field_validator` | `model_validator` |
# | ----- | ----------------- | ----------------- |
# | 검증 대상 | **단일 필드**         | **모델 전체**         |
# | 접근 범위 | 값 1개              | 모든 필드             |
# | 대표 용도 | 범위, 형식, 정규화       | 필드 간 조건           |
# | 반환 값  | 검증된 값             | `self`            |
# | 실행 시점 | 필드별               | 전체 필드             |
#

# %%
from pydantic import BaseModel, field_validator, model_validator  
from datetime import datetime

class StrictSurveyResponse(BaseModel):  # 설문 응답 + 날짜 범위를 함께 검증하는 모델
    id: int              # 설문 응답의 고유 ID
    category: str        # 설문 카테고리 (허용된 값만 가능)
    text: str            # 응답자가 작성한 텍스트 내용
    score: int           # 설문 점수 (1~5 사이 정수)
    start_date: str      # 시작 날짜 (예: "2024-01-01")
    end_date: str        # 종료 날짜 (예: "2024-01-31")
    
    @field_validator("category")        # category 필드에 대한 검증기
    @classmethod
    def validate_category(cls, v):      # 카테고리 값 검증 메서드
        allowed = ["제품", "배송", "서비스", "기타"]  # 허용 가능한 카테고리 목록
        if v not in allowed:             # 허용 목록에 없는 경우
            raise ValueError(f"카테고리는 {allowed} 중 하나여야 합니다")  # 오류 발생
        return v                         # 검증 통과 시 값 반환
    
    @field_validator("text")            # text 필드에 대한 검증기
    @classmethod
    def validate_text(cls, v):           # 텍스트 정규화 메서드
        return v.strip()                 # 문자열 앞뒤 공백 제거
    
    @field_validator("score")           # score 필드에 대한 검증기
    @classmethod
    def validate_score(cls, v):          # 점수 범위 검증 메서드
        if not 1 <= v <= 5:              # 점수가 1~5 범위를 벗어난 경우
            raise ValueError("점수는 1-5 사이여야 합니다")  # 오류 발생
        return v                         # 검증 통과 시 값 반환

    @field_validator("start_date", "end_date")
    @classmethod
    def validate_date_format(cls, v):
        try:
            datetime.strptime(v, "%Y-%m-%d")
        except ValueError:
            raise ValueError("날짜 형식은 YYYY-MM-DD 여야 합니다")
        return v

    @model_validator(mode="after")      # 모든 필드 검증 후 실행되는 모델 검증기
    def validate_dates(self):            # 시작일과 종료일의 관계를 검증하는 메서드
        if self.start_date > self.end_date:  # 시작일이 종료일보다 늦은 경우
            raise ValueError("시작일은 종료일보다 앞이어야 합니다")  # 오류 발생
        return self                      # 검증 통과 시 자기 자신 반환

# %%
# 유효한 응답
valid = StrictSurveyResponse(id=1, category="제품", text="  좋아요  ", score=5, start_date="2024-01-01", end_date="2024-01-31")
print(f"정규화된 텍스트: '{valid.text}'")  # 공백 제거됨

# %%
# 잘못된 카테고리
try:
    invalid = StrictSurveyResponse(id=2, category="잘못됨", text="테스트", score=3, start_date="2024-01-01", end_date="2024-01-31")
except ValidationError as e:
    print(e)

# %%
from pydantic import ValidationError  # Pydantic 검증 에러 클래스

# 정상 데이터 (model_validator 통과)
valid_response = StrictSurveyResponse(       # 모든 필드 + 날짜 조건 만족
    id=1,                                    # 설문 응답 ID
    category="서비스",                        # 허용된 카테고리
    text="  만족합니다  ",                    # 공백 포함 → field_validator에서 strip 처리
    score=5,                                 # 점수 범위 정상
    start_date="2024-01-01",                 # 시작일
    end_date="2024-01-31"                    # 종료일
)

print(valid_response)                        # 정상 생성된 모델 출력

# %%
try:
    invalid_response = StrictSurveyResponse(  # 날짜 관계가 잘못된 데이터
        id=2,                                 # 설문 응답 ID
        category="배송",                      # 허용된 카테고리
        text="빠른 배송이었어요",              # 텍스트
        score=4,                              # 점수 정상
        start_date="2024-02-01",              # ❌ 시작일이 종료일보다 늦음
        end_date="2024-01-01"                 # 종료일
    )
except ValidationError as e:                  # model_validator에서 발생한 에러
    print(e)                                  # 에러 메시지 출력

# %% [markdown]
# ### 7.15 JSON 스키마 생성
#
# Pydantic 모델에서 JSON 스키마를 자동 생성할 수 있습니다.
# 이것이 **AI 구조화 출력**의 핵심입니다!

# %%
# Pydantic 모델에서 JSON 스키마 자동 생성
schema = ReportModel.model_json_schema()
print(json.dumps(schema, indent=2, ensure_ascii=False)[:800])

# %% [markdown]
# ### 7.16 Literal 타입 (특정 값만 허용)

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





