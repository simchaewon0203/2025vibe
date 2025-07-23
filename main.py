import streamlit as st
import random
import time

st.set_page_config(page_title="랜덤 미니 게임 🎮", page_icon="🎲")

st.title("🎲 랜덤 미니 게임")
st.write("게임을 랜덤으로 골라 한 번 플레이해보세요!")

# --- 게임 목록 ---
games = ["가위바위보", "숫자 맞히기", "OX 퀴즈", "홀짝 게임", "타자 속도 테스트"]

# --- 세션 상태 초기화 ---
if 'selected_game' not in st.session_state:
    st.session_state.selected_game = None
if 'typing_start' not in st.session_state:
    st.session_state.typing_start = 0

# --- 랜덤 선택 버튼 ---
if st.button("🎰 게임 랜덤 선택"):
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
    question = "지구는 태양을 돈다."
    answer = "O"
    user = st.radio(f"문제: {question}", ["O", "X"])
    if st.button("정답 확인"):
        if user == answer:
            st.success("정답입니다! 🎉")
        else:
            st.error("틀렸어요 😅")

# 4. 홀짝 게임
def game_even_odd():
    st.subheader("🎯 홀짝 게임")
    user = st.radio("홀일까 짝일까?", ["홀", "짝"])
    if st.button("확인하기"):
        num = random.randint(1, 100)
        result = "홀" if num % 2 == 1 else "짝"
        st.write(f"🔢 생성된 숫자: {num}")
        if user == result:
            st.success("정답! 맞혔어요 🎉")
        else:
            st.error(f"틀렸어요! 정답은 {result}")

# 5. 타자 속도 테스트
def game_typing():
    st.subheader("⌨️ 타자 속도 테스트")

    sentence = "오늘도 즐겁게 코딩을 해봅시다!"
    st.markdown(f"**입력할 문장:** `{sentence}`")

    if st.button("시작하기"):
        st.session_state.typing_start = time.time()

    user_input = st.text_input("문장을 정확히 입력하세요:")
    if user_input and st.session_state.typing_start != 0:
        elapsed = round(time.time() - st.session_state.typing_start, 2)
        if user_input == sentence:
            st.success(f"정확히 입력했어요! 걸린 시간: {elapsed}초")
        else:
            st.warning("문장이 정확하지 않아요 😅")

# --- 선택된 게임 실행 ---
if st.session_state.selected_game == "가위바위보":
    game_rps()
elif st.session_state.selected_game == "숫자 맞히기":
    game_number()
elif st.session_state.selected_game == "OX 퀴즈":
    game_ox()
elif st.session_state.selected_game == "홀짝 게임":
    game_even_odd()
elif st.session_state.selected_game == "타자 속도 테스트":
    game_typing()
