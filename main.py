import streamlit as st
import requests
import random
import os

# ------------ 설정 ------------
OPENWEATHER_API_KEY = "YOUR_API_KEY"  # 여기에 본인의 API 키 입력
CITY = "Seoul"

# ------------ 날씨 함수 ------------
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&lang=kr&units=metric"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        weather = data['weather'][0]['main']
        temp = data['main']['temp']
        return weather, temp
    else:
        return "정보 없음", 0

# ------------ 메뉴 데이터 ------------
menu_data = {
    "맑은 날": {
        "든든한 한식": [("김치찌개", "images/김치찌개.jpg"),
                    ("된장국", "images/된장국.jpg"),
                    ("떡국", "images/떡국.jpg")],
        "가볍게 샐러드": [("과일 요거트", "images/요거트.jpg"),
                     ("닭가슴살 샐러드", "images/샐러드.jpg")]
    },
    "비 오는 날": {
        "따뜻한 국물": [("우동", "images/우동.jpg"),
                     ("잔치국수", "images/잔치국수.jpg"),
                     ("미역국", "images/미역국.jpg")],
        "포근한 한끼": [("토스트 + 우유", "images/토스트.jpg")]
    },
    "기타": {
        "빵류": [("크로와상 + 커피", "images/크로와상.jpg"),
               ("샌드위치", "images/샌드위치.jpg")]
    }
}

# ------------ UI 설정 ------------
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍳", layout="centered")

st.markdown("""
    <style>
    .title { font-size: 36px; text-align: center; color: #2c3e50; margin-bottom: 10px; }
    .subtitle { font-size: 18px; text-align: center; color: #888; margin-bottom: 20px; }
    .menu-card {
        background-color: #f2f2f2;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🍽️ 오늘 아침 뭐 먹을까?</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">날씨에 딱 맞는 메뉴를 추천해드려요!</div>', unsafe_allow_html=True)

# ------------ 날씨 정보 표시 ------------
weather, temp = get_weather(CITY)
st.info(f"📍 현재 위치: {CITY} / 날씨: {weather}, {temp}°C")

# ------------ 사용자 입력 ------------
with st.form("recommend_form"):
    style = st.selectbox("🍱 어떤 스타일의 아침을 원하시나요?", ["든든한 한식", "가볍게 샐러드", "따뜻한 국물", "포근한 한끼", "빵류"])
    submitted = st.form_submit_button("✨ 추천받기")

# ------------ 추천 결과 ------------
if submitted:
    if "맑음" in weather:
        group = "맑은 날"
    elif "비" in weather or "Rain" in weather:
        group = "비 오는 날"
    else:
        group = "기타"

    menus = menu_data.get(group, {}).get(style, [])
    if not menus:
        st.warning("선택한 스타일에 맞는 메뉴가 없습니다.")
    else:
        menu, image_path = random.choice(menus)
        st.markdown(f"""
            <div class="menu-card">
                <h3>오늘의 추천 메뉴 🍳</h3>
                <h2 style='color:#2980b9'>{menu}</h2>
            </div>
        """, unsafe_allow_html=True)
        if os.path.exists(image_path):
            st.image(image_path, use_column_width=True)
        else:
            st.text("이미지를 찾을 수 없습니다.")
