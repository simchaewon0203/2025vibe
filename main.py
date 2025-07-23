import streamlit as st
import random

st.set_page_config(page_title="칭찬 머신 💬", page_icon="😊")

st.markdown("""
    <style>
    .centered {
        display: flex;
        justify-content: center;
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
