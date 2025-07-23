import streamlit as st
import random

st.set_page_config(page_title="책 속 한 문장", page_icon="📖")

# 예시 문장 데이터 (원하는 만큼 추가 가능)
quotes = [
    {
        "quote": "우리는 모두 자기만의 방식으로 부서진 존재다.",
        "book": "파친코",
        "author": "이민진"
    },
    {
        "quote": "결국 해내는 사람은 끝까지 포기하지 않은 사람이다.",
        "book": "하마터면 열심히 살 뻔했다",
        "author": "하완"
    },
    {
        "quote": "슬픔은 지나가지만, 그때 했던 말은 남는다.",
        "book": "죽고 싶지만 떡볶이는 먹고 싶어",
        "author": "백세희"
    },
    {
        "quote": "완벽하지 않아도 괜찮아, 우린 인간이니까.",
        "book": "아무튼, 서른",
        "author": "김신회"
    },
    {
        "quote": "내가 괜찮아질 때까지 나를 기다려주기로 했다.",
        "book": "곰돌이 푸, 행복한 일은 매일 있어",
        "author": "곰돌이 푸"
    }
]

# UI 구성
st.title("📖 책 속 한 문장 인용기")
st.write("오늘 당신에게 필요한 문장을 선물해드릴게요.")

if st.button("🎲 문장 뽑기"):
    quote = random.choice(quotes)
    st.markdown(f"""
    > “*{quote['quote']}*”
    
    — <strong>{quote['book']}</strong>, {quote['author']}
    """, unsafe_allow_html=True)
