import streamlit as st

st.set_page_config(page_title="SNS 해시태그 추천기", page_icon="🏷️")

st.title("🏷️ SNS 해시태그 추천기")
st.markdown("키워드를 입력하면 해시태그를 추천해드리고, 원하는 해시태그도 직접 추가할 수 있어요!")

# 기본 해시태그 데이터
default_hashtag_db = {
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
}

# 세션 상태에 해시태그 DB 저장
if 'hashtag_db' not in st.session_state:
    st.session_state.hashtag_db = default_hashtag_db

# 🔍 키워드로 해시태그 조회
keyword = st.text_input("🔎 키워드를 입력하세요 (예: 카페, 다이어트 등)")

if keyword:
    matched = st.session_state.hashtag_db.get(keyword)
    if matched:
        st.subheader("📌 추천 해시태그")
        for size in ["대형", "중형", "소형"]:
            tags = matched.get(size, [])
            tag_string = " ".join(tags)
            st.markdown(f"**{size} 해시태그**:")
            st.code(tag_string, language='markdown')
    else:
        st.info("등록된 해시태그가 없어요. 아래에서 직접 추가해보세요!")

# ➕ 해시태그 추가 폼
st.subheader("➕ 새로운 해시태그 추가")
with st.form("add_hashtag_form"):
    new_keyword = st.text_input("키워드 (예: 여행, 음식 등)")
    tag_size = st.radio("해시태그 크기", ["대형", "중형", "소형"], horizontal=True)
    new_tags_input = st.text_input("추가할 해시태그들 (쉼표로 구분)", placeholder="#예시1, #예시2")
    submitted = st.form_submit_button("추가하기")

    if submitted and new_keyword and new_tags_input:
        tags_to_add = [tag.strip() for tag in new_tags_input.split(",") if tag.strip()]
        if new_keyword not in st.session_state.hashtag_db:
            st.session_state.hashtag_db[new_keyword] = {"대형": [], "중형": [], "소형": []}
        st.session_state.hashtag_db[new_keyword][tag_size].extend(tags_to_add)
        st.success(f"'{new_keyword}' 키워드에 {tag_size} 해시태그 추가 완료!")

# 전체 키워드 목록 보기 (선택 사항)
with st.expander("📂 현재 등록된 키워드 보기"):
    for key in st.session_state.hashtag_db:
        st.markdown(f"- `{key}`")
