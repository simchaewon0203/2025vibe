import streamlit as st
import random

# 예시 메뉴 데이터
menu_data = {
    "든든한 한식": ["김치찌개", "된장국", "소고기미역국", "떡국"],
    "가볍게 먹는 샐러드": ["닭가슴살 샐러드", "과일 요거트", "시리얼 + 우유"],
    "간단한 빵류": ["크로와상 + 아메리카노", "토스트 + 계란", "샌드위치"],
    "외식 추천": ["맥모닝", "편의점 도시락", "프랜차이즈 아침 세트"],
}

# 사용자 입력
st.title("🥣 오늘 아침 뭐 먹을까?")
st.write("아래 항목을 선택하면 오늘 아침 메뉴를 추천해드릴게요!")

mood = st.selectbox("오늘의 기분은 어떤가요?", ["상쾌함", "피곤함", "바쁨", "느긋함"])
place = st.radio("어디서 먹을 예정인가요?", ["집", "회사/학교", "외식"])
diet = st.multiselect("먹고 싶은 종류를 선택하세요", list(menu_data.keys()))

# 추천 버튼
if st.button("추천 받기"):
    selected = []

    if diet:
        for style in diet:
            selected.extend(menu_data[style])
    else:
        for style in menu_data:
            selected.extend(menu_data[style])

    recommendation = random.choice(selected)
    st.success(f"오늘의 추천 아침 메뉴는 🍽️ **{recommendation}** 입니다!")

    # 이미지가 있다면 아래와 같이 추가 가능
    # st.image("images/gimbap.jpg", use_column_width=True)

