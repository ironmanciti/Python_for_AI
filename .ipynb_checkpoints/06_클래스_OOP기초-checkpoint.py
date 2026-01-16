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
# # 6. 클래스와 객체지향 프로그래밍 기초 + Gemini API 실습
#
# **학습 목표**: 
# - 클래스의 기본 개념을 익히고, Pydantic(BaseModel)을 이해하기 위한 기반을 마련합니다.
# - 배운 클래스 문법으로 실제 Gemini API 클라이언트를 구현합니다.
#
# ---

# %% [markdown]
# ## Part 1: 클래스(Class) 기초
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
        
        # 인스턴스 변수 (객체마다 각각 다른 값을 가질 수 있음)
        self.name = name        # 사람 이름
        self.age = age          # 나이
        self.city = city        # 거주 도시 (기본값: 서울)
        
        # 기본값을 갖는 인스턴스 변수
        self.created_at = "2024-01-01"  # 객체 생성 날짜
        
        # 객체가 생성되었음을 알려주는 출력
        print(f"{name} 인스턴스 생성됨")
    
    def greet(self):
        """
        인스턴스 메서드
        - self를 통해 인스턴스 변수에 접근
        - 객체가 수행할 수 있는 동작(행동)을 정의
        """
        return f"안녕하세요, {self.city}에 사는 {self.name}입니다."
    
    def have_birthday(self):
        """
        인스턴스 메서드
        - 나이를 1 증가시키는 기능
        - 인스턴스 상태를 변경함
        """
        self.age += 1  # 나이 증가
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
    # 생성자 메서드: 설문 응답 객체가 생성될 때 자동으로 실행됨
    def __init__(self, id, category, text, score):
        """
        생성자(Constructor)
        - 설문 응답 1건에 대한 초기 정보 설정
        """
        self.id = id   # 설문 응답의 고유 ID
        self.category = category   # 설문 카테고리 (예: 서비스, 가격, 디자인 등)
        self.text = text   # 응답자가 작성한 텍스트 내용
        self.score = score   # 응답 점수 (예: 1~5점 척도)
    
    def to_dict(self):
        """
        인스턴스 메서드
        - 객체(SurveyResponse)를 딕셔너리 형태로 변환
        - JSON 변환, DataFrame 생성 등에 활용 가능
        """
        return {
            "id": self.id,
            "category": self.category,
            "text": self.text,
            "score": self.score
        }
    
    def is_positive(self):
        """
        인스턴스 메서드
        - 설문 응답이 긍정적인지 판단
        - 기준: score가 4 이상이면 긍정 응답으로 간주
        """
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
    # 클래스 변수
    # - 모든 User 인스턴스가 공유하는 변수
    user_count = 0
    
    def __init__(self, name):
        """
        생성자(Constructor)
        - User 객체가 생성될 때 자동으로 호출됨
        """
        
        # 인스턴스 변수
        # - 각 객체마다 개별적으로 가지는 값
        self.name = name
        
        # 클래스 변수 증가
        # - User 클래스 전체에서 공유됨
        User.user_count += 1
    
    @classmethod
    def get_count(cls):
        """
        클래스 메서드
        - 인스턴스가 없어도 호출 가능
        - cls를 통해 클래스 변수에 접근
        """
        return f"총 {cls.user_count}명의 사용자가 있습니다."

# %%
# User 클래스의 인스턴스 생성
user1 = User("홍길동")

# 또 다른 User 인스턴스 생성
user2 = User("김철수")

# - 현재까지 생성된 User 인스턴스 개수 출력
print(User.get_count())

# %% [markdown]
# ---
# ## 6.5 상속(Inheritance) 개념 소개
#
# 상속은 기존 클래스의 기능을 물려받아 새 클래스를 만드는 것입니다.
# - **부모 클래스(Parent/Base)**: 기능을 제공하는 클래스
# - **자식 클래스(Child/Derived)**: 기능을 물려받는 클래스

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
# ## Part 2: 실전 적용 - Gemini API 클라이언트 클래스
#
# 이제 배운 클래스 문법으로 실제 Gemini API 클라이언트를 만들어봅니다!
# ---

# %% [markdown]
# ## 6.6 API 키 설정

# %%
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY")

if api_key:
    print(f"API 키 로드됨: {api_key[:8]}...")
else:
    print("API 키가 설정되지 않았습니다.")

# %% [markdown]
# ---
# ## 6.7 GeminiClient 클래스 구현
#
# 지금까지 배운 클래스 문법을 이용하여 Gemini API 클라이언트를 만듭니다!

# %%
import requests

class GeminiClient:
    """
    Gemini API 클라이언트
    
    클래스 문법 활용:
    - 클래스 속성: BASE_URL (모든 인스턴스 공유)
    - 인스턴스 속성: api_key, model, timeout
    - 인스턴스 메서드: generate(), extract_text() 등
    """
    
    # 클래스 속성 (모든 인스턴스가 공유)
    BASE_URL = "https://generativelanguage.googleapis.com/v1beta"
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gemini-1.5-flash"):
        """
        생성자: 인스턴스 초기화
        
        Args:
            api_key: API 키 (없으면 환경변수에서 로드)
            model: 사용할 모델명
        """
        self.api_key = api_key or get_api_key()
        self.model = model
        self.timeout = 30
        self._request_count = 0  # 요청 횟수 추적
    
    def generate(
        self, 
        prompt: str, 
        system_prompt: Optional[str] = None,
        max_tokens: int = 1024
    ) -> dict:
        """
        텍스트 생성 API 호출
        
        Args:
            prompt: 사용자 프롬프트
            system_prompt: 시스템 프롬프트 (선택)
            max_tokens: 최대 출력 토큰
        
        Returns:
            API 응답 딕셔너리
        """
        if not self.api_key:
            return self._simulate_response(prompt)
        
        url = f"{self.BASE_URL}/models/{self.model}:generateContent"
        
        # 요청 본문 구성
        contents = []
        
        if system_prompt:
            contents.append({
                "role": "user",
                "parts": [{"text": f"System: {system_prompt}"}]
            })
        
        contents.append({
            "role": "user", 
            "parts": [{"text": prompt}]
        })
        
        payload = {
            "contents": contents,
            "generationConfig": {
                "maxOutputTokens": max_tokens,
                "temperature": 0.7
            }
        }
        
        try:
            response = requests.post(
                url,
                params={"key": self.api_key},
                headers={"Content-Type": "application/json"},
                json=payload,
                timeout=self.timeout
            )
            response.raise_for_status()
            self._request_count += 1
            return response.json()
            
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
    
    def _simulate_response(self, prompt: str) -> dict:
        """API 키 없을 때 시뮬레이션 응답 (private 메서드)"""
        if "JSON" in prompt or "json" in prompt:
            simulated_text = json.dumps({
                "summary": "시뮬레이션된 요약입니다.",
                "insights": ["인사이트 1", "인사이트 2"],
                "action_items": ["액션 1", "액션 2"]
            }, ensure_ascii=False)
        elif "요약" in prompt:
            simulated_text = "이것은 시뮬레이션된 요약 응답입니다. 실제 API 키를 설정하면 Gemini의 응답을 받을 수 있습니다."
        else:
            simulated_text = f"[시뮬레이션] 프롬프트에 대한 응답입니다. 입력 길이: {len(prompt)}자"
        
        self._request_count += 1
        return {
            "candidates": [{
                "content": {
                    "parts": [{"text": simulated_text}],
                    "role": "model"
                }
            }],
            "_simulated": True
        }
    
    def extract_text(self, response: dict) -> str:
        """응답에서 텍스트 추출"""
        try:
            return response["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            return response.get("error", "텍스트를 추출할 수 없습니다.")
    
    def generate_text(self, prompt: str, **kwargs) -> str:
        """텍스트만 반환하는 간편 메서드"""
        response = self.generate(prompt, **kwargs)
        return self.extract_text(response)
    
    def to_dict(self) -> dict:
        """객체를 딕셔너리로 변환 (to_dict 패턴)"""
        return {
            "model": self.model,
            "has_api_key": bool(self.api_key),
            "timeout": self.timeout,
            "request_count": self._request_count
        }
    
    def __str__(self) -> str:
        """print() 시 출력"""
        status = "활성" if self.api_key else "시뮬레이션"
        return f"GeminiClient(model={self.model}, status={status})"
    
    def __repr__(self) -> str:
        """객체 표현 (디버깅용)"""
        return f"GeminiClient(model='{self.model}', has_key={bool(self.api_key)}, requests={self._request_count})"

# %%
# 클라이언트 인스턴스 생성
gemini = GeminiClient()

# __str__ 확인
print(gemini)

# __repr__ 확인
print(repr(gemini))

# to_dict() 확인
print(gemini.to_dict())

# %% [markdown]
# ---
# ## 6.8 GeminiClient 사용하기

# %%
# 기본 텍스트 생성
response = gemini.generate_text("안녕하세요, 자기소개를 해주세요.")
print(response)

# %%
# 시스템 프롬프트 사용
response = gemini.generate_text(
    prompt="파이썬의 장점 3가지를 알려주세요.",
    system_prompt="당신은 친절한 프로그래밍 강사입니다. 간결하게 답변하세요."
)
print(response)

# %%
# 요청 횟수 확인
print(f"총 요청 횟수: {gemini._request_count}")

# %% [markdown]
# ---
# ## 6.9 상속으로 기능 확장: RobustGeminiClient

# %%
import time
import random

class RobustGeminiClient(GeminiClient):
    """
    재시도 로직이 포함된 Gemini 클라이언트
    
    상속 활용:
    - GeminiClient의 모든 기능 상속
    - super().__init__()으로 부모 생성자 호출
    - 새로운 메서드 추가
    """
    
    def __init__(self, api_key: Optional[str] = None, max_retries: int = 3):
        super().__init__(api_key)  # 부모 생성자 호출
        self.max_retries = max_retries  # 추가 속성
    
    def generate_with_retry(self, prompt: str, **kwargs) -> dict:
        """재시도 로직이 포함된 생성"""
        last_error = None
        
        for attempt in range(self.max_retries):
            try:
                response = self.generate(prompt, **kwargs)
                
                # 에러 응답 체크
                if "error" in response:
                    raise Exception(response["error"])
                
                return response
                
            except Exception as e:
                last_error = e
                
                # 지수 백오프
                delay = (2 ** attempt) + random.uniform(0, 1)
                print(f"시도 {attempt + 1}/{self.max_retries} 실패: {e}")
                print(f"{delay:.1f}초 후 재시도...")
                time.sleep(delay)
        
        return {"error": f"최대 재시도 횟수 초과: {last_error}"}
    
    def safe_generate_text(self, prompt: str, **kwargs) -> tuple[str, bool]:
        """
        안전한 텍스트 생성
        
        Returns:
            (텍스트, 성공여부) 튜플
        """
        response = self.generate_with_retry(prompt, **kwargs)
        
        if "error" in response:
            return response["error"], False
        
        text = self.extract_text(response)
        return text, True
    
    def __repr__(self) -> str:
        """부모 메서드 오버라이드"""
        return f"RobustGeminiClient(model='{self.model}', max_retries={self.max_retries})"

# %%
# 상속 클래스 사용
safe_gemini = RobustGeminiClient(max_retries=3)
print(safe_gemini)  # 부모의 __str__ 사용
print(repr(safe_gemini))  # 오버라이드된 __repr__ 사용

# %%
# 안전한 텍스트 생성
text, success = safe_gemini.safe_generate_text("클래스 상속의 장점은?")
if success:
    print("성공:", text)
else:
    print("실패:", text)

# %% [markdown]
# ---
# ## 6.10 캐싱 기능 추가: CachedGeminiClient

# %%
class CachedGeminiClient(RobustGeminiClient):
    """
    캐싱이 포함된 클라이언트
    
    다중 상속 체인:
    GeminiClient → RobustGeminiClient → CachedGeminiClient
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._cache = {}  # 캐시 저장소
    
    def generate_text(self, prompt: str, use_cache: bool = True, **kwargs) -> str:
        """캐시를 활용한 텍스트 생성 (메서드 오버라이드)"""
        cache_key = hash(prompt + str(kwargs))
        
        if use_cache and cache_key in self._cache:
            print("[캐시 히트]")
            return self._cache[cache_key]
        
        # 부모 메서드 호출
        result = super().generate_text(prompt, **kwargs)
        self._cache[cache_key] = result
        
        return result
    
    def clear_cache(self):
        """캐시 초기화"""
        self._cache = {}
        print("캐시가 초기화되었습니다.")
    
    @property
    def cache_size(self) -> int:
        """캐시된 항목 수 (프로퍼티)"""
        return len(self._cache)

# %%
# 캐시 클라이언트 테스트
cached_gemini = CachedGeminiClient()

# 첫 번째 요청
result1 = cached_gemini.generate_text("파이썬이란?")
print(f"첫 번째 요청: {result1[:50]}...")
print(f"캐시 크기: {cached_gemini.cache_size}")

# 동일한 요청 (캐시에서)
result2 = cached_gemini.generate_text("파이썬이란?")
print(f"두 번째 요청: {result2[:50]}...")

# %% [markdown]
# ---
# ## 6.11 PromptBuilder 클래스
#
# AI API 호출을 위한 프롬프트를 구성하는 유틸리티 클래스입니다.

# %%
class PromptBuilder:
    """
    프롬프트 구성 도우미
    
    메서드 체이닝 패턴:
    builder.set_role("...").add_context("...").build()
    """
    
    def __init__(self):
        self.system = ""
        self.context = []
        self.instruction = ""
        self.output_format = ""
        self.examples = []
    
    def set_role(self, role: str):
        """역할 설정"""
        self.system = f"당신은 {role}입니다."
        return self  # 체이닝을 위해 self 반환
    
    def add_context(self, text: str):
        """컨텍스트 추가"""
        self.context.append(text)
        return self
    
    def add_data(self, data: dict, label: str = "데이터"):
        """딕셔너리 데이터를 컨텍스트로 추가"""
        formatted = json.dumps(data, ensure_ascii=False, indent=2)
        self.context.append(f"[{label}]\n{formatted}")
        return self
    
    def set_instruction(self, instruction: str):
        """지시사항 설정"""
        self.instruction = instruction
        return self
    
    def set_output_format(self, format_desc: str):
        """출력 형식 지정"""
        self.output_format = format_desc
        return self
    
    def add_example(self, input_text: str, output_text: str):
        """예시 추가 (Few-shot)"""
        self.examples.append({"input": input_text, "output": output_text})
        return self
    
    def build(self) -> str:
        """최종 프롬프트 생성"""
        parts = []
        
        if self.system:
            parts.append(f"### 역할\n{self.system}")
        
        if self.context:
            parts.append("### 컨텍스트\n" + "\n\n".join(self.context))
        
        if self.examples:
            examples_text = "### 예시\n"
            for i, ex in enumerate(self.examples, 1):
                examples_text += f"입력 {i}: {ex['input']}\n출력 {i}: {ex['output']}\n\n"
            parts.append(examples_text)
        
        if self.instruction:
            parts.append(f"### 지시사항\n{self.instruction}")
        
        if self.output_format:
            parts.append(f"### 출력 형식\n{self.output_format}")
        
        return "\n\n".join(parts)
    
    def to_messages(self) -> list[dict]:
        """API 메시지 형식으로 변환"""
        messages = []
        
        if self.system:
            messages.append({"role": "system", "content": self.system})
        
        user_content = []
        if self.context:
            user_content.append("=== 컨텍스트 ===")
            user_content.extend(self.context)
        if self.instruction:
            user_content.append(f"\n=== 지시사항 ===\n{self.instruction}")
        
        if user_content:
            messages.append({"role": "user", "content": "\n".join(user_content)})
        
        return messages

# %%
# 프롬프트 빌더 사용 예시 (메서드 체이닝)
builder = PromptBuilder()

prompt = (builder
    .set_role("고객 설문 분석 전문가")
    .add_data({
        "총_응답": 50,
        "평균_점수": 3.74,
        "카테고리별": {
            "제품": {"count": 24, "avg": 3.83},
            "배송": {"count": 14, "avg": 3.79},
            "서비스": {"count": 12, "avg": 3.58}
        }
    }, label="설문 통계")
    .add_context("주요 불만: 배송 지연, 포장 훼손")
    .set_instruction("위 데이터를 바탕으로 3가지 핵심 인사이트를 제시해주세요.")
    .set_output_format("각 항목은 번호를 붙여 간결하게 작성해주세요.")
    .build()
)

print(prompt)

# %%
# 프롬프트로 Gemini 호출
response = gemini.generate_text(prompt)
print("\n=== Gemini 응답 ===")
print(response)

# %% [markdown]
# ---
# ## 6.12 실습: 설문 분석 보고서 생성 함수

# %%
def generate_survey_report(
    gemini_client: GeminiClient,
    survey_stats: dict,
    format_type: str = "text"
) -> str:
    """
    설문 분석 보고서 생성
    
    Args:
        gemini_client: Gemini 클라이언트 인스턴스
        survey_stats: 설문 통계 데이터
        format_type: "text" 또는 "json"
    
    Returns:
        생성된 보고서
    """
    builder = PromptBuilder()
    
    prompt = (builder
        .set_role("고객 경험 분석 전문가")
        .add_data(survey_stats, "설문 분석 결과")
        .set_instruction("""
위 설문 데이터를 분석하여 다음을 포함한 보고서를 작성해주세요:
1. 전체 현황 요약 (2-3문장)
2. 주요 인사이트 3가지
3. 개선 필요 영역 2가지
4. 구체적인 액션 아이템 2가지
""")
        .build()
    )
    
    if format_type == "json":
        prompt += """

### 출력 형식
반드시 아래 JSON 형식으로만 응답하세요:
{
    "summary": "요약 문장",
    "insights": ["인사이트1", "인사이트2", "인사이트3"],
    "improvements_needed": ["개선1", "개선2"],
    "action_items": ["액션1", "액션2"]
}
"""
    
    return gemini_client.generate_text(prompt)

# %%
# 테스트 데이터
survey_stats = {
    "period": "2024년 1월",
    "total_responses": 50,
    "average_score": 3.74,
    "response_rate": "68%",
    "category_breakdown": {
        "제품": {"count": 24, "avg_score": 3.83, "positive_ratio": "62.5%"},
        "배송": {"count": 14, "avg_score": 3.79, "positive_ratio": "57.1%"},
        "서비스": {"count": 12, "avg_score": 3.58, "positive_ratio": "58.3%"}
    },
    "trend": "전월 대비 0.2점 상승"
}

# %%
# 텍스트 형식 보고서
print("=== 텍스트 보고서 ===")
text_report = generate_survey_report(gemini, survey_stats, "text")
print(text_report)

# %%
# JSON 형식 보고서
print("\n=== JSON 보고서 ===")
json_report = generate_survey_report(gemini, survey_stats, "json")
print(json_report)

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
# ### 문제 3: TranslationClient 클래스
# GeminiClient를 상속받아 번역 전용 클라이언트를 만드세요.
# - translate(text, target_language) 메서드
# - 지원 언어 검증

# %%
class TranslationClient(GeminiClient):
    # 여기에 코드 작성
    pass


# %% [markdown]
# ### 문제 4: SentimentAnalyzer 클래스
# GeminiClient를 활용하여 텍스트 감성 분석기를 만드세요.
# - analyze(text) → {"sentiment": "긍정/부정/중립", "confidence": 0.0-1.0}
# - 배치 분석 기능

# %%
class SentimentAnalyzer:
    # 여기에 코드 작성
    pass


