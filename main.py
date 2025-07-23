import streamlit as st
import random
import time

st.set_page_config(page_title="랜덤 미니 게임 머신 🎮", page_icon="🎲")

st.title("🎲 랜덤 미니 게임 머신")
st.markdown("버튼을 누르면 무작위 미니 게임 하나가 나옵니다!")

# -------------------
# 게임 목록
# -------------------
games = [
    "가위바위보", "숫자 맞히기", "OX 퀴즈", "홀짝 게임", "타자 속도 테스트",
    "기억력 테스트", "초성 퀴즈", "주사위 대결", "수학 문제", "가사 빈칸 맞히기"
]

if 'selected_game' not in st.session_state:
    st.session_state.selected_game = None
if 'typing_start' not in st.session_state:
    st.session_state.typing_start = 0
if 'memory_answer' not in st.session_state:
    st.session_state.memory_answer = []

# -------------------
# 게임 선택 버튼
# -------------------
if st.button("🎰 게임 랜덤 선택"):
    st.session_state.selected_game = random.choice(games)

# -------------------
# 각 게임 정의
# -------------------

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

def game_number():
    st.subheader("🔢 숫자 맞히기 (1~10)")
    answer = random.randint(1, 10)
    guess = st.number_input("숫자를 입력하세요:", 1, 10, step=1)
    if st.button("정답 확인"):
        if guess == answer:
            st.success("정답입니다! 🎉")
        else:
            st.error(f"틀렸어요! 정답은 {answer}였어요.")

def game_ox():
    st.subheader("⭕ OX 퀴즈")
    q = "바다는 짜다."  # 예시
    user = st.radio(f"문제: {q}", ["O", "X"])
    if st.button("정답 확인"):
        if user == "O":
            st.success("정답입니다! 🧂")
        else:
            st.error("틀렸어요!")

def game_even_odd():
    st.subheader("🎯 홀짝 게임")
    user = st.radio("홀일까 짝일까?", ["홀", "짝"])
    if st.button("확인하기"):
        num = random.randint(1, 100)
        result = "홀" if num % 2 else "짝"
        st.write(f"숫자: {num}")
        if user == result:
            st.success("정답!")
        else:
            st.error(f"틀렸어요! 정답은 {result}")

def game_typing():
    st.subheader("⌨️ 타자 속도 테스트")
    sentence = "코딩은 생각하는 힘이다."
    st.write(f"문장: `{sentence}`")
    if st.button("시작"):
        st.session_state.typing_start = time.time()
    user_input = st.text_input("정확히 입력해보세요:")
    if user_input and st.session_state.typing_start:
        elapsed = round(time.time() - st.session_state.typing_start, 2)
        if user_input == sentence:
            st.success(f"완벽합니다! ⏱️ 걸린 시간: {elapsed}초")
        else:
            st.warning("문장이 달라요 😅")

def game_memory():
    st.subheader("🧠 기억력 테스트")
    words = ["사과", "고양이", "비행기", "커피", "하늘"]
    if not st.session_state.memory_answer:
        st.session_state.memory_answer = random.sample(words, 3)
    st.write("3초 동안 단어를 외워보세요!")
    st.write(st.session_state.memory_answer)
    time.sleep(3)
    st.write("이제 입력해보세요:")
    guesses = st.text_input("쉼표로 구분해서 입력 (예: 사과,하늘,커피)")
    if st.button("제출"):
        user_list = [x.strip() for x in guesses.split(",")]
        if set(user_list) == set(st.session_state.memory_answer):
            st.success("기억력 굿! 🎉")
        else:
            st.error("아쉽지만 틀렸어요.")
        st.session_state.memory_answer = []

def game_initials():
    st.subheader("💡 초성 퀴즈")
    answer = "코딩"
    hint = "ㅋㄷ"
    st.write(f"초성: {hint}")
    user = st.text_input("정답은?")
    if st.button("정답 확인"):
        if user.strip() == answer:
            st.success("정답입니다! 💡")
        else:
            st.error("오답입니다!")

def game_dice():
    st.subheader("🎲 주사위 대결")
    if st.button("던지기!"):
        user = random.randint(1, 6)
        comp = random.randint(1, 6)
        st.write(f"🎲 당신: {user}, 컴퓨터: {comp}")
        if user > comp:
            st.success("이겼어요! 🎉")
        elif user == comp:
            st.info("비겼어요!")
        else:
            st.error("졌어요 😢")

def game_math():
    st.subheader("➕ 랜덤 수학 문제")
    a, b = random.randint(1, 20), random.randint(1, 20)
    user = st.number_input(f"{a} + {b} = ?", step=1)
    if st.button("확인"):
        if user == a + b:
            st.success("정답입니다! 🔢")
        else:
            st.error(f"틀렸어요. 정답은 {a + b}")

def game_lyrics():
    st.subheader("🎵 가사 빈칸 맞히기")
    question = "나는 ______를 사랑해 (힌트: 동물)"
    answer = "고양이"
    st.write(question)
    user = st.text_input("빈칸에 들어갈 말은?")
    if st.button("제출"):
        if user.strip() == answer:
            st.success("정답! 🎵")
        else:
            st.error("틀렸어요!")

# -------------------
# 게임 실행
# -------------------
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
elif st.session_state.selected_game == "기억력 테스트":
    game_memory()
elif st.session_state.selected_game == "초성 퀴즈":
    game_initials()
elif st.session_state.selected_game == "주사위 대결":
    game_dice()
elif st.session_state.selected_game == "수학 문제":
    game_math()
elif st.session_state.selected_game == "가사 빈칸 맞히기":
    game_lyrics()
