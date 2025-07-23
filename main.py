import streamlit as st
import random

st.set_page_config(page_title="SNS 캡션 문구 생성기", page_icon="✍️")
st.title("✍️ SNS 캡션 문구 생성기")
st.markdown("브랜드나 제품 키워드를 입력하면 다양한 스타일의 SNS 문구를 생성해드립니다.")

# 입력
keyword = st.text_input("📝 키워드 입력 (예: 비건 화장품, 디저트카페 등)")
style = st.selectbox("🎭 문구 스타일 선택", ["감성형", "위트형", "정보형", "콜투액션형"])

# 스타일별 문구 템플릿 10개씩
templates = {
    "감성형": [
        "오늘도 {keyword}로 나에게 작은 선물을 줘요 🌿",
        "당신의 하루를 부드럽게 감싸줄 {keyword}",
        "{keyword}, 마음을 담은 하루의 쉼표처럼.",
        "{keyword} 덕분에 하루가 따뜻해졌어요.",
        "조용히 마음을 적시는 {keyword}",
        "{keyword}, 나만의 감성 포인트.",
        "햇살처럼 스며드는 {keyword}의 기분",
        "감정을 담은 {keyword}, 오늘은 조금 특별하게.",
        "내 일상에 잔잔한 위로를 주는 {keyword}",
        "차분한 순간, {keyword}와 함께"
    ],
    "위트형": [
        "{keyword}? 이미 내 인생템 😎",
        "진짜 이걸로 바꿨더니... 인생 바뀜 🤯 #놀람주의",
        "너도 아직 {keyword} 안 써봤다고...?🙄",
        "{keyword}, 이게 진짜 실화냐고요?ㅋㅋ",
        "내가 말했지? {keyword}는 못 참지!",
        "{keyword} 없이는 못 살아~",
        "찐으로 추천하는 {keyword} 꿀템",
        "{keyword} 덕분에 기분 업⬆️",
        "이건 무조건 사야 돼, {keyword}는 국룰",
        "나만 알고 싶은 {keyword}, 근데 공유함ㅋ"
    ],
    "정보형": [
        "{keyword}의 핵심 성분은 피부 진정에 탁월해요.",
        "{keyword} - 요즘 핫한 이유, 알아봅시다!",
        "왜 다들 {keyword}에 빠졌는지 알려드림 👇",
        "{keyword}는 이런 분들께 추천해요!",
        "전문가가 인정한 {keyword}의 효과",
        "데이터로 보는 {keyword}의 리뷰 평점은?",
        "실사용 후기가 증명하는 {keyword}의 매력",
        "{keyword}의 사용법, 어렵지 않아요!",
        "한눈에 보는 {keyword} 요약 정보",
        "당신의 선택을 도와줄 {keyword} 가이드"
    ],
    "콜투액션형": [
        "지금 바로 {keyword}를 경험해보세요!",
        "링크 클릭하고 {keyword} 20% 할인 받기 🎁",
        "{keyword}, 오늘부터 시작해보는 건 어때요?",
        "지금 구매하면 {keyword} 무료배송!",
        "이 기회를 놓치지 마세요, {keyword} 한정 특가!",
        "체험단 모집 중! {keyword} 써보고 후기 남기기",
        "{keyword}로 나만의 변화를 만들어보세요",
        "오늘 밤 12시까지! {keyword} 이벤트 종료 임박!",
        "간편하게 시작하는 {keyword} 라이프",
        "오직 이번 주만! {keyword} 특별 혜택"
    ]
}

# 결과 출력
if keyword:
    selected_template = random.choice(templates[style])
    result = selected_template.format(keyword=keyword)

    st.subheader("🎯 생성된 문구")
    st.success(result)

    st.code(result, language='markdown')

    # 새로고침 버튼
    if st.button("🔁 문구 다시 생성"):
        st.rerun()
