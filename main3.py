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

# 문구 템플릿 전체 14종
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
    ],
    "로맨틱형": [
        "너와 함께한 {keyword}, 기억 속에 영원히 남아.",
        "{keyword}, 사랑보다 더 깊은 감정.",
        "그날의 공기처럼, {keyword}는 여전히 설레.",
        "나를 웃게 해주는 {keyword}, 고마워.",
        "밤하늘의 별보다 반짝이는 {keyword}",
        "매 순간이 특별해, {keyword}와 함께라면.",
        "{keyword}, 운명처럼 찾아온 순간.",
        "사랑을 말할 땐 늘 {keyword}가 떠올라.",
        "너와 나를 이어주는 {keyword}의 선율.",
        "{keyword}, 매일이 첫 데이트처럼."
    ],
    "힐링형": [
        "{keyword}, 나를 위한 작은 쉼표.",
        "지친 하루 끝, {keyword}와 함께 리셋.",
        "마음을 차분히, {keyword}가 필요한 시간.",
        "조용한 위로가 되는 {keyword}",
        "오늘도 스스로를 돌보는 방법, {keyword}",
        "{keyword} 덕분에 한결 가벼운 하루.",
        "혼자만의 시간에 어울리는 {keyword}",
        "따뜻한 햇살 같은 {keyword}",
        "마음에 여유를 주는 {keyword}",
        "잠시 멈춰 서게 하는 {keyword}의 힘"
    ],
    "재치형": [
        "{keyword}? 내일도 반복재생 예정ㅋㅋ",
        "있어 보이고 싶을 땐 {keyword} 한 스푼",
        "다 필요 없고 {keyword} 하나면 돼.",
        "{keyword}, 이게 그렇게 좋다며?",
        "진짜야? {keyword} 실화냐고",
        "너도 이거 보면 웃는다, {keyword}ㅋㅋ",
        "하... 또 샀다. {keyword}에 진심임",
        "내 카드가 또 {keyword}에 당했어요",
        "난 진심인데 {keyword}는 어때?",
        "인생템 발견: {keyword} 대박쓰~"
    ],
    "극사실형": [
        "{keyword}, 진짜로 썼고, 진짜로 좋음.",
        "이건 광고 아님. {keyword}는 찐임.",
        "구매 후기 3줄 요약: {keyword} 대박, 실속, 재구매각.",
        "한 달 써봤는데 {keyword} 괜찮아요.",
        "사용법: {keyword} → 그냥 써, 후회 안 해.",
        "아무 말 없이 추천함. {keyword}는 말이 필요 없음.",
        "실사용자 리뷰: {keyword} 믿고 쓰는 중",
        "괜히 인기 많은 게 아님. {keyword} 굿.",
        "내돈내산: {keyword}, 가격값 함.",
        "{keyword}만큼은 내가 보장함."
    ],
    "ASMR형": [
        "조용히 귀에 속삭이듯... {keyword}",
        "속닥이는 감성, {keyword}로 전해요.",
        "스르르 잠드는 밤, {keyword}가 함께해요.",
        "귓가에 맴도는 {keyword}의 잔잔함",
        "나직이 말해볼게요, {keyword}",
        "심장이 말하는 소리처럼, {keyword}",
        "조용한 설렘, {keyword}에서 시작돼요.",
        "속삭이듯 전하는 {keyword}의 이야기",
        "아무 소리 없는 감정, {keyword}로 느껴봐요.",
        "{keyword}, 말 없는 위로"
    ],
    "궁서체형": [
        "{keyword}는 거들 뿐.",
        "지금 시작하지 않으면, {keyword}도 늦습니다.",
        "당신의 선택, {keyword}에 달렸습니다.",
        "{keyword}, 결코 평범하지 않습니다.",
        "우리는 {keyword}를 통해 말합니다.",
        "한 번쯤은 {keyword}를 경험해야 합니다.",
        "기록하라, {keyword}로.",
        "{keyword}, 그것이 전부다.",
        "진정한 변화는 {keyword}에서 시작된다.",
        "{keyword}는 더 이상 선택이 아닙니다."
    ],
    "쇼츠형": [
        "{keyword}만 있으면 끝!",
        "3초 만에 반함 👉 {keyword}",
        "{keyword} 이게 요즘 대세 🔥",
        "그냥 봐봐요. {keyword}는 다르니까.",
        "빠르게 보여드림 🎬 {keyword}",
        "1초 컷 리뷰: {keyword} 대박",
        "{keyword} 써봤더니 진짜 이렇습니다",
        "짧고 강하게, {keyword} 한 방이면 돼요",
        "짧은 영상으로 보는 {keyword}",
        "{keyword}, 핵심만 알려드림"
    ],
    "TMI형": [
        "사실 {keyword}에 이런 뒷이야기가 있어요.",
        "{keyword} 만든 사람, 알고 보니 ○○ 출신!",
        "이건 아무도 안 알려줬던 {keyword} 비밀",
        "{keyword} = 하루에 몇 번이나 검색되는지 아세요?",
        "진짜 {keyword} 써본 사람만 아는 팁",
        "이 얘기 어디서도 못 들었을걸요? {keyword} 이야기",
        "그때 그 {keyword}, 알고 보면 이런 사연이...",
        "{keyword}, 나만 알고 싶은 이유 있음",
        "나만 알고 싶은 {keyword}의 숨은 기능",
        "몰라도 되는 정보: {keyword}의 탄생 배경"
    ],
    "엔터형": [
        "그것은 바로... {keyword}!",
        "두둥‼️ {keyword} 등장!",
        "이 순간을 기다렸다... {keyword}의 시간",
        "{keyword}가 세상을 뒤흔든다!",
        "나타났다! {keyword}가!",
        "{keyword}, 전설의 귀환",
        "당신의 인생을 바꿀 {keyword}가 온다",
        "준비됐나요? {keyword}의 여정 시작!",
        "절대 놓치지 마세요! {keyword} 한정 공개",
        "바로 지금! {keyword}로 시작해보세요"
    ],
    "영화형": [
        "그는 말했다. '{keyword} 없인 못 살아'",
        "어둠 속 한 줄기 빛, 그것은 {keyword}였다.",
        "이 여름, 가장 뜨거운 이름은 {keyword}",
        "모든 건 {keyword}에서 시작됐다.",
        "우연처럼 찾아온 {keyword}, 운명이 되다.",
        "전혀 예상치 못한 {keyword}의 반전",
        "{keyword}, 그 이름만으로도 감동",
        "스크린 밖 현실로 나온 {keyword}",
        "진짜 이야기, {keyword}에 담다",
        "엔딩을 바꿀 단 하나의 선택: {keyword}"
    ]
}

# 결과 출력
if keyword:
    output = random.choice(templates[style]).format(keyword=keyword)
    st.subheader("🎯 생성된 문구")
    st.success(output)
    st.code(output, language='markdown')

    if st.button("🔁 문구 다시 생성"):
        st.rerun()

