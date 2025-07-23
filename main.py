import streamlit as st
import random

# --- 기본 설정 ---
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍽️", layout="centered")

# --- 스타일 커스터마이징 ---
st.markdown("""
    <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #4B8BBE;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 20px;
            text-align: center;
            color: #666666;
            margin-bottom: 30px;
        }
        .menu-card {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# --- 메뉴 데이터 ---
menu_data = {
    "든든한 한식": ["김치찌개", "된장국", "소고기미역국", "떡국"],
    "가볍게 먹는 샐러드": ["닭가슴살 샐러드", "과일 요거트", "시리얼 + 우유"],
    "간단한 빵류": ["크로와상 + 아메리카노", "토스트 + 계란", "샌드위치"],
    "외식 추천": ["맥모닝", "편의점 도시락", "프랜차이즈 아침 세트"],
}

# --- 타이틀 영역 ---
st.markdown('<div class="title">🥣 오늘 아침 뭐 먹을까?</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">기분과 상황에 따라 딱 맞는 메뉴를 추천해드릴게요!</div>', unsafe_allow_html=True)

# --- 입력 폼 ---
with st.form("recommendation_form"):
    mood = st.selectbox("😄 오늘의 기분은?", ["상쾌함", "피곤함", "바쁨", "느긋함"])
    place = st.radio("📍 어디서 식사할 예정인가요?", ["집", "회사/학교", "외식"])
    diet = st.multiselect("🍱 어떤 스타일을 원하시나요?", list(menu_data.keys()))
    submitted = st.form_submit_button("✨ 메뉴 추천받기")

# --- 추천 결과 ---
if submitted:
    selected = []

    if diet:
        for style in diet:
            selected.extend(menu_data[style])
    else:
        for style in menu_data:
            selected.extend(menu_data[style])

    recommendation = random.choice(selected)

    st.markdown(f"""
        <div class="menu-card">
            <h3>🍽️ 오늘의 추천 메뉴는</h3>
            <h2 style='color:#4B8BBE'>{recommendation}</h2>
            <p>좋은 하루를 위한 든든한 한 끼가 되어줄 거예요 😊</p>
        </div>
    """, unsafe_allow_html=True)
