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
# # 10. NumPy와 선형대수 기초
#
# **학습 목표**: NumPy의 핵심 연산과 선형대수를 익혀 AI 데이터 처리의 기반을 다집니다.
#
# ---

# %% [markdown]
# ## 문법 설명
#
# ### 1. NumPy 배열 (ndarray)
#
# **정의**: 다차원 배열을 효율적으로 처리하는 자료구조입니다.
#
# **임포트**:
# ```python
# import numpy as np
# ```
#
# **배열 생성**:
# | 함수 | 설명 | 예시 |
# |------|------|------|
# | `np.array(리스트)` | 리스트에서 배열 생성 | `np.array([1,2,3])` |
# | `np.zeros(shape)` | 0으로 채운 배열 | `np.zeros((3,3))` |
# | `np.ones(shape)` | 1로 채운 배열 | `np.ones((2,2))` |
# | `np.arange(시작, 끝, 증가분)` | 범위 배열 | `np.arange(0, 10, 2)` |
# | `np.linspace(시작, 끝, 개수)` | 균등 간격 배열 | `np.linspace(0, 1, 5)` |
# | `np.random.rand(shape)` | 랜덤 배열 (0~1) | `np.random.rand(3,3)` |
#
# **배열 속성**:
# - `arr.shape`: 차원 크기 `(행, 열)`
# - `arr.dtype`: 데이터 타입
# - `arr.size`: 전체 요소 개수
# - `arr.ndim`: 차원 수
#
# ---
#
# ### 2. 배열 연산
#
# **산술 연산** (요소별):
# - `+`, `-`, `*`, `/`: 요소별 연산
# - `**`: 거듭제곱
# - `np.sqrt()`, `np.exp()`, `np.log()`: 수학 함수
#
# **집계 함수**:
# | 함수 | 설명 | 예시 |
# |------|------|------|
# | `np.sum()` | 합계 | `np.sum(arr)` |
# | `np.mean()` | 평균 | `np.mean(arr)` |
# | `np.std()` | 표준편차 | `np.std(arr)` |
# | `np.min()`, `np.max()` | 최소/최대 | `np.min(arr)` |
# | `axis` 파라미터 | 축 지정 | `np.sum(arr, axis=0)` |
#
# **인덱싱과 슬라이싱**:
# - `arr[인덱스]`: 요소 접근
# - `arr[시작:끝]`: 슬라이싱
# - `arr[조건]`: 불리언 인덱싱
#
# ---
#
# ### 3. 선형대수 연산
#
# **행렬 연산**:
# | 함수 | 설명 | 예시 |
# |------|------|------|
# | `np.dot(a, b)` | 행렬 곱셈 | `np.dot(A, B)` |
# | `A @ B` | 행렬 곱셈 (연산자) | `A @ B` |
# | `np.transpose(A)` | 전치 행렬 | `A.T` |
# | `np.linalg.inv(A)` | 역행렬 | `np.linalg.inv(A)` |
# | `np.linalg.det(A)` | 행렬식 | `np.linalg.det(A)` |
#
# **벡터 연산**:
# - 내적: `np.dot(a, b)` 또는 `a @ b`
# - 외적: `np.outer(a, b)`
# - 노름: `np.linalg.norm(a)`
#
# **특이값 분해 (SVD)**:
# ```python
# U, s, Vt = np.linalg.svd(A)
# ```
#
# ---
# ## 실습 시작
#
# 아래 실습을 통해 위 문법들을 직접 사용해봅니다.
#
# ---

# %% [markdown]
# ## NumPy가 AI에서 중요한 이유
#
# - **수치 연산 최적화**: Python 리스트보다 수십 배 빠른 연산
# - **다차원 배열**: 이미지, 텍스트 임베딩, 시계열 등 다양한 데이터 표현
# - **선형대수 지원**: 딥러닝의 핵심 연산(행렬 곱셈, 내적 등) 기본 제공
# - **생태계 기반**: PyTorch, TensorFlow, scikit-learn 등 모든 AI 라이브러리가 NumPy 기반

# %% [markdown]
# ---
# ## 10.1 NumPy 배열 기초

# %% [markdown]
# ### 10.1.1 ndarray 생성

# %%
import numpy as np

# 스칼라 (0차원) - 단일 값
scalar = np.array(5)
print(f"스칼라: {scalar}, shape: {scalar.shape}, ndim: {scalar.ndim}")

# %%
# 벡터 (1차원) - AI에서 특성 벡터, 임베딩 등에 사용
vector = np.array([1, 2, 3, 4, 5])
print(f"벡터: {vector}")
print(f"shape: {vector.shape}, ndim: {vector.ndim}, size: {vector.size}")

# %%
# 행렬 (2차원) - 데이터셋, 이미지 등에 사용
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f"행렬:\n{matrix}")
print(f"shape: {matrix.shape}, ndim: {matrix.ndim}")

# %%
# 텐서 (3차원 이상) - 배치 데이터, 컬러 이미지, 시계열 등
# 예: (배치 크기, 높이, 너비) 또는 (샘플 수, 시간 스텝, 특성 수)
tensor = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(f"텐서:\n{tensor}")
print(f"shape: {tensor.shape}, ndim: {tensor.ndim}")

# %% [markdown]
# ### 10.1.2 배열 생성 함수

# %%
# zeros, ones - 초기화에 자주 사용
zeros = np.zeros((3, 4))  # 3x4 영행렬
ones = np.ones((2, 3))    # 2x3 1행렬
print(f"zeros (3x4):\n{zeros}")
print(f"\nones (2x3):\n{ones}")

# %%
# arange, linspace - 연속 데이터 생성
arr1 = np.arange(0, 10, 2)      # 0부터 10 미만, 2 간격
arr2 = np.linspace(0, 1, 5)     # 0부터 1까지 5개 균등 분할
print(f"arange: {arr1}")
print(f"linspace: {arr2}")

# %%
# random - AI 학습에서 가중치 초기화 등에 사용
np.random.seed(42)  # 재현성을 위한 시드 설정

rand_uniform = np.random.rand(3, 3)      # 0~1 균등 분포
rand_normal = np.random.randn(3, 3)      # 표준 정규 분포 (평균 0, 표준편차 1)
rand_int = np.random.randint(1, 10, (3, 3))  # 1~9 정수

print(f"균등 분포:\n{rand_uniform.round(2)}")
print(f"\n정규 분포:\n{rand_normal.round(2)}")
print(f"\n정수 랜덤:\n{rand_int}")

# %% [markdown]
# ### 10.1.3 dtype (데이터 타입)

# %%
# dtype 확인 및 지정
arr_int = np.array([1, 2, 3])
arr_float = np.array([1.0, 2.0, 3.0])
arr_bool = np.array([True, False, True])

print(f"정수: {arr_int.dtype}")
print(f"실수: {arr_float.dtype}")
print(f"불리언: {arr_bool.dtype}")

# %%
# dtype 명시적 지정 (AI에서 메모리 최적화에 중요)
arr_f32 = np.array([1.0, 2.0, 3.0], dtype=np.float32)  # 32비트 (딥러닝 기본)
arr_f64 = np.array([1.0, 2.0, 3.0], dtype=np.float64)  # 64비트 (정밀 계산)

print(f"float32: {arr_f32.dtype}, 메모리: {arr_f32.nbytes} bytes")
print(f"float64: {arr_f64.dtype}, 메모리: {arr_f64.nbytes} bytes")

# %% [markdown]
# ---
# ## 10.2 인덱싱과 슬라이싱

# %% [markdown]
# ### 10.2.1 기본 인덱싱
#
# ```
# 2D 배열 인덱싱: arr[행, 열]
#
#        열 0  열 1  열 2
#       +----+----+----+
# 행 0  |  1 |  2 |  3 |
#       +----+----+----+
# 행 1  |  4 |  5 |  6 |
#       +----+----+----+
# 행 2  |  7 |  8 |  9 |
#       +----+----+----+
# ```

# %%
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(f"원본:\n{arr}")
print(f"\narr[0, 0] = {arr[0, 0]}")  # 첫 번째 요소
print(f"arr[1, 2] = {arr[1, 2]}")    # 2행 3열
print(f"arr[-1, -1] = {arr[-1, -1]}")  # 마지막 요소

# %% [markdown]
# ### 10.2.2 슬라이싱
#
# `arr[시작:끝:간격]` - 끝 인덱스는 포함하지 않음

# %%
# 행 슬라이싱
print(f"arr[0] (첫 번째 행):\n{arr[0]}")
print(f"\narr[:2] (처음 2개 행):\n{arr[:2]}")
print(f"\narr[1:] (두 번째 행부터):\n{arr[1:]}")

# %%
# 열 슬라이싱
print(f"arr[:, 0] (첫 번째 열): {arr[:, 0]}")
print(f"arr[:, :2] (처음 2개 열):\n{arr[:, :2]}")
print(f"arr[:, 1:] (두 번째 열부터):\n{arr[:, 1:]}")

# %%
# 행과 열 동시 슬라이싱
print(f"arr[:2, 1:] (처음 2행, 두 번째 열부터):\n{arr[:2, 1:]}")
print(f"\narr[::2, ::2] (홀수 행/열만):\n{arr[::2, ::2]}")

# %% [markdown]
# ### 10.2.3 조건부 인덱싱 (Boolean Indexing)
#
# AI 데이터 전처리에서 매우 자주 사용됩니다.

# %%
scores = np.array([85, 92, 78, 95, 88, 72, 90])

# 조건을 만족하는 요소만 추출
high_scores = scores[scores >= 90]
print(f"원본: {scores}")
print(f"90점 이상: {high_scores}")

# %%
# 조건 마스크 확인
mask = scores >= 90
print(f"마스크: {mask}")
print(f"True 개수: {mask.sum()}")

# %%
# 여러 조건 조합
# 80점 이상 AND 90점 미만
mid_scores = scores[(scores >= 80) & (scores < 90)]
print(f"80~89점: {mid_scores}")

# 75점 미만 OR 95점 이상
extreme_scores = scores[(scores < 75) | (scores >= 95)]
print(f"극단값 (75 미만 또는 95 이상): {extreme_scores}")

# %%
# 2D 배열에서 조건부 인덱싱
data = np.array([
    [1, -2, 3],
    [-4, 5, -6],
    [7, -8, 9]
])

# 음수를 0으로 변환 (ReLU 활성화 함수와 유사)
data_relu = data.copy()
data_relu[data_relu < 0] = 0
print(f"원본:\n{data}")
print(f"\n음수를 0으로 (ReLU 유사):\n{data_relu}")

# %% [markdown]
# ### 10.2.4 팬시 인덱싱 (Fancy Indexing)

# %%
arr = np.array([10, 20, 30, 40, 50])

# 인덱스 배열로 선택
indices = [0, 2, 4]
print(f"indices {indices}로 선택: {arr[indices]}")

# 2D 배열에서
matrix = np.arange(1, 10).reshape(3, 3)
print(f"\n행렬:\n{matrix}")
print(f"[0, 2]행의 [1, 2]열: {matrix[[0, 2], [1, 2]]}")

# %% [markdown]
# ---
# ## 10.3 배열 연산과 브로드캐스팅

# %% [markdown]
# ### 10.3.1 요소별 연산 (Element-wise)

# %%
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {a + b}")
print(f"a * b = {a * b}")
print(f"a ** 2 = {a ** 2}")
print(f"np.sqrt(a) = {np.sqrt(a)}")

# %% [markdown]
# ### 10.3.2 집계 함수

# %%
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

print(f"데이터:\n{data}")
print(f"\n전체 합: {data.sum()}")
print(f"전체 평균: {data.mean()}")
print(f"전체 최대: {data.max()}")
print(f"전체 최소: {data.min()}")
print(f"표준편차: {data.std():.2f}")

# %%
# axis 매개변수: 연산 방향 지정
# axis=0: 열 방향 (위→아래), axis=1: 행 방향 (왼→오른)
print(f"열별 합 (axis=0): {data.sum(axis=0)}")
print(f"행별 합 (axis=1): {data.sum(axis=1)}")
print(f"열별 평균 (axis=0): {data.mean(axis=0)}")
print(f"행별 평균 (axis=1): {data.mean(axis=1)}")

# %%
# argmax, argmin: 최대/최소값의 인덱스
print(f"최대값 인덱스 (전체): {data.argmax()}")  # flatten된 인덱스
print(f"행별 최대값 인덱스: {data.argmax(axis=1)}")
print(f"열별 최대값 인덱스: {data.argmax(axis=0)}")

# %% [markdown]
# ### 10.3.3 브로드캐스팅 (Broadcasting)
#
# 크기가 다른 배열 간의 연산을 가능하게 하는 NumPy의 핵심 기능입니다.
#
# **브로드캐스팅 규칙:**
# 1. 차원이 다르면 작은 쪽의 shape 앞에 1을 추가
# 2. 각 차원에서 크기가 1이거나 같으면 브로드캐스팅 가능
# 3. 크기가 1인 차원은 다른 배열의 크기에 맞게 확장

# %%
# 스칼라와 배열
arr = np.array([1, 2, 3, 4])
print(f"arr + 10 = {arr + 10}")  # 10이 [10, 10, 10, 10]으로 브로드캐스트

# %%
# 1D 배열과 2D 배열
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
row = np.array([10, 20, 30])

print(f"matrix:\n{matrix}")
print(f"row: {row}")
print(f"\nmatrix + row (각 행에 row 더하기):\n{matrix + row}")

# %%
# 열 벡터와 행 벡터
col = np.array([[1], [2], [3]])  # (3, 1)
row = np.array([10, 20, 30])     # (3,)

print(f"col (3x1):\n{col}")
print(f"row (3,): {row}")
print(f"\ncol + row (3x3 결과):\n{col + row}")

# %% [markdown]
# ### 10.3.4 AI에서의 브로드캐스팅 활용

# %%
# 예시 1: 배치 데이터에 바이어스 더하기
# 신경망에서 각 샘플에 동일한 바이어스를 더하는 연산
batch_data = np.random.randn(4, 3)  # 4개 샘플, 3개 특성
bias = np.array([0.1, 0.2, 0.3])    # 3개 특성에 대한 바이어스

result = batch_data + bias
print(f"배치 데이터 (4x3):\n{batch_data.round(2)}")
print(f"\n바이어스 (3,): {bias}")
print(f"\n바이어스 추가 후:\n{result.round(2)}")

# %%
# 예시 2: 특성별 정규화 (각 열의 평균을 빼기)
data = np.array([[10, 200, 3000],
                 [20, 300, 4000],
                 [30, 400, 5000],
                 [40, 500, 6000]])

mean = data.mean(axis=0)  # 열별 평균
centered = data - mean    # 브로드캐스팅으로 모든 행에서 평균 빼기

print(f"원본 데이터:\n{data}")
print(f"\n열별 평균: {mean}")
print(f"\n중심화된 데이터:\n{centered}")

# %% [markdown]
# ---
# ## 연습문제

# %% [markdown]
# ### 문제 1: 배열 생성과 속성
# 다음 조건의 NumPy 배열을 생성하고 shape, dtype, size를 출력하세요.
# 1. 1부터 20까지의 정수 배열
# 2. 0부터 1까지 100개로 균등 분할된 배열
# 3. 평균 5, 표준편차 2인 정규분포에서 (3, 4) 형태의 랜덤 배열

# %%
# 여기에 코드 작성


# %% [markdown]
# ### 문제 2: 조건부 인덱싱
# 다음 성적 데이터에서 조건부 인덱싱을 사용하여:
# 1. 80점 이상인 점수만 추출
# 2. 60점 미만인 점수를 60점으로 변경 (하한선 적용)
# 3. 평균 이상인 점수의 개수 계산

# %%
grades = np.array([45, 78, 92, 56, 88, 73, 95, 62, 81, 49])
# 여기에 코드 작성


# %% [markdown]
# ### 문제 3: 브로드캐스팅 활용
# 다음 데이터를 열별로 정규화(각 열에서 최소값 빼고 범위로 나누기)하세요.
# ```python
# data = np.array([[10, 100, 1000],
#                  [20, 200, 2000],
#                  [30, 300, 3000],
#                  [40, 400, 4000]])
# ```

# %%
data = np.array([[10, 100, 1000],
                 [20, 200, 2000],
                 [30, 300, 3000],
                 [40, 400, 4000]])
# 여기에 코드 작성


# %%



