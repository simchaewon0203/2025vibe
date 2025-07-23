import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="광고 퍼널 분석기", page_icon="📉")

st.title("📉 광고 퍼널 분석 대시보드")
st.markdown("단계별 전환 데이터를 입력하면 퍼널을 시각화하고, 전환률을 자동 분석합니다.")

st.subheader("① 단계별 데이터 입력")

# 단계별 입력
st.write("각 퍼널 단계를 입력하세요:")
step_names = ["노출 수", "클릭 수", "랜딩 페이지 머무름", "장바구니 담기", "구매 완료"]
step_values = []

for step in step_names:
    val = st.number_input(f"{step}", min_value=0, step=1)
    step_values.append(val)

# 퍼널 데이터프레임
df = pd.DataFrame({
    "단계": step_names,
    "수치": step_values
})

# 전환률 계산
df["전환률(%)"] = df["수치"].pct_change().fillna(1) * 100
df["전환률(%)"] = df["전환률(%)"].round(2)
df.iloc[0, 2] = 100.0  # 첫 단계는 100%

st.subheader("② 전환 퍼널 시각화")

fig = px.funnel(df, x="수치", y="단계", text="전환률(%)", title="전환 퍼널", color_discrete_sequence=["#00BFC4"])
st.plotly_chart(fig, use_container_width=True)

# 테이블로 보기
st.subheader("③ 상세 데이터 보기")
st.dataframe(df)

# 위험 구간 알림
st.subheader("🚨 전환률 저하 경고")
threshold = st.slider("문제 구간 기준 전환률 (%)", min_value=0, max_value=100, value=40)

for i in range(1, len(df)):
    if df["전환률(%)"].iloc[i] < threshold:
        st.error(f"⚠️ `{df['단계'].iloc[i-1]} → {df['단계'].iloc[i]}` 구간 전환률 {df['전환률(%)'].iloc[i]}% (기준 미달)")

