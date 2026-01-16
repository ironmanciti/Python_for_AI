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
# # 6. 클래스와 객체지향 프로그래밍 기초
#
# **학습 목표**: 클래스의 기본 개념을 익히고, Pydantic(BaseModel)을 이해하기 위한 기반을 마련합니다.
#
# ---

# %% [markdown]
# ## 문법 설명
#
# ### 1. 클래스 (Class)
#
# **정의**: 데이터(속성)와 기능(메서드)을 하나로 묶은 설계도입니다.
#
# **문법**:
# ```python
# class 클래스명:
#     def __init__(self, 매개변수):
#         self.속성 = 매개변수
#     
#     def 메서드(self):
#         코드
# ```
#
# **핵심 개념**:
# - **클래스(Class)**: 설계도
# - **인스턴스(Instance)**: 클래스로 만든 실제 객체
# - **속성(Attribute)**: 객체가 가진 데이터 (`self.속성`)
# - **메서드(Method)**: 객체가 가진 함수
# - **self**: 인스턴스 자신을 가리키는 참조
#
# **인스턴스 생성**:
# ```python
# 객체 = 클래스명(인자)
# ```
#
# **특수 메서드**:
# | 메서드 | 의미 | 예시 |
# |--------|------|------|
# | `__init__()` | 생성자 | 객체 생성 시 호출 |
# | `__str__()` | 문자열 표현 | `print(객체)` 시 호출 |
# | `__repr__()` | 공식 표현 | 개발자용 표현 |
#
# **속성 접근**:
# - `객체.속성`: 속성 값 가져오기/설정
# - `객체.메서드()`: 메서드 호출
#
# ---
#
# ### 2. 상속 (Inheritance)
#
# **정의**: 기존 클래스를 확장하여 새로운 클래스를 만듭니다.
#
# **문법**:
# ```python
# class 자식클래스(부모클래스):
#     def __init__(self, ...):
#         super().__init__(...)  # 부모 생성자 호출
# ```
#
# **특징**:
# - 부모 클래스의 속성과 메서드 상속
# - 메서드 오버라이딩: 자식 클래스에서 재정의
# - `super()`: 부모 클래스 참조
#
# ---
# ## 실습 시작
#
# 아래 실습을 통해 위 문법들을 직접 사용해봅니다.
#
# ---

# %% [markdown]
# ## 6.1 클래스(Class)란?
#
# 클래스는 데이터(속성)와 기능(메서드)을 하나로 묶은 설계도입니다.
# - **클래스(Class)**: 설계도
# - **인스턴스(Instance)**: 설계도로 만든 실제 객체
# - **속성(Attribute)**: 객체가 가진 데이터
# - **메서드(Method)**: 객체가 가진 함수

# %%
# 간단한 클래스 정의
class Dog:
    # 클래스 속성 (모든 인스턴스가 공유)
    species = "개"
    
    # 생성자: 인스턴스 생성 시 호출
    def __init__(self, name, age):
        # 인스턴스 속성
        self.name = name
        self.age = age
    
    # 인스턴스 메서드
    def bark(self):
        return f"{self.name}가 멍멍!"
    
    def info(self):
        return f"{self.name}는 {self.age}살 {self.species}입니다."

# %%
# 인스턴스 생성
dog1 = Dog("바둑이", 3)
dog2 = Dog("흰둥이", 5)

print(dog1.name)      # 바둑이
print(dog1.bark())    # 바둑이가 멍멍!
print(dog1.info())    # 바둑이는 3살 개입니다.

# %%
# 각 인스턴스는 독립적
print(dog1.name, dog2.name)  # 바둑이 흰둥이
print(dog1.species)  # 클래스 속성 접근

# %% [markdown]
# ---
# ## 6.2 __init__과 self
#
# - `__init__`: 생성자(constructor). 인스턴스 생성 시 자동 호출됨
# - `self`: 인스턴스 자신을 가리킴 (첫 번째 매개변수로 자동 전달)

# %%
class Person:
    def __init__(self, name, age, city="서울"):
        """
        생성자(Constructor)
        - 인스턴스가 생성될 때 호출됨
        - 객체의 초기 상태(속성)를 설정
        """
        self.name = name
        self.age = age
        self.city = city
        self.created_at = "2024-01-01"  # 기본값
        print(f"{name} 인스턴스 생성됨")
    
    def greet(self):
        """인스턴스 메서드: self로 속성 접근"""
        return f"안녕하세요, {self.city}에 사는 {self.name}입니다."
    
    def have_birthday(self):
        """나이 증가"""
        self.age += 1
        return f"{self.name}이(가) {self.age}살이 되었습니다!"

# %%
person = Person("홍길동", 25)
print(person.greet())
print(person.have_birthday())
print(person.age)  # 26

# %% [markdown]
# ---
# ## 6.3 유용한 메서드 패턴

# %% [markdown]
# ### 6.3.1 to_dict() 메서드
#
# 객체를 딕셔너리로 변환 - JSON 직렬화에 유용합니다.

# %%
class SurveyResponse:
    def __init__(self, id, category, text, score):
        self.id = id
        self.category = category
        self.text = text
        self.score = score
    
    def to_dict(self):
        """객체를 딕셔너리로 변환"""
        return {
            "id": self.id,
            "category": self.category,
            "text": self.text,
            "score": self.score
        }
    
    def is_positive(self):
        """긍정 응답 여부"""
        return self.score >= 4

# %%
response = SurveyResponse(1, "제품", "품질이 좋습니다", 5)
print(response.to_dict())
print(response.is_positive())

# %%
import json

# JSON 변환 시 to_dict() 활용
responses = [
    SurveyResponse(1, "제품", "좋아요", 5),
    SurveyResponse(2, "배송", "빨라요", 4),
    SurveyResponse(3, "서비스", "불편해요", 2),
]

# 리스트를 JSON으로 변환
json_data = json.dumps([r.to_dict() for r in responses], ensure_ascii=False, indent=2)
print(json_data)

# %% [markdown]
# ### 6.3.2 __str__과 __repr__

# %%
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        """print() 시 출력되는 문자열"""
        return f"{self.name}: {self.price:,}원"
    
    def __repr__(self):
        """객체 표현 (디버깅용)"""
        return f"Product(name='{self.name}', price={self.price})"

# %%
product = Product("노트북", 1500000)

print(product)       # __str__ 호출: 노트북: 1,500,000원
print(repr(product)) # __repr__ 호출: Product(name='노트북', price=1500000)

# %%
# 리스트에서는 __repr__가 사용됨
products = [Product("키보드", 50000), Product("마우스", 30000)]
print(products)

# %% [markdown]
# ---
# ## 6.4 @classmethod

# %% [markdown]
# ### @classmethod: 클래스 자체에서 호출

# %%
class User:
    user_count = 0  # 클래스 변수
    
    def __init__(self, name):
        self.name = name
        User.user_count += 1
    
    @classmethod
    def get_count(cls):
        """클래스 메서드: 클래스 변수에 접근"""
        return f"총 {cls.user_count}명의 사용자가 있습니다."
    
    @classmethod
    def from_dict(cls, data):
        """딕셔너리에서 인스턴스 생성"""
        return cls(data["name"])

# %%
user1 = User("홍길동")
user2 = User("김철수")

# 클래스에서 직접 호출
print(User.get_count())

# 딕셔너리에서 생성
user3 = User.from_dict({"name": "이영희"})
print(user3.name)
print(User.get_count())

# %% [markdown]
# ---
# ## 6.5 상속(Inheritance) 개념 소개
#
# 상속은 기존 클래스의 기능을 물려받아 새 클래스를 만드는 것입니다.
# - **부모 클래스(Parent/Base)**: 기능을 제공하는 클래스
# - **자식 클래스(Child/Derived)**: 기능을 물려받는 클래스
#
# > 다음 장에서 배울 `Pydantic`의 `BaseModel`도 상속을 사용합니다!

# %%
# 부모 클래스
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name}이(가) 소리를 냅니다."
    
    def move(self):
        return "움직입니다."

# %%
# 자식 클래스
class Cat(Animal):  # Animal을 상속
    def speak(self):  # 메서드 오버라이드
        return f"{self.name}이(가) 야옹!"
    
    def purr(self):  # 새 메서드 추가
        return f"{self.name}이(가) 그르렁..."

# %%
cat = Cat("나비")
print(cat.speak())  # 오버라이드된 메서드
print(cat.move())   # 부모에서 상속받은 메서드
print(cat.purr())   # 자식 클래스의 새 메서드

# %% [markdown]
# ### super()로 부모 메서드 호출

# %%
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def info(self):
        return f"{self.name}: {self.salary:,}원"

class Manager(Employee):
    def __init__(self, name, salary, team):
        super().__init__(name, salary)  # 부모 생성자 호출
        self.team = team  # 추가 속성
    
    def info(self):
        base_info = super().info()  # 부모 메서드 호출
        return f"{base_info} (팀: {self.team})"

# %%
mgr = Manager("홍길동", 5000000, "개발팀")
print(mgr.info())

# %% [markdown]
# ---
# ## 6.6 실습: SurveyAnalyzer 클래스

# %%
class SurveyAnalyzer:
    """
    설문 데이터 분석기 클래스
    - 설문 응답 데이터를 받아 기본적인 통계/집계/필터링 기능을 제공
    """
    
    def __init__(self, data):
        """
        생성자(Constructor)
        - 분석할 설문 데이터를 초기화
        
        Args:
            data (list[dict]):
                설문 응답 리스트
                예: [{"category": "서비스", "score": 5}, {...}]
        """
        self.data = data          # 설문 응답 데이터 저장
    
    def count_by(self, key):
        """
        특정 키 기준으로 값의 개수를 집계
        
        Args:
            key (str): 집계 기준이 되는 키 이름
        
        Returns:
            dict: {값: 개수} 형태의 딕셔너리
        """
        counts = {}  # 집계 결과 저장용 딕셔너리
        
        for item in self.data:
            val = item.get(key, "기타")  # 키가 없으면 "기타"로 처리
            counts[val] = counts.get(val, 0) + 1
        
        return counts
    
    def average_by(self, group_key, value_key):
        """
        그룹별 평균 계산
        
        Args:
            group_key (str): 그룹 기준 키 (예: category)
            value_key (str): 평균을 낼 값의 키 (예: score)
        
        Returns:
            dict: {그룹: 평균값} 형태의 딕셔너리
        """
        sums = {}     # 그룹별 합계 저장
        counts = {}   # 그룹별 개수 저장
        
        for item in self.data:
            group = item.get(group_key, "기타")   # 그룹 키가 없으면 "기타"로 처리
            
            value = item.get(value_key, 0)   # 값이 없으면 0으로 처리
            
            sums[group] = sums.get(group, 0) + value
            counts[group] = counts.get(group, 0) + 1
        
        # 평균 계산 (소수점 둘째 자리까지 반올림)
        return {k: round(sums[k] / counts[k], 2) for k in counts}
    
    def filter_by(self, key, value):
        """
        특정 조건에 맞는 설문 응답만 필터링
        
        Args:
            key (str): 필터링 기준 키
            value: 필터링할 값
        
        Returns:
            SurveyAnalyzer | None:
                - 필터링 결과가 있으면 새로운 SurveyAnalyzer 객체 반환
                - 결과가 없으면 None 반환
        """
        # 조건에 맞는 데이터만 추출
        filtered = [item for item in self.data if item.get(key) == value]
        
        # 필터 결과가 있으면 새 분석기 생성, 없으면 None
        return SurveyAnalyzer(filtered) if filtered else None
    
    def summary(self):
        """
        데이터 요약 정보 반환
        
        Returns:
            dict:
                - total_count: 전체 응답 수
                - keys: 설문 데이터에 포함된 키 목록
        """
        return {
            "total_count": len(self.data),
            "keys": list(self.data[0].keys()) if self.data else []
        }
    
    def to_dict(self):
        """
        전체 데이터를 딕셔너리 형태로 반환
        - JSON 변환, API 응답 등에 사용 가능
        """
        return {
            "count": len(self.data),
            "data": self.data
        }

# %%
# 사용 예시
survey_data = [
    {"id": 1, "category": "제품", "score": 5},
    {"id": 2, "category": "서비스", "score": 4},
    {"id": 3, "category": "제품", "score": 3},
    {"id": 4, "category": "배송", "score": 5},
    {"id": 5, "category": "제품", "score": 4},
]

analyzer = SurveyAnalyzer(survey_data)

print("요약:", analyzer.summary())
print("카테고리별 개수:", analyzer.count_by("category"))
print("카테고리별 평균:", analyzer.average_by("category", "score"))

# %%
# 필터링 후 분석
product_analyzer = analyzer.filter_by("category", "제품")
if product_analyzer:
    print("\n제품 카테고리만:")
    print("  개수:", product_analyzer.summary()["total_count"])
    print("  데이터:", product_analyzer.to_dict()["data"])

# %% [markdown]
# ---
# ## 연습문제

# %% [markdown]
# ### 문제 1: Rectangle 클래스
# 너비와 높이를 가지는 사각형 클래스를 만드세요.
# - 면적과 둘레 계산 메서드
# - __str__ 메서드

# %%
class Rectangle:
    # 여기에 코드 작성
    pass


# %% [markdown]
# ### 문제 2: BankAccount 클래스
# 입금, 출금, 잔액 조회가 가능한 은행 계좌 클래스를 만드세요.
# - 출금 시 잔액 부족하면 에러
# - 거래 내역 기록

# %%
class BankAccount:
    # 여기에 코드 작성
    pass


# %% [markdown]
# ### 문제 3: Counter 클래스 (카운터)
# 다음 기능을 가진 카운터 클래스를 만드세요.
# - add(item): 항목 추가
# - count(item): 특정 항목 개수
# - most_common(n): 상위 n개
# - total(): 전체 개수

# %%
class Counter:
    # 여기에 코드 작성
    pass


# %% [markdown]
# ### 문제 4: ReportGenerator 클래스
# 분석 결과를 받아서 보고서를 생성하는 클래스를 만드세요.
# - add_section(title, content)
# - to_markdown()
# - to_dict()

# %%
class ReportGenerator:
    # 여기에 코드 작성
    pass



# %%
