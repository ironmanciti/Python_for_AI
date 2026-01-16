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
# # 5. 파일 I/O와 JSON
#
# **학습 목표**: 파일을 읽고 쓰는 방법과 JSON 데이터 처리를 익힙니다.
#
# ---

# %% [markdown]
# ## 문법 설명
#
# ### 1. 파일 읽기/쓰기
#
# **정의**: 파일을 열어 데이터를 읽거나 씁니다.
#
# **with 문 (권장)**:
# ```python
# with open("파일명", "모드") as 파일객체:
#     코드
# # 자동으로 파일 닫힘
# ```
#
# **파일 모드**:
# | 모드 | 의미 | 설명 |
# |------|------|------|
# | `"r"` | 읽기 | 기본값, 파일 없으면 에러 |
# | `"w"` | 쓰기 | 파일 덮어쓰기, 없으면 생성 |
# | `"a"` | 추가 | 파일 끝에 추가, 없으면 생성 |
# | `"x"` | 배타적 생성 | 파일 있으면 에러 |
# | `"r+"` | 읽기+쓰기 | 파일 수정 |
# | `"b"` | 바이너리 | 이미지 등 바이너리 파일 |
#
# **주요 메서드**:
# | 메서드 | 설명 | 예시 |
# |--------|------|------|
# | `read()` | 전체 읽기 | `f.read()` |
# | `readline()` | 한 줄 읽기 | `f.readline()` |
# | `readlines()` | 모든 줄 읽기 (리스트) | `f.readlines()` |
# | `write(문자열)` | 문자열 쓰기 | `f.write("text")` |
# | `writelines(리스트)` | 여러 줄 쓰기 | `f.writelines(lines)` |
#
# **파일 경로**:
# - 상대 경로: `"data/file.txt"`
# - 절대 경로: `"C:/Users/name/file.txt"`
# - `os.path.join()`: 경로 결합 (OS 독립적)
#
# ---
#
# ### 2. JSON 처리
#
# **정의**: JSON(JavaScript Object Notation)은 데이터 교환 형식입니다.
#
# **JSON 모듈**:
# ```python
# import json
# ```
#
# **주요 함수**:
# | 함수 | 설명 | 예시 |
# |------|------|------|
# | `json.loads(문자열)` | JSON 문자열 → Python 객체 | `json.loads('{"a":1}')` |
# | `json.dumps(객체)` | Python 객체 → JSON 문자열 | `json.dumps({"a":1})` |
# | `json.load(파일)` | JSON 파일 → Python 객체 | `json.load(f)` |
# | `json.dump(객체, 파일)` | Python 객체 → JSON 파일 | `json.dump(data, f)` |
#
# **타입 매핑**:
# | JSON | Python |
# |------|--------|
# | object | dict |
# | array | list |
# | string | str |
# | number | int/float |
# | true/false | True/False |
# | null | None |
#
# **옵션**:
# - `indent=숫자`: 들여쓰기 (가독성)
# - `ensure_ascii=False`: 한글 유지
# - `sort_keys=True`: 키 정렬
#
# ---
# ## 실습 시작
#
# 아래 실습을 통해 위 문법들을 직접 사용해봅니다.
#
# ---

# %% [markdown]
# ## 5.1 파일 읽기와 쓰기

# %% [markdown]
# ### 5.1.1 with open 문법
#
# `with` 문을 사용하면 파일을 자동으로 닫아주어 안전합니다.

# %%
# 파일 쓰기
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요!\n")
    f.write("파이썬 파일 I/O 연습입니다.\n")
    f.write("세 번째 줄입니다.\n")

print("파일이 생성되었습니다.")

# %%
# 파일 읽기 (전체)
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("=== 파일 내용 ===")
print(content)

# %%
# 한 줄씩 읽기
with open("sample.txt", "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, start=1):
        print(f"{line_num}: {line.strip()}")

# %%
# readlines(): 리스트로 읽기
with open("sample.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(type(lines))
print(lines)

# %% [markdown]
# ### 5.1.2 파일 모드

# %%
# 모드 설명
file_modes = """
파일 모드:
- 'r'  : 읽기 (기본값, 파일 없으면 에러)
- 'w'  : 쓰기 (파일 없으면 생성, 있으면 덮어쓰기)
- 'a'  : 추가 (파일 끝에 내용 추가)
- 'x'  : 배타적 생성 (파일 있으면 에러)
- 'b'  : 바이너리 모드 (rb, wb 등)
- '+'  : 읽기+쓰기 (r+, w+ 등)
"""
print(file_modes)

# %%
# 파일에 추가하기 (append)
with open("sample.txt", "a", encoding="utf-8") as f:
    f.write("추가된 네 번째 줄입니다.\n")

# 확인
with open("sample.txt", "r", encoding="utf-8") as f:
    print(f.read())

# %% [markdown]
# ### 5.1.3 writelines와 리스트 처리

# %%
# 리스트를 파일에 쓰기
lines_to_write = [
    "첫 번째 항목\n",
    "두 번째 항목\n",
    "세 번째 항목\n"
]

with open("list_output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines_to_write)

# 확인
with open("list_output.txt", "r", encoding="utf-8") as f:
    print(f.read())

# %% [markdown]
# ### mode, encoding 정리
# | 모드    | 읽기 | 쓰기 | 추가 | 파일 없을 때 | 파일 있을 때 | 내용 초기화 | 쓰기 위치 | 대표 용도       |
# | ----- | -- | -- | -- | ------- | ------- | ------ | ----- | ----------- |
# | `r`   | ✅  | ❌  | ❌  | ❌ 에러    | 유지      | ❌      | —     | 파일 내용 읽기    |
# | `w`   | ❌  | ✅  | ❌  | 생성      | **덮어씀** | ✅      | 처음    | 결과 파일 생성    |
# | `a`   | ❌  | ✅  | ✅  | 생성      | 유지      | ❌      | 끝     | 로그 누적       |
# | `x`   | ❌  | ✅  | ❌  | 생성      | ❌ 에러    | —      | 처음    | 최초 1회 생성    |
# | `r+`  | ✅  | ✅  | ❌  | ❌ 에러    | 유지      | ❌      | 처음    | 기존 파일 일부 수정 |
# | `w+`  | ✅  | ✅  | ❌  | 생성      | **덮어씀** | ✅      | 처음    | 초기화 + 검증    |
# | `a+`  | ✅  | ✅  | ✅  | 생성      | 유지      | ❌      | 끝     | 로그 + 조회     |
# | `x+`  | ✅  | ✅  | ❌  | 생성      | ❌ 에러    | —      | 처음    | 안전 생성 + 확인  |
# | `rb`  | ✅  | ❌  | ❌  | ❌ 에러    | 유지      | ❌      | —     | 바이너리 읽기     |
# | `wb`  | ❌  | ✅  | ❌  | 생성      | **덮어씀** | ✅      | 처음    | 바이너리 쓰기     |
# | `ab`  | ❌  | ✅  | ✅  | 생성      | 유지      | ❌      | 끝     | 바이너리 로그     |
# | `rb+` | ✅  | ✅  | ❌  | ❌ 에러    | 유지      | ❌      | 처음    | 바이너리 수정     |
#
#
# | 인코딩       | 한글 | 이모지 | 용량   | 주 용도        |
# | --------- | -- | --- | ---- | ----------- |
# | utf-8     | ✅  | ✅   | 작음   | 표준 ⭐        |
# | utf-8-sig | ✅  | ✅   | 약간 ↑ | Excel CSV   |
# | cp949     | ✅  | ❌   | 중간   | 구형 Windows  |
# | euc-kr    | ✅  | ❌   | 중간   | 레거시         |
# | ascii     | ❌  | ❌   | 작음   | 테스트         |
# | latin-1   | ❌  | ❌   | 작음   | 서양권         |
# | utf-16    | ✅  | ✅   | 큼    | Windows 시스템 |

# %% [markdown]
# ---
# ## 5.2 JSON 처리
#
# JSON(JavaScript Object Notation)은 데이터 교환에 널리 사용되는 형식입니다.

# %% [markdown]
# ### 5.2.1 json 모듈 기본

# %%
import json

# Python 객체 → JSON 문자열
data = {
    "name": "홍길동",
    "age": 25,
    "skills": ["Python", "SQL", "Excel"],
    "active": True
}

json_str = json.dumps(data, ensure_ascii=False, indent=2)
print("JSON 문자열:")
print(json_str)

# %%
# JSON 문자열 → Python 객체
json_text = '{"name": "김철수", "age": 30, "city": "서울"}'
parsed = json.loads(json_text)

print(type(parsed))
print(parsed)
print(parsed["name"])

# %% [markdown]
# ### 5.2.2 JSON 파일 저장과 읽기

# %%
# Python 객체를 JSON 파일로 저장
survey_result = {
    "total_responses": 50,
    "average_score": 3.74,
    "categories": {
        "제품": {"count": 24, "avg": 3.83},
        "배송": {"count": 14, "avg": 3.79},
        "서비스": {"count": 12, "avg": 3.58}
    },
    "top_keywords": ["배송", "품질", "좋아요", "만족", "친절"]
}

with open("summary.json", "w", encoding="utf-8") as f:
    json.dump(survey_result, f, ensure_ascii=False, indent=2)

print("JSON 파일 저장 완료!")

# %%
# JSON 파일 읽기
with open("summary.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(type(loaded))
print(f"총 응답: {loaded['total_responses']}")
print(f"평균 점수: {loaded['average_score']}")
print(f"카테고리: {list(loaded['categories'].keys())}")

# %% [markdown]
# ### 5.2.3 JSON 옵션들

# %%
data = {"이름": "홍길동", "점수": 95.5, "합격": True}

# ensure_ascii=False: 한글 그대로 출력
print("ensure_ascii=True (기본):")
print(json.dumps(data))

print("\nensure_ascii=False:")
print(json.dumps(data, ensure_ascii=False))

# %%
# indent: 들여쓰기
print("indent=2:")
print(json.dumps(data, ensure_ascii=False, indent=2))

# %%
# sort_keys: 키 정렬
data = {"c": 3, "a": 1, "b": 2}
print("정렬 전:", json.dumps(data))
print("정렬 후:", json.dumps(data, sort_keys=True))

# %% [markdown]
# ---
# ## 5.3 pathlib (경로 처리)
#
# 파일 경로를 객체지향적으로 다루는 현대적인 방법입니다.

# %%
from pathlib import Path

# 현재 디렉토리
current = Path(".")
print(f"현재 경로: {current.absolute()}")

# %%
# 경로 결합
data_dir = Path("data")
file_path = data_dir / "survey_responses.csv"
print(f"결합된 경로: {file_path}")

# %%
# 경로 정보
sample_path = Path("data/survey_responses.csv")

print(f"파일명: {sample_path.name}")
print(f"확장자: {sample_path.suffix}")
print(f"파일명(확장자 제외): {sample_path.stem}")
print(f"부모 디렉토리: {sample_path.parent}")

# %%
# 파일/디렉토리 확인
data_folder = Path("data")

print(f"존재 여부: {data_folder.exists()}")
print(f"디렉토리인가: {data_folder.is_dir()}")

# %%
# 디렉토리 내 파일 목록
if data_folder.exists():
    for file in data_folder.iterdir():
        print(f"  {file.name}")

# %%
# 특정 패턴 파일 찾기
if data_folder.exists():
    json_files = list(data_folder.glob("*.json"))
    print(f"JSON 파일들: {json_files}")

# %%
# pathlib으로 파일 읽기
file_path = Path("data/sample_report.json")
if file_path.exists():
    content = file_path.read_text(encoding="utf-8")
    data = json.loads(content)
    print(f"제목: {data.get('title', 'N/A')}")

# %% [markdown]
# ---
# ## 5.4 CSV 파일 처리

# %%
import csv

# CSV 파일 읽기
with open("data/survey_responses.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)  # 첫 줄(헤더)
    print(f"헤더: {header}")
    
    # 첫 3개 행만 출력
    for i, row in enumerate(reader):
        if i >= 3:
            break
        print(row)

# %%
# DictReader: 딕셔너리로 읽기
with open("data/survey_responses.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    
    for i, row in enumerate(reader):
        if i >= 3:
            break
        print(f"ID: {row['id']}, 카테고리: {row['category']}, 점수: {row['satisfaction_score']}")

# %%
# CSV 파일 쓰기
output_data = [
    ["id", "name", "score"],
    [1, "홍길동", 95],
    [2, "김철수", 88],
    [3, "이영희", 92]
]

with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(output_data)

print("CSV 파일 저장 완료!")

# %% [markdown]
# ---
# ## 5.5 실습: 분석 결과를 JSON으로 저장
#
# Day1 분석 결과를 `summary.json`으로 저장합니다.

# %%
import json
from pathlib import Path
from datetime import datetime

# %%
# 분석 함수들 (이전 모듈에서 정의)
def count_by_category(data, key="category"):
    counts = {}
    for item in data:
        cat = item.get(key, "기타")
        counts[cat] = counts.get(cat, 0) + 1
    return counts

def avg_by_category(data, cat_key="category", val_key="score"):
    sums = {}
    counts = {}
    for item in data:
        cat = item.get(cat_key, "기타")
        val = item.get(val_key, 0)
        sums[cat] = sums.get(cat, 0) + val
        counts[cat] = counts.get(cat, 0) + 1
    
    return {cat: round(sums[cat] / counts[cat], 2) for cat in counts}

def extract_keywords(texts, min_length=2):
    word_counts = {}
    for text in texts:
        words = text.split()
        for word in words:
            if len(word) >= min_length:
                word_counts[word] = word_counts.get(word, 0) + 1
    
    # 빈도순 정렬
    sorted_words = sorted(word_counts.items(), key=lambda x: -x[1])
    return sorted_words[:10]

# %%
# 샘플 데이터 로드
survey_data = [
    {"id": 1, "category": "제품", "text": "품질이 좋습니다 만족", "score": 5},
    {"id": 2, "category": "서비스", "text": "친절한 응대 감사", "score": 5},
    {"id": 3, "category": "제품", "text": "기대 이하 실망", "score": 2},
    {"id": 4, "category": "배송", "text": "배송 지연 불만", "score": 2},
    {"id": 5, "category": "서비스", "text": "빠른 문의 해결", "score": 4},
    {"id": 6, "category": "제품", "text": "가격 대비 좋음", "score": 4},
    {"id": 7, "category": "배송", "text": "새벽배송 좋아요", "score": 5},
    {"id": 8, "category": "제품", "text": "디자인 예쁨 만족", "score": 5},
    {"id": 9, "category": "서비스", "text": "앱 불편 개선", "score": 2},
    {"id": 10, "category": "배송", "text": "포장 훼손 불만", "score": 2},
]

# %%
# 분석 실행
category_counts = count_by_category(survey_data)
category_avgs = avg_by_category(survey_data, val_key="score")

texts = [item["text"] for item in survey_data]
top_keywords = extract_keywords(texts)

# 전체 통계
total_count = len(survey_data)
total_avg = sum(item["score"] for item in survey_data) / total_count

# %%
# 요약 리포트 생성
summary = {
    "title": "설문 분석 결과 요약",
    "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "total_responses": total_count,
    "average_score": round(total_avg, 2),
    "category_stats": {
        cat: {
            "count": category_counts[cat],
            "avg_score": category_avgs[cat]
        }
        for cat in category_counts
    },
    "top_keywords": [
        {"keyword": word, "count": count}
        for word, count in top_keywords
    ],
    "notes": "Day1 분석 결과입니다. Day2에서 이 데이터를 활용합니다."
}

# %%
# JSON 파일로 저장
output_path = Path("data/day1_summary.json")

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

print(f"저장 완료: {output_path}")

# %%
# 저장된 파일 확인
with open(output_path, "r", encoding="utf-8") as f:
    loaded = json.load(f)

print("=== 저장된 내용 ===")
print(f"제목: {loaded['title']}")
print(f"생성 시간: {loaded['generated_at']}")
print(f"총 응답: {loaded['total_responses']}")
print(f"평균 점수: {loaded['average_score']}")
print(f"카테고리 수: {len(loaded['category_stats'])}")
print(f"상위 키워드 수: {len(loaded['top_keywords'])}")

# %% [markdown]
# ---
# ## 연습문제

# %% [markdown]
# ### 문제 1: 텍스트 파일 통계
# 텍스트 파일을 읽어서 총 줄 수, 단어 수, 글자 수를 반환하는 함수를 작성하세요.

# %%
def file_stats(filepath):
    """
    파일 통계 반환
    
    Returns:
        {"lines": 줄 수, "words": 단어 수, "chars": 글자 수}
    """
    # 여기에 코드 작성
    pass


# %% [markdown]
# ### 문제 2: JSON 병합
# 여러 JSON 파일을 읽어서 하나로 병합하는 함수를 작성하세요.

# %%
def merge_json_files(file_paths, output_path):
    """
    여러 JSON 파일을 하나로 병합
    
    Args:
        file_paths: JSON 파일 경로 리스트
        output_path: 출력 파일 경로
    """
    # 여기에 코드 작성
    pass


# %% [markdown]
# ### 문제 3: CSV to JSON 변환
# CSV 파일을 JSON 파일로 변환하는 함수를 작성하세요.

# %%
def csv_to_json(csv_path, json_path):
    """
    CSV 파일을 JSON으로 변환
    """
    # 여기에 코드 작성
    pass


# %% [markdown]
# ### 문제 4: 설정 파일 관리자
# 설정을 JSON으로 저장하고 로드하는 클래스를 작성하세요.

# %%
class ConfigManager:
    """
    JSON 기반 설정 관리자
    
    사용 예:
        config = ConfigManager("config.json")
        config.set("api_key", "abc123")
        config.get("api_key")
        config.save()
    """
    
    def __init__(self, filepath):
        # 여기에 코드 작성
        pass
    
    def get(self, key, default=None):
        pass
    
    def set(self, key, value):
        pass
    
    def save(self):
        pass

# %% [markdown]
# ### 정리 (테스트 파일 삭제)

# %%
import os

# 테스트로 생성한 파일들 정리
test_files = ["sample.txt", "list_output.txt", "output.csv"]
for f in test_files:
    if os.path.exists(f):
        os.remove(f)
        print(f"삭제: {f}")


# %%


