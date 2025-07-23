import streamlit as st
import random
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #fffde7, #fce4ec);
        }
        .title {
            font-size: 42px;
            font-weight: 800;
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subtitle {
            font-size: 18px;
            color: #555;
        }
        .highlight-box {
            background-color: #ffffffee;
            border-radius: 16px;
            padding: 1.5rem;
            margin-top: 1.5rem;
            box-shadow: 0px 6px 15px rgba(0,0,0,0.1);
        }
        .highlight-box h4 {
            color: #c2185b;
            font-size: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🎬 콘텐츠 타이틀/제목 생성기</div>', unsafe_allow_html=True)

keyword = st.text_input("🔍 키워드 입력 (예: 다이어트, 비건 뷰티, 홈트레이닝 등)")
channel = st.selectbox("📺 콘텐츠 채널", [
    "YouTube", "YouTube Shorts", "Instagram 피드", "Instagram 릴스",
    "TikTok", "블로그", "뉴스레터", "브런치", "LinkedIn", "카카오뷰",
    "Facebook", "Notion 페이지", "슬라이드쉐어", "YouTube 커뮤니티 글", "티스토리 블로그"
])
style = st.selectbox("🎯 제목 스타일", [
    "정보형", "감성형", "자극형", "리스트형", "의문형",
    "공감형", "고민해결형", "실험형", "TMI형", "궁서체형",
    "스토리텔링형", "의사결정형", "비교형", "후기형", "활용팁형",
    "팩트체크형", "실패사례형", "반전형", "데이터형", "유머형"
])
# 스타일 설명 딕셔너리
style_descriptions = {
    "정보형": "사실과 데이터를 중심으로 정보를 제공하는 형식입니다.",
    "감성형": "감정과 분위기를 자극하는 서정적인 스타일입니다.",
    "자극형": "강렬한 문구로 호기심과 클릭을 유도하는 스타일입니다.",
    "리스트형": "숫자나 항목으로 나열해 명확하게 정보를 전달합니다.",
    "의문형": "질문을 던져 관심과 클릭을 유도합니다.",
    "공감형": "독자의 감정과 상황에 공감하는 방식으로 접근합니다.",
    "고민해결형": "문제에 대한 해결책을 제시하는 스타일입니다.",
    "실험형": "직접 시도한 결과를 중심으로 전달하는 콘텐츠입니다.",
    "TMI형": "불필요하지만 흥미로운 정보를 공유하는 스타일입니다.",
    "궁서체형": "진지하고 단호한 어조로 강조하는 스타일입니다.",
    "스토리텔링형": "이야기 형식으로 자연스럽게 내용을 전달합니다.",
    "의사결정형": "선택을 유도하거나 비교하는 형식입니다.",
    "비교형": "둘 이상의 대상을 비교하여 차이를 강조합니다.",
    "후기형": "직접 사용해 본 느낌을 진솔하게 공유합니다.",
    "활용팁형": "노하우와 꿀팁 위주의 실용 콘텐츠입니다.",
    "팩트체크형": "사실 여부를 검증하고 정리해주는 형식입니다.",
    "실패사례형": "실패 경험을 공유하고 교훈을 주는 스타일입니다.",
    "반전형": "예상과 다른 놀라운 내용을 담은 스타일입니다.",
    "데이터형": "통계, 수치 기반의 분석 콘텐츠입니다.",
    "유머형": "재미있고 웃긴 방식으로 정보를 전달합니다."
}
# 스타일 설명 출력
if style:
    st.caption(f"ℹ️ 스타일 설명: {style_descriptions.get(style, '설명이 준비되지 않았습니다.')}")
# 제목 템플릿 정의
title_templates = {
    "스토리텔링형": [
        "처음 {keyword}를 시작했던 그날의 이야기",
        "{keyword}로 인해 달라진 내 인생",
        "그날 나는 {keyword}를 선택했다",
        "{keyword}가 내게 남긴 진짜 의미",
        "{keyword}, 그 선택이 가져온 기적",
        "눈물로 시작한 {keyword}, 웃음으로 끝나다",
        "내가 겪은 {keyword}의 모든 순간",
        "그토록 바라던 {keyword}, 드디어 해냈다",
        "작은 용기가 만든 {keyword}의 변화",
        "{keyword}, 포기하지 않아 다행이야",
        "{keyword}를 둘러싼 7일간의 여정",
        "돌아보면 시작은 {keyword}였다",
        "아무도 몰랐던 {keyword}의 진심",
        "그땐 몰랐지, {keyword}가 이렇게 클 줄은",
        "실패에서 배운 {keyword}의 교훈",
        "{keyword}, 그때의 나에게 전하고 싶은 말",
        "그날의 선택이 만든 {keyword} 이야기",
        "{keyword}를 향한 나의 집착과 용기",
        "{keyword}, 나를 성장시킨 여정",
        "모든 건 {keyword}에서 시작되었다"
    ],
    "의사결정형": [
        "{keyword} 할까 말까? 이 글 보면 결정남",
        "당신의 선택은? {keyword} or NO",
        "{keyword}, 고민된다면 이 글을 보세요",
        "지금 {keyword}를 선택해야 할 이유",
        "{keyword}냐 다른 것이냐, 결정의 순간",
        "아직도 {keyword} 고민 중이라면",
        "{keyword} 선택 전 반드시 고려할 것들",
        "{keyword}를 선택한 나의 이유",
        "내가 {keyword}를 택한 3가지 이유",
        "이 글을 보면 {keyword}로 기울게 됩니다",
        "{keyword}, 선택은 당신의 몫",
        "{keyword}를 선택한 사람들의 공통점",
        "선택의 갈림길, {keyword}가 정답일까?",
        "{keyword}, 선택의 핵심 포인트 정리",
        "{keyword}냐 포기냐, 지금 선택하세요",
        "{keyword}를 결정하기 전 반드시 보세요",
        "이 기준으로 보면 {keyword} 선택 쉬워져요",
        "결정 못하고 있다면 {keyword} 체크리스트",
        "{keyword} 선택 시 고려할 5가지 기준",
        "당신의 선택은 {keyword}일 수밖에 없습니다"
    ],
    "비교형": [
        "{keyword} VS ○○, 뭐가 더 좋을까?",
        "{keyword}와 ○○, 직접 써보고 비교해봤어요",
        "{keyword}와 이것, 어떤 걸 선택할까?",
        "비슷하지만 다른 {keyword}와 ○○의 차이점",
        "{keyword}보다 나은 대안이 있을까?",
        "비교해보니 확실히 드러난 {keyword}의 장점",
        "{keyword}가 ○○보다 좋은 5가지 이유",
        "{keyword}와 ○○ 중 고민된다면 이 글을!",
        "{keyword}와 ○○, 소비자 선택은?",
        "{keyword} 써봤더니 ○○보다 이게 더 낫다",
        "직접 써본 {keyword}와 ○○ 솔직 비교",
        "비교 후 알게 된 {keyword}의 숨은 매력",
        "{keyword}와 ○○, 누가 더 가성비 갑?",
        "{keyword}, 솔직히 ○○보다 나은 점은?",
        "{keyword}냐 ○○냐, 내 경험은 이렇습니다",
        "전문가가 비교한 {keyword}와 ○○의 차이",
        "{keyword}와 ○○, 이건 선택의 문제다",
        "{keyword}와 ○○ 비교 후 구매결정은 이거!",
        "{keyword}가 결국 선택받은 이유",
        "○○ 대신 {keyword}를 고른 결정적 이유"
    ],
    "후기형": [
        "{keyword} 써본 후기 솔직 공개합니다",
        "내돈내산 {keyword} 리얼 후기",
        "{keyword} 솔직 사용기: 기대 이상일까?",
        "직접 써본 {keyword}, 결과는 이랬습니다",
        "{keyword} 체험 2주차, 효과는?",
        "{keyword} 후기, 장단점 정리해봤어요",
        "{keyword}, 다시 살 건가요? 후기 정리",
        "{keyword} 실사용 후기, 참고해보세요",
        "{keyword} 후기, 솔직히 말합니다",
        "{keyword}, 이건 좀 별로였어요",
        "{keyword} 사용 후 바뀐 점 3가지",
        "후회 없던 {keyword} 경험기",
        "{keyword} 효과 있었나요? 직접 써봤습니다",
        "솔직 리뷰: {keyword}에 대한 모든 것",
        "{keyword} 쓰고 달라진 나의 루틴",
        "{keyword}, 장점과 단점 총정리",
        "처음 써본 {keyword}, 만족도는 몇 점?",
        "{keyword} 후기, 이건 꼭 공유하고 싶어요",
        "{keyword}, 입소문 이유 알겠네요",
        "내가 겪은 {keyword}의 리얼 경험담"
    ],
    "활용팁형": [
        "{keyword}, 이렇게 활용해보세요",
        "{keyword} 100% 활용하는 법",
        "이렇게 쓰면 {keyword} 더 유용해요",
        "{keyword} 잘 쓰는 꿀팁 5가지",
        "{keyword} 활용도 MAX로 높이는 방법",
        "{keyword} 이렇게만 써보세요, 진짜 달라집니다",
        "{keyword} 유용하게 쓰는 사람들의 습관",
        "{keyword} 잘 쓰는 노하우 대공개",
        "{keyword}는 이렇게 활용하세요",
        "{keyword} 활용법, 몰랐던 팁 총정리",
        "{keyword}를 생활 속에서 200% 활용하는 법",
        "{keyword}를 업무에 적용하는 스마트한 방법",
        "{keyword} 사용법, 알면 쉬워요",
        "{keyword}, 이렇게만 바꿔도 효율 2배",
        "{keyword}, 초보도 쉽게 활용하는 법",
        "{keyword} 기능 10가지 총정리",
        "{keyword}를 창의적으로 활용하는 7가지 방법",
        "{keyword}, 잘 쓰는 사람은 이렇게 다릅니다",
        "모두가 쓰지만 잘 못 쓰는 {keyword} 활용법",
        "{keyword}, 이렇게 써보면 어떨까요?"
    ],
    "팩트체크형": [
        "{keyword}, 사실일까? 진실을 밝힙니다",
        "{keyword}에 대한 오해와 진실",
        "{keyword}, 진짜 효과 있나요? 확인해봤습니다",
        "{keyword} 루머, 뭐가 진짜일까?",
        "팩트체크: {keyword} 정말 괜찮은가?",
        "{keyword} 관련 정보, 과장일까?",
        "이건 사실입니다: {keyword} 데이터 공개",
        "{keyword}의 실제 효과, 직접 증명해봄",
        "{keyword}에 대한 5가지 오해 풀기",
        "진짜일까? {keyword} 논란 정리해봤어요",
        "{keyword}가 인기 많은 진짜 이유는?",
        "{keyword}는 진짜일까, 상술일까?",
        "{keyword}, 그 말 믿어도 되나요?",
        "{keyword}와 관련된 흔한 착각들",
        "팩트만 정리: {keyword} 요점 정리",
        "{keyword}의 진짜 모습, 직접 확인해봤습니다",
        "팩트체크: {keyword}가 진짜인 이유",
        "사실은 이렇습니다: {keyword} 편견 깨기",
        "{keyword}에 대한 진실 혹은 거짓",
        "의외로 잘못 알고 있는 {keyword} 상식"
    ],
    "실패사례형": [
        "{keyword} 하다 망한 이야기",
        "내가 실패한 {keyword} 경험담",
        "이렇게 하면 {keyword} 망합니다",
        "실제로 {keyword} 실패한 이유",
        "{keyword} 실패 사례 모음",
        "실패하고 깨달은 {keyword}의 교훈",
        "{keyword}, 이렇게 하니까 망했어요",
        "{keyword}에서 배우는 반면교사",
        "{keyword} 실패담, 참고하세요",
        "이런 식으로 하면 {keyword} 안 됩니다",
        "실패한 {keyword} 프로젝트 분석",
        "{keyword} 하다 생긴 문제점들",
        "피해야 할 {keyword} 실수 TOP5",
        "실패했지만 배웠습니다: {keyword} 이야기",
        "다시 한다면 이렇게 안 할 {keyword}",
        "{keyword}, 어디서부터 잘못됐을까?",
        "{keyword} 하다 겪은 최악의 상황",
        "실패 후 다시 일어선 {keyword} 이야기",
        "{keyword} 실패에서 얻은 3가지 교훈",
        "나처럼 {keyword} 망하지 않으려면 꼭 보세요"
    ],
    "반전형": [
        "처음엔 평범했던 {keyword}, 그런데...",
        "알고 보면 소름 돋는 {keyword}의 정체",
        "이건 몰랐죠? {keyword}의 반전 매력",
        "{keyword}, 사실은 이런 비밀이?!",
        "모두가 예상 못한 {keyword}의 결말",
        "{keyword}에 이런 반전이 있을 줄이야",
        "끝까지 보고 놀란 {keyword} 이야기",
        "평범한 줄 알았던 {keyword}, 그런데 반전",
        "{keyword}, 기대 이상으로 놀라운 이유",
        "{keyword}, 이렇게 될 줄 몰랐어요",
        "결과는 완전 예상 밖! {keyword} 체험기",
        "{keyword}, 숨겨진 매력 폭발",
        "{keyword}, 겉보기와는 다른 속내",
        "모두가 틀렸던 {keyword}의 진실",
        "{keyword}, 알고 나면 놀라는 이유",
        "{keyword}, 마지막에 웃은 건 누구였을까?",
        "이건 반칙입니다… {keyword}의 반전",
        "끝까지 봐야 안다! {keyword}의 비밀",
        "{keyword}, 이 정도일 줄은 몰랐죠?",
        "{keyword}, 이게 진짜일까?"
    ],
    "데이터형": [
        "{keyword} 관련 통계로 알아본 트렌드",
        "수치로 증명된 {keyword}의 효과",
        "{keyword}, 데이터로 본 결과는 이렇습니다",
        "숫자로 보는 {keyword} 핵심 요약",
        "{keyword} 관련 그래프 대공개",
        "{keyword} 이용자 분석 리포트",
        "{keyword} 데이터 기반 인사이트 정리",
        "{keyword} 수치로 보는 성공률",
        "{keyword} 활용 현황 및 분석 결과",
        "실제 통계로 알아본 {keyword}의 진실",
        "{keyword} 관련 데이터를 기반으로 한 팁",
        "{keyword} 실적 분석 보고서 요약",
        "{keyword} 핵심 수치 모아봤습니다",
        "{keyword} 이용률 변화 추이 분석",
        "{keyword} 관련 지표 정리 요약",
        "{keyword} 성과 지표로 본 효과 측정",
        "{keyword} 트렌드를 수치로 이해하기",
        "{keyword} 수치 분석 결과 인포그래픽",
        "{keyword}, 데이터로 보는 성장 흐름",
        "숫자만 보면 이해되는 {keyword}"
    ],
    "유머형": [
        "{keyword}? 웃기지만 진짜예요ㅋㅋ",
        "{keyword}, 나만 웃김?",
        "이걸로 {keyword}하면 친구가 웃어요",
        "{keyword}하다 빵 터진 순간 모음",
        "진지하게 소개하는 {keyword} (아님 주의)",
        "{keyword}, 이건 너무 웃겨서 공유함",
        "웃고 넘기는 {keyword} 이야기",
        "{keyword}, 이건 못 참지ㅋㅋ",
        "웃음주의! {keyword} 사례 대방출",
        "{keyword}, 그저 웃지요",
        "{keyword}, 뭐라고 설명해야 하죠?ㅋㅋ",
        "{keyword} 하다 생긴 웃픈 에피소드",
        "{keyword} 관련 드립 모음.zip",
        "현웃 터지는 {keyword} 사용기",
        "{keyword}, 개그콘서트급 반전",
        "{keyword}, 너무 웃겨서 혼자 봄",
        "{keyword} 실패담이 이렇게 웃길 일?",
        "{keyword} 개그 버전 해석해드립니다",
        "{keyword}, 웃음 없이 못 지나침",
        "{keyword}, 내가 왜 그랬을까ㅋㅋ"
    ],
    "TMI형": [
        "{keyword}, 알고 보면 이런 비밀이 있습니다",
        "이런 {keyword} 이야기, 아무도 몰랐을걸요?",
        "{keyword}의 유래는 사실 이랬다?!",
        "{keyword}에 얽힌 사소하지만 놀라운 사실",
        "{keyword} 만든 사람은 누구일까요?",
        "왜 하필 이름이 {keyword}일까?",
        "이건 몰라도 되는 {keyword} 정보입니다",
        "{keyword}, 처음에는 이렇게 시작됐어요",
        "{keyword}에 숨겨진 뒷이야기 전해드림",
        "나도 몰랐던 {keyword}의 과거",
        "{keyword} = 알고 보니 ○○에서 유래",
        "{keyword}를 보면 떠오르는 사소한 기억",
        "진짜 별거 없지만 말하고 싶은 {keyword} 이야기",
        "이런 {keyword} 알고 있었나요?",
        "어쩌다 이렇게 된 걸까, {keyword}의 사연",
        "이건 사실 아무 쓸모 없는 {keyword} 이야기",
        "그때 그 시절 {keyword}, 혹시 기억하나요?",
        "이걸 왜 기억하고 있지? {keyword}의 잔상",
        "{keyword}에 대한 완전 쓸데없는 정보 대방출",
        "그냥 심심해서 쓰는 {keyword} 이야기"
    ],
    "궁서체형": [
        "{keyword}는 선택이 아닌 필수입니다.",
        "지금 시작하지 않으면, {keyword}도 늦습니다.",
        "기록하라. {keyword}로.",
        "{keyword}, 결코 평범하지 않습니다.",
        "우리는 {keyword}를 통해 말합니다.",
        "진정한 변화는 {keyword}에서 시작된다.",
        "그것이 바로 {keyword}입니다.",
        "{keyword}는 더 이상 뒤로 미룰 수 없습니다.",
        "당신의 선택, {keyword}에 달렸습니다.",
        "지금 하지 않으면, 평생 {keyword}는 없습니다.",
        "{keyword}, 그것이 전부다.",
        "반드시 이뤄야 할 목표, {keyword}.",
        "{keyword}는 운명이었습니다.",
        "이건 시작일 뿐입니다. {keyword}가 끝입니다.",
        "모든 가능성은 {keyword}에서 비롯된다.",
        "역사가 말해줍니다. {keyword}의 힘을.",
        "{keyword}는 운이 아니라 전략이다.",
        "{keyword}, 준비된 자만이 잡는다.",
        "이건 단순한 선택이 아니다. {keyword}다.",
        "승리는 {keyword}로부터." 
    ],
    "고민해결형": [
        "{keyword} 때문에 고민이신가요? 해답은 여기 있습니다",
        "{keyword} 문제, 이렇게 해결했습니다",
        "누구나 겪는 {keyword} 고민, 해결책은?",
        "더 이상 {keyword}로 고민하지 마세요",
        "실제로 효과 본 {keyword} 해결 방법",
        "{keyword} 문제, 이렇게 간단히 해결했어요",
        "{keyword}가 어려운 당신을 위한 가이드",
        "{keyword} 때문에 잠 못 이루는 당신에게",
        "혼자 해결하기 어려운 {keyword}, 도와드릴게요",
        "{keyword}, 이렇게만 하면 해결됩니다",
        "전문가가 추천하는 {keyword} 해결책",
        "{keyword}를 피하지 말고 해결해보세요",
        "고민 끝! {keyword}의 솔루션 제안",
        "{keyword} 문제, 생각보다 쉬웠던 해결법",
        "이건 몰랐죠? {keyword}의 해결 비밀",
        "당신의 {keyword} 고민, 저도 겪었습니다",
        "해결하지 못한 {keyword}, 이유는 이것",
        "{keyword}, 더 이상 방치하지 마세요",
        "지금 당장 가능한 {keyword} 해결 팁",
        "끝나지 않던 {keyword} 문제, 마침표 찍기"
    ],
    "실험형": [
        "{keyword}, 직접 해봤습니다",
        "1주일간 {keyword} 해본 후기",
        "{keyword}, 과연 진짜 효과 있을까? 직접 검증해봤어요",
        "실제로 해보니 알게 된 {keyword}의 진실",
        "{keyword}를 직접 써본 솔직 리뷰",
        "30일 동안 {keyword}를 실천해보니",
        "실험으로 확인한 {keyword} 결과 공개",
        "내 돈 주고 해본 {keyword} 체험기",
        "{keyword}, 해보기 전엔 몰랐던 사실",
        "직접 겪은 {keyword}의 효과와 부작용",
        "{keyword}, 단순한 이론일까? 실제로 해보자",
        "한 달간 {keyword} 생활 해본 솔직 후기",
        "{keyword}, 도전해본 리얼 후기",
        "{keyword} 실험기록: 시작부터 결과까지",
        "리얼하게 체험한 {keyword} 이야기",
        "{keyword}, 과연 기대만큼일까?",
        "이런 결과는 처음! {keyword} 실험 후기",
        "{keyword}, 상상 그 이상이었어요",
        "직접 겪은 {keyword}, 말 그대로 반전",
        "실험을 통해 증명된 {keyword}의 효과"
    ],
    "공감형": [
        "{keyword} 때문에 나도 힘들었어요",
        "혹시 당신도 이런 {keyword} 겪고 있나요?",
        "{keyword}, 나만 그런 거 아니었어",
        "{keyword}가 힘들었던 나의 이야기",
        "모두가 겪지만 말 못하는 {keyword}의 진실",
        "나도 몰랐던 {keyword}의 무게",
        "그 누구도 알려주지 않았던 {keyword}의 현실",
        "이 글을 본다면 당신도 {keyword}를 겪고 있을지도",
        "어느 날 갑자기 찾아온 {keyword}의 그림자",
        "{keyword}, 그저 남의 일일 줄 알았어요",
        "이건 내 이야기일지도 몰라요: {keyword}",
        "당신도 이런 {keyword} 고민 있으셨죠?",
        "{keyword}가 불편했던 진짜 이유",
        "모두가 피하고 싶은 {keyword}, 나도 예외 아니었다",
        "지금 생각해보면 {keyword}가 나를 살렸다",
        "다들 {keyword} 얘기를 꺼내지 않는 이유",
        "{keyword}에 대해 우리가 잘못 알고 있는 것들",
        "지금 이 순간에도 누군가는 {keyword}로 고통받고 있다",
        "내가 말하지 못했던 {keyword} 이야기",
        "이건 당신에게 꼭 하고 싶은 {keyword} 이야기"
    ],
    "정보형": [
        "{keyword}, 이것만은 꼭 알아두세요!",
        "당신이 몰랐던 {keyword}의 모든 것",
        "지금 바로 실천 가능한 {keyword} 꿀팁",
        "초보도 쉽게 배우는 {keyword} 방법",
        "하루 5분! {keyword} 루틴 정리",
        "{keyword} 시작하기 전에 꼭 알아야 할 5가지",
        "누구나 할 수 있는 {keyword} 노하우 정리",
        "{keyword}, 이런 분들에게 추천합니다",
        "아직도 몰라? {keyword} 기초 완전 정복",
        "{keyword} 마스터를 위한 핵심 요약",
        "입문자를 위한 {keyword} 첫걸음 가이드",
        "전문가가 알려주는 {keyword} 꿀팁 모음",
        "당장 실천 가능한 {keyword} 실전 팁",
        "{keyword}, 이렇게 하면 효과 두 배",
        "알면 유용한 {keyword} 핵심 정보 정리",
        "한 눈에 보는 {keyword} 체크리스트",
        "{keyword} 실수 줄이는 7가지 방법",
        "최신 트렌드 반영한 {keyword} 전략",
        "{keyword} 제대로 배우는 3단계 로드맵",
        "성공한 사람들이 말하는 {keyword} 활용법"
    ],
    "감성형": [
        "{keyword}로 물든 오늘 하루",
        "조용히 마음을 적시는 {keyword} 이야기",
        "당신에게도 필요한 {keyword}의 순간",
        "감정을 담은 {keyword}, 지금 공유할게요",
        "나를 위한 {keyword}, 지금 시작해요",
        "{keyword}, 하루를 감싸는 온기",
        "지친 마음에 스며드는 {keyword}",
        "차 한 잔과 함께하는 {keyword} 이야기",
        "마음이 따뜻해지는 {keyword} 한 줄",
        "{keyword}가 전하는 잔잔한 위로",
        "소중한 순간마다 함께하는 {keyword}",
        "조용히 다가오는 {keyword}의 온도",
        "감성 가득 담은 {keyword} 추천",
        "{keyword}로 물든 감정의 파도",
        "잠시 멈춰 바라본 {keyword}의 풍경",
        "{keyword}, 나를 위한 작은 쉼표",
        "감성적인 하루의 시작, {keyword}",
        "생각을 멈추고 느끼는 {keyword}",
        "마음을 간지럽히는 {keyword}의 문장",
        "{keyword}, 잊고 있던 감정을 깨우다"
    ],
    "자극형": [
        "이걸 안 보면 당신만 손해?! {keyword}의 진실",
        "모두가 놀란 {keyword}의 반전 효과",
        "{keyword}, 이렇게 하면 당신도 변할 수 있습니다",
        "10명 중 9명이 후회한 {keyword} 실수",
        "이 방법 하나로 {keyword} 완전 정복",
        "충격 폭발! {keyword} 결과에 모두 놀람",
        "{keyword} 때문에 생긴 놀라운 변화",
        "지금 안 보면 후회할 {keyword} 정보",
        "믿기 힘든 {keyword}의 효과, 직접 확인",
        "당신이 몰랐던 {keyword}의 충격 진실",
        "{keyword}, 당신의 인생을 바꿀지도?",
        "{keyword} 써본 사람들 100% 반응 폭발",
        "이건 진짜다… {keyword} 실화임",
        "단 1주일만에 {keyword}로 바뀐 인생",
        "{keyword}, 지금 시작하지 않으면 늦습니다",
        "후회 없는 선택, {keyword} 입문 가이드",
        "수많은 후기로 검증된 {keyword} 효과",
        "{keyword}로 성공한 사람들의 비밀 공개",
        "모두가 숨기고 싶은 {keyword}의 진짜 비밀",
        "당신도 몰랐던 {keyword}의 반전 매력"
    ],
    "리스트형": [
        "{keyword} 추천 TOP5 정리해드립니다",
        "지금 당장 써먹는 {keyword} 꿀팁 3가지",
        "알아두면 쓸모 있는 {keyword} 리스트",
        "{keyword} 잘하는 사람들이 지키는 7가지 습관",
        "{keyword} 완전정복! 단계별 가이드",
        "이것만은 꼭! {keyword} 실전 팁 5선",
        "초보자를 위한 {keyword} 핵심 3단계",
        "모두가 추천하는 {keyword} 활용법 10가지",
        "{keyword} 전문가들이 말하는 7가지 원칙",
        "효과 200% 보장하는 {keyword} 방법 TOP3",
        "{keyword} 입문자를 위한 체크리스트 6가지",
        "지금 필요한 {keyword} 핵심 꿀팁 8가지",
        "하루 10분 {keyword} 실천법 4선",
        "{keyword} 성공 노하우 TOP7 정리",
        "반드시 알아야 할 {keyword} 요약 리스트",
        "시간 절약! {keyword} 핵심만 뽑은 5가지",
        "{keyword}로 인생 바꾼 사람들의 3가지 습관",
        "완벽한 {keyword}를 위한 단계별 체크포인트",
        "이건 저장각! {keyword} 베스트 팁 모음",
        "{keyword} 잘하는 사람들이 자주 하는 말 TOP5"
    ],
    "의문형": [
        "왜 요즘 다들 {keyword}에 빠졌을까?",
        "{keyword}, 진짜 효과 있는 걸까?",
        "당신은 {keyword} 제대로 알고 있나요?",
        "{keyword}, 어떻게 시작하는 게 좋을까?",
        "{keyword}가 나에게도 맞을까?",
        "{keyword}, 모두가 좋아하는 이유는?",
        "왜 지금 {keyword}를 시작해야 할까?",
        "{keyword}, 과연 필요한 선택일까?",
        "어쩌다 나도 {keyword}를 시작했을까?",
        "{keyword}, 이대로 괜찮은 걸까?",
        "{keyword}는 어떻게 내 삶을 바꿨을까?",
        "왜 이렇게 많은 사람이 {keyword}를 찾을까?",
        "{keyword}, 정말 돈값을 할까?",
        "과연 {keyword}는 효과가 있을까?",
        "{keyword}, 이건 진짜일까 혹은 과장일까?",
        "{keyword}, 시도해도 괜찮은 걸까?",
        "나는 왜 {keyword}가 끌릴까?",
        "{keyword}, 다들 말하지만 정말 필요할까?",
        "{keyword}, 믿어도 되는 걸까?",
        "당신에게 {keyword}는 어떤 의미인가요?"
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
