# --- 배경 스타일 CSS 추가 ---
st.markdown("""
    <style>
    body {
        background-image: url("https://images.unsplash.com/photo-1510626176961-4bfb7f9ada2d");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
    }

    .stApp {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 15px;
    }

    .title {
        font-size: 36px;
        text-align: center;
        color: #2c3e50;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 18px;
        text-align: center;
        color: #555;
        margin-bottom: 20px;
    }

    .menu-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)
