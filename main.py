import streamlit as st
import random

st.set_page_config(page_title="랜덤 미니 게임 🎲", page_icon="🎮")

st.title("🎲 랜덤 미니 게임")
st.write("아래 버튼을 눌러 무작위 게임을 즐겨보세요!")

# --- 게임 목록 ---
games = ["가위바위보", "숫자 맞히기", "OX 퀴즈"]

# 세션에 선택된 게임 저장
if 'selected_game' not in st.session_state:
    st.session_state.selected_game = None

if st.button("게임 랜덤 선택 🎰"):
    st.session_state.selected_game = random.choice(games)

# --- 각 게임 정의 ---

# 1. 가위바위보
def game_rps():
    st.subheader("✊ 가위바위보")
    user = st.radio("당신의 선택은?", ["가위", "바위", "보"])
    if st.button("결과 보기"):
        comp = random.choice(["가위", "바위", "보"])
        st.write(f"👾 컴퓨터: {comp}")
        if user == comp:
            st.success("비겼어요!")
        elif (user == "가위" and comp == "보") or (user == "바위" and comp == "가위") or (user == "보" and comp == "바위"):
            st.success("이겼어요! 🎉")
        else:
            st.error("졌어요 😢")

# 2. 숫자 맞히기
def game_number():
    st.subheader("🔢 숫자 맞히기 (1~10)")
    answer = random.randint(1, 10)
    guess = st.number_input("숫자를 입력하세요:", min_value=1, max_value=10, step=1)
    if st.button("정답 확인"):
        if guess == answer:
            st.success("정답입니다! 🎉")
        else:
            st.error(f"틀렸어요! 정답은 {answer}였어요.")

# 3. OX 퀴즈
def game_ox():
    st.subheader("⭕ OX 퀴즈")
    question = "코끼리는 날 수 있다."
    user = st.radio(f"문제: {question}", ["O", "X"])
    if st.button("정답 확인"):
        if user == "X":
            st.success("정답입니다! 🎉")
        else:
            st.error("틀렸어요 😅")

# --- 선택된 게임 실행 ---
if st.session_state.selected_game == "가위바위보":
    game_rps()
elif st.session_state.selected_game == "숫자 맞히기":
    game_number()
elif st.session_state.selected_game == "OX 퀴즈":
    game_ox()
