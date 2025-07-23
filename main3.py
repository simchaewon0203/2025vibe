# SNS 캡션 문구 생성기 PRO 버전 (핵심 기능 MVP)
import streamlit as st
import openai
import random
import pandas as pd

# 👉 GPT API KEY 설정 (필요 시 입력 받게 설정)
openai.api_key = st.secrets["openai_api_key"] if "openai_api_key" in st.secrets else ""

st.set_page_config(page_title="SNS 캡션 생성기 PRO", page_icon="✍️")
st.title("✍️ SNS 캡션 문구 생성기 PRO")
st.markdown("키워드, 스타일, SNS 채널을 선택하면 AI가 문구를 자동으로 추천합니다!")

# 입력 영역
with st.sidebar:
    st.header("⚙️ 설정")
    keyword = st.text_input("📝 키워드 입력", value="비건 화장품")
    style = st.selectbox("🎭 문구 스타일", [
        "감성형", "위트형", "정보형", "콜투액션형", "로맨틱형", "힐링형",
        "재치형", "극사실형", "ASMR형", "궁서체형", "쇼츠형", "TMI형", "엔터형", "영화형"
    ])
    channel = st.selectbox("📱 SNS 채널", ["Instagram", "YouTube", "Blog", "TikTok"])
    language = st.selectbox("🌍 언어 선택", ["한국어", "영어", "일본어", "스페인어"])
    num_captions = st.slider("🔢 생성할 문구 개수", 1, 5, 3)
    generate = st.button("🚀 캡션 생성")

# 프롬프트 생성 함수
def create_prompt(keyword, style, channel, language, num):
    return f"""
    다음 조건에 맞는 SNS 캡션을 {num}개 생성해줘.
    - 키워드: {keyword}
    - 스타일: {style}
    - 채널: {channel}
    - 언어: {language}
    각 문장은 줄 바꿈 없이 간결하게 만들어줘.
    """

# GPT 호출 함수
def generate_captions(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "너는 SNS 마케터야. 감각적인 문장을 생성해."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8
        )
        return response.choices[0].message.content.strip().split("\n")
    except Exception as e:
        return [f"❌ 오류 발생: {e}"]

# 생성 결과 출력
if generate and keyword and openai.api_key:
    with st.spinner("AI가 문구를 생성 중입니다..."):
        prompt = create_prompt(keyword, style, channel, language, num_captions)
        results = generate_captions(prompt)

    st.subheader("📋 생성된 캡션")
    for i, cap in enumerate(results):
        st.markdown(f"**{i+1}.** {cap}")
        col1, col2 = st.columns([1, 5])
        with col1:
            st.button("⭐ 저장", key=f"save_{i}")
        with col2:
            st.code(cap, language='markdown')

    # 다운로드
    st.download_button("📥 문구 다운로드", pd.DataFrame(results, columns=["caption"]).to_csv(index=False),
                       file_name="captions.csv", mime="text/csv")

elif generate and not openai.api_key:
    st.error("❗ OpenAI API 키가 설정되지 않았습니다. Streamlit Secrets 또는 코드에 키를 설정해주세요.")
