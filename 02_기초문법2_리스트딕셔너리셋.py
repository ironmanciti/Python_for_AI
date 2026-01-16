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
# # 2. 기초 문법 2: 리스트, 딕셔너리, 셋
#
# **학습 목표**: Python의 핵심 자료구조를 익히고, 데이터 집계 패턴을 이해합니다.
#
# ---

# %% [markdown]
# ## 문법 설명
#
# ### 1. 리스트 (List)
#
# **정의**: 순서가 있는 데이터 모음입니다. 변경 가능(mutable)한 자료구조입니다.
#
# **문법**:
# ```python
# 리스트명 = [요소1, 요소2, 요소3]
# ```
#
# **특징**:
# - 인덱스로 접근: `리스트[인덱스]` (0부터 시작)
# - 슬라이싱: `리스트[시작:끝:증가분]`
# - 다양한 타입 혼합 가능
#
# **주요 메서드**:
# | 메서드 | 설명 | 예시 |
# |--------|------|------|
# | `append(x)` | 끝에 추가 | `lst.append(1)` |
# | `insert(i, x)` | i번 위치에 삽입 | `lst.insert(0, 1)` |
# | `remove(x)` | 값으로 삭제 | `lst.remove(1)` |
# | `pop([i])` | 인덱스로 삭제 (반환) | `lst.pop()` |
# | `sort()` | 정렬 (원본 변경) | `lst.sort()` |
# | `sorted()` | 정렬 (새 리스트 반환) | `sorted(lst)` |
# | `reverse()` | 역순 | `lst.reverse()` |
# | `index(x)` | 값의 위치 | `lst.index(1)` |
# | `count(x)` | 값의 개수 | `lst.count(1)` |
# | `extend(iterable)` | 리스트 확장 | `lst.extend([1,2])` |
#
# **복사 주의**: `copy()`, `[:]`, `list()` 사용 (참조 복사 방지)
#
# ---
#
# ### 2. 딕셔너리 (Dictionary)
#
# **정의**: 키-값(key-value) 쌍으로 이루어진 자료구조입니다. 순서가 있습니다(Python 3.7+).
#
# **문법**:
# ```python
# 딕셔너리명 = {"키1": 값1, "키2": 값2}
# ```
#
# **특징**:
# - 키는 불변(immutable) 타입만 가능 (str, int, tuple 등)
# - 값은 모든 타입 가능
# - 키는 중복 불가
#
# **접근 방법**:
# - `딕셔너리["키"]`: 키가 없으면 `KeyError`
# - `딕셔너리.get("키", 기본값)`: 키가 없으면 기본값 반환
#
# **주요 메서드**:
# | 메서드 | 설명 | 예시 |
# |--------|------|------|
# | `keys()` | 모든 키 | `d.keys()` |
# | `values()` | 모든 값 | `d.values()` |
# | `items()` | 모든 키-값 쌍 | `d.items()` |
# | `get(k, default)` | 값 가져오기 | `d.get("key", 0)` |
# | `pop(k)` | 키 삭제 (값 반환) | `d.pop("key")` |
# | `update(other)` | 딕셔너리 병합 | `d.update(d2)` |
# | `in` 연산자 | 키 존재 확인 | `"key" in d` |
#
# **집계 패턴**: `딕셔너리[키] = 딕셔너리.get(키, 0) + 1`
#
# ---
#
# ### 3. 셋 (Set)
#
# **정의**: 중복을 허용하지 않는 순서 없는 집합입니다.
#
# **문법**:
# ```python
# 셋명 = {요소1, 요소2, 요소3}
# ```
#
# **특징**:
# - 중복 자동 제거
# - 순서 없음 (Python 3.7+에서는 삽입 순서 유지)
# - 요소는 불변(immutable) 타입만 가능
#
# **집합 연산**:
# | 연산자 | 메서드 | 의미 | 예시 |
# |--------|--------|------|------|
# | `\|` | `union()` | 합집합 | `a \| b` |
# | `&` | `intersection()` | 교집합 | `a & b` |
# | `-` | `difference()` | 차집합 | `a - b` |
#
# **주요 메서드**:
# - `add(x)`: 요소 추가
# - `remove(x)`: 요소 삭제 (없으면 에러)
# - `discard(x)`: 요소 삭제 (없어도 에러 없음)
# - `in` 연산자: 요소 존재 확인
#
# ---
#
# ### 4. 리스트 컴프리헨션 (List Comprehension)
#
# **정의**: 리스트를 간결하게 생성하는 문법입니다.
#
# **문법**:
# ```python
# [표현식 for 항목 in 반복가능객체]
# [표현식 for 항목 in 반복가능객체 if 조건]
# [표현식1 if 조건 else 표현식2 for 항목 in 반복가능객체]
# ```
#
# **예시**:
# - 기본: `[i**2 for i in range(5)]` → `[0, 1, 4, 9, 16]`
# - 조건부: `[i for i in range(10) if i % 2 == 0]` → `[0, 2, 4, 6, 8]`
# - 삼항: `["짝수" if i%2==0 else "홀수" for i in range(5)]`
# - 중첩: `[i*j for i in range(2) for j in range(3)]`
#
# **딕셔너리/셋 컴프리헨션**:
# - 딕셔너리: `{k: v for k, v in items}`
# - 셋: `{x for x in iterable}`
#
# ---
# ## 실습 시작
#
# 아래 실습을 통해 위 문법들을 직접 사용해봅니다.
#
# ---

# %% [markdown]
# ## 2.1 리스트 (List)
#
# 리스트는 순서가 있는 데이터 모음입니다. 대괄호 `[]`로 생성합니다.

# %%
# 리스트 생성
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]  # 다양한 타입 혼합 가능

print(fruits)
print(type(fruits))

# %% [markdown]
# ### 2.1.1 리스트 인덱싱과 슬라이싱

# %%
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# 인덱싱
print(fruits[0])    # apple (첫 번째)
print(fruits[-1])   # elderberry (마지막)
print(fruits[2])    # cherry (세 번째)

# %%
# 슬라이싱
print(fruits[1:3])   # ['banana', 'cherry']
print(fruits[:2])    # ['apple', 'banana']
print(fruits[2:])    # ['cherry', 'date', 'elderberry']
print(fruits[::2])   # ['apple', 'cherry', 'elderberry'] (2칸씩)

# %% [markdown]
# ### 2.1.2 리스트 수정

# %%
numbers = [1, 2, 3, 4, 5]

# 요소 변경
numbers[0] = 100
print(numbers)  # [100, 2, 3, 4, 5]

# 슬라이스로 여러 요소 변경
numbers[1:3] = [200, 300]
print(numbers)  # [100, 200, 300, 4, 5]

# %% [markdown]
# ### 2.1.3 리스트 주요 메서드

# %%
# append: 끝에 요소 추가
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

# %%
# insert: 특정 위치에 삽입
fruits.insert(1, "apricot")
print(fruits)  # ['apple', 'apricot', 'banana', 'cherry']

# %%
# extend: 다른 리스트 확장
fruits.extend(["date", "elderberry"])
print(fruits)

# %%
# remove: 값으로 삭제
fruits.remove("apricot")
print(fruits)

# %%
# pop: 인덱스로 삭제 (삭제된 값 반환)
removed = fruits.pop()  # 마지막 요소
print(f"삭제됨: {removed}")
print(fruits)

# %%
# pop: 특정 인덱스 삭제
removed = fruits.pop(1)  # 두 번째 요소
print(f"삭제됨: {removed}")
print(fruits)

# %%
# sort: 정렬
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)  # 오름차순

numbers.sort(reverse=True)
print(numbers)  # 내림차순

# %%
# sorted: 원본 유지하며 정렬
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(f"원본: {original}")
print(f"정렬: {sorted_list}")

# %%
# reverse: 뒤집기
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)

# %%
# index: 값의 위치 찾기
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits.index("banana"))  # 1 (첫 번째 위치)

# %%
# count: 값의 개수
print(fruits.count("banana"))  # 2

# %%
# len: 리스트 길이
print(len(fruits))  # 4

# %% [markdown]
# ### 2.1.4 리스트 복사 주의사항

# %%
# 잘못된 복사 (같은 객체 참조)
original = [1, 2, 3]
wrong_copy = original
wrong_copy[0] = 100
print(f"원본도 변경됨: {original}")  # [100, 2, 3]

# %%
# 올바른 복사 방법들
original = [1, 2, 3]
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

copy1[0] = 100
print(f"원본 유지: {original}")  # [1, 2, 3]
print(f"복사본 변경: {copy1}")   # [100, 2, 3]

# %% [markdown]
# ---
# ## 2.2 딕셔너리 (Dictionary)
#
# 딕셔너리는 키-값(key-value) 쌍으로 이루어진 자료구조입니다. 중괄호 `{}`로 생성합니다.

# %%
# 딕셔너리 생성
person = {
    "name": "홍길동",
    "age": 25,
    "city": "서울"
}
print(person)
print(type(person))

# %%
# 빈 딕셔너리 생성
empty_dict = {}
another_dict = dict()

# %% [markdown]
# ### 2.2.1 딕셔너리 접근과 수정

# %%
person = {"name": "홍길동", "age": 25, "city": "서울"}

# 값 접근
print(person["name"])  # 홍길동
print(person["age"])   # 25

# %%
# get 메서드 (키가 없어도 에러 안남)
print(person.get("name"))          # 홍길동
print(person.get("job"))           # None
print(person.get("job", "무직"))   # 무직 (기본값)

# %%
# 값 수정
person["age"] = 26
print(person)

# 새 키-값 추가
person["job"] = "개발자"
print(person)

# %%
# 키 삭제
del person["city"]
print(person)

# pop으로 삭제 (삭제된 값 반환)
age = person.pop("age")
print(f"삭제된 값: {age}")
print(person)

# %% [markdown]
# ### 2.2.2 딕셔너리 주요 메서드

# %%
person = {"name": "홍길동", "age": 25, "city": "서울"}

# keys: 모든 키
print(person.keys())

# values: 모든 값
print(person.values())

# items: 모든 키-값 쌍
print(person.items())

# %%
# 키, 값, 아이템 순회
for key in person.keys():
    print(f"키: {key}")

# %%
for value in person.values():
    print(f"값: {value}")

# %%
for key, value in person.items():
    print(f"{key}: {value}")

# %%
# 키 존재 여부 확인
print("name" in person)   # True
print("email" in person)  # False

# %%
# update: 딕셔너리 병합
person = {"name": "홍길동", "age": 25}
extra_info = {"city": "서울", "job": "개발자"}
person.update(extra_info)
print(person)

# %% [markdown]
# ### 2.2.3 중첩 딕셔너리

# %%
# 중첩 딕셔너리
users = {
    "user1": {"name": "홍길동", "age": 25},
    "user2": {"name": "김철수", "age": 30},
    "user3": {"name": "이영희", "age": 28}
}

# 접근
print(users["user1"]["name"])  # 홍길동
print(users["user2"]["age"])   # 30

# %%
# 중첩 딕셔너리 순회
for user_id, info in users.items():
    print(f"{user_id}: {info['name']} ({info['age']}세)")

# %% [markdown]
# ---
# ## 2.3 셋 (Set)
#
# 셋은 중복을 허용하지 않는 순서 없는 집합입니다.

# %%
# 셋 생성
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
print(fruits)
print(type(fruits))

# %%
# 중복 자동 제거
duplicates = {1, 2, 2, 3, 3, 3, 4}
print(duplicates)  # {1, 2, 3, 4}

# %%
# 리스트에서 셋 생성 (중복 제거)
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = set(my_list)
print(unique)  # {1, 2, 3, 4}

# %% [markdown]
# ### 2.3.1 셋 연산

# %%
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# 합집합 (Union)
print(a | b)  # {1, 2, 3, 4, 5, 6, 7, 8}
print(a.union(b))

# %%
# 교집합 (Intersection)
print(a & b)  # {4, 5}
print(a.intersection(b))

# %%
# 차집합 (Difference)
print(a - b)  # {1, 2, 3}
print(a.difference(b))

# %% [markdown]
# ### 2.3.2 셋 주요 메서드

# %%
fruits = {"apple", "banana"}

# add: 요소 추가
fruits.add("cherry")
print(fruits)

# %%
# remove: 요소 삭제
fruits.remove("banana")
print(fruits)

# %%
# add: 요소 추가
fruits.add("apple")
fruits.add("cherry")
print(fruits)

# %%
# 요소 존재 확인
print("apple" in fruits)  # True
print("mango" in fruits)  # False

# %% [markdown]
# ---
# ## 2.4 누적 집계 패턴 (빈도수 카운트)
#
# 딕셔너리를 활용한 가장 흔한 패턴 중 하나입니다.

# %% [markdown]
# ### 2.4.1 기본 카운트 패턴

# %%
# 단어 빈도수 세기
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# 패턴 1: get 메서드 활용
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)  # {'apple': 3, 'banana': 2, 'cherry': 1}

# %%
# 패턴 2: if-else 활용
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

print(word_count)

# %% [markdown]
# ### 2.4.2 카테고리별 집계

# %%
# 설문 응답 데이터
responses = [
    {"category": "제품", "score": 5},
    {"category": "서비스", "score": 4},
    {"category": "제품", "score": 3},
    {"category": "배송", "score": 5},
    {"category": "제품", "score": 4},
    {"category": "서비스", "score": 5},
    {"category": "배송", "score": 2},
]

# 카테고리별 개수 집계
category_count = {}
for response in responses:
    cat = response["category"]
    category_count[cat] = category_count.get(cat, 0) + 1

print("카테고리별 개수:", category_count)

# %%
# 카테고리별 점수 합계
category_sum = {}
for response in responses:
    cat = response["category"]
    score = response["score"]
    category_sum[cat] = category_sum.get(cat, 0) + score

print("카테고리별 점수 합계:", category_sum)

# %%
# 카테고리별 평균 점수 계산
category_avg = {}
for cat in category_count:
    avg = category_sum[cat] / category_count[cat]
    category_avg[cat] = round(avg, 2)

print("카테고리별 평균 점수:", category_avg)

# %% [markdown]
# ### 2.4.3 collections.Counter 활용

# %%
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# Counter로 간단하게
word_count = Counter(words)
print(word_count)

# %%
# 가장 흔한 항목
print(word_count.most_common(2))  # [('apple', 3), ('banana', 2)]

# %%
# 문자열에서 문자 빈도
text = "hello world"
char_count = Counter(text)
print(char_count.most_common(3))

# %% [markdown]
# ---
# ## 2.5 리스트 컴프리헨션 (List Comprehension)
#
# 리스트를 간결하게 생성하는 파이썬의 강력한 문법입니다.

# %% [markdown]
# ### 2.5.1 기본 문법

# %%
# 일반 for 루프
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)

# %%
# 리스트 컴프리헨션
squares = [i ** 2 for i in range(1, 6)]
print(squares)

# %% [markdown]
# ### 2.5.2 조건부 컴프리헨션

# %%
# 짝수만 필터링
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# %%
# 조건에 따라 변환
numbers = [1, 2, 3, 4, 5]
result = ["짝수" if n % 2 == 0 else "홀수" for n in numbers]
print(result)

# %% [markdown]
# ### 2.5.3 중첩 컴프리헨션

# %%
# 2중 for 루프
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# %%
# 구구단 예시
multiplication = [[i * j for j in range(1, 4)] for i in range(2, 5)]
print(multiplication)
# [[2, 4, 6], [3, 6, 9], [4, 8, 12]]

# %% [markdown]
# ### 2.5.4 딕셔너리/셋 컴프리헨션

# %%
# 딕셔너리 컴프리헨션
names = ["alice", "bob", "charlie"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'alice': 5, 'bob': 3, 'charlie': 7}

# %%
# 셋 컴프리헨션
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_squares = {n ** 2 for n in numbers}
print(unique_squares)  # {1, 4, 9, 16}

# %% [markdown]
# ---
# ## 2.6 실습: 카테고리별 설문 응답 집계
#
# 설문 응답 데이터를 분석하여 카테고리별 통계를 생성합니다.

# %%
# 설문 응답 데이터 (이전 모듈에서 이어짐)
survey_data = [
    {"id": 1, "category": "제품", "text": "품질이 좋습니다", "score": 5},
    {"id": 2, "category": "서비스", "text": "친절했어요", "score": 5},
    {"id": 3, "category": "제품", "text": "기대 이하", "score": 2},
    {"id": 4, "category": "배송", "text": "배송 지연", "score": 2},
    {"id": 5, "category": "서비스", "text": "문의 해결 빠름", "score": 4},
    {"id": 6, "category": "제품", "text": "가격 대비 좋음", "score": 4},
    {"id": 7, "category": "배송", "text": "새벽배송 좋아요", "score": 5},
    {"id": 8, "category": "제품", "text": "디자인 예쁨", "score": 5},
    {"id": 9, "category": "서비스", "text": "앱 불편", "score": 2},
    {"id": 10, "category": "배송", "text": "포장 훼손", "score": 2},
]

# %% [markdown]
# ### Step 1: 카테고리별 개수와 점수 집계

# %%
def count_by_category(data, category_key="category"):
    """카테고리별 개수 집계"""
    counts = {}
    for item in data:
        cat = item[category_key]
        counts[cat] = counts.get(cat, 0) + 1
    return counts

# %%
def sum_by_category(data, category_key="category", value_key="score"):
    """카테고리별 값 합계"""
    sums = {}
    for item in data:
        cat = item[category_key]
        val = item[value_key]
        sums[cat] = sums.get(cat, 0) + val
    return sums

# %%
# 집계 실행
category_counts = count_by_category(survey_data)
category_sums = sum_by_category(survey_data)

print("카테고리별 개수:", category_counts)
print("카테고리별 점수 합계:", category_sums)

# %% [markdown]
# ### Step 2: 카테고리별 평균 점수 계산

# %%
def avg_by_category(counts, sums):
    """개수와 합계로 평균 계산"""
    averages = {}
    for cat in counts:
        avg = sums[cat] / counts[cat]
        averages[cat] = round(avg, 2)
    return averages

# %%
category_avg = avg_by_category(category_counts, category_sums)
print("카테고리별 평균:", category_avg)

# %% [markdown]
# ### Step 3: 긍정/부정 비율 계산

# %%
def sentiment_ratio(data, category_key="category", score_key="score", threshold=4):
    """
    점수 기준으로 긍정/부정 비율 계산
    threshold 이상이면 긍정
    """
    positive_counts = {}
    total_counts = {}
    
    for item in data:
        cat = item[category_key]
        score = item[score_key]
        
        total_counts[cat] = total_counts.get(cat, 0) + 1
        if score >= threshold:
            positive_counts[cat] = positive_counts.get(cat, 0) + 1
    
    ratios = {}
    for cat in total_counts:
        positive = positive_counts.get(cat, 0)
        total = total_counts[cat]
        ratios[cat] = round(positive / total, 2)
    
    return ratios

# %%
positive_ratios = sentiment_ratio(survey_data)
print("긍정 비율:", positive_ratios)

# %% [markdown]
# ### Step 4: 전체 통계 보고서 생성

# %%
def generate_summary(data):
    """설문 데이터 요약 통계 생성"""
    # 기본 집계
    counts = count_by_category(data)
    sums = sum_by_category(data)
    avgs = avg_by_category(counts, sums)
    ratios = sentiment_ratio(data)
    
    # 전체 통계
    total_count = len(data)
    total_avg = sum(item["score"] for item in data) / total_count
    
    summary = {
        "total_responses": total_count,
        "average_score": round(total_avg, 2),
        "category_stats": {}
    }
    
    for cat in counts:
        summary["category_stats"][cat] = {
            "count": counts[cat],
            "avg_score": avgs[cat],
            "positive_ratio": ratios[cat]
        }
    
    return summary

# %%
# 요약 생성
summary = generate_summary(survey_data)

# 결과 출력
print("=" * 50)
print("설문 분석 요약")
print("=" * 50)
print(f"총 응답 수: {summary['total_responses']}")
print(f"전체 평균 점수: {summary['average_score']}")
print()
print("카테고리별 통계:")
for cat, stats in summary["category_stats"].items():
    print(f"  [{cat}]")
    print(f"    - 응답 수: {stats['count']}")
    print(f"    - 평균 점수: {stats['avg_score']}")
    print(f"    - 긍정 비율: {stats['positive_ratio'] * 100:.0f}%")

# %% [markdown]
# ### Step 5: 리스트 컴프리헨션으로 간결하게

# %%
# 점수 4 이상인 응답만 필터링
positive_responses = [r for r in survey_data if r["score"] >= 4]
print(f"긍정 응답 수: {len(positive_responses)}")

# %%
# 카테고리별 응답 텍스트 추출
category_texts = {
    cat: [r["text"] for r in survey_data if r["category"] == cat]
    for cat in set(r["category"] for r in survey_data)
}
print(category_texts)

# %%
# 점수별 그룹화
score_groups = {
    score: [r["id"] for r in survey_data if r["score"] == score]
    for score in range(1, 6)
}
print("점수별 응답 ID:", score_groups)

# %% [markdown]
# ---
# ## 연습문제

# %% [markdown]
# ### 문제 1: 리스트 연산
# 다음 리스트에서:
# 1. 3번째 요소를 "python"으로 변경
# 2. 마지막에 "java" 추가
# 3. 첫 번째 요소 삭제
# 4. 알파벳 순으로 정렬

# %%
languages = ["javascript", "ruby", "c++", "go", "rust"]
# 여기에 코드 작성


# %% [markdown]
# ### 문제 2: 딕셔너리 활용
# 다음 학생 정보를 딕셔너리로 표현하고, 평균 점수를 계산하세요.
# - 이름: 김철수
# - 과목 점수: 국어 85, 영어 92, 수학 78

# %%
# 여기에 코드 작성


# %% [markdown]
# ### 문제 3: 중복 제거
# 다음 리스트에서 중복을 제거하고 정렬된 리스트로 반환하세요.

# %%
numbers = [5, 2, 8, 2, 5, 1, 9, 1, 5, 8, 3]
# 여기에 코드 작성
# 결과: [1, 2, 3, 5, 8, 9]


# %% [markdown]
# ### 문제 4: 단어 빈도수
# 다음 문장에서 각 단어의 등장 횟수를 딕셔너리로 만드세요.

# %%
sentence = "the quick brown fox jumps over the lazy dog the fox"
# 여기에 코드 작성


# %% [markdown]
# ### 문제 5: 리스트 컴프리헨션
# 1부터 20까지 숫자 중 3의 배수만 제곱한 리스트를 컴프리헨션으로 만드세요.
# 결과: [9, 36, 81, 144, 225, 324]

# %%
# 여기에 코드 작성


# %% [markdown]
# ### 문제 6: 카테고리별 집계 함수 확장
# 아래 데이터에서 카테고리별로:
# 1. 가장 높은 점수
# 2. 가장 낮은 점수
# 를 구하는 함수를 작성하세요.

# %%
data = [
    {"category": "A", "score": 85},
    {"category": "B", "score": 92},
    {"category": "A", "score": 78},
    {"category": "B", "score": 88},
    {"category": "A", "score": 95},
    {"category": "C", "score": 70},
]

def min_max_by_category(data):
    """카테고리별 최소/최대 점수"""
    # 여기에 코드 작성
    pass

# 결과: {"A": {"min": 78, "max": 95}, "B": {"min": 88, "max": 92}, ...}


# %%
