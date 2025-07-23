import streamlit as st

st.set_page_config(page_title="SNS 해시태그 추천기", page_icon="🏷️")
st.title("🏷️ SNS 해시태그 추천기")
st.markdown("키워드를 입력하면 해시태그를 추천해드리고, 원하는 해시태그도 직접 추가할 수 있어요!")

# 🔸 초기 해시태그 데이터셋 (10개 키워드 × 3단계)
initial_db = {
    "카페": {
        "대형": ["#카페스타그램", "#카페투어", "#카페추천"],
        "중형": ["#감성카페", "#카페일상", "#예쁜카페"],
        "소형": ["#한적한카페", "#동네카페", "#비오는날카페"]
    },
    "다이어트": {
        "대형": ["#다이어트", "#운동스타그램", "#헬스타그램"],
        "중형": ["#다이어터", "#식단일기", "#홈트"],
        "소형": ["#저탄고지식단", "#다이어트일기", "#아침운동"]
    },
    "여행": {
        "대형": ["#여행", "#여행스타그램", "#해외여행"],
        "중형": ["#국내여행", "#자유여행", "#여행일기"],
        "소형": ["#일본여행", "#혼자여행", "#주말여행"]
    },
    "맛집": {
        "대형": ["#맛집", "#먹스타그램", "#맛집추천"],
        "중형": ["#한식맛집", "#분위기맛집", "#맛있는하루"],
        "소형": ["#동네맛집", "#숨은맛집", "#혼밥맛집"]
    },
    "패션": {
        "대형": ["#패션", "#데일리룩", "#옷스타그램"],
        "중형": ["#오늘의코디", "#패션스타그램", "#쇼핑"],
        "소형": ["#가을패션", "#캐주얼룩", "#패션피플"]
    },
    "뷰티": {
        "대형": ["#뷰티", "#화장품추천", "#스킨케어"],
        "중형": ["#립추천", "#기초화장", "#메이크업"],
        "소형": ["#저자극화장품", "#비건뷰티", "#톤업크림"]
    },
    "운동": {
        "대형": ["#운동", "#헬스", "#피트니스"],
        "중형": ["#홈트레이닝", "#운동일지", "#스트레칭"],
        "소형": ["#하체운동", "#아침운동", "#운동자극"]
    },
    "책": {
        "대형": ["#책스타그램", "#독서", "#서점"],
        "중형": ["#독후감", "#오늘의책", "#책추천"],
        "소형": ["#북카페", "#독서일기", "#문학"]
    },
    "음악": {
        "대형": ["#음악", "#노래추천", "#뮤직"],
        "중형": ["#감성노래", "#음악스타그램", "#멜론차트"],
        "소형": ["#플레이리스트", "#밤에듣기좋은노래", "#노래모음"]
    },
    "강아지": {
        "대형": ["#강아지", "#멍스타그램", "#반려견"],
        "중형": ["#강아지일상", "#강아지훈련", "#강아지산책"],
        "소형": ["#푸들", "#말티즈", "#강아지사진"]
    }
}

# 📌 세션 상태로 해시태그 DB 유지
if "hashtag_db" not in st.session_state:
    st.session_state.hashtag_db = initial_db

# 🔍 키워드 입력 후 해시태그 추천
keyword = st.text_input("🔎 키워드를 입력하세요 (예: 여행, 맛집, 강아지 등)")

if keyword:
    matched = st.session_state.hashtag_db.get(keyword)
    if matched:
        st.subheader("📌 추천 해시태그")
        for size in ["대형", "중형", "소형"]:
            tags = matched.get(size, [])
            tag_str = " ".join(tags)
            st.markdown(f"**{size} 해시태그**")
            st.code(tag_str, language='markdown')
    else:
        st.info("등록된 해시태그가 없어요. 아래에서 직접 추가해보세요!")

# ➕ 해시태그 직접 추가
st.subheader("➕ 새로운 해시태그 추가")
with st.form("add_form"):
    new_keyword = st.text_input("추가할 키워드 (예: 꽃, 재테크 등)")
    tag_size = st.radio("해시태그 크기", ["대형", "중형", "소형"], horizontal=True)
    new_tags_input = st.text_input("추가할 해시태그들 (쉼표로 구분)", placeholder="#예시1, #예시2")
    submitted = st.form_submit_button("등록하기")

    if submitted and new_keyword and new_tags_input:
        new_tags = [tag.strip() for tag in new_tags_input.split(",") if tag.strip()]
        if new_keyword not in st.session_state.hashtag_db:
            st.session_state.hashtag_db[new_keyword] = {"대형": [], "중형": [], "소형": []}
        st.session_state.hashtag_db[new_keyword][tag_size].extend(new_tags)
        st.success(f"✅ '{new_keyword}' 키워드에 해시태그가 추가되었습니다!")

# 📂 키워드 전체 목록 보기
with st.expander("📂 현재 등록된 키워드 보기"):
    for k in sorted(st.session_state.hashtag_db.keys()):
        st.markdown(f"- `{k}`")
