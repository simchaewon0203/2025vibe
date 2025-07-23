import streamlit as st
import random

st.set_page_config(page_title="SNS 캡션 문구 생성기", page_icon="✍️")
st.title("✍️ SNS 캡션 문구 생성기")
st.markdown("브랜드나 제품 키워드를 입력하면 다양한 스타일의 SNS 문구를 생성해드립니다.")

# 입력
keyword = st.text_input("📝 키워드 입력 (예: 비건 화장품, 디저트카페 등)")
style = st.selectbox("🎭 문구 스타일 선택", ["감성형", "위트형", "정보형", "콜투액션형"])

# 문구 템플릿
templates = {
    "감성형": [
        "오늘도 {keyword}로 나에게 작은 선물을 줘요 🌿",
        "당신의 하루를 부드럽게 감싸줄 {keyword}",
        "{keyword}, 마음을 담은 하루의 쉼표처럼."
    ],
    "위트형": [
        "{keyword}? 이미 내 인생템 😎",
        "진짜 이걸로 바꿨더니... 인생 바뀜 🤯 #놀람주의",
        "너도 아직 {keyword} 안 써봤다고...?🙄"
    ],
    "정보형": [
        "{keyword}의 핵심 성분은 피부 진정에 탁월해요.",
        "{keyword} - 요즘 핫한 이유, 알아봅시다!",
        "왜 다들 {keyword}에 빠졌는지 알려드림 👇"
    ],
    "콜투액션형": [
        "지금 바로 {keyword}를 경험해보세요!",
        "링크 클릭하고 {keyword} 20% 할인 받기 🎁",
        "{keyword}, 오늘부터 시작해보는 건 어때요?"
    ]
}

# 결과
if keyword:
    sentence = random.choice(templates[style]).format(keyword=keyword)
    st.subheader("🎯 생성된 문구")
    st.success(sentence)
    if st.button("🔁 다시 생성하기"):
        st.rerun()  # <- 여기를 수정
    st.code(sentence, language='markdown')
