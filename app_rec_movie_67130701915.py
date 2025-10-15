import streamlit as st
import pickle
from myfunction_67130701915 import get_movie_recommendations

# -----------------------------
# ส่วนหัวของหน้าเว็บ
# -----------------------------
st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬", layout="centered")

st.title("🎥 Movie Recommendation System")
st.write("ระบบแนะนำภาพยนตร์อัจฉริยะ — แนะนำหนังที่คุณอาจจะชอบตามพฤติกรรมของผู้ใช้ที่คล้ายกัน")

# -----------------------------
# โหลดข้อมูล
# -----------------------------
@st.cache_data
def load_data():
    with open('recommendation_data.pkl', 'rb') as file:
        user_similarity_df, user_movie_ratings = pickle.load(file)
    return user_similarity_df, user_movie_ratings

user_similarity_df, user_movie_ratings = load_data()

# -----------------------------
# อินพุตจากผู้ใช้
# -----------------------------
st.sidebar.header("⚙️ ตั้งค่าการแนะนำ")
user_id = st.sidebar.number_input("กรอกหมายเลขผู้ใช้ (User ID):", min_value=1, value=1, step=1)
num_recommendations = st.sidebar.slider("จำนวนหนังที่ต้องการแนะนำ:", 1, 20, 10)

# -----------------------------
# ปุ่มกดเพื่อแสดงผลลัพธ์
# -----------------------------
if st.button("🔍 แนะนำหนังให้ฉัน"):
    try:
        recommendations = get_movie_recommendations(user_id, user_similarity_df, user_movie_ratings, num_recommendations)
        
        if recommendations:
            st.success(f"🎯 ผลการแนะนำสำหรับผู้ใช้หมายเลข {user_id}")
            for i, movie_title in enumerate(recommendations, start=1):
                st.write(f"{i}. **{movie_title}**")
        else:
            st.warning("ไม่พบข้อมูลคำแนะนำสำหรับผู้ใช้นี้")
    except Exception as e:
        st.error(f"เกิดข้อผิดพลาด: {e}")

# -----------------------------
# ส่วนท้าย (Footer)
# -----------------------------
st.markdown("---")
st.caption("พัฒนาโดย : ระบบแนะนำภาพยนตร์อัจฉริยะ (Movie Recommender AI)")


