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
# # 11. Matplotlib 데이터 시각화
#
# **학습 목표**: Matplotlib으로 데이터를 시각화하여 AI 모델 분석과 인사이트 도출에 활용합니다.
#
# ---

# %% [markdown]
# ## 문법 설명
#
# ### 1. Matplotlib 기본
#
# **정의**: Python의 대표적인 데이터 시각화 라이브러리입니다.
#
# **임포트**:
# ```python
# import matplotlib.pyplot as plt
# import numpy as np
# ```
#
# **핵심 개념**:
# - **Figure**: 전체 그림 (캔버스)
# - **Axes**: 개별 그래프 (플롯 영역)
# - **Axis**: 축 (x축, y축)
#
# **OOP 스타일 (권장)**:
# ```python
# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_title("제목")
# plt.show()
# ```
#
# **한글 폰트 설정**:
# ```python
# plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호
# ```
#
# ---
#
# ### 2. 기본 차트 유형
#
# **선 그래프 (Line Plot)**:
# ```python
# ax.plot(x, y, label="레이블", linewidth=2, marker='o')
# ```
#
# **막대 그래프 (Bar Chart)**:
# ```python
# ax.bar(x, y, color='blue', edgecolor='black')
# ```
#
# **산점도 (Scatter Plot)**:
# ```python
# ax.scatter(x, y, s=크기, c=색상, alpha=투명도)
# ```
#
# **히스토그램 (Histogram)**:
# ```python
# ax.hist(data, bins=30, color='blue', edgecolor='white')
# ```
#
# **박스 플롯 (Box Plot)**:
# ```python
# ax.boxplot(data, vert=True, patch_artist=True)
# ```
#
# ---
#
# ### 3. 서브플롯
#
# **여러 그래프 배치**:
# ```python
# fig, axes = plt.subplots(행, 열, figsize=(너비, 높이))
# axes[0, 0].plot(x, y)  # 첫 번째 서브플롯
# axes[0, 1].bar(x, y)   # 두 번째 서브플롯
# ```
#
# **다양한 크기 배치**:
# ```python
# fig = plt.figure()
# ax1 = fig.add_subplot(2, 2, 1)  # 2x2 중 첫 번째
# ax2 = fig.add_subplot(2, 2, 2)  # 2x2 중 두 번째
# ```
#
# ---
#
# ### 4. 차트 커스터마이징
#
# **축 설정**:
# - `ax.set_xlim(시작, 끝)`: x축 범위
# - `ax.set_ylim(시작, 끝)`: y축 범위
# - `ax.set_xticks(리스트)`: x축 눈금
# - `ax.set_xlabel("레이블")`: x축 레이블
# - `ax.grid(True)`: 그리드 표시
#
# **범례와 주석**:
# - `ax.legend(loc="위치")`: 범례
# - `ax.annotate("텍스트", xy=(x,y), xytext=(x,y))`: 주석
# - `ax.text(x, y, "텍스트")`: 텍스트 추가
#
# **색상과 스타일**:
# - 색상: `color='red'`, `color='#3498db'`, `color=(0.2, 0.4, 0.8)`
# - 선 스타일: `linestyle='-'`, `'--'`, `'-.'`, `':'`
# - 마커: `marker='o'`, `'s'`, `'^'`, `'D'`
#
# ---
# ## 실습 시작
#
# 아래 실습을 통해 위 문법들을 직접 사용해봅니다.
#
# ---

# %% [markdown]
# ## 시각화가 AI에서 중요한 이유
#
# - **데이터 이해**: 분포, 이상치, 패턴을 직관적으로 파악
# - **모델 디버깅**: 학습 곡선, 예측 결과 분석
# - **결과 보고**: 성능 지표, 비교 분석 결과 전달
# - **탐색적 분석(EDA)**: 특성 간 관계, 클래스 분포 확인

# %% [markdown]
# ---
# ## 11.1 Matplotlib 기초

# %% [markdown]
# ### 11.1.1 기본 설정과 한글 폰트

# %%
import numpy as np
import matplotlib.pyplot as plt

# 한글 폰트 설정
import platform
from matplotlib import font_manager

if platform.system() == "Darwin":  # Mac
    plt.rc('font', family='AppleGothic')
elif platform.system() == "Windows":
    font_path = 'C:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_name)
else:  # Linux
    plt.rc('font', family='NanumGothic')

# 마이너스 기호 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

# 기본 스타일 설정 (선택사항)
plt.rcParams['figure.figsize'] = (8, 5)
plt.rcParams['figure.dpi'] = 100

print("Matplotlib 설정 완료!")

# %% [markdown]
# ### 11.1.2 Figure와 Axes 개념
#
# Matplotlib의 핵심 구조:
# - **Figure**: 전체 그림 (캔버스)
# - **Axes**: 개별 그래프 (플롯 영역)
# - **Axis**: 축 (x축, y축)
#
# ```
# Figure (전체 캔버스)
# ┌─────────────────────────────────┐
# │  Axes 1        │  Axes 2        │
# │  ┌──────────┐  │  ┌──────────┐  │
# │  │  그래프  │  │  │  그래프  │  │
# │  └──────────┘  │  └──────────┘  │
# └─────────────────────────────────┘
# ```

# %%
# Figure와 Axes 생성
fig, ax = plt.subplots()

# 간단한 선 그래프
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]
ax.plot(x, y)

ax.set_title("Figure와 Axes 기본 구조")
ax.set_xlabel("X축")
ax.set_ylabel("Y축")

plt.show()

# %% [markdown]
# ---
# ## 11.2 기본 차트 유형

# %% [markdown]
# ### 11.2.1 선 그래프 (Line Plot)
#
# 시간에 따른 변화, 추세 분석에 적합합니다.

# %%
# 데이터 준비
epochs = np.arange(1, 11)
train_acc = [0.65, 0.72, 0.78, 0.82, 0.85, 0.87, 0.89, 0.90, 0.91, 0.92]
val_acc = [0.60, 0.68, 0.73, 0.76, 0.78, 0.79, 0.80, 0.80, 0.81, 0.81]

fig, ax = plt.subplots(figsize=(8, 5))

# 선 그래프 그리기
ax.plot(epochs, train_acc, 'b-o', label='훈련 정확도', linewidth=2, markersize=6)
ax.plot(epochs, val_acc, 'r--s', label='검증 정확도', linewidth=2, markersize=6)

ax.set_title('모델 학습 곡선', fontsize=14, fontweight='bold')
ax.set_xlabel('에포크', fontsize=12)
ax.set_ylabel('정확도', fontsize=12)
ax.set_ylim(0.5, 1.0)
ax.legend(loc='lower right', fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# %% [markdown]
# ### 11.2.2 막대 그래프 (Bar Chart)
#
# 카테고리별 비교에 적합합니다.

# %%
categories = ['제품', '배송', '서비스', '가격', '품질']
scores = [4.2, 3.8, 4.5, 3.5, 4.0]
colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6']

fig, ax = plt.subplots(figsize=(8, 5))

bars = ax.bar(categories, scores, color=colors, edgecolor='black', linewidth=1.2)

# 값 표시
for bar, score in zip(bars, scores):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
            f'{score:.1f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

ax.set_title('카테고리별 만족도 점수', fontsize=14, fontweight='bold')
ax.set_ylabel('평균 점수', fontsize=12)
ax.set_ylim(0, 5)
ax.axhline(y=4, color='red', linestyle='--', alpha=0.5, label='목표 (4.0)')
ax.legend()

plt.tight_layout()
plt.show()

# %%
# 그룹 막대 그래프
models = ['모델 A', '모델 B', '모델 C']
precision = [0.85, 0.82, 0.88]
recall = [0.80, 0.85, 0.82]
f1_score = [0.82, 0.83, 0.85]

x = np.arange(len(models))
width = 0.25

fig, ax = plt.subplots(figsize=(9, 5))

bars1 = ax.bar(x - width, precision, width, label='정밀도', color='#3498db')
bars2 = ax.bar(x, recall, width, label='재현율', color='#2ecc71')
bars3 = ax.bar(x + width, f1_score, width, label='F1 점수', color='#e74c3c')

ax.set_title('모델별 성능 비교', fontsize=14, fontweight='bold')
ax.set_ylabel('점수', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.set_ylim(0.7, 1.0)
ax.legend()
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

# %% [markdown]
# ### 11.2.3 산점도 (Scatter Plot)
#
# 두 변수 간의 관계, 분포 확인에 적합합니다.

# %%
# 가상의 2D 데이터 (2개 클래스)
np.random.seed(42)

# 클래스 A
class_a_x = np.random.randn(50) + 2
class_a_y = np.random.randn(50) + 2

# 클래스 B
class_b_x = np.random.randn(50) - 1
class_b_y = np.random.randn(50) - 1

fig, ax = plt.subplots(figsize=(8, 6))

ax.scatter(class_a_x, class_a_y, c='#3498db', s=80, alpha=0.7, 
           label='클래스 A', edgecolors='white', linewidth=1)
ax.scatter(class_b_x, class_b_y, c='#e74c3c', s=80, alpha=0.7, 
           label='클래스 B', edgecolors='white', linewidth=1)

ax.set_title('2D 데이터 분포 (분류 문제)', fontsize=14, fontweight='bold')
ax.set_xlabel('특성 1', fontsize=12)
ax.set_ylabel('특성 2', fontsize=12)
ax.legend()
ax.grid(True, alpha=0.3)
ax.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
ax.axvline(x=0.5, color='gray', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

# %% [markdown]
# ### 11.2.4 히스토그램 (Histogram)
#
# 데이터 분포 확인에 적합합니다.

# %%
# 정규분포와 비정규분포 비교
np.random.seed(42)
normal_data = np.random.randn(1000)
skewed_data = np.random.exponential(2, 1000)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 정규분포
axes[0].hist(normal_data, bins=30, color='#3498db', edgecolor='white', alpha=0.8)
axes[0].set_title('정규분포 데이터', fontsize=12, fontweight='bold')
axes[0].set_xlabel('값')
axes[0].set_ylabel('빈도')
axes[0].axvline(normal_data.mean(), color='red', linestyle='--', label=f'평균: {normal_data.mean():.2f}')
axes[0].legend()

# 지수분포 (비대칭)
axes[1].hist(skewed_data, bins=30, color='#e74c3c', edgecolor='white', alpha=0.8)
axes[1].set_title('비대칭 분포 데이터 (지수분포)', fontsize=12, fontweight='bold')
axes[1].set_xlabel('값')
axes[1].set_ylabel('빈도')
axes[1].axvline(skewed_data.mean(), color='blue', linestyle='--', label=f'평균: {skewed_data.mean():.2f}')
axes[1].legend()

plt.tight_layout()
plt.show()

# %% [markdown]
# ---
# ## 11.3 OOP 스타일과 서브플롯

# %% [markdown]
# ### 11.3.1 OOP 스타일 vs Functional 스타일
#
# - **Functional**: `plt.plot()`, `plt.title()` - 간단한 그래프에 적합
# - **OOP**: `fig, ax = plt.subplots()` - 복잡한 그래프, 서브플롯에 권장

# %%
# Functional 스타일 (간단한 경우)
plt.figure(figsize=(6, 4))
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.title('Functional 스타일')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# %%
# OOP 스타일 (권장)
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
ax.set_title('OOP 스타일')
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()

# %% [markdown]
# ### 11.3.2 여러 서브플롯 배치

# %%
# 2x2 서브플롯
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 데이터 준비
x = np.linspace(0, 10, 100)

# 각 서브플롯에 그래프 그리기
axes[0, 0].plot(x, np.sin(x), 'b-')
axes[0, 0].set_title('sin(x)')

axes[0, 1].plot(x, np.cos(x), 'r-')
axes[0, 1].set_title('cos(x)')

axes[1, 0].plot(x, np.exp(-x/5) * np.sin(x), 'g-')
axes[1, 0].set_title('감쇠 진동')

axes[1, 1].plot(x, x**2, 'm-')
axes[1, 1].set_title('x²')

# 전체 제목
fig.suptitle('다양한 함수 그래프', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# %%
# 다양한 크기의 서브플롯
fig = plt.figure(figsize=(12, 6))

# 왼쪽 큰 플롯
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(np.random.randn(100).cumsum(), 'b-', linewidth=2)
ax1.set_title('랜덤 워크')
ax1.set_xlabel('시간')
ax1.set_ylabel('값')

# 오른쪽 위
ax2 = fig.add_subplot(2, 2, 2)
ax2.bar(['A', 'B', 'C'], [3, 7, 5], color=['#3498db', '#e74c3c', '#2ecc71'])
ax2.set_title('막대 그래프')

# 오른쪽 아래
ax3 = fig.add_subplot(2, 2, 4)
ax3.hist(np.random.randn(500), bins=20, color='#9b59b6', edgecolor='white')
ax3.set_title('히스토그램')

plt.tight_layout()
plt.show()

# %% [markdown]
# ---
# ## 11.4 차트 커스터마이징

# %% [markdown]
# ### 11.4.1 색상과 스타일

# %%
# 다양한 색상 지정 방법
fig, ax = plt.subplots(figsize=(10, 6))

x = np.linspace(0, 10, 50)

ax.plot(x, np.sin(x), color='red', label='이름으로')
ax.plot(x, np.sin(x + 1), color='#2ecc71', label='HEX 코드')
ax.plot(x, np.sin(x + 2), color=(0.2, 0.4, 0.8), label='RGB 튜플')
ax.plot(x, np.sin(x + 3), color='C3', label='기본 색상 순환')

ax.set_title('다양한 색상 지정 방법')
ax.legend()
plt.show()

# %%
# 선 스타일과 마커
fig, ax = plt.subplots(figsize=(10, 6))

styles = ['-', '--', '-.', ':']
markers = ['o', 's', '^', 'D']

for i, (style, marker) in enumerate(zip(styles, markers)):
    ax.plot(x, np.sin(x + i), linestyle=style, marker=marker, 
            markevery=5, label=f'스타일: {style}, 마커: {marker}')

ax.set_title('선 스타일과 마커')
ax.legend()
plt.show()

# %% [markdown]
# ### 11.4.2 축 설정

# %%
fig, ax = plt.subplots(figsize=(8, 5))

x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x))

# 축 범위 설정
ax.set_xlim(0, 12)
ax.set_ylim(-1.5, 1.5)

# 눈금 설정
ax.set_xticks(np.arange(0, 13, 2))
ax.set_yticks([-1, -0.5, 0, 0.5, 1])

# 눈금 레이블
ax.set_xticklabels(['0', '2', '4', '6', '8', '10', '12'])
ax.set_yticklabels(['-1.0', '-0.5', '0.0', '0.5', '1.0'])

# 그리드
ax.grid(True, linestyle='--', alpha=0.5)

# 보조 눈금
ax.minorticks_on()
ax.grid(which='minor', linestyle=':', alpha=0.3)

ax.set_title('축 커스터마이징')
plt.show()

# %% [markdown]
# ### 11.4.3 범례와 주석

# %%
fig, ax = plt.subplots(figsize=(10, 6))

x = np.linspace(0, 2*np.pi, 100)
ax.plot(x, np.sin(x), label='sin(x)')
ax.plot(x, np.cos(x), label='cos(x)')

# 범례 위치 지정
ax.legend(loc='upper right', fontsize=12, 
          framealpha=0.9, edgecolor='black')

# 주석 추가
ax.annotate('최대값', xy=(np.pi/2, 1), xytext=(np.pi/2 + 0.5, 1.3),
            fontsize=11, arrowprops=dict(arrowstyle='->', color='red'))

# 텍스트 추가
ax.text(np.pi, 0, 'π', fontsize=14, ha='center', va='bottom',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

ax.set_title('범례와 주석')
ax.grid(True, alpha=0.3)
plt.show()

# %% [markdown]
# ---
# ## 연습문제

# %% [markdown]
# ### 문제 1: 기본 그래프
# 다음 데이터로 선 그래프와 막대 그래프를 나란히 그리세요.
# ```python
# months = ['1월', '2월', '3월', '4월', '5월', '6월']
# sales = [150, 180, 220, 190, 250, 310]
# ```

# %%
months = ['1월', '2월', '3월', '4월', '5월', '6월']
sales = [150, 180, 220, 190, 250, 310]
# 여기에 코드 작성


# %% [markdown]
# ### 문제 2: 산점도와 회귀선
# 랜덤 데이터를 생성하고 산점도를 그린 후, 추세선을 추가하세요.
# (힌트: numpy.polyfit, numpy.poly1d 사용)

# %%
np.random.seed(42)
x = np.linspace(0, 10, 50)
y = 2 * x + 1 + np.random.randn(50) * 2
# 여기에 코드 작성


# %% [markdown]
# ### 문제 3: 파이 차트
# 다음 데이터로 파이 차트를 그리세요. 가장 큰 부분을 강조하세요.
# ```python
# categories = ['A', 'B', 'C', 'D', 'E']
# values = [30, 25, 20, 15, 10]
# ```

# %%
categories = ['A', 'B', 'C', 'D', 'E']
values = [30, 25, 20, 15, 10]
# 여기에 코드 작성


# %% [markdown]
# ### 문제 4: 박스 플롯
# 3개 그룹의 데이터 분포를 박스 플롯으로 비교하세요.

# %%
np.random.seed(42)
group1 = np.random.normal(100, 10, 50)
group2 = np.random.normal(90, 15, 50)
group3 = np.random.normal(110, 8, 50)
# 여기에 코드 작성


# %%



