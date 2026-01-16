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
# # 12. EDA 종합실습: Titanic 데이터 분석
#
# **학습 목표**: pandas, matplotlib, numpy를 종합 활용하여 실제 데이터셋의 탐색적 데이터 분석(EDA)을 수행합니다.
#
# ---
#
# ## Titanic 데이터셋 소개
#
# 1912년 타이타닉호 침몰 사고의 승객 데이터입니다. 생존 여부를 예측하는 대표적인 머신러닝 입문 데이터셋입니다.
#
# | 컬럼명 | 설명 |
# |--------|------|
# | PassengerId | 승객 ID |
# | Survived | 생존 여부 (0=사망, 1=생존) |
# | Pclass | 객실 등급 (1=1등석, 2=2등석, 3=3등석) |
# | Name | 이름 |
# | Sex | 성별 |
# | Age | 나이 |
# | SibSp | 동승한 형제/배우자 수 |
# | Parch | 동승한 부모/자녀 수 |
# | Ticket | 티켓 번호 |
# | Fare | 운임 (영국 파운드) |
# | Cabin | 선실 번호 |
# | Embarked | 탑승 항구 (C=Cherbourg, Q=Queenstown, S=Southampton) |

# %% [markdown]
# ---
# ## 12.1 데이터 로드 및 기본 탐색

# %% [markdown]
# ### 12.1.1 라이브러리 임포트 및 설정

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정
import platform
from matplotlib import font_manager
import warnings
warnings.filterwarnings('ignore')

if platform.system() == "Darwin":  # Mac
    font_name = 'AppleGothic'
elif platform.system() == "Windows":
    font_path = 'C:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_path).get_name()
else:  # Linux
    font_name = 'NanumGothic'

# seaborn 스타일 설정 (폰트 포함)
sns.set_theme(style='whitegrid', font=font_name)

# matplotlib 추가 설정
plt.rcParams['font.family'] = font_name
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.figsize'] = (10, 6)

print("라이브러리 로드 완료!")

# %% [markdown]
# ### 12.1.2 데이터 로드

# %%
# CSV 파일 로드
df = pd.read_csv("data/titanic.csv")

print(f"데이터 로드 완료!")
print(f"데이터 크기: {df.shape[0]}행 × {df.shape[1]}열")

# %% [markdown]
# ### 12.1.3 데이터 미리보기

# %%
# 처음 5개 행 확인
df.head()

# %%
# 마지막 5개 행 확인
df.tail()

# %% [markdown]
# ### 12.1.4 데이터 구조 파악

# %%
# 데이터 타입 및 결측치 정보
df.info()

# %%
# 컬럼 목록
print("컬럼 목록:")
print(df.columns.tolist())

# %%
# 데이터 타입별 컬럼 분류
print("\n수치형 컬럼:", df.select_dtypes(include=[np.number]).columns.tolist())
print("범주형 컬럼:", df.select_dtypes(include=['object']).columns.tolist())

# %% [markdown]
# ### 12.1.5 기술 통계 확인

# %%
# 수치형 변수의 기술 통계
df.describe()

# %%
# 범주형 변수의 기술 통계
df.describe(include='object')

# %% [markdown]
# ---
# ## 12.2 결측치 분석

# %% [markdown]
# ### 12.2.1 결측치 현황 파악

# %%
# 컬럼별 결측치 개수
missing_count = df.isnull().sum()
print("컬럼별 결측치 개수:")
print(missing_count[missing_count > 0])

# %%
# 결측치 비율 계산
missing_ratio = (df.isnull().sum() / len(df) * 100).round(2)
missing_df = pd.DataFrame({
    '결측치 수': missing_count,
    '결측치 비율(%)': missing_ratio
})
missing_df = missing_df[missing_df['결측치 수'] > 0].sort_values('결측치 비율(%)', ascending=False)
print("\n결측치 현황:")
print(missing_df)

# %% [markdown]
# ### 12.2.2 결측치 시각화

# %%
# 결측치 비율 막대 그래프
if len(missing_df) > 0:
    fig, ax = plt.subplots(figsize=(8, 5))
    
    colors = plt.cm.Reds(np.linspace(0.4, 0.8, len(missing_df)))
    bars = ax.barh(missing_df.index, missing_df['결측치 비율(%)'], color=colors)
    
    # 값 표시
    for bar, val in zip(bars, missing_df['결측치 비율(%)']):
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
               f'{val:.1f}%', va='center', fontsize=10)
    
    ax.set_xlabel('결측치 비율 (%)')
    ax.set_title('컬럼별 결측치 비율', fontsize=14, fontweight='bold')
    ax.set_xlim(0, max(missing_df['결측치 비율(%)']) * 1.2)
    
    plt.tight_layout()
    plt.show()

# %% [markdown]
# ### 12.2.3 결측치 분석 인사이트
#
# **관찰 결과:**
# - `Cabin`: 약 77%의 결측치 → 분석에서 제외하거나 '있음/없음'으로 변환 고려
# - `Age`: 약 20%의 결측치 → 평균, 중앙값 또는 그룹별 대체 필요
# - `Embarked`: 소수의 결측치 → 최빈값으로 대체 가능

# %% [markdown]
# ---
# ## 12.3 범주형 변수 분석

# %% [markdown]
# ### 12.3.1 타겟 변수: Survived (생존 여부)

# %%
# 생존 여부 분포
survived_counts = df['Survived'].value_counts()
survived_ratio = df['Survived'].value_counts(normalize=True) * 100

print("생존 여부 분포:")
print(f"  사망(0): {survived_counts[0]}명 ({survived_ratio[0]:.1f}%)")
print(f"  생존(1): {survived_counts[1]}명 ({survived_ratio[1]:.1f}%)")

# %%
# 생존 여부 시각화
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 파이 차트
colors = ['#e74c3c', '#2ecc71']
axes[0].pie(survived_counts, labels=['사망', '생존'], autopct='%1.1f%%',
           colors=colors, explode=[0, 0.05], startangle=90)
axes[0].set_title('생존 여부 비율', fontsize=12, fontweight='bold')

# 막대 그래프
bars = axes[1].bar(['사망 (0)', '생존 (1)'], survived_counts, color=colors, edgecolor='black')
for bar, count in zip(bars, survived_counts):
    axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
                f'{count}명', ha='center', fontsize=11, fontweight='bold')
axes[1].set_ylabel('승객 수')
axes[1].set_title('생존 여부 분포', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()

# %% [markdown]
# ### 12.3.2 성별(Sex)과 생존율

# %%
# 성별 분포
print("성별 분포:")
print(df['Sex'].value_counts())

# %%
# 성별에 따른 생존율
sex_survival = df.groupby('Sex')['Survived'].agg(['count', 'sum', 'mean'])
sex_survival.columns = ['전체', '생존자', '생존율']
sex_survival['생존율'] = (sex_survival['생존율'] * 100).round(1)
print("\n성별 생존율:")
print(sex_survival)

# %%
# 성별 생존율 시각화
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 생존율 막대 그래프
survival_rate = df.groupby('Sex')['Survived'].mean() * 100
bars = axes[0].bar(['여성', '남성'], survival_rate, color=['#e91e63', '#2196f3'], edgecolor='black')
for bar, rate in zip(bars, survival_rate):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{rate:.1f}%', ha='center', fontsize=12, fontweight='bold')
axes[0].set_ylabel('생존율 (%)')
axes[0].set_ylim(0, 100)
axes[0].set_title('성별 생존율', fontsize=12, fontweight='bold')

# 성별-생존 카운트 플롯
sns.countplot(data=df, x='Sex', hue='Survived', ax=axes[1], palette=['#e74c3c', '#2ecc71'])
axes[1].set_xticklabels(['여성', '남성'])
axes[1].set_xlabel('성별')
axes[1].set_ylabel('승객 수')
axes[1].set_title('성별에 따른 생존/사망 분포', fontsize=12, fontweight='bold')
axes[1].legend(['사망', '생존'])

plt.tight_layout()
plt.show()

# %% [markdown]
# **인사이트**: 여성의 생존율(약 74%)이 남성(약 19%)보다 현저히 높습니다. "여성과 어린이 먼저" 원칙이 적용된 것으로 보입니다.

# %% [markdown]
# ### 12.3.3 객실 등급(Pclass)과 생존율

# %%
# 객실 등급 분포
print("객실 등급 분포:")
print(df['Pclass'].value_counts().sort_index())

# %%
# 객실 등급별 생존율
pclass_survival = df.groupby('Pclass')['Survived'].agg(['count', 'sum', 'mean'])
pclass_survival.columns = ['전체', '생존자', '생존율']
pclass_survival['생존율'] = (pclass_survival['생존율'] * 100).round(1)
print("\n객실 등급별 생존율:")
print(pclass_survival)

# %%
# 객실 등급 생존율 시각화
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 등급별 승객 수
pclass_counts = df['Pclass'].value_counts().sort_index()
colors_pclass = ['#FFD700', '#C0C0C0', '#CD7F32']  # 금, 은, 동
bars = axes[0].bar(['1등석', '2등석', '3등석'], pclass_counts, color=colors_pclass, edgecolor='black')
for bar, count in zip(bars, pclass_counts):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
                f'{count}명', ha='center', fontsize=11)
axes[0].set_ylabel('승객 수')
axes[0].set_title('객실 등급별 승객 수', fontsize=12, fontweight='bold')

# 등급별 생존율
survival_rate = df.groupby('Pclass')['Survived'].mean() * 100
bars = axes[1].bar(['1등석', '2등석', '3등석'], survival_rate, color=colors_pclass, edgecolor='black')
for bar, rate in zip(bars, survival_rate):
    axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{rate:.1f}%', ha='center', fontsize=11, fontweight='bold')
axes[1].set_ylabel('생존율 (%)')
axes[1].set_ylim(0, 100)
axes[1].set_title('객실 등급별 생존율', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()

# %% [markdown]
# **인사이트**: 1등석 승객의 생존율(약 63%)이 3등석(약 24%)보다 2.5배 이상 높습니다. 사회경제적 지위가 생존에 영향을 미쳤습니다.

# %% [markdown]
# ### 12.3.4 탑승 항구(Embarked)와 생존율

# %%
# 탑승 항구 분포
print("탑승 항구 분포:")
embarked_counts = df['Embarked'].value_counts()
print(embarked_counts)

# %%
# 탑승 항구별 생존율
embarked_survival = df.groupby('Embarked')['Survived'].agg(['count', 'sum', 'mean'])
embarked_survival.columns = ['전체', '생존자', '생존율']
embarked_survival['생존율'] = (embarked_survival['생존율'] * 100).round(1)
print("\n탑승 항구별 생존율:")
print(embarked_survival)

# %%
# 탑승 항구 시각화
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

port_names = {'S': 'Southampton', 'C': 'Cherbourg', 'Q': 'Queenstown'}
colors_port = ['#3498db', '#e74c3c', '#2ecc71']

# 항구별 승객 수
axes[0].bar([port_names.get(p, p) for p in embarked_counts.index], 
           embarked_counts.values, color=colors_port, edgecolor='black')
axes[0].set_ylabel('승객 수')
axes[0].set_title('탑승 항구별 승객 수', fontsize=12, fontweight='bold')

# 항구별 생존율
sns.barplot(data=df, x='Embarked', y='Survived', ax=axes[1], 
            palette=colors_port, errorbar=None, order=['S', 'C', 'Q'])
axes[1].set_xticklabels(['Southampton', 'Cherbourg', 'Queenstown'])
axes[1].set_ylabel('생존율')
axes[1].set_title('탑승 항구별 생존율', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()

# %% [markdown]
# ---
# ## 12.4 수치형 변수 분석

# %% [markdown]
# ### 12.4.1 나이(Age) 분포

# %%
# 나이 기술 통계 (numpy 활용)
age_data = df['Age'].dropna()

print("나이 기술 통계:")
print(f"  평균: {np.mean(age_data):.1f}세")
print(f"  중앙값: {np.median(age_data):.1f}세")
print(f"  표준편차: {np.std(age_data):.1f}세")
print(f"  최소: {np.min(age_data):.1f}세")
print(f"  최대: {np.max(age_data):.1f}세")
print(f"  사분위수: Q1={np.percentile(age_data, 25):.1f}, Q2={np.percentile(age_data, 50):.1f}, Q3={np.percentile(age_data, 75):.1f}")

# %%
# 나이 분포 시각화
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 히스토그램
axes[0].hist(age_data, bins=30, color='steelblue', edgecolor='white', alpha=0.8)
axes[0].axvline(np.mean(age_data), color='red', linestyle='--', linewidth=2, label=f'평균: {np.mean(age_data):.1f}세')
axes[0].axvline(np.median(age_data), color='green', linestyle='--', linewidth=2, label=f'중앙값: {np.median(age_data):.1f}세')
axes[0].set_xlabel('나이')
axes[0].set_ylabel('승객 수')
axes[0].set_title('나이 분포 (히스토그램)', fontsize=12, fontweight='bold')
axes[0].legend()

# 박스플롯
bp = axes[1].boxplot(age_data, vert=True, patch_artist=True)
bp['boxes'][0].set_facecolor('steelblue')
axes[1].set_ylabel('나이')
axes[1].set_title('나이 분포 (박스플롯)', fontsize=12, fontweight='bold')
axes[1].set_xticklabels(['Age'])

plt.tight_layout()
plt.show()

# %% [markdown]
# ### 12.4.2 나이와 생존율 관계

# %%
# 나이대별 생존율 시각화
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 생존/사망별 나이 분포 비교
for survived, color, label in [(0, '#e74c3c', '사망'), (1, '#2ecc71', '생존')]:
    subset = df[df['Survived'] == survived]['Age'].dropna()
    axes[0].hist(subset, bins=30, alpha=0.6, color=color, label=label, edgecolor='white')

axes[0].set_xlabel('나이')
axes[0].set_ylabel('승객 수')
axes[0].set_title('생존 여부에 따른 나이 분포', fontsize=12, fontweight='bold')
axes[0].legend()

# 바이올린 플롯
sns.violinplot(data=df, x='Survived', y='Age', ax=axes[1], palette=['#e74c3c', '#2ecc71'])
axes[1].set_xticklabels(['사망', '생존'])
axes[1].set_xlabel('생존 여부')
axes[1].set_ylabel('나이')
axes[1].set_title('생존 여부에 따른 나이 분포 (바이올린)', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()

# %% [markdown]
# ### 12.4.3 운임(Fare) 분포

# %%
# 운임 기술 통계
fare_data = df['Fare'].dropna()

print("운임 기술 통계:")
print(f"  평균: ${np.mean(fare_data):.2f}")
print(f"  중앙값: ${np.median(fare_data):.2f}")
print(f"  표준편차: ${np.std(fare_data):.2f}")
print(f"  최소: ${np.min(fare_data):.2f}")
print(f"  최대: ${np.max(fare_data):.2f}")

# %%
# 운임 분포 시각화
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 전체 운임 분포
axes[0].hist(fare_data, bins=50, color='purple', edgecolor='white', alpha=0.7)
axes[0].set_xlabel('운임 ($)')
axes[0].set_ylabel('승객 수')
axes[0].set_title('운임 분포', fontsize=12, fontweight='bold')

# 객실 등급별 운임 분포
colors_pclass = ['#FFD700', '#C0C0C0', '#CD7F32']
for pclass, color in zip([1, 2, 3], colors_pclass):
    subset = df[df['Pclass'] == pclass]['Fare']
    axes[1].hist(subset, bins=30, alpha=0.6, color=color, label=f'{pclass}등석', edgecolor='white')
axes[1].set_xlabel('운임 ($)')
axes[1].set_ylabel('승객 수')
axes[1].set_title('객실 등급별 운임 분포', fontsize=12, fontweight='bold')
axes[1].legend()

# 등급별 운임 박스플롯
df.boxplot(column='Fare', by='Pclass', ax=axes[2])
axes[2].set_xlabel('객실 등급')
axes[2].set_ylabel('운임 ($)')
axes[2].set_title('객실 등급별 운임 (박스플롯)', fontsize=12, fontweight='bold')
plt.suptitle('')  # 기본 제목 제거

plt.tight_layout()
plt.show()

# %% [markdown]
# ### 12.4.4 이상치 탐지 (IQR 방식)
#
# IQR(Inter-Quartile Range) = Q3 - Q1  
# 이상치 기준: Q1 - 1.5×IQR 미만 또는 Q3 + 1.5×IQR 초과

# %%
def detect_outliers_iqr(data, column_name):
    """IQR 방식으로 이상치 탐지"""
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    
    print(f"\n[{column_name}] 이상치 분석:")
    print(f"  Q1: {Q1:.2f}, Q3: {Q3:.2f}, IQR: {IQR:.2f}")
    print(f"  하한: {lower_bound:.2f}, 상한: {upper_bound:.2f}")
    print(f"  이상치 개수: {len(outliers)}개 ({len(outliers)/len(data)*100:.1f}%)")
    
    return outliers, lower_bound, upper_bound

# %%
# 수치형 변수별 이상치 탐지
numeric_cols = ['Age', 'Fare', 'SibSp', 'Parch']

fig, axes = plt.subplots(1, 4, figsize=(16, 4))

for ax, col in zip(axes, numeric_cols):
    data = df[col].dropna()
    outliers, lower, upper = detect_outliers_iqr(data, col)
    
    # 박스플롯
    bp = ax.boxplot(data, vert=True, patch_artist=True)
    bp['boxes'][0].set_facecolor('lightblue')
    ax.set_title(f'{col}', fontsize=11, fontweight='bold')
    ax.set_ylabel('값')

plt.suptitle('수치형 변수 이상치 분석 (박스플롯)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# %% [markdown]
# ---
# ## 12.5 변수 간 관계 분석

# %% [markdown]
# ### 12.5.1 교차표 (Crosstab)

# %%
# 성별 × 객실등급 × 생존 교차표
crosstab = pd.crosstab([df['Sex'], df['Pclass']], df['Survived'], margins=True)
crosstab.columns = ['사망', '생존', '합계']
print("성별 × 객실등급별 생존 현황:")
print(crosstab)

# %%
# 성별 × 객실등급별 생존율
survival_pivot = df.pivot_table(values='Survived', index='Sex', columns='Pclass', aggfunc='mean')
survival_pivot = (survival_pivot * 100).round(1)
print("\n성별 × 객실등급별 생존율 (%):")
print(survival_pivot)

# %%
# 히트맵으로 시각화
fig, ax = plt.subplots(figsize=(8, 5))

sns.heatmap(survival_pivot, annot=True, fmt='.1f', cmap='RdYlGn', 
            linewidths=0.5, ax=ax, vmin=0, vmax=100,
            annot_kws={'size': 14, 'fontweight': 'bold'})

ax.set_xlabel('객실 등급', fontsize=12)
ax.set_ylabel('성별', fontsize=12)
ax.set_title('성별 × 객실등급별 생존율 (%)', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()

# %% [markdown]
# **인사이트**: 1등석 여성의 생존율이 약 97%로 가장 높고, 3등석 남성의 생존율이 약 14%로 가장 낮습니다.

# %% [markdown]
# ### 12.5.2 상관관계 분석

# %%
# 수치형 변수 간 상관계수
numeric_df = df[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']].dropna()
correlation = numeric_df.corr()

print("상관계수 행렬:")
print(correlation.round(2))

# %%
# 상관관계 히트맵
fig, ax = plt.subplots(figsize=(10, 8))

mask = np.triu(np.ones_like(correlation, dtype=bool))  # 상삼각 마스크
sns.heatmap(correlation, mask=mask, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, linewidths=0.5, ax=ax, annot_kws={'size': 11})

ax.set_title('변수 간 상관관계 히트맵', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()

# %% [markdown]
# **상관관계 해석:**
# - `Survived`와 `Fare`: 양의 상관 (운임이 높을수록 생존율↑)
# - `Survived`와 `Pclass`: 음의 상관 (등급 숫자가 낮을수록, 즉 좋은 객실일수록 생존율↑)
# - `Pclass`와 `Fare`: 음의 상관 (좋은 객실일수록 운임↑)

# %% [markdown]
# ### 12.5.3 다변량 시각화

# %%
# 나이, 운임, 생존여부 관계 (산점도)
fig, ax = plt.subplots(figsize=(10, 6))

# 결측치 제거
plot_df = df[['Age', 'Fare', 'Survived', 'Pclass']].dropna()

colors = ['#e74c3c' if s == 0 else '#2ecc71' for s in plot_df['Survived']]
sizes = [(4 - p) * 30 for p in plot_df['Pclass']]  # 등급에 따른 크기

scatter = ax.scatter(plot_df['Age'], plot_df['Fare'], c=colors, s=sizes, alpha=0.6, edgecolor='white')

ax.set_xlabel('나이', fontsize=12)
ax.set_ylabel('운임 ($)', fontsize=12)
ax.set_title('나이 vs 운임 (색상=생존여부, 크기=객실등급)', fontsize=14, fontweight='bold')

# 범례 추가
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#e74c3c', markersize=10, label='사망'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#2ecc71', markersize=10, label='생존')
]
ax.legend(handles=legend_elements, loc='upper right')

plt.tight_layout()
plt.show()

# %%
# 객실등급별 나이-생존 관계
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for ax, pclass in zip(axes, [1, 2, 3]):
    subset = df[df['Pclass'] == pclass]
    
    sns.violinplot(data=subset, x='Survived', y='Age', ax=ax, 
                   palette=['#e74c3c', '#2ecc71'], split=True)
    
    ax.set_xticklabels(['사망', '생존'])
    ax.set_xlabel('생존 여부')
    ax.set_ylabel('나이')
    ax.set_title(f'{pclass}등석: 나이 vs 생존', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()

# %% [markdown]
# ---
# ## 12.6 실습: EDA 인사이트 도출

# %% [markdown]
# ### Step 1: 생존율 요인 분석 함수

# %%
def analyze_survival_factor(df, column, column_name):
    """특정 변수에 따른 생존율 분석"""
    survival_stats = df.groupby(column)['Survived'].agg(['count', 'sum', 'mean'])
    survival_stats.columns = ['전체', '생존자', '생존율']
    survival_stats['생존율'] = (survival_stats['생존율'] * 100).round(1)
    
    print(f"\n{'='*50}")
    print(f"[{column_name}] 생존율 분석")
    print('='*50)
    print(survival_stats)
    
    # 생존율 범위
    min_rate = survival_stats['생존율'].min()
    max_rate = survival_stats['생존율'].max()
    print(f"\n생존율 범위: {min_rate:.1f}% ~ {max_rate:.1f}% (차이: {max_rate - min_rate:.1f}%p)")
    
    return survival_stats

# %%
# 주요 변수별 생존율 분석
analyze_survival_factor(df, 'Sex', '성별')
analyze_survival_factor(df, 'Pclass', '객실등급')
analyze_survival_factor(df, 'Embarked', '탑승항구')

# %% [markdown]
# ### Step 2: 주요 발견사항 정리

# %%
def generate_eda_summary(df):
    """EDA 요약 리포트 생성"""
    print("=" * 60)
    print("           Titanic EDA 요약 리포트")
    print("=" * 60)
    
    # 1. 데이터 개요
    print(f"\n[1. 데이터 개요]")
    print(f"   - 전체 승객 수: {len(df)}명")
    print(f"   - 생존자 수: {df['Survived'].sum()}명 ({df['Survived'].mean()*100:.1f}%)")
    print(f"   - 사망자 수: {(1-df['Survived']).sum():.0f}명 ({(1-df['Survived'].mean())*100:.1f}%)")
    
    # 2. 성별 분석
    print(f"\n[2. 성별 생존율]")
    female_rate = df[df['Sex'] == 'female']['Survived'].mean() * 100
    male_rate = df[df['Sex'] == 'male']['Survived'].mean() * 100
    print(f"   - 여성: {female_rate:.1f}%")
    print(f"   - 남성: {male_rate:.1f}%")
    print(f"   → 여성이 남성보다 {female_rate - male_rate:.1f}%p 높음")
    
    # 3. 객실등급 분석
    print(f"\n[3. 객실등급 생존율]")
    for pclass in [1, 2, 3]:
        rate = df[df['Pclass'] == pclass]['Survived'].mean() * 100
        print(f"   - {pclass}등석: {rate:.1f}%")
    
    # 4. 나이 분석
    print(f"\n[4. 나이 분석]")
    age_data = df['Age'].dropna()
    print(f"   - 평균 나이: {age_data.mean():.1f}세")
    print(f"   - 결측치: {df['Age'].isnull().sum()}명 ({df['Age'].isnull().mean()*100:.1f}%)")
    
    # 5. 주요 인사이트
    print(f"\n[5. 주요 인사이트]")
    print("   ✓ '여성과 어린이 먼저' 원칙이 적용됨")
    print("   ✓ 사회경제적 지위(객실등급)가 생존에 큰 영향")
    print("   ✓ 1등석 여성의 생존율이 가장 높음")
    print("   ✓ 3등석 남성의 생존율이 가장 낮음")
    
    print("\n" + "=" * 60)

# %%
generate_eda_summary(df)

# %% [markdown]
# ### Step 3: 시각화 대시보드 구성

# %%
def create_eda_dashboard(df):
    """EDA 종합 대시보드 생성"""
    fig = plt.figure(figsize=(16, 12))
    
    # 1. 생존율 파이 차트 (좌상단)
    ax1 = fig.add_subplot(2, 3, 1)
    survived_counts = df['Survived'].value_counts()
    ax1.pie(survived_counts, labels=['사망', '생존'], autopct='%1.1f%%',
           colors=['#e74c3c', '#2ecc71'], explode=[0, 0.05])
    ax1.set_title('전체 생존율', fontweight='bold')
    
    # 2. 성별 생존율 (중상단)
    ax2 = fig.add_subplot(2, 3, 2)
    survival_by_sex = df.groupby('Sex')['Survived'].mean() * 100
    bars = ax2.bar(['여성', '남성'], survival_by_sex, color=['#e91e63', '#2196f3'])
    for bar, rate in zip(bars, survival_by_sex):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{rate:.1f}%', ha='center', fontweight='bold')
    ax2.set_ylabel('생존율 (%)')
    ax2.set_ylim(0, 100)
    ax2.set_title('성별 생존율', fontweight='bold')
    
    # 3. 객실등급 생존율 (우상단)
    ax3 = fig.add_subplot(2, 3, 3)
    survival_by_class = df.groupby('Pclass')['Survived'].mean() * 100
    colors_class = ['#FFD700', '#C0C0C0', '#CD7F32']
    bars = ax3.bar(['1등석', '2등석', '3등석'], survival_by_class, color=colors_class)
    for bar, rate in zip(bars, survival_by_class):
        ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{rate:.1f}%', ha='center', fontweight='bold')
    ax3.set_ylabel('생존율 (%)')
    ax3.set_ylim(0, 100)
    ax3.set_title('객실등급별 생존율', fontweight='bold')
    
    # 4. 나이 분포 (좌하단)
    ax4 = fig.add_subplot(2, 3, 4)
    for survived, color, label in [(0, '#e74c3c', '사망'), (1, '#2ecc71', '생존')]:
        subset = df[df['Survived'] == survived]['Age'].dropna()
        ax4.hist(subset, bins=20, alpha=0.6, color=color, label=label)
    ax4.set_xlabel('나이')
    ax4.set_ylabel('승객 수')
    ax4.set_title('생존여부별 나이 분포', fontweight='bold')
    ax4.legend()
    
    # 5. 성별×등급 생존율 히트맵 (중하단)
    ax5 = fig.add_subplot(2, 3, 5)
    pivot = df.pivot_table(values='Survived', index='Sex', columns='Pclass', aggfunc='mean') * 100
    sns.heatmap(pivot, annot=True, fmt='.0f', cmap='RdYlGn', ax=ax5,
               vmin=0, vmax=100, annot_kws={'fontweight': 'bold'})
    ax5.set_title('성별×등급 생존율 (%)', fontweight='bold')
    
    # 6. 상관관계 (우하단)
    ax6 = fig.add_subplot(2, 3, 6)
    numeric_df = df[['Survived', 'Pclass', 'Age', 'Fare']].dropna()
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0, ax=ax6)
    ax6.set_title('변수 간 상관관계', fontweight='bold')
    
    fig.suptitle('Titanic EDA 대시보드', fontsize=16, fontweight='bold')
    plt.tight_layout()
    
    return fig

# %%
fig = create_eda_dashboard(df)
plt.show()

# %% [markdown]
# ---
# ## 연습문제

# %% [markdown]
# ### 문제 1: 가족 규모와 생존율
# `SibSp`(형제/배우자)와 `Parch`(부모/자녀)를 합쳐 `FamilySize` 변수를 만들고,
# 가족 규모에 따른 생존율을 분석하세요.
#
# **힌트:**
# - `FamilySize = SibSp + Parch + 1` (본인 포함)
# - groupby로 생존율 계산
# - 막대 그래프로 시각화

# %%
# 여기에 코드 작성


# %% [markdown]
# ### 문제 2: 나이 구간별 생존율
# 나이를 다음과 같이 구간화하고, 구간별 생존율을 분석하세요.
# - 0~16세: 어린이
# - 17~30세: 청년
# - 31~50세: 중년
# - 51세 이상: 노년
#
# **힌트:**
# - `pd.cut()` 함수 사용
# - 각 구간별 생존율 계산 및 시각화

# %%
# 여기에 코드 작성


# %% [markdown]
# ### 문제 3: 이름에서 호칭 추출
# `Name` 컬럼에서 호칭(Mr, Mrs, Miss 등)을 추출하고, 호칭별 생존율을 분석하세요.
#
# **힌트:**
# - `str.extract()` 함수로 정규식 패턴 `'([A-Za-z]+)\.'` 사용
# - 추출된 호칭별 생존율 계산

# %%
# 여기에 코드 작성


# %% [markdown]
# ### 문제 4: 운임 구간별 분석
# 운임을 4분위수로 구간화하고, 구간별 생존율과 객실등급 분포를 분석하세요.
#
# **힌트:**
# - `pd.qcut()` 함수로 4분위 구간 생성
# - 교차표(crosstab)로 운임구간×객실등급 분포 확인

# %%
# 여기에 코드 작성


# %% [markdown]
# ### 문제 5: 종합 분석 함수
# 임의의 범주형 변수를 입력받아 생존율 분석과 시각화를 자동으로 수행하는 함수를 작성하세요.
#
# **요구사항:**
# - 함수명: `analyze_categorical(df, column)`
# - 출력: 범주별 전체/생존자/생존율 테이블
# - 시각화: 2개의 서브플롯 (카운트, 생존율)

# %%
def analyze_categorical(df, column):
    """
    범주형 변수의 생존율 분석 및 시각화
    
    Args:
        df: DataFrame
        column: 분석할 컬럼명
    """
    # 여기에 코드 작성
    pass

# 테스트
# analyze_categorical(df, 'Embarked')


# %%

