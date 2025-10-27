import streamlit as st
import pandas as pd
import numpy as np

# 페이지 설정
st.set_page_config(page_title="자율주행 도입 전후 도시 변화 대시보드", page_icon="🌆", layout="wide")

st.title("🌆 자율주행 도입 전후 도시 변화 대시보드")
st.markdown("""
#### 자율주행 기술이 도입되면, **교통량**, **사고율**, **탄소배출량**은 어떻게 변할까요?  
아래 데이터를 통해 함께 살펴봅시다!
""")

# -------------------------------
# 1️⃣ 자율주행 기술 소개
st.header("1️⃣ 자율주행 기술의 핵심 요소")
col1, col2 = st.columns(2)

with col1:
    st.subheader("센서 기술")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/64/Self-driving_car.png",
             caption="LiDAR, 카메라, GPS 센서")
    st.write("- LiDAR: 거리 측정\n- Camera: 사물 인식\n- GPS: 위치 파악")

with col2:
    st.subheader("AI & 통신 기술")
    st.write("""
    - AI가 주행 데이터를 학습해 도로 상황 판단  
    - 차량 간(V2V), 도로 인프라(V2X)와 통신으로 효율적 교통 관리  
    """)

st.divider()

# -------------------------------
# 2️⃣ 자율주행 도입 전후 비교 데이터
st.header("2️⃣ 자율주행 도입 전후 비교")

st.write("아래 슬라이더로 **자율주행차 보급률(%)**을 조정해보세요!")

adoption = st.slider("자율주행차 비율", 0, 100, 30, 10)

# 기본 데이터
base_traffic = 1000  # 단위: 차량/시간
base_emission = 100  # 단위: CO2 배출량(kg)
base_accidents = 10  # 단위: 건/월

# 간단한 가정 기반 계산 (보급률에 따라 감소)
traffic = base_traffic * (1 - adoption / 200)
emission = base_emission * (1 - adoption / 150)
accidents = base_accidents * (1 - adoption / 100)

data = pd.DataFrame({
    "항목": ["교통량(대/시간)", "탄소배출량(kg)", "교통사고(건/월)"],
    "도입 전": [base_traffic, base_emission, base_accidents],
    "도입 후": [traffic, emission, accidents]
})

st.bar_chart(data.set_index("항목"))

st.success(f"✅ 자율주행차 보급률이 **{adoption}%**일 때, 탄소배출량은 약 **{emission:.1f}kg**, 사고는 **{accidents:.1f}건/월**로 줄어듭니다!")

st.divider()

# -------------------------------
# 3️⃣ 환경 변화 시각화
st.header("3️⃣ 환경 영향 시뮬레이션")

years = np.arange(2020, 2041, 5)
emission_data = 100 * (1 - (years - 2020) / 100)  # 단순 감소 예시
accident_data = 10 * (1 - (years - 2020) / 80)

chart_data = pd.DataFrame({
    "연도": years,
    "탄소배출량(kg)": emission_data,
    "사고율(건/월)": accident_data
}).set_index("연도")

st.line_chart(chart_data)

st.caption("📉 시간이 지날수록 자율주행 기술 발전과 함께 교통사고율, 탄소배출량이 감소하는 추세를 볼 수 있습니다.")

# -------------------------------
# 4️⃣ 나의 생각
st.header("💬 나의 생각")
opinion = st.text_area("자율주행 기술이 환경에 어떤 변화를 가져올까요?")
if st.button("의견 제출"):
    if opinion.strip():
        st.success(f"🗣️ 당신의 의견: {opinion}")
    else:
        st.warning("✏️ 의견을 입력해주세요!")

st.divider()
st.caption("© 2025 중학교 기술수업 | Streamlit을 활용한 미래 수송기술 프로젝트")
