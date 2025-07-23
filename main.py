import streamlit as st

st.set_page_config(page_title="SNS 해시태그 추천기", page_icon="🏷️")
st.title("🏷️ SNS 해시태그 추천기")
st.markdown("제품/주제/키워드를 입력하면 관련 해시태그를 추천해드립니다.")

# 샘플 해시태그 사전 (확장 가능)
hashtag_db = {
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
    "디저트": {
        "대형": ["#디저트", "#디저트맛집", "#먹스타그램"],
        "중형": ["#케이크맛집", "#달달한하루", "#디저트카페"],
        "소형": ["#크로플", "#초코덕후", "#디저트타임"]
    }
}

# 사용자 입력
keyword = st.text_input("🔎 키워드를 입력하세요 (예: 카페, 다이어트, 디저트 등)")

if keyword:
    matched = hashtag_db.get(keyword)
    if matched:
        st.subheader("📌 추천 해시태그")

        for size in ["대형", "중형", "소형"]:
            tags = matched.get(size, [])
            tag_string = " ".join(tags)
            st.markdown(f"**{size} 해시태그**: `{tag_string}`")
            st.code(tag_string, language='markdown')
    else:
        st.warning("😥 해당 키워드는 아직 등록되어 있지 않아요. 다른 키워드를 시도해보세요!")

