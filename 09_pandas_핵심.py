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
# # 9. pandas 핵심 (분석 최소 세트)
#
# **학습 목표**: pandas로 데이터를 로드하고 기본 분석을 수행합니다.
#
# ---

# %% [markdown]
# ## 문법 설명
#
# ### 1. DataFrame 기본
#
# **정의**: 2차원 표 형태의 데이터 구조입니다.
#
# **생성**:
# ```python
# import pandas as pd
# df = pd.DataFrame({"컬럼1": [값1, 값2], "컬럼2": [값3, 값4]})
# ```
#
# **데이터 로드**:
# | 함수 | 설명 | 예시 |
# |------|------|------|
# | `pd.read_csv()` | CSV 파일 읽기 | `pd.read_csv("file.csv")` |
# | `pd.read_json()` | JSON 파일 읽기 | `pd.read_json("file.json")` |
# | `pd.read_excel()` | Excel 파일 읽기 | `pd.read_excel("file.xlsx")` |
#
# **기본 정보 확인**:
# | 메서드/속성 | 설명 |
# |------------|------|
# | `df.head(n)` | 처음 n개 행 |
# | `df.tail(n)` | 마지막 n개 행 |
# | `df.info()` | 데이터 타입, 결측치 정보 |
# | `df.describe()` | 기술 통계 |
# | `df.shape` | (행 수, 열 수) |
# | `df.columns` | 컬럼명 목록 |
#
# ---
#
# ### 2. 데이터 선택
#
# **컬럼 선택**:
# - `df["컬럼명"]`: Series 반환
# - `df[["컬럼1", "컬럼2"]]`: DataFrame 반환
#
# **행 선택**:
# - `df.loc[인덱스]`: 라벨 기반
# - `df.iloc[위치]`: 위치 기반
# - `df[조건]`: 불리언 인덱싱
#
# **조건 필터링**:
# ```python
# df[df["컬럼"] > 값]
# df[(df["컬럼1"] > 값1) & (df["컬럼2"] < 값2)]
# ```
#
# ---
#
# ### 3. 데이터 조작
#
# **결측치 처리**:
# | 메서드 | 설명 |
# |--------|------|
# | `df.isnull()` | 결측치 여부 (True/False) |
# | `df.dropna()` | 결측치 행 삭제 |
# | `df.fillna(값)` | 결측치 채우기 |
#
# **그룹화 및 집계**:
# ```python
# df.groupby("컬럼")["컬럼2"].agg(["mean", "sum", "count"])
# ```
#
# **정렬**:
# - `df.sort_values("컬럼")`: 값으로 정렬
# - `df.sort_index()`: 인덱스로 정렬
#
# **새 컬럼 추가**:
# ```python
# df["새컬럼"] = df["컬럼1"] + df["컬럼2"]
# ```
#
# ---
# ## 실습 시작
#
# 아래 실습을 통해 위 문법들을 직접 사용해봅니다.
#
# ---

# %% [markdown]
# ## 9.1 pandas 기초

# %% [markdown]
# ### 8.1.1 DataFrame 생성

# %%
import pandas as pd

# 딕셔너리에서 생성
data = {
    "이름": ["홍길동", "김철수", "이영희", "박민수"],
    "나이": [25, 30, 28, 35],
    "도시": ["서울", "부산", "서울", "대구"]
}

df = pd.DataFrame(data)
print(df)
print(type(df))

# %%
# 리스트에서 생성
rows = [
    ["홍길동", 25, "서울"],
    ["김철수", 30, "부산"],
    ["이영희", 28, "서울"]
]
df2 = pd.DataFrame(rows, columns=["이름", "나이", "도시"])
print(df2)

# %% [markdown]
# ### 8.1.2 CSV 파일 읽기

# %%
# CSV 파일 읽기
df = pd.read_csv("data/survey_responses.csv")
print(f"shape: {df.shape}")  # (행, 열)
df.head()

# %%
# 처음/마지막 N개 행
print("=== 처음 3개 ===")
print(df.head(3))

print("\n=== 마지막 3개 ===")
print(df.tail(3))

# %% [markdown]
# ### 8.1.3 기본 정보 확인

# %%
# 기본 정보
df.info()

# %%
# 통계 요약
df.describe()

# %%
# 컬럼 목록
print(df.columns.tolist())

# %%
# 데이터 타입
print(df.dtypes)

# %% [markdown]
# ---
# ## 8.2 데이터 선택과 필터링

# %% [markdown]
# ### 8.2.1 컬럼 선택

# %%
# 단일 컬럼 (Series)
print(df["category"])
print(type(df["category"]))

# %%
# 여러 컬럼 (DataFrame)
df[["id", "category", "satisfaction_score"]]

# %% [markdown]
# ### 8.2.2 행 선택

# %%
# 인덱스로 선택 (iloc: 정수 위치)
print(df.iloc[0])     # 첫 번째 행
print()
print(df.iloc[0:3])   # 0~2번째 행

# %%
# 라벨로 선택 (loc)
print(df.loc[0])      # 인덱스 라벨 0
print()
print(df.loc[0:2])    # 라벨 0~2 (끝 포함!)

# %%
# 특정 행, 열 선택
print(df.loc[0, "response_text"])
print(df.iloc[0, 2])  # 첫 행, 세 번째 열

# %% [markdown]
# ### 8.2.3 조건 필터링

# %%
# 단일 조건
high_score = df[df["satisfaction_score"] >= 4]
print(f"높은 점수 응답: {len(high_score)}건")
high_score.head()

# %%
# 여러 조건 (AND)
condition = (df["category"] == "제품") & (df["satisfaction_score"] >= 4)
filtered = df[condition]
print(f"제품 카테고리 & 고득점: {len(filtered)}건")
filtered.head()

# %%
# 여러 조건 (OR)
condition = (df["category"] == "제품") | (df["category"] == "배송")
filtered = df[condition]
print(f"제품 또는 배송: {len(filtered)}건")

# %%
# isin: 여러 값 중 하나
categories = ["제품", "배송"]
filtered = df[df["category"].isin(categories)]
print(f"제품/배송 카테고리: {len(filtered)}건")

# %%
# 문자열 포함 여부
contains_delivery = df[df["response_text"].str.contains("배송", na=False)]
print(f"'배송' 포함 응답: {len(contains_delivery)}건")
contains_delivery.head(3)

# %% [markdown]
# ---
# ## 8.3 정렬과 집계

# %% [markdown]
# ### 8.3.1 정렬

# %%
# 단일 컬럼 정렬
df.sort_values("satisfaction_score", ascending=False).head()

# %%
# 여러 컬럼 정렬
df.sort_values(["category", "satisfaction_score"], ascending=[True, False]).head(10)

# %% [markdown]
# ### 8.3.2 value_counts()

# %%
# 카테고리별 개수
print(df["category"].value_counts())

# %%
# 점수별 개수
print(df["satisfaction_score"].value_counts().sort_index())

# %%
# 비율로 표시
print(df["category"].value_counts(normalize=True))

# %% [markdown]
# ### 8.3.3 groupby와 집계

# %%
# 카테고리별 평균 점수
df.groupby("category")["satisfaction_score"].mean()

# %%
# 여러 집계 함수
df.groupby("category")["satisfaction_score"].agg(["count", "mean", "min", "max"])

# %%
# 사용자 정의 집계
df.groupby("category")["satisfaction_score"].agg(
    count="count",
    avg="mean",
    positive_ratio=lambda x: (x >= 4).sum() / len(x)
).round(2)

# %%
# 여러 컬럼 집계
df.groupby("category").agg({
    "id": "count",
    "satisfaction_score": ["mean", "std"]
}).round(2)

# %% [markdown]
# ---
# ## 8.4 결측치 처리

# %%
# 결측치 확인
print(df.isna().sum())

# %%
# 결측치가 있는 행 확인
df[df.isna().any(axis=1)]

# %%
# 결측치 채우기 예시
# df["column"] = df["column"].fillna("기본값")
# df["score"] = df["score"].fillna(df["score"].mean())

# 결측치 제거 예시
# df_clean = df.dropna()

# %% [markdown]
# ---
# ## 8.5 실습: 보고서용 요약표 만들기

# %% [markdown]
# ### 요약표 1: 카테고리별 종합 통계

# %%
def create_category_summary(df):
    """카테고리별 종합 통계 테이블 생성"""
    summary = df.groupby("category").agg(
        응답수=("id", "count"),
        평균점수=("satisfaction_score", "mean"),
        최소점수=("satisfaction_score", "min"),
        최대점수=("satisfaction_score", "max"),
        긍정비율=("satisfaction_score", lambda x: (x >= 4).sum() / len(x) * 100)
    ).round(2)
    
    # 전체 합계 행 추가
    total = pd.DataFrame({
        "응답수": [df.shape[0]],
        "평균점수": [df["satisfaction_score"].mean().round(2)],
        "최소점수": [df["satisfaction_score"].min()],
        "최대점수": [df["satisfaction_score"].max()],
        "긍정비율": [(df["satisfaction_score"] >= 4).sum() / len(df) * 100]
    }, index=["전체"])
    
    return pd.concat([summary, total])

# %%
summary_table1 = create_category_summary(df)
print("=== 카테고리별 종합 통계 ===")
print(summary_table1)

# %% [markdown]
# ### 요약표 2: 점수 분포

# %%
def create_score_distribution(df):
    """점수별 분포 테이블 생성"""
    score_counts = df["satisfaction_score"].value_counts().sort_index()
    score_pct = (score_counts / len(df) * 100).round(1)
    
    distribution = pd.DataFrame({
        "응답수": score_counts,
        "비율(%)": score_pct
    })
    
    # 누적 비율 추가
    distribution["누적(%)"] = distribution["비율(%)"].cumsum()
    
    return distribution

# %%
summary_table2 = create_score_distribution(df)
print("=== 점수 분포 ===")
print(summary_table2)

# %% [markdown]
# ### 요약표를 딕셔너리/JSON으로 변환

# %%
def tables_to_dict(table1, table2):
    """요약표들을 딕셔너리로 변환"""
    return {
        "category_stats": table1.reset_index().to_dict(orient="records"),
        "score_distribution": table2.reset_index().rename(
            columns={"index": "score"}
        ).to_dict(orient="records")
    }

# %%
summary_dict = tables_to_dict(summary_table1, summary_table2)

# JSON 저장
import json
with open("data/pandas_summary.json", "w", encoding="utf-8") as f:
    json.dump(summary_dict, f, ensure_ascii=False, indent=2)

print("요약 데이터 저장 완료: data/pandas_summary.json")

# %% [markdown]
# ### 추가: 키워드 빈도 분석

# %%
from collections import Counter

def analyze_keywords(df, text_column="response_text", top_n=10):
    """텍스트에서 키워드 빈도 분석"""
    all_text = " ".join(df[text_column].astype(str))
    
    # 간단한 토큰화 (공백 기준)
    words = all_text.split()
    
    # 불용어 제거 (2글자 이상만)
    words = [w for w in words if len(w) >= 2]
    
    # 빈도 계산
    word_counts = Counter(words)
    
    # DataFrame으로 변환
    top_words = pd.DataFrame(
        word_counts.most_common(top_n),
        columns=["키워드", "빈도"]
    )
    
    return top_words

# %%
keywords_df = analyze_keywords(df)
print("=== 상위 키워드 ===")
print(keywords_df)

# %% [markdown]
# ---
# ## 8.6 새 컬럼 추가와 데이터 변환

# %%
# 새 컬럼 추가
df["sentiment"] = df["satisfaction_score"].apply(
    lambda x: "긍정" if x >= 4 else ("부정" if x <= 2 else "중립")
)

# %%
# 확인
print(df["sentiment"].value_counts())

# %%
# apply로 복잡한 변환
def categorize_response(row):
    """응답을 종합 분류"""
    score = row["satisfaction_score"]
    category = row["category"]
    
    if score >= 4:
        return f"{category}_긍정"
    elif score <= 2:
        return f"{category}_부정"
    else:
        return f"{category}_중립"

df["detailed_label"] = df.apply(categorize_response, axis=1)
print(df["detailed_label"].value_counts())

# %% [markdown]
# ---
# ## 연습문제

# %% [markdown]
# ### 문제 1: 필터링
# 점수가 3점 이하인 부정적 응답만 필터링하고, 카테고리별 개수를 구하세요.

# %%
# 여기에 코드 작성


# %% [markdown]
# ### 문제 2: 시간대별 분석
# timestamp 컬럼에서 날짜만 추출하여 일별 응답 수를 계산하세요.

# %%
# 힌트: pd.to_datetime(), .dt.date
# 여기에 코드 작성


# %% [markdown]
# ### 문제 3: 크로스탭
# 카테고리와 sentiment 간의 교차표(crosstab)를 만드세요.

# %%
# 힌트: pd.crosstab()
# 여기에 코드 작성


# %% [markdown]
# ### 문제 4: 긍정 응답 텍스트 추출
# 점수 5점인 응답의 텍스트만 리스트로 추출하세요.

# %%
# 여기에 코드 작성


# %% [markdown]
# ### 정리

# %%
# 생성한 컬럼 제거 (다음 모듈에서 원본 데이터 사용)
df = df.drop(columns=["sentiment", "detailed_label"])
print("원본 컬럼으로 복원 완료")


# %%
