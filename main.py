import streamlit as st
import random

st.set_page_config(page_title="칭찬 머신 💬", page_icon="😊")

st.markdown("""
    <style>
    .centered {
        display: flex;
        justify-content: center;import streamlit as st
import random
import datetime
import os
import json

st.set_page_config(page_title="상상력 퀘스트 🎨", page_icon="🧩")

st.title("🧩 상상력 퀘스트")
st.markdown("당신의 창의력을 깨울 작은 질문 하나 💭")

# 퀘스트 목록
quests = [
    "지금 눈앞에 있는 물건 3개로 짧은 이야기를 만들어보세요.",
    "고양이가 회의실에 들어왔다면 어떤 일이 벌어질까요?",
    "시간이 멈추고 당신만 움직일 수 있다면 무엇을 하시겠어요?",
    "하늘에서 종이비가 내린다면 어떤 일이 벌어질까요?",
    "냉장고 안에 사는 생명체가 있다면 어떤 모습일까요?",
    "당신이 투명 인간이 되었다면 첫 날 무엇을 하겠어요?",
    "하루 동안 다른 사람과 삶을 바꿔 살 수 있다면 누구와 바꾸고 싶나요?",
    "구름 위에서 살 수 있다면 집은 어떤 모습일까요?",
    "당신의 그림자가 말을 걸어온다면 무슨 이야기를 할까요?",
    "잊어버린 기억 하나가 돌아온다면 무엇이었으면 하나요?"
]

# 저장 파일
SAVE_FILE = "imagination_logs.json"

# 퀘스트 선택
if 'today_quest' not in st.session_state:
    st.session_state.today_quest = random.choice(quests)

st.subheader("✨ 오늘의 퀘스트")
st.markdown(f"**_{st.session_state.today_quest}_**")

# 사용자 작성 입력
st.subheader("📝 나의 상상력 답변")
user_response = st.text_area("여기에 당신의 상상을 적어주세요!", height=200)

if st.button("저장하기"):
    response = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "quest": st.session_state.today_quest,
        "answer": user_response
    }

    # 기존 저장 데이터 불러오기
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(response)

    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, ensure_ascii=False, indent=2)

    st.success("상상력이 저장되었어요! ✨")
    st.session_state.today_quest = random.choice(quests)
    st.experimental_rerun()

# 기록 보기
with st.expander("📜 나의 상상 기록 보기"):
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            saved = json.load(f)
            for item in reversed(saved):
                st.markdown(f"**[{item['date']}]**")
                st.markdown(f"🧠 *{item['quest']}*")
                st.write(f"💬 {item['answer']}")
                st.markdown("---")
    else:
        st.info("아직 저장된 상상력이 없어요!")

        align-items: center;
        flex-direction: column;
    }
    .compliment {
        font-size: 32px;
        font-weight: bold;
        color: #4CAF50;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# 칭찬 리스트
compliments = [
    "오늘도 살아낸 당신, 정말 멋져요 🌱",
    "당신은 생각보다 훨씬 더 소중한 사람이에요.",
    "계속 나아가는 그 모습, 정말 대단해요 💪",
    "오늘의 작은 노력도 분명히 의미 있어요.",
    "지금까지 잘 해왔고, 앞으로도 잘 할 거예요 🌈",
    "당신의 존재만으로도 이미 충분해요.",
    "실수해도 괜찮아요, 그건 성장의 일부니까요.",
    "오늘도 잘 버텨줘서 고마워요 😊",
    "당신은 사랑받기 충분한 사람이에요 ❤️",
    "지금 이 순간도 당신 편이에요. 나도 그래요."
]

# UI
st.title("🎁 랜덤 칭찬 머신")
st.markdown("당신을 위한 작은 응원 한마디 💬")

if st.button("칭찬 받기 💌"):
    msg = random.choice(compliments)
    st.markdown(f"<div class='compliment'>{msg}</div>", unsafe_allow_html=True)
