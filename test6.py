import streamlit as st

st.set_page_config(page_title="AX 교육 검증 시험", layout="wide")

st.markdown("## 📊 AX 교육 모듈별 최종 검증 시험")
st.markdown("""
본 화면은 AX(AI Transformation) 교육 과정 수료 후, 각 모듈별 핵심 개념의 이해도를 점검하기 위한 검증 시험장입니다.
좌측에서 평가를 진행할 **모듈 시나리오**를 선택하고, 제시된 문제 상황을 분석하여 가운데 **답안 작성 영역**에 해결 방안을 기술해 주십시오. 
필요시 우측의 **생성형 AI 어시스턴트**를 활용하여 프롬프트 엔지니어링 및 바이브 코딩을 통해 문제 해결의 힌트를 얻거나 코드를 생성할 수 있습니다.
""")
st.divider()

scenarios = {
    "1. 기술통계 (Descriptive Statistics)": {
        "text": "생산 라인에서 수집된 온도 센서 데이터(측정 척도)를 분석하려 합니다. 데이터에 일부 센서 오작동으로 인한 빈칸(결측치)이 존재합니다. 결측치를 적절히 처리한 후, 온도의 퍼짐 정도(분산)를 확인하고, 데이터가 종 모양의 이상적인 형태(정규분포)를 띠는지 점검하세요. 마지막으로 히스토그램을 그려 특정 시간대에 온도가 튀는 현상(패턴 인식)이 있는지 파악해야 합니다.",
        "files": ["sensor_data.csv", "temperature_log.xlsx", "missing_report.csv"]
    },
    "2. 추론통계 (Inferential Statistics)": {
        "text": "두 생산 공장(A, B)의 제품 강도 데이터를 수집했습니다. 각 공장 데이터의 분산이 비슷한지(동질성) 먼저 확인한 후, 두 공장 간 강도의 실질적인 격차(집단 간 평균 차이)가 있는지 검정하고 유의확률(p-value)을 통해 결론을 내리세요. 강도와 제조 온도 간의 선형적 관계(상관계수)를 계산하고, 샘플이 충분히 크므로 표본 평균들이 정규성을 띤다는 원리(중심극한정리)를 바탕으로 결과를 해석하세요.",
        "files": ["factory_a_strength.csv", "factory_b_strength.csv", "temp_strength_corr.xlsx"]
    },
    "3. 실험계획법 (Design of Experiments, DOE)": {
        "text": "신소재 배합 공정에서 수율을 극대화(최적화)하기 위한 실험을 설계합니다. 온도와 압력이 수율에 미치는 단독 영향(주효과)과 두 인자가 결합되어 나타나는 시너지(교호작용)를 분석하세요. 시간과 비용 제약으로 일부 실험만 진행하므로 인자 간 효과가 섞이는 현상(교락)을 주의해야 하며, 실험 순서에 따른 환경 오차를 줄이기 위해 순서를 무작위로 배정(랜덤화)하여 실시해야 합니다.",
        "files": ["doe_plan.xlsx", "yield_results.csv", "factor_levels.csv"]
    },
    "4. 통계적공정관리 (Statistical Process Control, SPC)": {
        "text": "가죽 시트 제조 공정에서 두께를 측정합니다. 파괴검사 특성을 고려해 계측기 및 작업자의 오차(Gage R&R)가 허용 수준인지 검증하세요. 이후 공정 데이터를 관리도에 타점하여 중심선 상하의 기준(관리한계선)을 벗어나는 외부 요인(이상원인)이 있는지 탐지합니다. 최종적으로 단기 공정능력지수(Cpk)를 산출하고 전체 생산량 대비 불량품의 비율(불량비율)을 모니터링하세요.",
        "files": ["leather_thickness.csv", "gage_rr_data.xlsx", "control_chart_points.csv"]
    },
    "5. 구조적 문제해결 방법론": {
        "text": "현재 불량 발생률을 수치로 명확히 정의(As-Is 정량화)하고, 어골도를 통해 발생 가능한 모든 요인을 도출하여 진짜 이유(근본 원인)를 파악하세요. 데이터 분석을 거쳐 불량에 가장 큰 영향을 미치는 소수의 변수(핵심 인자)를 검증해 냅니다. 이를 해결하기 위한 여러 대안 중 효과와 실현 가능성을 바탕으로 순서(우선순위)를 매기고, 개선 후 상태가 유지되도록 표준화 문서(관리계획)를 작성하세요.",
        "files": ["defect_rate_asis.xlsx", "fishbone_factors.csv", "vital_few_analysis.csv"]
    },
    "6. 미니탭 기초 (Minitab Basics)": {
        "text": "분석을 위해 원본 데이터를 분석용 구조에 맞게 정리(데이터 포맷팅)하여 미니탭에 입력합니다. 작업자 및 설비별로 데이터를 나누어(층별화) 기초 통계량과 그래프를 확인하고, 상단의 텍스트 결과 영역(세션 창)에 출력된 통계 검정 수치들을 바탕으로 비즈니스적 의미를 도출(결과 해석)하세요. 마지막으로 Assistant 기능을 활용해 경영진 보고용 종합 보고서(자동 리포팅)를 생성하세요.",
        "files": ["raw_inspection.xlsx", "stratified_data.csv", "minitab_export.csv"]
    },
    "7. 파이썬 리터러시 (Python Literacy)": {
        "text": "파이썬을 활용해 데이터를 분석합니다. 먼저 숫자, 문자 등 데이터의 성격(자료형)을 이해하고 리스트나 딕셔너리 형태(자료구조)로 저장하세요. 특정 조건에 따라 데이터를 분류하는 조건문(논리 제어)을 작성한 뒤, 엑셀 데이터를 표 형태의 2차원 구조(데이터프레임)로 불러옵니다. 마지막으로 특정 범주별 합계나 평균을 구하기 위해 기준 컬럼으로 데이터를 묶어(GroupBy) 요약하세요.",
        "files": ["sales_raw.csv", "customer_info.xlsx", "region_mapping.csv"]
    },
    "8. 프롬프트 엔지니어링과 바이브 코딩": {
        "text": "AI에게 데이터 병합 작업을 요청하려 합니다. 현재 상황과 목표를 명확히 설명(맥락 부여)하고, 한국어 요구사항을 파이썬 코드로 변환(자연어-코드 번역)하도록 요청하세요. 복잡한 작업은 한 번에 묻지 않고 순서대로 나누어(단계별 지시) 프롬프트를 작성합니다. 코드 실행 중 오류가 나면 메시지(에러 로그)를 복사해 디버깅을 요청하고, 완성된 코드를 자동화 형태(반복 스크립트)로 저장하세요.",
        "files": ["prompt_template.txt", "vibe_coding_test.xlsx", "error_traceback.csv"]
    },
    "9. 머신러닝 : 이론": {
        "text": "불량품을 예측하는 모델(학습 패러다임)을 구축합니다. 변수 간의 비례적 관계(선형성)를 가정하는 모델과 여러 모델을 결합하는 기법(앙상블)을 비교하세요. 모델 평가 시 '불량(NG)'을 기준(Positive)으로 한 평가 지표(혼동 행렬)를 산출하고, 모델이 훈련 데이터에만 과하게 맞춰지거나 너무 단순화되는 현상 간의 균형(편향-분산 트레이드오프)을 맞춰 최상의 예측력을 확보하세요.",
        "files": ["ml_train_data.csv", "ml_test_data.csv", "confusion_matrix.xlsx"]
    },
    "10. 머신러닝 : 탐색적 데이터분석 (EDA)": {
        "text": "모델링 전 데이터 탐색을 수행합니다. 데이터의 행과 열 크기, 기본 정보(데이터 윤곽)를 확인하고 변수들 간의 연관성(상관관계)을 시각화하세요. 비어있는 값은 평균이나 중앙값 등으로 채워넣고(결측치 대치), 서로 다른 단위의 변수들을 동일한 스케일로 맞추어(정규화) 모델의 왜곡을 방지합니다. 마지막으로 기존 변수들을 조합하여 예측에 유용한 새로운 변수를 생성(특성 추출)하세요.",
        "files": ["eda_raw.csv", "missing_values.xlsx", "scaled_features.csv"]
    },
    "11. 머신러닝 : 모델링 및 강화": {
        "text": "훈련 데이터와 평가 데이터를 분리하여 모델이 미지의 데이터에 약해지는 현상(과적합 방지)을 막습니다. 데이터를 여러 겹으로 나누어 교대로 훈련 및 평가(K-Fold 검증)를 수행해 신뢰성을 높이세요. 순차적으로 오류를 보완하는 트리 기반 알고리즘(부스팅)을 적용하고 내부 설정값을 조절(파라미터 최적화)하여 성능을 극대화합니다. 최종 모델에서 어떤 변수가 예측에 중요한지 파악(특성 중요도)하세요.",
        "files": ["modeling_dataset.csv", "hyperparameters.xlsx", "feature_importance.csv"]
    },
    "12. AI Automation": {
        "text": "원시 데이터 수집부터 예측 결과 출력까지의 전 과정(End-to-End 아키텍처)을 설계합니다. 외부 시스템의 날씨 데이터를 호출(API 연동)하여 분석에 추가하고, 매일 특정 시간에 코드가 일괄 실행(배치 작업)되도록 설정하세요. 예측된 불량률이 임계치를 넘으면 관리자에게 알림을 발송(트리거)하며, 시간이 지나 입력 데이터의 패턴이 달라져 성능이 떨어지는 현상(데이터 드리프트)을 모니터링하세요.",
        "files": ["pipeline_config.json", "api_response_log.csv", "drift_metrics.xlsx"]
    },
    "13. 시각화 - Tableau와 Power BI": {
        "text": "사내 데이터베이스(데이터 원본)에 연결하여 대시보드를 구축합니다. 중심이 되는 팩트 테이블과 주변의 디멘전 테이블들을 관계 맺어(스타 스키마) 분석 구조를 짭니다. 데이터 특성에 맞는 적절한 차트를 선택(시각화 매핑)하고, 내장된 고급 계산식(DAX 및 LOD 표현식)을 활용해 복잡한 집계 척도를 생성하세요. 사용자가 클릭하면 전체 차트가 연동되어 변하는 동적 대시보드(상호작용)를 완성하세요.",
        "files": ["bi_fact_table.csv", "bi_dim_tables.xlsx", "dashboard_layout.json"]
    }
}

col1, col2, col3 = st.columns([1, 1.2, 1])

with col1:
    st.subheader("📋 시나리오 선택")
    selected_module = st.selectbox("모듈 별 시나리오를 선택하시오", list(scenarios.keys()))
    
    st.info(scenarios[selected_module]["text"])
    
    st.markdown("**📎 첨부 데이터**")
    for file_name in scenarios[selected_module]["files"]:
        st.download_button(label=f"💾 {file_name}", data="dummy_data", file_name=file_name, key=file_name)

with col2:
    st.subheader("📝 답안 작성")
    answer = st.text_area("제시된 시나리오에 대한 분석 결과 및 코드, 해결 방안을 작성해주세요.", height=500)
    if st.button("답안 제출"):
        if answer:
            st.success("답안이 성공적으로 제출되었습니다.")
        else:
            st.warning("답안을 입력해주세요.")

with col3:
    st.subheader("🤖 생성형 AI (바이브 코딩)")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    chat_container = st.container(height=400)
    
    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
                
    prompt = st.chat_input("질문이나 코딩 요청을 입력하세요.")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with chat_container:
            with st.chat_message("user"):
                st.markdown(prompt)
            with st.chat_message("assistant"):
                response = f"입력하신 프롬프트 '{prompt}' 에 대한 생성형 AI의 답변입니다. (Vibe Coding 지원 모드)"
                st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
