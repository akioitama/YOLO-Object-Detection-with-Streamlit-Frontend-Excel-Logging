# app.py
import streamlit as st
import pandas as pd
from ultralytics import YOLO
from collections import Counter
from PIL import Image
import os

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="YOLO Detection Dashboard",
    layout="wide",
    page_icon="🎯"
)

# -----------------------------
# DARK THEME & HIGH CONTRAST CSS
# -----------------------------
st.markdown("""
<style>
/* Global dark background */
.stApp {
    background-color: #0f172a;
}

/* Main title */
.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 5px;
}

/* Subtitle */
.sub-text {
    color: #cbd5f5;
    font-size: 18px;
    margin-bottom: 25px;
}

/* Card containers */
.card {
    background-color: #1e293b;
    padding: 25px;
    border-radius: 16px;
    border: 1px solid #334155;
    box-shadow: 0 6px 20px rgba(0,0,0,0.4);
    color: #ffffff;
}

/* Detection badges (high contrast) */
.badge {
    display: inline-block;
    background-color: #38bdf8;
    color: #0f172a;
    padding: 10px 18px;
    border-radius: 20px;
    margin: 6px 6px 6px 0px;
    font-weight: 700;
    font-size: 16px;
    letter-spacing: 0.3px;
    box-shadow: 0 4px 12px rgba(56,189,248,0.35);
    animation: fadeIn 0.25s ease-in-out;
}

/* Fade animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(8px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Sidebar dark */
section[data-testid="stSidebar"] {
    background-color: #020617;
}

/* Improve text visibility */
h1, h2, h3, h4, h5, h6, p, label {
    color: #ffffff !important;
}

/* Remove extra top padding */
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown("<div class='main-title'>🎯 YOLO Image Detection Dashboard</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-text'>Dark Mode • High Contrast • Upload Image • Smart Excel Max Detection</div>",
    unsafe_allow_html=True
)

# -----------------------------
# Load YOLO Model
# -----------------------------
model = YOLO("yolov8n.pt")
excel_file = "items.xlsx"

# -----------------------------
# MAX FRAME UPDATE LOGIC
# -----------------------------
def update_excel_max(frame_counts):
    if not os.path.exists(excel_file):
        st.error("❌ items.xlsx not found in project folder.")
        return None

    df = pd.read_excel(excel_file)

    for label, count in frame_counts.items():
        if label in df['items'].values:
            df.loc[df['items'] == label, 'status'] = 'checked'
            prev_qty = df.loc[df['items'] == label, 'quantity'].fillna(0).values[0]
            if count > prev_qty:
                df.loc[df['items'] == label, 'quantity'] = count

    # Safe write
    temp_file = excel_file + ".temp.xlsx"
    df.to_excel(temp_file, index=False)
    os.replace(temp_file, excel_file)
    return df

# -----------------------------
# IMAGE UPLOAD MODE
# -----------------------------
st.markdown("<div class='card'><h3>📤 Upload Image for Detection</h3></div>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.image(image, caption="Uploaded Image", use_container_width=True)

    # YOLO detection
    results = model(image)
    detected_labels = [results[0].names[int(box.cls[0])] for box in results[0].boxes]
    frame_counts = Counter(detected_labels)

    with col2:
        st.markdown("<div class='card'><h4>🧠 Detected Objects</h4>", unsafe_allow_html=True)

        if frame_counts:
            badge_html = ""
            for label, count in frame_counts.items():
                badge_html += f"<span class='badge'>{label} × {count}</span>"
            st.markdown(badge_html, unsafe_allow_html=True)

            df_updated = update_excel_max(frame_counts)
            if df_updated is not None:
                st.success("✅ Excel updated (MAX frame logic applied)")
                with st.expander("View Updated Excel"):
                    st.dataframe(df_updated)
        else:
            st.warning("⚠️ No objects detected")

        st.markdown("</div>", unsafe_allow_html=True)