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
# # 4. 함수, 모듈, 예외처리
#
# **학습 목표**: 재사용 가능한 함수를 만들고, 모듈화하며, 오류를 안전하게 처리합니다.
# ---

# %% [markdown]
# ## 문법 설명
#
# ### 1. 함수 (Function)
#
# **정의**: 특정 작업을 수행하는 재사용 가능한 코드 블록입니다.
#
# **문법**:
# ```python
# def 함수명(매개변수1, 매개변수2=기본값):
#     """문서 문자열 (docstring)"""
#     코드
#     return 반환값
# ```
#
# **매개변수 종류**:
# - **위치 인자**: 순서대로 전달
# - **키워드 인자**: 이름으로 전달 `함수(키=값)`
# - **기본값**: 매개변수에 기본값 지정 가능
# - **가변 인자**: `*args` (튜플), `**kwargs` (딕셔너리)
#
# **반환값**:
# - `return 값`: 값 반환
# - `return`: `None` 반환
# - 반환값 없으면 자동으로 `None` 반환
#
# **변수 스코프**:
# - **지역 변수**: 함수 내부에서만 유효
# - **전역 변수**: 함수 외부에서 정의, `global` 키워드로 수정 가능
#
# ---
#
# ### 2. 모듈 (Module)
#
# **정의**: 함수, 클래스, 변수 등을 모아놓은 파일입니다.
#
# **모듈 임포트**:
# | 문법 | 설명 | 예시 |
# |------|------|------|
# | `import 모듈명` | 모듈 전체 임포트 | `import math` |
# | `from 모듈 import 함수` | 특정 함수만 임포트 | `from math import sqrt` |
# | `import 모듈 as 별칭` | 별칭으로 임포트 | `import numpy as np` |
#
# **표준 라이브러리 예시**:
# - `math`: 수학 함수
# - `random`: 난수 생성
# - `datetime`: 날짜/시간 처리
# - `os`: 운영체제 인터페이스
# - `json`: JSON 처리
#
# ---
#
# ### 3. 예외처리 (Exception Handling)
#
# **정의**: 프로그램 실행 중 발생할 수 있는 오류를 안전하게 처리합니다.
#
# **문법**:
# ```python
# try:
#     코드
# except 예외타입 as 변수:
#     예외 처리 코드
# else:
#     예외 없을 때 실행
# finally:
#     항상 실행
# ```
#
# **주요 예외 타입**:
# | 예외 | 발생 상황 | 예시 |
# |------|----------|------|
# | `ZeroDivisionError` | 0으로 나눔 | `10 / 0` |
# | `ValueError` | 값이 잘못됨 | `int("abc")` |
# | `TypeError` | 타입이 잘못됨 | `"str" + 123` |
# | `KeyError` | 딕셔너리 키 없음 | `d["없는키"]` |
# | `IndexError` | 인덱스 범위 초과 | `lst[100]` |
# | `FileNotFoundError` | 파일 없음 | `open("없는파일")` |
# | `Exception` | 모든 예외 | `except Exception:` |
#
# **예외 처리 패턴**:
# - 구체적인 예외부터 처리
# - 여러 예외 동시 처리: `except (Type1, Type2):`
# - 예외 정보 활용: `except Exception as e:`
# - `finally`: 정리 작업 (파일 닫기 등)
#
# ---
# ## 실습 시작
#
# 아래 실습을 통해 위 문법들을 직접 사용해봅니다.
#
# ---

# %% [markdown]
# ## 4.1 함수 (Function)
#
# 함수는 특정 작업을 수행하는 재사용 가능한 코드 블록입니다.

# %% [markdown]
# ### 4.1.1 함수 정의와 호출

# %%
# 기본 함수 정의
def greet():
    print("안녕하세요!")

# 함수 호출
greet()

# %%
# 매개변수(parameter)가 있는 함수
def greet_person(name):
    print(f"안녕하세요, {name}님!")

greet_person("홍길동")
greet_person("김철수")

# %%
# 반환값(return)이 있는 함수
def add(a, b):
    result = a + b
    return result

sum_result = add(3, 5)
print(f"3 + 5 = {sum_result}")

# %%
# 여러 값 반환
def get_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return total, average, count

nums = [10, 20, 30, 40, 50]
total, avg, cnt = get_stats(nums)
print(f"합계: {total}, 평균: {avg}, 개수: {cnt}")

# %% [markdown]
# ### 4.1.2 기본값 매개변수와 키워드 인자

# %%
# 기본값 매개변수
def greet(name, greeting="안녕하세요"):
    print(f"{greeting}, {name}님!")

greet("홍길동")  # 기본값 사용
greet("김철수", "반갑습니다")  # 기본값 대체

# %%
# 키워드 인자
def create_profile(name, age, city="서울"):
    return {"name": name, "age": age, "city": city}

# 위치 인자
profile1 = create_profile("홍길동", 25)
print(profile1)

# 키워드 인자 (순서 무관)
profile2 = create_profile(age=30, name="김철수", city="부산")
print(profile2)

# %% [markdown]
# ### 4.1.3 가변 인자 (*args, **kwargs)

# %%
# *args: 가변 위치 인자 (튜플로 받음)
def sum_all(*args):
    print(f"받은 인자: {args}")
    return sum(args)

print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5))

# %%
# **kwargs: 가변 키워드 인자 (딕셔너리로 받음)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="홍길동", age=25, city="서울")

# %%
# 혼합 사용
def mixed_args(required, *args, **kwargs):
    print(f"필수: {required}")
    print(f"추가 위치 인자: {args}")
    print(f"추가 키워드 인자: {kwargs}")

mixed_args("첫번째", "두번째", "세번째", option1="A", option2="B")

# %% [markdown]
# ### 4.1.4 독스트링 (Docstring)

# %%
def calculate_average(numbers):
    """
    숫자 리스트의 평균을 계산합니다.
    
    Args:
        numbers: 숫자 리스트
    
    Returns:
        평균값 (float)
    
    Raises:
        ValueError: 빈 리스트가 입력된 경우
    
    Example:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
    """
    if len(numbers) == 0:
        raise ValueError("빈 리스트는 처리할 수 없습니다")
    return sum(numbers) / len(numbers)

# 도움말 확인
help(calculate_average)

# %% [markdown]
# ### 4.1.5 람다 함수 (Lambda)

# %%
# 일반 함수
def square(x):
    return x ** 2

# 람다 함수 (익명 함수)
square_lambda = lambda x: x ** 2

print(square(5))
print(square_lambda(5))

# %%
# 람다 활용: 정렬 기준 지정
students = [
    {"name": "홍길동", "score": 85},
    {"name": "김철수", "score": 92},
    {"name": "이영희", "score": 78},
]

# 점수로 정렬
sorted_by_score = sorted(students, key=lambda x: x["score"], reverse=True)
for s in sorted_by_score:
    print(f"{s['name']}: {s['score']}점")

# %% [markdown]
# ---
# ## 4.2 모듈 (Module)
#
# 모듈은 Python 코드가 담긴 파일(.py)로, 함수/변수/클래스를 재사용할 수 있게 합니다.

# %% [markdown]
# ### 4.2.1 import 사용법

# %%
# 전체 모듈 import
import math

print(math.pi)
print(math.sqrt(16))

# %%
# 특정 함수만 import
from math import sqrt, pi

print(pi)
print(sqrt(25))

# %%
# 별명(alias) 사용
import math as m

print(m.pi)
print(m.ceil(3.2))

# %%
# 모듈 내용 확인
import random
print(dir(random)[:10])  # 처음 10개만

# %% [markdown]
# ### 4.2.2 자주 사용하는 내장 모듈

# %%
# math: 수학 함수
import math

print(f"원주율: {math.pi}")
print(f"e: {math.e}")
print(f"sqrt(2): {math.sqrt(2)}")
print(f"log(10): {math.log(10)}")
print(f"ceil(3.2): {math.ceil(3.2)}")
print(f"floor(3.8): {math.floor(3.8)}")

# %%
# random: 난수 생성
import random

print(f"0~1 랜덤: {random.random()}")
print(f"1~10 정수: {random.randint(1, 10)}")
print(f"리스트에서 선택: {random.choice(['a', 'b', 'c'])}")

# 리스트 섞기
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(f"섞은 결과: {items}")

# %%
# datetime: 날짜/시간
from datetime import datetime, timedelta

now = datetime.now()
print(f"현재 시각: {now}")
print(f"포맷팅: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 날짜 연산
tomorrow = now + timedelta(days=1)
print(f"내일: {tomorrow.strftime('%Y-%m-%d')}")

# %%
# os: 운영체제 관련
import os

print(f"현재 디렉토리: {os.getcwd()}")
print(f"파일 목록: {os.listdir('.')[:5]}")  # 처음 5개

# %% [markdown]
# ### 4.2.3 사용자 정의 모듈 만들기

# %%
# 모듈로 사용할 코드 (text_utils.py로 저장 가능)
# 여기서는 함수만 정의

def clean_text(text):
    """텍스트 정리: 공백 제거, 소문자 변환"""
    return text.strip().lower()

def count_words(text):
    """단어 수 세기"""
    return len(text.split())

def extract_keywords(text, min_length=2):
    """최소 길이 이상의 단어 추출"""
    words = text.lower().split()
    return [w for w in words if len(w) >= min_length]

# %%
# 사용 예시
sample = "  Python is AWESOME for AI development!  "
print(f"정리: '{clean_text(sample)}'")
print(f"단어 수: {count_words(sample)}")
print(f"키워드: {extract_keywords(sample, 3)}")

# %% [markdown]
# ---
# ## 4.3 예외처리 (Exception Handling)
#
# 프로그램 실행 중 발생할 수 있는 오류를 안전하게 처리합니다.

# %% [markdown]
# ### 4.3.1 기본 try-except

# %%
# 에러 발생 상황
try:
    result = 10 / 0
except:
    print("에러가 발생했습니다")

# %%
# 구체적인 예외 지정
try:
    result = 10 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")

# %%
# 예외 정보 가져오기
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"에러 메시지: {e}")

# %% [markdown]
# ### 4.3.2 여러 예외 처리

# %%
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다")
        return None
    except TypeError:
        print("숫자만 입력 가능합니다")
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "a"))

# %% [markdown]
# ### 4.3.3 try-except-else-finally

# %%
def read_number(value):
    try:
        number = int(value)
    except ValueError:
        print(f"'{value}'는 숫자로 변환할 수 없습니다")
        return None
    else:
        # 예외가 발생하지 않았을 때 실행
        print(f"변환 성공: {number}")
        return number
    finally:
        # 항상 실행 (정리 작업에 사용)
        print("처리 완료")

read_number("123")
print()
read_number("abc")

# %% [markdown]
# ### 4.3.4 일반적인 예외 타입

# %%
# ValueError: 값이 잘못된 경우
try:
    int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

# %%
# TypeError: 타입이 잘못된 경우
try:
    "hello" + 123
except TypeError as e:
    print(f"TypeError: {e}")

# %%
# KeyError: 딕셔너리 키가 없는 경우
try:
    d = {"a": 1}
    print(d["b"])
except KeyError as e:
    print(f"KeyError: {e}")

# %%
# IndexError: 인덱스 범위 초과
try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError as e:
    print(f"IndexError: {e}")

# %%
# FileNotFoundError: 파일 없음
try:
    with open("없는파일.txt") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

# %% [markdown]
# ### 4.3.5 Exception으로 모든 예외 잡기

# %%
def safe_operation(func, *args):
    """안전하게 함수 실행"""
    try:
        return func(*args)
    except Exception as e:
        print(f"오류 발생: {type(e).__name__}: {e}")
        return None

# 테스트
safe_operation(lambda: 10 / 0)
safe_operation(lambda: int("abc"))
safe_operation(lambda: [1,2,3][10])

# %% [markdown]
# ### 4.3.6 예외 발생시키기 (raise)

# %%
def validate_age(age):
    if age < 0:
        raise ValueError("나이는 0 이상이어야 합니다")
    if age > 150:
        raise ValueError("나이가 너무 큽니다")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"검증 실패: {e}")

# %% [markdown]
# ---
# ## 4.4 실습: Day1 코드 리팩토링
#
# 지금까지 만든 함수들을 모듈화하고 예외처리를 추가합니다.

# %% [markdown]
# ### 이전 코드들을 함수로 정리

# %%
# text_processor.py 모듈로 사용할 함수들

def clean_whitespace(text):
    """
    앞뒤 공백 제거 및 중복 공백 정리
    
    Args:
        text: 정리할 텍스트
    
    Returns:
        정리된 텍스트
    
    Raises:
        TypeError: text가 문자열이 아닌 경우
    """
    if not isinstance(text, str):
        raise TypeError(f"문자열이 필요합니다. 받은 타입: {type(text).__name__}")
    
    text = text.strip()
    words = text.split()
    return " ".join(words)


def remove_stopwords(text, stopwords):
    """
    불용어 제거
    
    Args:
        text: 원본 텍스트
        stopwords: 제거할 단어 리스트
    
    Returns:
        불용어가 제거된 텍스트
    """
    if stopwords is None:
        stopwords = []
    
    words = text.split()
    filtered = [w for w in words if w not in stopwords]
    return " ".join(filtered)


def count_by_category(data, category_key="category"):
    """
    카테고리별 개수 집계
    
    Args:
        data: 딕셔너리 리스트
        category_key: 카테고리 키 이름
    
    Returns:
        카테고리별 개수 딕셔너리
    
    Raises:
        KeyError: category_key가 데이터에 없는 경우
    """
    counts = {}
    for i, item in enumerate(data):
        if category_key not in item:
            raise KeyError(f"항목 {i}에 '{category_key}' 키가 없습니다")
        
        cat = item[category_key]
        counts[cat] = counts.get(cat, 0) + 1
    
    return counts


def classify_sentiment(text, positive_words, negative_words):
    """
    감성 분류 (긍정/부정/중립)
    
    Args:
        text: 분석할 텍스트
        positive_words: 긍정 키워드 리스트
        negative_words: 부정 키워드 리스트
    
    Returns:
        "긍정", "부정", "중립" 중 하나
    """
    if not text:
        return "중립"
    
    text_lower = text.lower() if isinstance(text, str) else str(text)
    
    pos_count = sum(1 for w in positive_words if w in text_lower)
    neg_count = sum(1 for w in negative_words if w in text_lower)
    
    if pos_count > neg_count:
        return "긍정"
    elif neg_count > pos_count:
        return "부정"
    else:
        return "중립"

# %% [markdown]
# ### 안전한 데이터 처리 함수

# %%
def safe_process_responses(responses, processor_func):
    """
    응답 리스트를 안전하게 처리
    
    Args:
        responses: 처리할 응답 리스트
        processor_func: 각 응답에 적용할 함수
    
    Returns:
        (성공 결과 리스트, 실패 정보 리스트)
    """
    results = []
    errors = []
    
    for i, response in enumerate(responses):
        try:
            result = processor_func(response)
            results.append(result)
        except Exception as e:
            error_info = {
                "index": i,
                "input": response,
                "error_type": type(e).__name__,
                "error_message": str(e)
            }
            errors.append(error_info)
    
    return results, errors

# %% [markdown]
# ### 테스트

# %%
# 테스트 데이터 (일부러 잘못된 데이터 포함)
test_data = [
    "  정상적인 텍스트입니다  ",
    "  이것도   정상  ",
    None,  # 에러 발생
    123,   # 에러 발생
    "마지막 정상 텍스트"
]

# 안전한 처리
results, errors = safe_process_responses(test_data, clean_whitespace)

print("=== 성공 결과 ===")
for r in results:
    print(f"  '{r}'")

print("\n=== 오류 정보 ===")
for e in errors:
    print(f"  인덱스 {e['index']}: {e['error_type']} - {e['error_message']}")

# %% [markdown]
# ### 전체 파이프라인 함수

# %%
def process_survey_data(data, stopwords=None, positive_words=None, negative_words=None):
    """
    설문 데이터 전체 처리 파이프라인
    
    Args:
        data: 설문 응답 리스트
        stopwords: 불용어 리스트
        positive_words: 긍정 키워드 리스트
        negative_words: 부정 키워드 리스트
    
    Returns:
        처리 결과 딕셔너리
    """
    # 기본값 설정
    if stopwords is None:
        stopwords = ["너무", "정말", "매우", "그냥"]
    if positive_words is None:
        positive_words = ["좋", "만족", "추천", "빠르", "친절"]
    if negative_words is None:
        negative_words = ["불", "안", "늦", "느리", "나쁘"]
    
    processed = []
    error_count = 0
    
    for i, item in enumerate(data):
        try:
            # 텍스트 추출 (딕셔너리 또는 문자열)
            if isinstance(item, dict):
                text = item.get("text", item.get("response", ""))
            else:
                text = str(item)
            
            # 정리
            cleaned = clean_whitespace(text)
            cleaned = remove_stopwords(cleaned, stopwords)
            
            # 감성 분류
            sentiment = classify_sentiment(cleaned, positive_words, negative_words)
            
            processed.append({
                "original": text,
                "cleaned": cleaned,
                "sentiment": sentiment
            })
            
        except Exception as e:
            error_count += 1
            processed.append({
                "original": str(item),
                "cleaned": None,
                "sentiment": "오류",
                "error": str(e)
            })
    
    # 집계
    sentiment_counts = {}
    for p in processed:
        sent = p["sentiment"]
        sentiment_counts[sent] = sentiment_counts.get(sent, 0) + 1
    
    return {
        "processed": processed,
        "total_count": len(data),
        "error_count": error_count,
        "sentiment_distribution": sentiment_counts
    }

# %% [markdown]
# ### 실행 및 결과

# %%
# 테스트 데이터
survey_responses = [
    {"id": 1, "text": "  배송이 빠르고 좋았습니다!  "},
    {"id": 2, "text": "품질이 정말 안 좋아요."},
    {"id": 3, "text": "그냥 보통이에요."},
    {"id": 4, "response": "친절한 서비스 감사합니다."},  # 다른 키
    "직접 문자열도 가능합니다. 만족!",
    None,  # 에러 케이스
]

# 처리
result = process_survey_data(survey_responses)

# 결과 출력
print("=" * 60)
print("설문 데이터 처리 결과")
print("=" * 60)
print(f"총 처리: {result['total_count']}건")
print(f"오류: {result['error_count']}건")
print(f"감성 분포: {result['sentiment_distribution']}")

print("\n--- 상세 결과 ---")
for p in result["processed"]:
    print(f"[{p['sentiment']}] {p['cleaned']}")

# %% [markdown]
# ---
# ## 연습문제

# %% [markdown]
# ### 문제 1: 팩토리얼 함수
# 재귀 함수로 팩토리얼(n!)을 계산하세요. 음수 입력 시 ValueError를 발생시키세요.

# %%
def factorial(n):
    # 여기에 코드 작성
    pass

# 테스트
for n in [0, 1, 5, 10, -1]:
    try:
        print(f"{n}! = {factorial(n)}")
    except ValueError as e:
        print(f"{n}: 오류 - {e}")


# %% [markdown]
# ### 문제 2: 안전한 딕셔너리 접근
# 중첩 딕셔너리에서 안전하게 값을 가져오는 함수를 작성하세요.

# %%
def safe_get(dictionary, keys, default=None):
    """
    중첩 딕셔너리에서 안전하게 값 가져오기
    
    Args:
        dictionary: 대상 딕셔너리
        keys: 키 리스트 또는 점(.)으로 구분된 문자열
        default: 키가 없을 때 반환값
    
    Example:
        safe_get({"a": {"b": 1}}, "a.b") → 1
        safe_get({"a": {"b": 1}}, "a.c", "없음") → "없음"
    """
    # 여기에 코드 작성
    pass

# 테스트
data = {
    "user": {
        "profile": {
            "name": "홍길동",
            "age": 25
        }
    }
}

print(safe_get(data, "user.profile.name"))
print(safe_get(data, "user.profile.email", "없음"))


# %% [markdown]
# ### 문제 3: 재시도 데코레이터 (심화)
# 실패 시 자동으로 재시도하는 데코레이터를 만드세요.

# %%
import random
import time

def retry(max_attempts=3, delay=1):
    """재시도 데코레이터"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 여기에 코드 작성
            pass
        return wrapper
    return decorator

# 테스트용 불안정한 함수
@retry(max_attempts=3, delay=0.5)
def unstable_api_call():
    """50% 확률로 실패하는 함수"""
    if random.random() < 0.5:
        raise ConnectionError("API 연결 실패")
    return "성공!"

# 테스트 (여러 번 실행해보세요)
# result = unstable_api_call()
# print(result)


# %% [markdown]
# ### 문제 4: 로깅이 포함된 처리 함수
# 처리 과정을 로그로 남기는 함수를 작성하세요.

# %%
def process_with_logging(data, processor):
    """
    데이터 처리 및 로그 기록
    
    Returns:
        (결과 리스트, 로그 리스트)
    """
    # 여기에 코드 작성
    pass


# %%


