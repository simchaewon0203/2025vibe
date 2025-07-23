import streamlit as st
import random

st.set_page_config(page_title="콘텐츠 타이틀 생성기", page_icon="🎬")
st.title("🎬 콘텐츠 타이틀/제목 생성기")
st.markdown("키워드와 스타일을 입력하면 클릭을 유도할 수 있는 제목을 자동으로 생성해드립니다.")

# 입력 폼
keyword = st.text_input("🔍 키워드 입력 (예: 다이어트, 비건 뷰티, 홈트레이닝 등)")
channel = st.selectbox("📺 콘텐츠 채널", [
    "YouTube", "YouTube Shorts", "Instagram 피드", "Instagram 릴스",
    "TikTok", "블로그", "뉴스레터", "브런치", "LinkedIn", "카카오뷰",
    "Facebook", "Notion 페이지", "슬라이드쉐어", "YouTube 커뮤니티 글", "티스토리 블로그"
])
style = st.selectbox("🎯 제목 스타일", ["정보형", "감성형", "자극형", "리스트형", "의문형"])

# 제목 템플릿 정의
title_templates = {
    "정보형": [
        "{keyword}, 이것만은 꼭 알아두세요!",
        "당신이 몰랐던 {keyword}의 모든 것",
        "지금 바로 실천 가능한 {keyword} 꿀팁",
        "초보도 쉽게 배우는 {keyword} 방법",
        "하루 5분! {keyword} 루틴 정리"
    ],
    "감성형": [
        "{keyword}로 물든 오늘 하루",
        "조용히 마음을 적시는 {keyword} 이야기",
        "당신에게도 필요한 {keyword}의 순간",
        "감정을 담은 {keyword}, 지금 공유할게요",
        "나를 위한 {keyword}, 지금 시작해요"
    ],
    "자극형": [
        "이걸 안 보면 당신만 손해?! {keyword}의 진실",
        "모두가 놀란 {keyword}의 반전 효과",
        "{keyword}, 이렇게 하면 당신도 변할 수 있습니다",
        "10명 중 9명이 후회한 {keyword} 실수",
        "이 방법 하나로 {keyword} 완전 정복"
    ],
    "리스트형": [
        "{keyword} 추천 TOP5 정리해드립니다",
        "지금 당장 써먹는 {keyword} 꿀팁 3가지",
        "알아두면 쓸모 있는 {keyword} 리스트",
        "{keyword} 잘하는 사람들이 지키는 7가지 습관",
        "{keyword} 완전정복! 단계별 가이드"
    ],
    "의문형": [
        "왜 요즘 다들 {keyword}에 빠졌을까?",
        "{keyword}, 진짜 효과 있는 걸까?",
        "당신은 {keyword} 제대로 알고 있나요?",
        "{keyword}, 어떻게 시작하는 게 좋을까?",
        "{keyword}가 나에게도 맞을까?"
    ]
}

# 결과 출력
if keyword:
    titles = random.sample(title_templates[style], 3)
    st.subheader("📢 추천 제목 3개")
    for i, title in enumerate(titles, 1):
        result = title.format(keyword=keyword)
        st.markdown(f"**{i}.** {result}")
        st.code(result, language="markdown")

    if st.button("🔁 제목 다시 생성"):
        st.rerun()
