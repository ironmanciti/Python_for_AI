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
# # 3. 제어문: 조건문과 반복문
#
# **학습 목표**: if/for 문을 활용하여 데이터를 조건별로 처리하고 반복 작업을 수행합니다.
# ---

# %% [markdown]
# ## 문법 설명
#
# ### 1. 조건문 (if/elif/else)
#
# **정의**: 조건에 따라 다른 코드를 실행합니다.
#
# **문법**:
# ```python
# if 조건1:
#     코드1
# elif 조건2:
#     코드2
# else:
#     코드3
# ```
#
# **비교 연산자**:
# | 연산자 | 의미 | 예시 |
# |--------|------|------|
# | `==` | 같음 | `a == b` |
# | `!=` | 다름 | `a != b` |
# | `<`, `<=` | 작음, 작거나 같음 | `a < b` |
# | `>`, `>=` | 큼, 크거나 같음 | `a > b` |
#
# **논리 연산자**:
# | 연산자 | 의미 | 예시 |
# |--------|------|------|
# | `and` | 논리곱 | `a and b` |
# | `or` | 논리합 | `a or b` |
# | `not` | 논리부정 | `not a` |
#
# **in 연산자**: 멤버십 테스트
# - `x in 리스트`: 리스트에 포함 여부
# - `"문자열" in 문자열`: 부분 문자열 포함 여부
#
# **조건부 표현식 (삼항 연산자)**:
# ```python
# 값 = 표현식1 if 조건 else 표현식2
# ```
#
# ---
#
# ### 2. 반복문 (for)
#
# **정의**: 시퀀스(리스트, 문자열 등)의 각 요소를 순회합니다.
#
# **문법**:
# ```python
# for 항목 in 반복가능객체:
#     코드
# ```
#
# **range() 함수**:
# | 문법 | 의미 | 예시 |
# |------|------|------|
# | `range(끝)` | 0부터 끝-1까지 | `range(5)` → `0,1,2,3,4` |
# | `range(시작, 끝)` | 시작부터 끝-1까지 | `range(1,5)` → `1,2,3,4` |
# | `range(시작, 끝, 증가분)` | 증가분만큼 건너뛰기 | `range(0,10,2)` → `0,2,4,6,8` |
#
# **enumerate() 함수**: 인덱스와 값 동시 순회
# ```python
# for 인덱스, 값 in enumerate(리스트):
#     코드
# ```
#
# **zip() 함수**: 여러 시퀀스 동시 순회
# ```python
# for a, b in zip(리스트1, 리스트2):
#     코드
# ```
#
# **중첩 반복문**: 반복문 안에 반복문
# ```python
# for i in range(3):
#     for j in range(3):
#         코드
# ```
#
# **반복문 제어**:
# - `break`: 반복문 즉시 종료
# - `continue`: 현재 반복 건너뛰고 다음 반복으로
# - `else`: 반복문이 정상 종료되면 실행 (break로 종료되면 실행 안됨)
#
# ---
# ## 실습 시작
#
# 아래 실습을 통해 위 문법들을 직접 사용해봅니다.
#
# ---

# %% [markdown]
# ## 3.1 조건문 (if/elif/else)
#
# 조건에 따라 다른 코드를 실행합니다.

# %% [markdown]
# ### 3.1.1 기본 if 문

# %%
score = 85

if score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")
elif score >= 70:
    print("C학점")
elif score >= 60:
    print("D학점")
else:
    print("F학점")

# %% [markdown]
# ### 3.1.2 비교 연산자와 in 연산자

# %%
# 숫자 비교
age = 25
if age >= 20:
    print("성인입니다")

# %%
# 문자열 비교
name = "Python"
if name == "Python":
    print("파이썬입니다!")

# %%
# in 연산자: 포함 여부 확인
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("바나나가 있습니다!")

# %%
# 문자열에서 in 연산자
text = "Hello, Python World!"
if "Python" in text:
    print("Python이 포함되어 있습니다!")

# %% [markdown]
# ### 3.1.3 논리 연산자 (and, or, not)

# %%
age = 25
income = 3000

# and: 둘 다 True여야 True
if age >= 20 and income >= 2500:
    print("대출 신청 가능")

# %%
# or: 하나만 True여도 True
score = 85
if score >= 90 or score >= 80:
    print("장학금 대상")

# %%
# not: 반대
is_holiday = False
if not is_holiday:
    print("오늘은 근무일입니다")

# %%
# 복합 조건
age = 25
has_license = True
has_car = False

if age >= 18 and has_license and (has_car or True):
    print("운전 가능")

# %% [markdown]
# ### 3.1.4 중첩 if 문

# %%
score = 85
attendance = 90

if score >= 60:
    if attendance >= 80:
        print("수료")
    else:
        print("출석 미달로 미수료")
else:
    print("성적 미달로 미수료")

# %% [markdown]
# ### 3.1.5 조건부 표현식 (삼항 연산자)

# %%
age = 20

# 일반 if-else
if age >= 18:
    status = "성인"
else:
    status = "미성년"
print(status)

# %%
# 조건부 표현식 (한 줄로)
status = "성인" if age >= 18 else "미성년"
print(status)

# %%
# 실용적인 예: 절대값
num = -5
abs_num = num if num >= 0 else -num
print(abs_num)

# %% [markdown]
# ---
# ## 3.2 반복문 (for)
#
# 시퀀스(리스트, 문자열 등)의 각 요소를 순회합니다.

# %% [markdown]
# ### 3.2.1 기본 for 문

# %%
# 리스트 순회
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# %%
# 문자열 순회
for char in "Python":
    print(char, end=" ")

# %%
# 딕셔너리 순회
person = {"name": "홍길동", "age": 25, "city": "서울"}
for key in person:
    print(f"{key}: {person[key]}")

# %%
# items()로 키-값 동시 순회
for key, value in person.items():
    print(f"{key} = {value}")

# %% [markdown]
# ### 3.2.2 range() 함수

# %%
# range(끝): 0부터 끝-1까지
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4

# %%
# range(시작, 끝): 시작부터 끝-1까지
for i in range(1, 6):
    print(i, end=" ")  # 1 2 3 4 5

# %%
# range(시작, 끝, 증가분)
for i in range(0, 10, 2):
    print(i, end=" ")  # 0 2 4 6 8

# %%
# 역순
for i in range(5, 0, -1):
    print(i, end=" ")  # 5 4 3 2 1

# %%
# 인덱스로 리스트 접근
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# %% [markdown]
# ### 3.2.3 enumerate() 함수
#
# 인덱스와 값을 동시에 얻을 수 있습니다.

# %%
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# %%
# 시작 인덱스 지정
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# %% [markdown]
# ### 3.2.4 zip() 함수
#
# 여러 시퀀스를 동시에 순회합니다.

# %%
names = ["홍길동", "김철수", "이영희"]
ages = [25, 30, 28]
cities = ["서울", "부산", "대구"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}({age}세) - {city}")

# %% [markdown]
# ### 3.2.5 break와 continue

# %%
# break: 반복문 종료
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")  # 0 1 2 3 4

# %%
# continue: 현재 반복 건너뛰기
for i in range(10):
    if i % 2 == 0:  # 짝수 건너뛰기
        continue
    print(i, end=" ")  # 1 3 5 7 9

# %%
# 특정 조건에서 검색 후 종료
numbers = [12, 45, 78, 32, 56, 89, 23]
target = 32

for i, num in enumerate(numbers):
    if num == target:
        print(f"찾았습니다! 인덱스: {i}")
        break
else:
    # break 없이 루프가 끝났을 때
    print("찾지 못했습니다")

# %% [markdown]
# ### 3.2.6 중첩 for 문

# %%
# 구구단
for i in range(2, 4):  # 2단, 3단
    print(f"\n=== {i}단 ===")
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")

# %%
# 2차원 리스트 순회
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for num in row:
        print(num, end=" ")
    print()  # 줄바꿈

# %% [markdown]
# ---
# ## 3.3 실습: 규칙 기반 분류기
#
# 키워드에 따라 설문 응답을 자동으로 분류하는 규칙 기반 분류기를 만듭니다.

# %% [markdown]
# ### 실습 목표
# 1. 텍스트에 포함된 키워드로 감성 분류 (긍정/부정/중립)
# 2. 카테고리 자동 태깅
# 3. 분류 결과 집계

# %%
# 설문 응답 데이터
responses = [
    "배송이 빠르고 포장이 꼼꼼했습니다. 매우 만족합니다!",
    "고객센터 응대가 친절했어요. 문의 해결이 빨랐습니다.",
    "품질이 기대 이하였습니다. 사진과 달라요.",
    "배송 지연이 있었습니다. 예상보다 3일 늦게 도착.",
    "교환 절차가 복잡했습니다. 개선이 필요해요.",
    "가격 대비 품질이 좋습니다. 재구매 의향 있어요.",
    "색상이 예쁘고 사이즈도 딱 맞아요!",
    "새벽배송 너무 좋아요. 신선하게 받았습니다.",
    "반품 처리가 신속했습니다. 감사합니다.",
    "앱 사용이 불편합니다. UI 개선 바랍니다.",
]

# %% [markdown]
# ### Step 1: 감성 분류 규칙 정의

# %%
# 감성 키워드 정의
positive_keywords = ["좋", "만족", "빠르", "친절", "예쁘", "감사", "추천", "최고", "신선", "신속"]
negative_keywords = ["불", "안", "늦", "지연", "복잡", "이하", "달라", "불편", "훼손", "아쉬"]

# %%
def classify_sentiment(text):
    """
    텍스트의 감성을 분류
    Returns: "긍정", "부정", "중립"
    """
    positive_count = 0
    negative_count = 0
    
    # 긍정 키워드 체크
    for keyword in positive_keywords:
        if keyword in text:
            positive_count = positive_count + 1
    
    # 부정 키워드 체크
    for keyword in negative_keywords:
        if keyword in text:
            negative_count = negative_count + 1
    
    # 판정
    if positive_count > negative_count:
        return "긍정"
    elif negative_count > positive_count:
        return "부정"
    else:
        return "중립"

# %%
# 테스트
test_texts = [
    "정말 좋아요! 만족합니다.",
    "불편하고 안 좋아요.",
    "그냥 보통이에요."
]

for text in test_texts:
    result = classify_sentiment(text)
    print(f"'{text}' → {result}")

# %% [markdown]
# ### Step 2: 카테고리 자동 태깅

# %%
# 카테고리별 키워드
category_keywords = {
    "배송": ["배송", "택배", "도착", "새벽배송", "포장"],
    "품질": ["품질", "색상", "사이즈", "디자인", "소재"],
    "서비스": ["고객센터", "응대", "문의", "교환", "반품", "AS"],
    "가격": ["가격", "비싸", "저렴", "할인", "가성비"],
    "앱/UI": ["앱", "UI", "사용", "불편"]
}

# %%
def auto_tag_category(text):
    """
    텍스트에서 자동으로 카테고리 태그 추출
    Returns: 매칭된 카테고리 리스트
    """
    matched_categories = []
    
    for category, keywords in category_keywords.items():
        for keyword in keywords:
            if keyword in text:
                matched_categories.append(category)
                break  # 한 카테고리에서 하나만 매칭되면 OK
    
    # 매칭된 카테고리가 없으면 "기타"
    if len(matched_categories) == 0:
        matched_categories.append("기타")
    
    return matched_categories

# %%
# 테스트
for response in responses[:3]:
    tags = auto_tag_category(response)
    print(f"응답: {response[:30]}...")
    print(f"태그: {tags}")
    print()

# %% [markdown]
# ### Step 3: 전체 응답 분류

# %%
def classify_responses(responses):
    """
    모든 응답을 분류하여 결과 반환
    """
    results = []
    
    for i, response in enumerate(responses, start=1):
        sentiment = classify_sentiment(response)
        categories = auto_tag_category(response)
        
        result = {
            "id": i,
            "text": response,
            "sentiment": sentiment,
            "categories": categories
        }
        results.append(result)
    
    return results

# %%
# 분류 실행
classified = classify_responses(responses)

# 결과 출력
print("=" * 60)
print("응답 분류 결과")
print("=" * 60)

for item in classified:
    print(f"\n[{item['id']}] {item['sentiment']}")
    print(f"   카테고리: {', '.join(item['categories'])}")
    print(f"   내용: {item['text'][:40]}...")

# %% [markdown]
# ### Step 4: 분류 결과 집계

# %%
def summarize_classification(classified_results):
    """
    분류 결과 집계
    """
    # 감성별 집계
    sentiment_counts = {}
    for item in classified_results:
        sent = item["sentiment"]
        sentiment_counts[sent] = sentiment_counts.get(sent, 0) + 1
    
    # 카테고리별 집계
    category_counts = {}
    for item in classified_results:
        for cat in item["categories"]:
            category_counts[cat] = category_counts.get(cat, 0) + 1
    
    # 감성-카테고리 교차 집계
    cross_counts = {}
    for item in classified_results:
        sent = item["sentiment"]
        for cat in item["categories"]:
            key = f"{sent}_{cat}"
            cross_counts[key] = cross_counts.get(key, 0) + 1
    
    return {
        "sentiment": sentiment_counts,
        "category": category_counts,
        "cross": cross_counts
    }

# %%
# 집계 실행
summary = summarize_classification(classified)

print("\n" + "=" * 40)
print("감성 분포")
print("=" * 40)
for sent, count in summary["sentiment"].items():
    ratio = count / len(classified) * 100
    bar = "█" * int(ratio / 5)
    print(f"  {sent}: {count}건 ({ratio:.1f}%) {bar}")

print("\n" + "=" * 40)
print("카테고리 분포")
print("=" * 40)
for cat, count in sorted(summary["category"].items(), key=lambda x: -x[1]):
    print(f"  {cat}: {count}건")

# %% [markdown]
# ### Step 5: 개선된 분류기 (가중치 적용)

# %%
def classify_sentiment_weighted(text):
    """
    가중치가 적용된 감성 분류
    강한 표현에는 더 높은 가중치
    """
    # 가중치가 있는 키워드
    positive_weighted = {
        "최고": 2, "만족": 2, "추천": 2, "완벽": 3,
        "좋": 1, "빠르": 1, "친절": 1, "예쁘": 1, "감사": 1
    }
    negative_weighted = {
        "최악": 3, "불만": 2, "화나": 2,
        "불편": 1, "늦": 1, "지연": 1, "복잡": 1, "실망": 2
    }
    
    positive_score = 0
    negative_score = 0
    
    for keyword, weight in positive_weighted.items():
        if keyword in text:
            positive_score = positive_score + weight
    
    for keyword, weight in negative_weighted.items():
        if keyword in text:
            negative_score = negative_score + weight
    
    # 점수 차이로 판정
    diff = positive_score - negative_score
    
    if diff >= 2:
        return "강한 긍정"
    elif diff > 0:
        return "긍정"
    elif diff <= -2:
        return "강한 부정"
    elif diff < 0:
        return "부정"
    else:
        return "중립"

# %%
# 가중치 분류 테스트
test_cases = [
    "완벽합니다! 최고예요!",
    "좋아요",
    "그냥 보통",
    "불편해요",
    "최악입니다. 불만이에요."
]

for text in test_cases:
    result = classify_sentiment_weighted(text)
    print(f"'{text}' → {result}")

# %% [markdown]
# ---
# ## 연습문제

# %% [markdown]
# ### 문제 1: 학점 계산기
# 점수(0-100)를 입력받아 학점을 반환하는 함수를 작성하세요.
# - 90 이상: A
# - 80 이상: B
# - 70 이상: C
# - 60 이상: D
# - 60 미만: F

# %%
def get_grade(score):
    # 여기에 코드 작성
    pass

# 테스트
for s in [95, 85, 75, 65, 55]:
    print(f"{s}점 → {get_grade(s)}")


# %% [markdown]
# ### 문제 2: FizzBuzz
# 1부터 30까지:
# - 3의 배수면 "Fizz"
# - 5의 배수면 "Buzz"  
# - 3과 5의 공배수면 "FizzBuzz"
# - 그 외에는 숫자 출력

# %%
# 여기에 코드 작성


# %% [markdown]
# ### 문제 3: 소수 판별기
# 주어진 숫자가 소수인지 판별하는 함수를 작성하세요.
# (소수: 1과 자기 자신으로만 나누어지는 1보다 큰 자연수)

# %%
def is_prime(n):
    # 여기에 코드 작성
    pass

# 테스트
for n in [2, 3, 4, 5, 10, 11, 13, 15, 17]:
    result = "소수" if is_prime(n) else "합성수"
    print(f"{n}: {result}")


# %% [markdown]
# ### 문제 4: 2차원 리스트 합계
# 아래 2차원 리스트의 모든 숫자 합계를 구하세요.

# %%
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 여기에 코드 작성


# %% [markdown]
# ### 문제 5: 패턴 출력
# 다음 패턴을 출력하세요 (n=5):
# ```
# *
# **
# ***
# ****
# *****
# ```

# %%
n = 5
# 여기에 코드 작성


# %% [markdown]
# ### 문제 6: 키워드 우선순위 분류기
# 여러 카테고리가 매칭될 때 우선순위가 높은 카테고리만 반환하도록 수정하세요.
# 우선순위: 품질 > 배송 > 서비스 > 가격 > 앱/UI > 기타

# %%
def classify_with_priority(text):
    """
    우선순위에 따라 하나의 카테고리만 반환
    """
    priority = ["품질", "배송", "서비스", "가격", "앱/UI", "기타"]
    # 여기에 코드 작성
    pass


# %%
