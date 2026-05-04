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

# Custom CSS - Gamma Design System
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* ===== GAMMA DESIGN SYSTEM ===== */
    :root {
        /* Colors */
        --color-gamma-blue: #002253;
        --color-cloud-white: #ffffff;
        --color-coal-black: #000000;
        --gradient-sky: linear-gradient(to top, rgb(255, 255, 255), rgb(198, 230, 250));

        /* Typography */
        --font-ppmori: 'Inter', 'Roboto', ui-sans-serif, system-ui, sans-serif;
        --font-esbuild: 'Roboto', ui-sans-serif, system-ui, sans-serif;

        /* Spacing */
        --spacing-8: 8px;
        --spacing-20: 20px;
        --spacing-32: 32px;

        /* Border Radius */
        --radius-cards: 12px;

        /* Shadows */
        --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.08);
        --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.08);
    }

    /* عام */
    body {
        direction: rtl;
        text-align: right;
        background: var(--gradient-sky) !important;
        font-family: var(--font-ppmori);
    }

    .main {
        background: var(--gradient-sky);
        padding: var(--spacing-32);
    }

    /* Cards */
    .stat-card {
        background: var(--color-cloud-white);
        padding: var(--spacing-32);
        border-radius: var(--radius-cards);
        border-left: 3px solid var(--color-gamma-blue);
        box-shadow: var(--shadow-md);
        direction: rtl;
    }

    .stat-value {
        font-size: 32px;
        font-weight: bold;
        color: #333;

    /* استيراد الخط العربي الجميل */
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');

    /* Sidebar AI Chat */
    .sidebar-chat-container {
        background: linear-gradient(135deg, #F0F5FF 0%, #F5F7FA 100%);
        border: 2px solid #D4AF37;
        border-radius: 15px;
        padding: 12px;
        margin-top: 16px;
        font-family: 'Tajawal', sans-serif;
        direction: rtl;
    }

    .sidebar-chat-header {
        background: linear-gradient(135deg, #0066CC 0%, #004499 100%);
        color: white;
        padding: 10px 12px;
        border-radius: 10px;
        text-align: center;
        font-weight: 700;
        font-size: 14px;
        margin-bottom: 10px;
        box-shadow: 0 2px 8px rgba(0, 102, 204, 0.2);
    }

    .sidebar-chat-messages {
        background: white;
        border-radius: 10px;
        padding: 10px;
        max-height: 280px;
        overflow-y: auto;
        margin-bottom: 10px;
        direction: rtl;
    }

    .sidebar-chat-messages::-webkit-scrollbar {
        width: 4px;
    }

    .sidebar-chat-messages::-webkit-scrollbar-track {
        background: transparent;
    }

    .sidebar-chat-messages::-webkit-scrollbar-thumb {
        background: #D4AF37;
        border-radius: 2px;
    }

    .sidebar-message {
        margin: 6px 0;
        padding: 8px 10px;
        border-radius: 8px;
        font-size: 12px;
        line-height: 1.4;
        animation: fadeIn 0.3s ease-in;
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(3px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .sidebar-user-message {
        background: linear-gradient(135deg, #0066CC 0%, #0052A3 100%);
        color: white;
        text-align: right;
        border-radius: 8px 2px 8px 8px;
        margin-left: 20px;
        font-weight: 500;
    }

    .sidebar-bot-message {
        background: #E8F0FE;
        color: #1a1a2e;
        text-align: right;
        border-right: 3px solid #D4AF37;
        border-radius: 2px 8px 8px 8px;
        margin-right: 20px;
    }

    .sidebar-chat-input-area {
        display: flex;
        gap: 6px;
        align-items: center;
    }

    .sidebar-chat-input-area input {
        flex: 1;
        border: 2px solid #E0E0E0;
        border-radius: 20px;
        padding: 8px 12px;
        font-size: 12px;
        direction: rtl;
        font-family: 'Tajawal', sans-serif;
        background: white;
        transition: all 0.3s ease;
    }

    .sidebar-chat-input-area input:focus {
        outline: none;
        border-color: #0066CC;
        box-shadow: 0 0 0 2px rgba(0, 102, 204, 0.1);
    }

    .sidebar-chat-input-area input::placeholder {
        color: #999;
    }

    .sidebar-chat-input-area button {
        background: linear-gradient(135deg, #0066CC 0%, #004499 100%);
        color: white;
        border: none;
        border-radius: 50%;
        width: 32px;
        height: 32px;
        cursor: pointer;
        font-size: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s ease;
        box-shadow: 0 2px 6px rgba(0, 102, 204, 0.3);
        flex-shrink: 0;
    }

    .sidebar-chat-input-area button:hover {
        background: linear-gradient(135deg, #004499 0%, #003366 100%);
        transform: scale(1.05);
        box-shadow: 0 3px 8px rgba(0, 102, 204, 0.4);
    }

    .sidebar-chat-input-area button:active {
        transform: scale(0.95);
    }
    }

    .stat-label {
        font-size: 12px;
        color: #666;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)


# Initialize Session State
if 'page' not in st.session_state:
    st.session_state.page = '📊 Dashboard'

if 'chat_messages' not in st.session_state:
    st.session_state.chat_messages = []

if 'ai_chat_visible' not in st.session_state:
    st.session_state.ai_chat_visible = True

if 'project_data' not in st.session_state:
    st.session_state.project_data = {
        'name': 'عمارة سكنية حي الرقعة',
        'type': 'سكني',
        'location': 'حي الرقعة - الكويت',
        'contractor': 'شركة البناء الحديثة',
        'start_date': '2026-01-15',
        'end_date': '2026-06-30',
    }

if 'pricing_data' not in st.session_state:
    st.session_state.pricing_data = {
        'contract_value': 100000,
        'currency': 'د.ك',
        'first_payment': 30,
        'final_payment': 10,
    }

if 'criteria_data' not in st.session_state:
    st.session_state.criteria_data = {
        'daily_penalty': 0.5,
        'max_penalty': 10,
        'quality_bonus': 1.0,
    }

# نظام RAG للـ Chatbot الذكي
if CHATBOT_AVAILABLE and 'rag_system' not in st.session_state:
    try:
        st.session_state.rag_system = create_rag_system()
    except Exception as e:
        st.session_state.rag_system = None
        st.warning(f"⚠️ تعذر تفعيل الـ Chatbot الذكي: {str(e)}")
else:
    if 'rag_system' not in st.session_state:
        st.session_state.rag_system = None

# Header
# ===============================
# Helper Functions
# ===============================

def extract_text_from_file(file) -> str:
    """استخراج النص من الملفات بأنواعها المختلفة"""
    try:
        file_type = file.name.lower().split('.')[-1]

        if file_type == 'pdf':
            try:
                import PyPDF2
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() or ""
                return text
            except Exception as e:
                st.warning(f"خطأ في قراءة PDF: {str(e)}")
                return ""

        elif file_type in ['docx', 'doc']:
            try:
                from docx import Document
                doc = Document(file)
                text = "\n".join([p.text for p in doc.paragraphs])
                return text
            except Exception as e:
                st.warning(f"خطأ في قراءة Word: {str(e)}")
                return ""

        elif file_type in ['xlsx', 'xls']:
            try:
                import openpyxl
                import pandas as pd
                df = pd.read_excel(file, sheet_name=None)
                text = ""
                for sheet_name, sheet_df in df.items():
                    text += f"\n=== {sheet_name} ===\n"
                    text += sheet_df.to_string()
                return text
            except Exception as e:
                st.warning(f"خطأ في قراءة Excel: {str(e)}")
                return ""

        elif file_type == 'txt':
            try:
                content = file.read()
                return content.decode('utf-8', errors='ignore')
            except Exception as e:
                st.warning(f"خطأ في قراءة TXT: {str(e)}")
                return ""

        elif file_type == 'csv':
            try:
                import pandas as pd
                df = pd.read_csv(file)
                return df.to_string()
            except Exception as e:
                st.warning(f"خطأ في قراءة CSV: {str(e)}")
                return ""

        else:
            return ""

    except Exception as e:
        st.warning(f"خطأ في معالجة الملف: {str(e)}")
        return ""


# AI Chat Functions
def search_documents(query, limit=5):
    """البحث في المستندات المحفوظة"""
    try:
        if 'documents' not in st.session_state:
            return []

        results = []
        query_lower = query.lower()

        for doc in st.session_state.get('documents', []):
            if isinstance(doc, dict) and 'content' in doc:
                content = doc.get('content', '').lower()
                if query_lower in content:
                    idx = content.find(query_lower)
                    start = max(0, idx - 80)
                    end = min(len(doc['content']), idx + len(query) + 80)
                    snippet = doc['content'][start:end].strip()
                    results.append({
                        'source': doc.get('filename', 'مستند'),
                        'snippet': f"...{snippet}..."
                    })

        return results[:limit]
    except:
        return []

def get_ai_response(user_query):
    """الحصول على إجابة ذكية بناء على المستندات"""
    search_results = search_documents(user_query)

    # إذا وجدنا نتائج
    if search_results:
        response = "📚 وجدت معلومات:\n\n"
        for result in search_results:
            response += f"**من {result['source']}:**\n{result['snippet']}\n\n"
        return response

    # إجابات عامة عن المشروع
    if any(word in user_query for word in ['المشروع', 'اسم', 'الموقع', 'المقاول']):
        project = st.session_state.get('project_data', {})
        return f"""📋 بيانات المشروع:
- **الاسم:** {project.get('name', 'غير محدد')}
- **النوع:** {project.get('type', 'غير محدد')}
- **الموقع:** {project.get('location', 'غير محدد')}
- **المقاول:** {project.get('contractor', 'غير محدد')}"""

    return "🤔 أعتذر، لم أجد معلومات حول هذا. يمكنك رفع الملفات والمستندات للحصول على إجابات أفضل!"

col1, col2 = st.columns([0.8, 0.2])
with col1:
    st.title("⚡ تطبيق المعاينات الكهربائية - الإصدار 3.0")
with col2:
    st.write(f"📅 {datetime.now().strftime('%Y-%m-%d')}")

st.divider()

# Sidebar Navigation
with st.sidebar:
    st.write("### 📋 القائمة الرئيسية")
    st.write("---")

    pages = {
        '📊 Dashboard': 'dashboard',
        '📝 إدخال البيانات': 'input',
        '📚 المصادر': 'sources',
        '📈 التحليل': 'analysis',
        '📄 التقارير': 'reports',
    }

    for page_name, page_key in pages.items():
        if st.button(page_name, key=page_key, use_container_width=True):
            st.session_state.page = page_name

    st.write("---")
    st.write("### ℹ️ معلومات")
    st.write(f"**المشروع**: {st.session_state.project_data['name']}")
    st.write(f"**الموقع**: {st.session_state.project_data['location']}")
    st.write(f"**القيمة**: {st.session_state.pricing_data['contract_value']:,} {st.session_state.pricing_data['currency']}")

    # Sidebar AI Chat
    st.write("---")
    st.write("### 🤖 مساعدك الذكي")

    # عرض حالة الـ Chatbot
    if st.session_state.rag_system:
        st.info("✅ الـ Chatbot جاهز", icon="✨")
        doc_summary = st.session_state.rag_system.get_document_summary()
        if "لا توجد" not in doc_summary:
            with st.expander("📁 الملفات المحملة"):
                st.caption(doc_summary)
    else:
        st.warning("⚠️ الـ Chatbot غير متاح - تحقق من API Key")

    # نافذة الدردشة
    chat_container = st.container(height=300, border=True)

    if st.session_state.rag_system and st.session_state.rag_system.conversation_history:
        with chat_container:
            for msg in st.session_state.rag_system.conversation_history:
                if msg["role"] == "user":
                    st.chat_message("user").write(msg["content"].split("السياق من")[0].split("السؤال:")[-1].strip()[:100])
                else:
                    st.chat_message("assistant").write(msg["content"][:150] + "...")
    else:
        with chat_container:
            st.caption("لا توجد رسائل بعد")

    # حقل الإدخال
    if st.session_state.rag_system:
        user_input = st.text_input(
            "اسأل عن المشروع أو الملفات:",
            placeholder="أدخل سؤالك...",
            key="sidebar_chat_input"
        )

        if user_input:
            with st.spinner("جاري المعالجة..."):
                try:
                    response, sources = st.session_state.rag_system.chat(user_input)

                    # عرض الإجابة
                    st.chat_message("assistant").write(response)

                    # عرض المصادر إذا وجدت
                    if sources:
                        st.caption(f"📚 المصادر: {', '.join(sources)}")
                except Exception as e:
                    st.error(f"❌ خطأ: {str(e)}")
    else:
        st.warning("⚠️ يرجى تعيين ANTHROPIC_API_KEY في ملف .env")

# ===============================
# PAGE 1: DASHBOARD
# ===============================
if st.session_state.page == '📊 Dashboard':
    st.header("📊 لوحة التحكم والإحصائيات")

    # Stats Cards
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "✅ الأعمال المنفذة",
            "38",
            "من أصل 45 نقطة (84%)",
            delta_color="off"
        )

    with col2:
        st.metric(
            "⚠️ الأعمال الناقصة",
            "5",
            "11% من الإجمالي",
            delta_color="off"
        )

    with col3:
        st.metric(
            "❌ الأعمال المعيبة",
            "2",
            "4% تحتاج إصلاح",
            delta_color="off"
        )

    with col4:
        st.metric(
            "💰 المستحق الحالي",
            "67,500",
            "دينار كويتي",
            delta_color="off"
        )

    st.divider()

    # Charts
    col1, col2 = st.columns(2)

    # Chart 1: Bar Chart (Work Types)
    with col1:
        st.subheader("📊 تقدم الأعمال حسب النوع")

        work_data = {
            'نوع العمل': ['نقاط إنارة', 'نقاط قوى', 'لوحات فرعية', 'أسلاك تمديد', 'نظام التأريص'],
            'المخطط': [45, 30, 3, 500, 100],
            'المنفذ': [38, 30, 2, 450, 100],
        }
        df_work = pd.DataFrame(work_data)

        fig1 = go.Figure(data=[
            go.Bar(name='المخطط', x=df_work['نوع العمل'], y=df_work['المخطط'], marker_color='#D4AF37'),
            go.Bar(name='المنفذ', x=df_work['نوع العمل'], y=df_work['المنفذ'], marker_color='#0066CC')
        ])
        fig1.update_layout(
            barmode='group',
            hovermode='x unified',
            showlegend=True,
            height=400,
            margin=dict(l=0, r=0, t=0, b=0)
        )
        st.plotly_chart(fig1, use_container_width=True)

    # Chart 2: Pie Chart (Status Distribution)
    with col2:
        st.subheader("📈 توزيع حالة الأعمال")

        status_data = {
            'الحالة': ['✅ مكتمل', '⚠️ ناقص', '❌ معيب'],
            'النسبة': [84, 11, 5],
            'اللون': ['#27AE60', '#F39C12', '#E74C3C']
        }

        fig2 = go.Figure(data=[go.Pie(
            labels=status_data['الحالة'],
            values=status_data['النسبة'],
            marker=dict(colors=status_data['اللون']),
            textposition='inside',
            textinfo='label+percent'
        )])
        fig2.update_layout(
            height=400,
            margin=dict(l=0, r=0, t=0, b=0)
        )
        st.plotly_chart(fig2, use_container_width=True)

    # Chart 3: Line Chart (Timeline)
    st.subheader("📉 تطور الإنجاز على الوقت")

    timeline_data = {
        'الأسبوع': ['الأسبوع 1', 'الأسبوع 2', 'الأسبوع 3', 'الأسبوع 4', 'الأسبوع 5', 'الأسبوع 6'],
        'النسبة': [10, 25, 40, 60, 75, 87]
    }
    df_timeline = pd.DataFrame(timeline_data)

    fig3 = go.Figure(data=[go.Scatter(
        x=df_timeline['الأسبوع'],
        y=df_timeline['النسبة'],
        mode='lines+markers',
        fill='tozeroy',
        line=dict(color='#0066CC', width=3),
        marker=dict(size=10, color='#D4AF37', line=dict(color='white', width=2)),
        hovertemplate='<b>%{x}</b><br>إنجاز: %{y}%<extra></extra>'
    )])
    fig3.update_layout(
        xaxis_title='الفترة الزمنية',
        yaxis_title='نسبة الإنجاز (%)',
        hovermode='x unified',
        height=400,
        yaxis=dict(range=[0, 100])
    )
    st.plotly_chart(fig3, use_container_width=True)

    st.divider()

    # Summary Table
    st.subheader("📋 ملخص الأعمال التفصيلي")

    summary_data = {
        'نوع العمل': ['نقاط الإنارة', 'نقاط القوى', 'اللوحات الفرعية', 'تمديدات البايبات', 'نظام التأريص'],
        'المخطط': [45, 30, 3, '500 م', 'كامل'],
        'المنفذ': [38, 30, 2, '450 م', 'كامل'],
        'النسبة': ['84%', '100%', '67%', '90%', '100%'],
        'الناقص': [5, 0, 1, '50 م', 0],
        'المعيب': [2, 0, 0, 0, 0],
        'الحالة': ['متقدم', 'مكتمل', 'قيد العمل', 'متقدم', 'مكتمل']
    }
    df_summary = pd.DataFrame(summary_data)

    st.dataframe(df_summary, use_container_width=True, hide_index=True)

# ===============================
# PAGE 2: MANUAL INPUT
# ===============================
elif st.session_state.page == '📝 إدخال البيانات':
    st.header("📝 إدخال البيانات")

    tabs = st.tabs(["بيانات المشروع", "الأسعار والتكاليف", "معايير التقييم", "الصيغ الحسابية"])

    # Tab 1: Project Data
    with tabs[0]:
        st.subheader("بيانات المشروع الأساسية")

        col1, col2 = st.columns(2)
        with col1:
            st.session_state.project_data['name'] = st.text_input(
                "📌 اسم المشروع",
                value=st.session_state.project_data['name']
            )
            st.session_state.project_data['location'] = st.text_input(
                "📍 الموقع",
                value=st.session_state.project_data['location']
            )
            st.session_state.project_data['start_date'] = st.date_input(
                "📅 تاريخ البدء",
                value=pd.to_datetime(st.session_state.project_data['start_date']).date()
            )

        with col2:
            st.session_state.project_data['type'] = st.selectbox(
                "🏢 نوع المشروع",
                ['سكني', 'تجاري', 'صناعي'],
                index=['سكني', 'تجاري', 'صناعي'].index(st.session_state.project_data['type'])
            )
            st.session_state.project_data['contractor'] = st.text_input(
                "🏗️ المقاول الرئيسي",
                value=st.session_state.project_data['contractor']
            )
            st.session_state.project_data['end_date'] = st.date_input(
                "🏁 تاريخ الانتهاء المتوقع",
                value=pd.to_datetime(st.session_state.project_data['end_date']).date()
            )

        notes = st.text_area("📝 ملاحظات عامة", height=100)

        if st.button("💾 حفظ بيانات المشروع", key="save_project"):
            st.success("✅ تم حفظ بيانات المشروع بنجاح!")

    # Tab 2: Pricing
    with tabs[1]:
        st.subheader("الأسعار والشروط المالية")

        col1, col2 = st.columns(2)
        with col1:
            st.session_state.pricing_data['contract_value'] = st.number_input(
                "💰 قيمة العقد الإجمالية",
                value=st.session_state.pricing_data['contract_value'],
                min_value=0
            )
            st.session_state.pricing_data['first_payment'] = st.number_input(
                "🎁 الدفعة الأولى (%)",
                value=st.session_state.pricing_data['first_payment'],
                min_value=0,
                max_value=100
            )

        with col2:
            st.session_state.pricing_data['currency'] = st.selectbox(
                "💵 العملة",
                ['د.ك (دينار كويتي)', 'ر.ع (ريال سعودي)', '$ (دولار أمريكي)'],
                index=0
            )
            st.session_state.pricing_data['final_payment'] = st.number_input(
                "✅ الدفعة الختامية (%)",
                value=st.session_state.pricing_data['final_payment'],
                min_value=0,
                max_value=100
            )

        payment_terms = st.text_area("📊 شروط الدفع الدورية", height=100)

        if st.button("💾 حفظ بيانات الأسعار", key="save_pricing"):
            st.success("✅ تم حفظ بيانات الأسعار بنجاح!")

    # Tab 3: Criteria
    with tabs[2]:
        st.subheader("معايير التقييم والجودة")

        col1, col2 = st.columns(2)
        with col1:
            st.session_state.criteria_data['daily_penalty'] = st.number_input(
                "📉 نسبة الغرامات اليومية (%)",
                value=st.session_state.criteria_data['daily_penalty'],
                min_value=0.0,
                max_value=100.0,
                step=0.1
            )
            st.session_state.criteria_data['quality_bonus'] = st.number_input(
                "⭐ حافز الجودة (%)",
                value=st.session_state.criteria_data['quality_bonus'],
                min_value=0.0,
                max_value=100.0,
                step=0.1
            )

        with col2:
            st.session_state.criteria_data['max_penalty'] = st.number_input(
                "🛑 أقصى غرامات (%)",
                value=st.session_state.criteria_data['max_penalty'],
                min_value=0,
                max_value=100
            )
            acceptance_rate = st.number_input(
                "⚠️ نسبة الأعمال الناقصة المقبولة (%)",
                min_value=0,
                max_value=100,
                value=5
            )

        if st.button("💾 حفظ معايير التقييم", key="save_criteria"):
            st.success("✅ تم حفظ معايير التقييم بنجاح!")

    # Tab 4: Formulas
    with tabs[3]:
        st.subheader("الصيغ الحسابية المتقدمة")

        st.info("ℹ️ الصيغ الحسابية محددة مسبقاً وتُطبق تلقائياً على جميع الحسابات")

        st.write("**🔢 صيغة حساب المستحق الأساسي:**")
        st.code("قيمة العقد × نسبة الإنجاز", language="text")

        st.write("**📊 صيغة حساب الغرامات:**")
        st.code("المستحق × (نسبة الغرامة اليومية × عدد أيام التأخير)", language="text")

        st.write("**💎 صيغة حساب الحوافز:**")
        st.code("المستحق × (نسبة الجودة + حافز الجودة)", language="text")

# ===============================
# PAGE 3: SOURCES
# ===============================
elif st.session_state.page == '📚 المصادر':
    st.header("📚 إدارة المصادر والملفات")

    st.subheader("📤 رفع المصادر والملفات")

    uploaded_files = st.file_uploader(
        "اختر الملفات (PDF, Excel, Word, صور)",
        accept_multiple_files=True,
        type=['pdf', 'xlsx', 'docx', 'txt', 'csv', 'png', 'jpg', 'jpeg']
    )

    if uploaded_files:
        st.success(f"✅ تم رفع {len(uploaded_files)} ملف(ات)")

        st.subheader("📋 الملفات المرفوعة")

        # معالجة الملفات وإضافتها إلى نظام RAG
        if st.session_state.rag_system:
            for file in uploaded_files:
                try:
                    content = extract_text_from_file(file)
                    if content:
                        st.session_state.rag_system.add_document(file.name, content)
                except Exception as e:
                    st.warning(f"⚠️ خطأ في معالجة {file.name}: {str(e)}")

        for file in uploaded_files:
            col1, col2 = st.columns([0.9, 0.1])
            with col1:
                st.write(f"📄 **{file.name}**")
                st.caption(f"الحجم: {file.size/1024:.1f} KB | التاريخ: {datetime.now().strftime('%Y-%m-%d')}")
            with col2:
                if st.button("حذف", key=f"delete_{file.name}"):
                    st.info("تم حذف الملف")
    else:
        # Default Files
        st.subheader("📋 الملفات المرفوعة")

        default_files = [
            {"name": "معايير_MEW.pdf", "size": 1.2, "date": "2026-05-01"},
            {"name": "جدول_الأسعار.xlsx", "size": 0.45, "date": "2026-05-02"},
            {"name": "الشروط_الحقوقية.pdf", "size": 2.1, "date": "2026-04-28"},
        ]

        for file in default_files:
            col1, col2 = st.columns([0.9, 0.1])
            with col1:
                st.write(f"📄 **{file['name']}**")
                st.caption(f"الحجم: {file['size']} MB | التاريخ: {file['date']}")
            with col2:
                if st.button("حذف", key=f"delete_{file['name']}"):
                    st.info("تم حذف الملف")

# ===============================
# PAGE 4: ANALYSIS
# ===============================
elif st.session_state.page == '📈 التحليل':
    st.header("📈 التحليل والمقارنة")

    st.subheader("📊 جدول المقارنة التفصيلي")

    analysis_data = {
        'بند العمل': ['نقاط إنارة داخلية', 'نقاط قوى مفردة', 'لوحات فرعية', 'أسلاك تمديد', 'نظام تأريص'],
        'الوحدة': ['نقطة', 'نقطة', 'لوحة', 'متر', 'كامل'],
        'المخطط': [45, 30, 3, 500, '✓'],
        'المنفذ': [38, 30, 2, 450, '✓'],
        'النسبة': ['84%', '100%', '67%', '90%', '100%'],
        'الفرق': ['-7', '0', '-1', '-50', '0'],
        'ملاحظات': ['قيد التركيب', '✅ مكتملة', 'لم تصل الأجهزة', 'قيد التمديد', '✅ مكتمل'],
    }
    df_analysis = pd.DataFrame(analysis_data)
    st.dataframe(df_analysis, use_container_width=True, hide_index=True)

    st.divider()
    st.subheader("💡 التوصيات")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**✓ الأمور الإيجابية:**")
        st.write("✅ الإنجاز الكلي وصل 87% وهو متقدماً")
        st.write("✅ نقاط القوى اكتملت بنسبة 100%")
        st.write("✅ نظام التأريص مكتمل حسب المعايير")

    with col2:
        st.write("**⚠️ النقاط التي تحتاج متابعة:**")
        st.write("📌 إكمال تركيب نقاط الإنارة المتبقية (7 نقاط)")
        st.write("📌 استلام وتركيب اللوحة الفرعية الثالثة")
        st.write("📌 إكمال تمديد الأسلاك المتبقية (50 متر)")

# ===============================
# PAGE 5: REPORTS
# ===============================
elif st.session_state.page == '📄 التقارير':
    st.header("📄 إنشاء التقارير")

    st.subheader("🖨️ خيارات التقرير")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📊 تقرير شامل", use_container_width=True):
            st.info("جداول + رسوم بيانية + توصيات")

    with col2:
        if st.button("📝 تقرير موجز", use_container_width=True):
            st.info("البيانات الأساسية فقط")

    with col3:
        if st.button("💰 تقرير مالي", use_container_width=True):
            st.info("الحسابات والدفعات فقط")

    st.divider()

    st.subheader("✓ محتويات التقرير")

    col1, col2 = st.columns(2)

    with col1:
        st.checkbox("🏗️ بيانات المشروع", value=True)
        st.checkbox("📈 الرسوم البيانية", value=True)
        st.checkbox("💡 التوصيات", value=True)

    with col2:
        st.checkbox("📊 جداول المقارنة", value=True)
        st.checkbox("💰 حسابات الدفعات", value=True)
        st.checkbox("🔐 ملخص قانوني", value=False)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📥 تحميل PDF", use_container_width=True, key="download_pdf"):
            st.success("✅ يتم إنشاء التقرير PDF... (قريباً)")

    with col2:
        if st.button("🖨️ طباعة", use_container_width=True, key="print_report"):
            st.info("ℹ️ استخدم Ctrl+P في متصفحك للطباعة")

# Footer
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.caption("⚡ تطبيق المعاينات الكهربائية الإصدار 3.0")

with col2:
    st.caption("🔒 معايير الكويت الرسمية (MEW, BS, IEC)")

with col3:
    st.caption(f"📅 آخر تحديث: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# Sidebar Chat - استُبدل بـ Streamlit Chat Implementation
