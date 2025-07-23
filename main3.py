import streamlit as st
import random

st.set_page_config(page_title="SNS 캡션 문구 생성기", page_icon="✍️")
st.title("✍️ SNS 캡션 문구 생성기")
st.markdown("브랜드나 제품 키워드를 입력하면 다양한 스타일의 SNS 문구를 생성해드립니다.")

# 사용자 입력
keyword = st.text_input("📝 키워드 입력 (예: 비건 화장품, 감성카페 등)")
style = st.selectbox("🎭 문구 스타일 선택", [
    "감성형", "위트형", "정보형", "콜투액션형",
    "로맨틱형", "힐링형", "재치형", "극사실형", "ASMR형",
    "궁서체형", "쇼츠형", "TMI형", "엔터형", "영화형"
])

# 템플릿 수 조정 (30개로 확장된 예시)
templates = {
    "감성형": [f"감성형 문구 {i} - {{keyword}}" for i in range(1, 31)],
    "위트형": [f"위트형 문구 {i} - {{keyword}}" for i in range(1, 31)],
    "정보형": [f"정보형 문구 {i} - {{keyword}}" for i in range(1, 31)],
    "콜투액션형": [f"콜투액션형 문구 {i} - {{keyword}}" for i in range(1, 31)],
    "로맨틱형": [f"로맨틱형 문구 {i} - {{keyword}}" for i in range(1, 31)],
    "힐링형": [f"힐링형 문구 {i} - {{keyword}}" for i in range(1, 31)],
    "재치형": [f"재치형 문구 {i} - {{keyword}}" for i in range(1, 31)],
    "극사실형": [f"극사실형 문구 {i} - {{keyword}}" for i in range(1, 31)],
    "ASMR형": [f"ASMR형 문구 {i} - {{keyword}}" for i in range(1, 31)],
    "궁서체형": [f"궁서체형 문구 {i} - {{keyword}}" for i in range(1, 31)],
    "쇼츠형": [f"쇼츠형 문구 {i} - {{keyword}}" for i in range(1, 31)],
    "TMI형": [f"TMI형 문구 {i} - {{keyword}}" for i in range(1, 31)],
    "엔터형": [f"엔터형 문구 {i} - {{keyword}}" for i in range(1, 31)],
    "영화형": [f"영화형 문구 {i} - {{keyword}}" for i in range(1, 31)],
}

# 결과 출력
if keyword:
    outputs = random.sample(templates[style], 3)
    st.subheader("🎯 생성된 문구 3종 추천")
    for i, template in enumerate(outputs, 1):
        output = template.format(keyword=keyword)
        st.markdown(f"**{i}.** {output}")
        st.code(output, language="markdown")

    if st.button("🔁 문구 다시 생성"):
        st.rerun()
