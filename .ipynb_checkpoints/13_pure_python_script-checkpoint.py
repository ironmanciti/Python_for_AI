"""
13. 순수 Python 스크립트 예제: 데이터 분석 + Gemini 구조화 출력

이 스크립트는 순수 Python 프로그램의 기본 구조를 보여줍니다:
- pandas로 CSV 파일 읽기
- 데이터 전처리 함수
- Gemini API로 구조화된 분석 결과 요청

사용법:
    python 13_pure_python_script.py
    python 13_pure_python_script.py --file data/titanic.csv
"""

import os
import sys
import argparse
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field
from typing import List

# ============================================================================
# 1. 함수 정의: 데이터 전처리
# ============================================================================

def load_data(filepath: str) -> pd.DataFrame:
    """CSV 파일을 pandas DataFrame으로 읽어 반환"""
    try:
        df = pd.read_csv(filepath)
        print(f"데이터 로드 완료: {len(df)}행, {len(df.columns)}열")
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {filepath}")


def get_data_summary(df: pd.DataFrame) -> str:
    """DataFrame의 요약 정보를 문자열로 반환"""
    summary = []
    summary.append(f"데이터 크기: {len(df)}행 × {len(df.columns)}열")
    summary.append(f"\n컬럼: {', '.join(df.columns.tolist())}")
    summary.append(f"\n결측치:")
    for col in df.columns:
        missing = df[col].isna().sum()
        if missing > 0:
            summary.append(f"  {col}: {missing}개 ({missing/len(df)*100:.1f}%)")
    
    if 'Survived' in df.columns:
        summary.append(f"\n생존률:")
        summary.append(f"  생존: {df['Survived'].sum()}명 ({df['Survived'].mean()*100:.1f}%)")
        summary.append(f"  사망: {(df['Survived']==0).sum()}명 ({(df['Survived']==0).mean()*100:.1f}%)")
    
    return "\n".join(summary)


# ============================================================================
# 2. Pydantic 모델: 구조화된 출력 스키마
# ============================================================================

class DataAnalysisResult(BaseModel):
    """데이터 분석 결과"""
    key_insights: List[str] = Field(description="주요 인사이트 3-5개")
    data_quality: str = Field(description="데이터 품질 평가")
    recommendations: List[str] = Field(description="추가 분석 권장사항")
    summary: str = Field(description="전체 요약 (2-3문장)")


# ============================================================================
# 3. 함수 정의: AI 분석
# ============================================================================

def analyze_with_ai(api_key: str, data_summary: str, sample_data: str) -> DataAnalysisResult:
    """Gemini API를 사용하여 데이터를 분석하는 함수"""
    # Gemini 클라이언트 생성
    client = genai.Client(api_key=api_key)
    
    prompt = f"""다음은 Titanic 데이터셋의 요약 정보입니다:

{data_summary}

샘플 데이터 (처음 5행):
{sample_data}

이 데이터를 분석하여 다음을 제공해주세요:
1. 주요 인사이트 (데이터 패턴, 특징 등)
2. 데이터 품질 평가 (결측치, 이상치 등)
3. 추가 분석 권장사항
4. 전체 요약
"""
    
    # Gemini API 호출
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": DataAnalysisResult,
        },
    )
    
    # 결과 파싱 및 반환
    result = DataAnalysisResult.model_validate_json(response.text)
    return result


# ============================================================================
# 4. 메인 함수
# ============================================================================

def main():
    """프로그램의 진입점"""
    # 명령줄 인자 파싱
    parser = argparse.ArgumentParser(
        description="Titanic 데이터 분석 도구",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--file",
        default="data/titanic.csv",
        help="분석할 CSV 파일 경로 (기본값: data/titanic.csv)"
    )
    
    args = parser.parse_args()
    
    # API 키 확인
    load_dotenv()
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("오류: GOOGLE_API_KEY 환경변수가 설정되지 않았습니다.")
        print(".env 파일에 GOOGLE_API_KEY=your-api-key를 추가하세요.")
        sys.exit(1)
    
    try:
        # 1. 데이터 로드
        print("=" * 50)
        print("1. 데이터 로드 중...")
        df = load_data(args.file)
        
        # 2. 데이터 요약 생성
        print("\n2. 데이터 요약 생성 중...")
        summary = get_data_summary(df)
        sample_data = df.head(5).to_string()
        
        # 3. AI 분석 수행
        print("\n3. Gemini AI로 분석 중...")
        result = analyze_with_ai(api_key, summary, sample_data)
        
        # 4. 결과 출력
        print("\n" + "=" * 50)
        print("분석 결과")
        print("=" * 50)
        print(f"\n주요 인사이트:")
        for i, insight in enumerate(result.key_insights, 1):
            print(f"  {i}. {insight}")
        
        print(f"\n데이터 품질: {result.data_quality}")
        
        print(f"\n추가 분석 권장사항:")
        for i, rec in enumerate(result.recommendations, 1):
            print(f"  {i}. {rec}")
        
        print(f"\n전체 요약: {result.summary}")
        print("=" * 50)
        
    except FileNotFoundError as e:
        print(f"오류: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"오류 발생: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


# ============================================================================
# 5. 스크립트 실행
# ============================================================================

if __name__ == "__main__":
    main()

