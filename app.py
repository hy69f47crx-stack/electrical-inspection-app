import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import json
import os
from dotenv import load_dotenv

# استيراد نظام RAG
try:
    from chatbot_rag import create_rag_system
    CHATBOT_AVAILABLE = True
except ImportError:
    CHATBOT_AVAILABLE = False

# تحميل متغيرات البيئة
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="تطبيق المعاينات الكهربائية",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== PRIDE BAR THEME - CSS الكاملة =====
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');

    /* ===== متغيرات الألوان - Pride Bar Theme ===== */
    :root {
        --bg-cream: #f0eee9;
        --bg-cream-2: #f5efe6;
        --bg-paper: #ffffff;
        --color-accent: #E0C896;
        --accent-light: #f0e6d0;
        --accent-dark: #d4af6a;
        --color-dark: #5C4A3A;
        --color-text-dark: #1a1410;
        --color-text-medium: #3d3226;
        --color-text-light: #8b7d6b;
        --line-color: #e0d9d0;
        --border-color: #ddd0c8;
        --shadow-sm: 0 1px 3px rgba(92, 74, 58, 0.12);
        --shadow-md: 0 4px 12px rgba(92, 74, 58, 0.15);
        --shadow-lg: 0 12px 32px rgba(92, 74, 58, 0.18);
        --font-primary: 'Inter', 'Roboto', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* ===== العناصر الأساسية ===== */
    * { box-sizing: border-box; }

    html, body {
        background-color: var(--bg-cream) !important;
        color: var(--color-text-dark) !important;
        font-family: var(--font-primary) !important;
    }

    .main {
        background-color: var(--bg-cream) !important;
        padding: 20px !important;
    }

    .stApp {
        background-color: var(--bg-cream) !important;
    }

    /* ===== Sidebar ===== */
    [data-testid="stSidebar"] {
        background-color: var(--bg-paper) !important;
        border-right: 2px solid var(--color-accent) !important;
    }

    [data-testid="stSidebar"] > div:first-child {
        background-color: var(--bg-paper) !important;
    }

    /* ===== العناوين ===== */
    h1 {
        color: var(--color-accent) !important;
        font-size: 36px !important;
        font-weight: 800 !important;
        border-bottom: 3px solid var(--color-accent) !important;
        padding-bottom: 12px !important;
        margin-bottom: 24px !important;
    }

    h2 {
        color: var(--color-dark) !important;
        font-size: 28px !important;
        font-weight: 700 !important;
        margin-bottom: 16px !important;
    }

    h3 {
        color: var(--color-dark) !important;
        font-size: 22px !important;
        font-weight: 700 !important;
        margin-bottom: 12px !important;
    }

    h4, h5, h6 {
        color: var(--color-text-dark) !important;
        font-weight: 600 !important;
    }

    /* ===== الأزرار ===== */
    .stButton > button {
        background: linear-gradient(135deg, #E0C896 0%, #d4af6a 100%) !important;
        color: var(--color-text-dark) !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px 24px !important;
        font-weight: 700 !important;
        font-size: 15px !important;
        transition: all 0.3s ease !important;
        box-shadow: var(--shadow-md) !important;
        cursor: pointer !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #d4af6a 0%, #c9975e 100%) !important;
        box-shadow: var(--shadow-lg) !important;
        transform: translateY(-2px) !important;
    }

    .stButton > button:active {
        background: linear-gradient(135deg, #c9975e 0%, #b8855a 100%) !important;
        transform: translateY(0) !important;
    }

    /* ===== حقول الإدخال ===== */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select,
    .stNumberInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: var(--bg-paper) !important;
        border: 2px solid var(--color-accent) !important;
        border-radius: 8px !important;
        color: var(--color-text-dark) !important;
        padding: 12px 16px !important;
        font-family: var(--font-primary) !important;
        font-size: 14px !important;
        transition: all 0.3s ease !important;
    }

    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus,
    .stNumberInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--accent-dark) !important;
        box-shadow: 0 0 0 4px rgba(224, 200, 150, 0.2) !important;
        outline: none !important;
    }

    /* ===== البطاقات والحاويات ===== */
    .stContainer {
        background-color: var(--bg-paper) !important;
        border-radius: 12px !important;
        padding: 20px !important;
        border: 2px solid var(--color-accent) !important;
        box-shadow: var(--shadow-sm) !important;
        margin-bottom: 16px !important;
    }

    /* ===== الإحصائيات والمقاييس ===== */
    [data-testid="stMetricValue"] {
        color: var(--color-accent) !important;
        font-weight: 800 !important;
        font-size: 32px !important;
    }

    [data-testid="stMetricLabel"] {
        color: var(--color-text-dark) !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }

    /* ===== الجداول والجداول البيانية ===== */
    .stDataFrame {
        background-color: var(--bg-paper) !important;
        border-radius: 12px !important;
        overflow: hidden !important;
        box-shadow: var(--shadow-sm) !important;
        border: 1px solid var(--border-color) !important;
    }

    .stDataFrame table {
        width: 100% !important;
    }

    .stDataFrame th {
        background: linear-gradient(135deg, #E0C896 0%, #d4af6a 100%) !important;
        color: var(--color-text-dark) !important;
        font-weight: 700 !important;
        padding: 14px !important;
        border-bottom: 2px solid var(--color-accent) !important;
        text-align: right !important;
    }

    .stDataFrame td {
        padding: 12px 14px !important;
        border-bottom: 1px solid var(--border-color) !important;
        color: var(--color-text-dark) !important;
    }

    .stDataFrame tr:hover {
        background-color: rgba(224, 200, 150, 0.1) !important;
    }

    /* ===== التبويبات ===== */
    .stTabs [data-baseweb="tab-list"] {
        border-bottom: 3px solid var(--color-accent) !important;
        background-color: var(--bg-cream) !important;
    }

    .stTabs [aria-selected="true"] {
        color: var(--color-accent) !important;
        border-bottom: 4px solid var(--color-accent) !important;
        font-weight: 700 !important;
    }

    .stTabs [aria-selected="false"] {
        color: var(--color-text-light) !important;
    }

    /* ===== الرسوم البيانية ===== */
    .plotly-graph-div {
        background-color: var(--bg-paper) !important;
        border-radius: 12px !important;
        padding: 16px !important;
        box-shadow: var(--shadow-sm) !important;
        border: 1px solid var(--border-color) !important;
    }

    /* ===== المنسقات ===== */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, rgba(224, 200, 150, 0.15) 0%, rgba(224, 200, 150, 0.08) 100%) !important;
        border-left: 4px solid var(--color-accent) !important;
        border-radius: 8px !important;
        padding: 12px 16px !important;
        font-weight: 600 !important;
        color: var(--color-dark) !important;
    }

    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, rgba(224, 200, 150, 0.2) 0%, rgba(224, 200, 150, 0.12) 100%) !important;
    }

    /* ===== رسائل الحالة ===== */
    .stSuccess {
        background-color: rgba(76, 175, 80, 0.1) !important;
        border-left: 4px solid #4caf50 !important;
        border-radius: 8px !important;
        padding: 12px !important;
    }

    .stWarning {
        background-color: rgba(255, 193, 7, 0.1) !important;
        border-left: 4px solid #ffc107 !important;
        border-radius: 8px !important;
        padding: 12px !important;
    }

    .stError {
        background-color: rgba(244, 67, 54, 0.1) !important;
        border-left: 4px solid #f44336 !important;
        border-radius: 8px !important;
        padding: 12px !important;
    }

    .stInfo {
        background-color: rgba(224, 200, 150, 0.15) !important;
        border-left: 4px solid var(--color-accent) !important;
        border-radius: 8px !important;
        padding: 12px !important;
    }

    /* ===== النصوص والروابط ===== */
    p, span, label {
        color: var(--color-text-dark) !important;
        line-height: 1.6 !important;
    }

    a {
        color: var(--color-accent) !important;
        text-decoration: none !important;
        font-weight: 600 !important;
        transition: color 0.3s ease !important;
    }

    a:hover {
        color: var(--accent-dark) !important;
        text-decoration: underline !important;
    }

    /* ===== الخطوط الفاصلة ===== */
    hr {
        border: none !important;
        border-top: 2px solid var(--color-accent) !important;
        margin: 24px 0 !important;
    }

    /* ===== المربعات الاختيارية والراديو ===== */
    .stCheckbox, .stRadio {
        padding: 8px 12px !important;
        background-color: transparent !important;
        border-radius: 8px !important;
        transition: background-color 0.3s ease !important;
    }

    .stCheckbox:hover, .stRadio:hover {
        background-color: rgba(224, 200, 150, 0.1) !important;
    }

    /* ===== الرسوم المتحركة ===== */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .stApp { animation: fadeIn 0.4s ease-out !important; }

    /* ===== Responsive ===== */
    @media (max-width: 768px) {
        h1 { font-size: 28px !important; }
        h2 { font-size: 22px !important; }
        .stContainer { padding: 16px !important; }
    }
    </style>
""", unsafe_allow_html=True)

# ===== تطبيق الواجهة الرئيسية =====
st.title("⚡ تطبيق المعاينات الكهربائية")
st.markdown("---")

# الشريط الجانبي
with st.sidebar:
    st.markdown("## 🔧 القائمة الرئيسية")
    page = st.radio(
        "اختر الصفحة:",
        ["لوحة التحكم", "المشاريع", "المعاينات", "التقارير", "الإعدادات"]
    )

# لوحة التحكم الرئيسية
if page == "لوحة التحكم":
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("المشاريع النشطة", "12", "↑ 2")
    with col2:
        st.metric("المعاينات المكتملة", "34", "↑ 5")
    with col3:
        st.metric("التقارير المعلقة", "8", "↓ 1")
    with col4:
        st.metric("معدل الإنجاز", "92%", "↑ 3%")

    st.markdown("---")
    st.markdown("### 📊 الإحصائيات")

    # رسم بياني تجريبي
    data = {
        "الشهر": ["يناير", "فبراير", "مارس", "أبريل", "مايو"],
        "المعاينات": [10, 15, 12, 18, 22]
    }
    df = pd.DataFrame(data)

    fig = px.bar(df, x="الشهر", y="المعاينات", color="المعاينات",
                 color_continuous_scale=["#E0C896", "#d4af6a", "#5C4A3A"])
    st.plotly_chart(fig, use_container_width=True)

elif page == "المشاريع":
    st.markdown("### 📁 إدارة المشاريع")
    st.info("📌 سيتم إضافة إدارة المشاريع قريباً")

elif page == "المعاينات":
    st.markdown("### 🔍 سجل المعاينات")
    st.info("📌 سيتم إضافة سجل المعاينات قريباً")

elif page == "التقارير":
    st.markdown("### 📋 التقارير")
    st.info("📌 سيتم إضافة إنشاء التقارير قريباً")

elif page == "الإعدادات":
    st.markdown("### ⚙️ الإعدادات")
    st.info("📌 سيتم إضافة الإعدادات قريباً")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: var(--color-text-light); font-size: 12px;">
    © 2026 تطبيق المعاينات الكهربائية | جميع الحقوق محفوظة
</div>
""", unsafe_allow_html=True)
