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
# # 1. 기초 문법 1: 변수, 자료형, 문자열
#
# **학습 목표**: Python의 기본 자료형과 문자열 처리 방법을 익혀, AI 데이터 전처리의 기초를 다집니다.
#
# ---

# %% [markdown]
# ## 문법 설명
#
# ### 1. 변수 (Variable)
#
# **정의**: 변수는 데이터를 저장하는 메모리 공간에 붙인 이름입니다.
#
# **문법**:
# ```python
# 변수명 = 값
# ```
#
# **특징**:
# - 변수명은 영문자, 숫자, 언더스코어(`_`)로 구성
# - 숫자로 시작 불가, 예약어 사용 불가
# - 대소문자 구분
#
# **할당 방법**:
# - 단일 할당: `x = 10`
# - 다중 할당: `x, y = 1, 2`
# - 동일 값 할당: `a = b = c = 100`
#
# ---
#
# ### 2. 자료형 (Data Type)
#
# Python의 기본 자료형은 다음과 같습니다:
#
# | 자료형 | 타입명 | 예시 | 설명 |
# |--------|--------|------|------|
# | 정수 | `int` | `42`, `-10`, `0` | 정수 값 |
# | 실수 | `float` | `3.14`, `-5.5`, `1.23e4` | 소수점이 있는 수 |
# | 문자열 | `str` | `"Hello"`, `'World'` | 텍스트 데이터 |
# | 불리언 | `bool` | `True`, `False` | 논리값 |
# | None | `NoneType` | `None` | 값 없음을 나타냄 |
#
# **타입 확인**: `type(값)` 또는 `type(변수명)`
#
# **타입 변환**:
# - `int(값)`: 정수로 변환
# - `float(값)`: 실수로 변환
# - `str(값)`: 문자열로 변환
# - `bool(값)`: 불리언으로 변환
#
# **불리언 변환 규칙**:
# - `False`가 되는 값: `0`, `""`, `None`, `[]`, `{}`
# - 그 외 모든 값은 `True`
#
# ---
#
# ### 3. 연산자 (Operators)
#
# #### 3.1 산술 연산자
#
# | 연산자 | 의미 | 예시 | 결과 |
# |--------|------|------|------|
# | `+` | 덧셈 | `10 + 3` | `13` |
# | `-` | 뺄셈 | `10 - 3` | `7` |
# | `*` | 곱셈 | `10 * 3` | `30` |
# | `/` | 나눗셈 | `10 / 3` | `3.333...` |
# | `//` | 몫 | `10 // 3` | `3` |
# | `%` | 나머지 | `10 % 3` | `1` |
# | `**` | 거듭제곱 | `10 ** 3` | `1000` |
#
# #### 3.2 비교 연산자
#
# | 연산자 | 의미 | 예시 | 결과 |
# |--------|------|------|------|
# | `==` | 같음 | `5 == 5` | `True` |
# | `!=` | 다름 | `5 != 10` | `True` |
# | `<` | 작음 | `5 < 10` | `True` |
# | `<=` | 작거나 같음 | `5 <= 5` | `True` |
# | `>` | 큼 | `5 > 10` | `False` |
# | `>=` | 크거나 같음 | `5 >= 10` | `False` |
#
# #### 3.3 논리 연산자
#
# | 연산자 | 의미 | 설명 |
# |--------|------|------|
# | `and` | 논리곱 | 두 조건 모두 `True`일 때만 `True` |
# | `or` | 논리합 | 하나라도 `True`이면 `True` |
# | `not` | 논리부정 | `True` ↔ `False` 반전 |
#
# **진리표**:
# ```
# A     B     A and B   A or B   not A
# True  True  True      True     False
# True  False False     True     False
# False True  False     True     True
# False False False     False    True
# ```
#
# ---
#
# ### 4. 문자열 (String)
#
# #### 4.1 문자열 생성
#
# **문법**:
# ```python
# "문자열"      # 큰따옴표
# '문자열'      # 작은따옴표
# """여러 줄
#    문자열"""  # 삼중 따옴표
# ```
#
# #### 4.2 문자열 인덱싱 (Indexing)
#
# **문법**: `문자열[인덱스]`
#
# - 인덱스는 0부터 시작
# - 음수 인덱스: `-1`은 마지막 문자, `-2`는 뒤에서 두 번째
#
# **예시**:
# ```python
# text = "Hello"
# text[0]   # 'H' (첫 번째)
# text[-1]  # 'o' (마지막)
# ```
#
# #### 4.3 문자열 슬라이싱 (Slicing)
#
# **문법**: `문자열[시작:끝:증가분]`
#
# - `시작`: 포함 (기본값: 0)
# - `끝`: 제외 (기본값: 끝까지)
# - `증가분`: 건너뛸 칸 수 (기본값: 1)
#
# **예시**:
# ```python
# text = "Python"
# text[0:3]    # "Pyt" (0~2번)
# text[:3]     # "Pyt" (처음부터 2번까지)
# text[3:]     # "hon" (3번부터 끝까지)
# text[::2]    # "Pto" (2칸씩)
# text[::-1]   # "nohtyP" (역순)
# ```
#
# #### 4.4 주요 문자열 메서드
#
# | 메서드 | 설명 | 예시 | 결과 |
# |--------|------|------|------|
# | `strip()` | 양쪽 공백 제거 | `"  hi  ".strip()` | `"hi"` |
# | `upper()` | 대문자 변환 | `"hello".upper()` | `"HELLO"` |
# | `lower()` | 소문자 변환 | `"HELLO".lower()` | `"hello"` |
# | `replace(old, new)` | 문자열 치환 | `"hi".replace("h", "H")` | `"Hi"` |
# | `split(sep)` | 문자열 분리 | `"a,b,c".split(",")` | `["a", "b", "c"]` |
# | `join(iterable)` | 문자열 결합 | `", ".join(["a", "b"])` | `"a, b"` |
# | `find(sub)` | 부분 문자열 찾기 | `"hello".find("ll")` | `2` (없으면 `-1`) |
# | `count(sub)` | 부분 문자열 개수 | `"banana".count("a")` | `3` |
# | `startswith(prefix)` | 접두사 확인 | `"hello".startswith("he")` | `True` |
# | `endswith(suffix)` | 접미사 확인 | `"hello".endswith("lo")` | `True` |
#
# #### 4.5 f-string (포맷 문자열)
#
# **문법**: `f"문자열 {표현식} 문자열"`
#
# **기본 사용**:
# ```python
# name = "홍길동"
# age = 25
# f"이름: {name}, 나이: {age}"  # "이름: 홍길동, 나이: 25"
# ```
#
# **포맷 지정자**:
# - 소수점: `f"{pi:.2f}"` → 소수점 2자리
# - 천단위 구분: `f"{amount:,}"` → `1,234,567`
# - 퍼센트: `f"{ratio:.1%}"` → `85.6%`
# - 자릿수 맞추기: `f"{num:05d}"` → `00042`
#
# ---
# ## 실습 시작
#
# 아래 실습을 통해 위 문법들을 직접 사용해봅니다.
#
# ---

# %% [markdown]
# ## 1.1 변수(Variable)와 할당
#
# 변수는 데이터를 저장하는 이름표입니다. Python에서는 `=` 연산자로 값을 할당합니다.

# %%
# 변수 할당
name = "Python"
version = 3.11
is_easy = True

print(name)
print(version)
print(is_easy)

# %%
# 여러 변수를 한 줄에 할당
x, y, z = 1, 2, 3
print(x, y, z)

# %%
# 같은 값을 여러 변수에 할당
a = b = c = 100
print(a, b, c)

# %% [markdown]
# ### 변수 이름 규칙
# - 영문자, 숫자, 언더스코어(`_`)만 사용 가능
# - 숫자로 시작할 수 없음
# - 예약어(if, for, class 등) 사용 불가
# - 대소문자 구분

# %%
# 좋은 변수명 예시
user_name = "홍길동"
total_count = 100
MAX_VALUE = 999  # 상수는 대문자로 표현

# %% [markdown]
# ---
# ## 1.2 기본 자료형 (Data Types)
#
# Python의 기본 자료형: `int`, `float`, `str`, `bool`, `None`

# %% [markdown]
# ### 1.2.1 숫자형: int (정수), float (실수)

# %%
# 정수 (integer)
count = 42
negative = -10
print(type(count))  # <class 'int'>

# %%
# 실수 (float)
pi = 3.14159
temperature = -5.5
scientific = 1.23e4  # 1.23 × 10^4 = 12300.0
print(type(pi))

# %%
# 타입 확인
print(type(42))
print(type(3.14))
print(type(1.0))  # 1.0은 float

# %% [markdown]
# ### 1.2.2 문자열: str (string)

# %%
# 문자열 생성 - 작은따옴표, 큰따옴표 모두 가능
greeting = "안녕하세요"
message = 'Hello, Python!'
print(type(greeting))

# %%
# 여러 줄 문자열 - 삼중 따옴표 사용
long_text = """이것은
여러 줄에 걸친
문자열입니다."""
print(long_text)

# %% [markdown]
# ### 1.2.3 불리언: bool (True/False)

# %%
# 불리언 값
is_valid = True
has_error = False
print(type(is_valid))

# %%
# 비교 연산 결과는 불리언
result = 10 > 5
print(result)  # True
print(type(result))

# %% [markdown]
# ### 1.2.4 None 타입
#
# `None`은 "값이 없음"을 나타내는 특별한 값입니다.

# %%
# None 사용
result = None
print(result)
print(type(result))

# %%
# None 체크
if result is None:
    print("결과가 없습니다")

if not result:
    print("결과가 없습니다")

# %% [markdown]
# ### 1.2.5 타입 변환 (Type Casting)

# %%
# 문자열 → 정수
age_str = "25"
age_int = int(age_str)
print(age_int, type(age_int))

# %%
# 정수 → 실수
num = 10
num_float = float(num)
print(num_float, type(num_float))

# %%
# 숫자 → 문자열
price = 15000
price_str = str(price)
print(price_str, type(price_str))

# %%
# 불리언 변환 - False가 되는 값들
print(bool(0))      # False
print(bool(""))     # False
print(bool(None))   # False
print(bool([]))     # False

# %%
# 불리언 변환 - True가 되는 값들
print(bool(1))      # True
print(bool(-1))     # True
print(bool("text")) # True
print(bool([1,2]))  # True

# %% [markdown]
# ---
# ## 1.3 연산자 (Operators)

# %% [markdown]
# ### 1.3.1 산술 연산자

# %%
a, b = 10, 3

print(f"a + b = {a + b}")   # 덧셈: 13
print(f"a - b = {a - b}")   # 뺄셈: 7
print(f"a * b = {a * b}")   # 곱셈: 30
print(f"a / b = {a / b}")   # 나눗셈: 3.333...
print(f"a // b = {a // b}") # 몫: 3
print(f"a % b = {a % b}")   # 나머지: 1
print(f"a ** b = {a ** b}") # 거듭제곱: 1000

# %% [markdown]
# ### 1.3.2 비교 연산자

# %%
x, y = 5, 10

print(f"x == y: {x == y}")  # 같음: False
print(f"x != y: {x != y}")  # 다름: True
print(f"x < y: {x < y}")    # 작음: True
print(f"x <= y: {x <= y}")  # 작거나 같음: True
print(f"x > y: {x > y}")    # 큼: False
print(f"x >= y: {x >= y}")  # 크거나 같음: False

# %% [markdown]
# ### 1.3.3 논리 연산자

# %%
a, b = True, False

print(f"a and b: {a and b}")  # 둘 다 True여야 True
print(f"a or b: {a or b}")    # 하나라도 True면 True
print(f"not a: {not a}")      # 반대값

# %%
# 실제 조건 조합
age = 25
income = 3000

# 두 조건 모두 만족
if age >= 20 and income >= 2500:
    print("조건 충족!")

# %%
# 하나라도 만족
score = 85
if score >= 90 or score >= 80:
    print("합격!")

# %% [markdown]
# ---
# ## 1.4 문자열 다루기

# %% [markdown]
# ### 1.4.1 문자열 인덱싱 (Indexing)
#
# 문자열의 각 문자는 인덱스(위치)로 접근할 수 있습니다.
# ```
#   0   1   2   3   4   5 
# +---+---+---+---+---+---+
# | H | e | l | l | o | ! |
# +---+---+---+---+---+---+
#  -6  -5  -4  -3  -2  -1
# ```

# %%
text = "Hello!"

print(text[0])   # 첫 번째 문자: H
print(text[1])   # 두 번째 문자: e
print(text[-1])  # 마지막 문자: !
print(text[-2])  # 뒤에서 두 번째: o

# %% [markdown]
# ### 1.4.2 문자열 슬라이싱 (Slicing)
#
# `문자열[시작:끝:증가분]` - 시작 인덱스부터 끝 인덱스 **직전**까지

# %%
text = "Python Programming"

print(text[0:6])    # Python (0~5)
print(text[7:])     # Programming (7부터 끝까지)
print(text[:6])     # Python (처음부터 5까지)
print(text[-11:])   # Programming (뒤에서 11번째부터)

# %%
# 증가분(step) 사용
text = "ABCDEFGHIJ"

print(text[::2])    # ACEGI (2칸씩 건너뛰기)
print(text[1::2])   # BDFHJ (1번부터 2칸씩)
print(text[::-1])   # JIHGFEDCBA (역순)

# %% [markdown]
# ### 1.4.3 주요 문자열 메서드

# %%
text = "  Hello, Python World!  "

# 공백 제거
print(text.strip())   # 양쪽 공백 제거
print(text.lstrip())  # 왼쪽 공백 제거
print(text.rstrip())  # 오른쪽 공백 제거

# %%
text = "Hello, Python World!"

# 대소문자 변환
print(text.upper())   # 전부 대문자
print(text.lower())   # 전부 소문자
print(text.title())   # 단어 첫글자만 대문자

# %%
# 문자열 치환
text = "Hello, Python!"
new_text = text.replace("Python", "AI")
print(new_text)  # Hello, AI!

# %%
# 문자열 분리 (split)
sentence = "apple,banana,cherry,date"
fruits = sentence.split(",")  # 쉼표로 분리
print(fruits)  # ['apple', 'banana', 'cherry', 'date']

# %%
# 공백으로 분리
text = "Python is awesome"
words = text.split()  # 기본값: 공백으로 분리
print(words)  # ['Python', 'is', 'awesome']

# %%
# 문자열 결합 (join)
fruits = ['apple', 'banana', 'cherry']
result = ", ".join(fruits)
print(result)  # apple, banana, cherry

# %%
# 문자열 검색
text = "Python Programming"

print(text.find("Pro"))      # 7 (시작 위치)
print(text.find("Java"))     # -1 (없으면 -1)
print("Python" in text)      # True (포함 여부)
print(text.startswith("Py")) # True
print(text.endswith("ing"))  # True

# %%
# 문자 개수 세기
text = "banana"
print(text.count("a"))  # 3

# %% [markdown]
# ### 1.4.4 f-string (포맷 문자열)
#
# Python 3.6+에서 사용 가능한 가장 편리한 문자열 포맷팅 방법입니다.

# %%
# 기본 사용법
name = "홍길동"
age = 25
print(f"이름: {name}, 나이: {age}")

# %%
# 표현식 사용
price = 15000
quantity = 3
print(f"총 금액: {price * quantity}원")

# %%
# 숫자 포맷팅
pi = 3.14159265
print(f"원주율: {pi:.2f}")      # 소수점 2자리: 3.14
print(f"원주율: {pi:.4f}")      # 소수점 4자리: 3.1416

# %%
# 자릿수 맞추기
num = 42
print(f"숫자: {num:5d}")       # 5자리 정수 (오른쪽 정렬)
print(f"숫자: {num:05d}")      # 5자리, 빈칸은 0으로
print(f"숫자: {num:<5d}")      # 왼쪽 정렬

# %%
# 천단위 구분자
amount = 1234567890
print(f"금액: {amount:,}원")   # 1,234,567,890원

# %%
# 퍼센트 표시
ratio = 0.856
print(f"정확도: {ratio:.1%}")  # 85.6%


# %% [markdown]
# ---
# ## 1.5 실습: 설문 응답 텍스트 정리 함수 만들기
#
# AI 데이터 전처리의 첫 단계! 설문 응답 텍스트를 정리하는 함수를 만들어봅니다.

# %% [markdown]
# ### 실습 목표
# 1. 불필요한 공백 제거
# 2. 불용어(의미 없는 단어) 제거
# 3. 특정 단어 치환
# 4. 키워드 카운트

# %% [markdown]
# ### Step 1: 공백 정리 함수

# %%
def clean_whitespace(text):
    """앞뒤 공백 제거 및 중복 공백 정리"""
    # 앞뒤 공백 제거
    text = text.strip()
    # 중복 공백을 단일 공백으로 (split 후 join 활용)
    words = text.split()
    text = " ".join(words)
    return text

# 테스트
sample = "  배송이  너무   빠르고  "
print(f"원본: '{sample}'")
print(f"정리: '{clean_whitespace(sample)}'")

# %% [markdown]
# ### Step 2: 불용어 제거 함수

# %%
def remove_stopwords(text, stopwords):
    """불용어 목록에 있는 단어들을 제거"""
    words = text.split()
    filtered_words = []
    for word in words:
        if word not in stopwords:
            filtered_words.append(word)
    return " ".join(filtered_words)

# 테스트
stopwords = ["너무", "정말", "매우"]
sample = "배송이 너무 빠르고 정말 좋았습니다"
print(f"원본: '{sample}'")
print(f"정리: '{remove_stopwords(sample, stopwords)}'")

# %% [markdown]
# ### Step 3: 단어 치환 함수

# %%
def replace_words(text, replacements):
    """replacements 딕셔너리에 따라 단어 치환"""
    for old_word, new_word in replacements.items():
        text = text.replace(old_word, new_word)
    return text

# 테스트
replacements = {
    "좋았습니다": "긍정",
    "빠르고": "신속",
    "달라요": "상이"
}
sample = "배송이 빠르고 좋았습니다"
print(f"원본: '{sample}'")
print(f"치환: '{replace_words(sample, replacements)}'")

# %% [markdown]
# ### Step 4: 키워드 카운트 함수

# %%
# 샘플 설문 응답 데이터
responses = [
    "  배송이 너무 빠르고  포장이 꼼꼼했습니다. 매우 만족합니다!  ",
    "고객센터 응대가 정말 친절했어요. 문의 해결이 빨랐습니다.",
    "품질이 너무 기대 이하였습니다. 사진과 정말 달라요.",
    "  배송 지연이  있었습니다. 예상보다 3일 정말 늦게 도착.  ",
    "교환 절차가 너무 복잡했습니다. 개선이 정말 필요해요."
]

def count_keyword(texts, keyword):
    """텍스트 목록에서 특정 키워드의 등장 횟수 카운트"""
    total_count = 0
    for text in texts:
        total_count = total_count + text.count(keyword)
    return total_count

# 테스트
print(f"'배송' 등장 횟수: {count_keyword(responses, '배송')}")
print(f"'품질' 등장 횟수: {count_keyword(responses, '품질')}")
print(f"'만족' 등장 횟수: {count_keyword(responses, '만족')}")

# %% [markdown]
# ### Step 5: 통합 텍스트 정리 함수

# %%
def clean_text(text, stopwords=None, replacements=None):
    """
    텍스트 정리 통합 함수
    
    Args:
        text: 정리할 텍스트
        stopwords: 제거할 단어 목록 (기본값: None)
        replacements: 치환할 단어 딕셔너리 (기본값: None)
    
    Returns:
        정리된 텍스트
    """
    # 1. 공백 정리
    text = clean_whitespace(text)
    
    # 2. 불용어 제거 (제공된 경우)
    if stopwords is not None:
        text = remove_stopwords(text, stopwords)
    
    # 3. 단어 치환 (제공된 경우)
    if replacements is not None:
        text = replace_words(text, replacements)
    
    return text

# %% [markdown]
# ### 실습 결과 확인

# %%
# 설정
stopwords = ["너무", "정말", "매우"]
replacements = {"좋았습니다": "👍", "만족합니다": "👍"}

print("=" * 50)
print("설문 응답 텍스트 정리 결과")
print("=" * 50)

for i, response in enumerate(responses, 1):
    cleaned = clean_text(response, stopwords, replacements)
    print(f"\n[응답 {i}]")
    print(f"  원본: {response}")
    print(f"  정리: {cleaned}")

# %%
# 키워드 빈도 분석
keywords = ["배송", "품질", "서비스", "만족", "불만", "친절", "지연"]

print("\n" + "=" * 50)
print("키워드 빈도 분석")
print("=" * 50)

for keyword in keywords:
    count = count_keyword(responses, keyword)
    if count > 0:
        print(f"  '{keyword}': {count}회")

# %% [markdown]
# ---
# ## 연습문제

# %% [markdown]
# ### 문제 1: 타입 확인
# 다음 값들의 타입을 예측하고, `type()` 함수로 확인하세요.
# ```python
# a = 3.0
# b = "3"
# c = 3 > 2
# d = None
# e = 1 + 2j
# ```

# %%
# 여기에 코드 작성


# %% [markdown]
# ### 문제 2: 문자열 슬라이싱
# 문자열 `text = "PYTHON_PROGRAMMING"`에서 다음을 추출하세요.
# 1. 앞 6글자: "PYTHON"
# 2. 뒤 11글자: "PROGRAMMING"
# 3. 역순: "GNIMMARGORP_NOHTYP"
# 4. 홀수 위치 문자만: "YHN_RGAMN"

# %%
text = "PYTHON_PROGRAMMING"
# 여기에 코드 작성


# %% [markdown]
# ### 문제 3: 이메일 파싱
# 이메일 주소에서 사용자명과 도메인을 분리하세요.
# ```python
# email = "user.name@example.com"
# # 결과: 사용자명 = "user.name", 도메인 = "example.com"
# ```

# %%
email = "user.name@example.com"
# 여기에 코드 작성


# %% [markdown]
# ### 문제 4: 가격 포맷팅
# 다음 가격 정보를 f-string으로 포맷팅하세요.
# ```python
# product = "노트북"
# price = 1250000
# discount = 0.15
# # 결과: "노트북: 1,250,000원 (15.0% 할인)"
# ```

# %%
product = "노트북"
price = 1250000
discount = 0.15
# 여기에 코드 작성


# %% [markdown]
# ### 문제 5: 텍스트 정규화 함수
# 다음 조건을 만족하는 `normalize_text()` 함수를 작성하세요.
# 1. 앞뒤 공백 제거
# 2. 모두 소문자로 변환
# 3. 특수문자(!, ?, .) 제거

# %%
def normalize_text(text):
    """
    텍스트 정규화 함수
    - 앞뒤 공백 제거
    - 소문자 변환
    - 특수문자 제거
    """
    # 여기에 코드 작성
    pass

# 테스트
test_cases = [
    "  Hello, World!  ",
    "PYTHON is AWESOME!!!",
    "  What's your name?  "
]

for test in test_cases:
    result = normalize_text(test)
    print(f"'{test}' → '{result}'")


# %%
