import streamlit as st
import os
import json
from datetime import datetime

# --- 설정 ---
DATA_FILE = "plant_data.json"
MAX_STAGE = 5  # 최대 성장 단계 (0~5)
PLANT_IMAGES = [
    "🌱",  # 0단계
    "🌿",  # 1단계
    "🍀",  # 2단계
    "🌼",  # 3단계
    "🌷",  # 4단계
    "🌻"   # 5단계 - 만개
]

# --- 데이터 로드/저장 ---
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"stage": 0, "last_watered": ""}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# --- 앱 시작 ---
st.set_page_config(page_title="나의 식물 키우기 🌱", page_icon="🌿")
st.title("🌿 나만의 식물을 키워보세요!")
st.write("매일 물을 주면 식물이 자라나요. 하루에 한 번만 줄 수 있어요.")

# --- 데이터 처리 ---
data = load_data()
today = datetime.now().strftime("%Y-%m-%d")

# --- 식물 상태 보여주기 ---
stage = data["stage"]
plant_icon = PLANT_IMAGES[stage]
st.markdown(f"## 현재 식물 상태: {plant_icon} (단계 {stage})")

# --- 물주기 기능 ---
if data["last_watered"] == today:
    st.info("오늘은 이미 물을 줬어요! 내일 또 와주세요 🌞")
else:
    if st.button("💧 물 주기"):
        if stage < MAX_STAGE:
            data["stage"] += 1
            st.success("식물이 조금 자랐어요! 🌱")
        else:
            st.success("식물이 이미 활짝 피었어요! 🌻")
        data["last_watered"] = today
        save_data(data)
        st.experimental_rerun()

