import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import json

# Page Configuration
st.set_page_config(
    page_title="تطبيق المعاينات الكهربائية",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    :root {
        --primary-blue: #0066CC;
        --gold-warm: #D4AF37;
        --beige-light: #F5E6D3;
        --success: #27AE60;
        --warning: #F39C12;
        --danger: #E74C3C;
    }

    /* عام */
    body {
        direction: rtl;
        text-align: right;
    }

    .main {
        padding: 20px;
    }

    /* Cards */
    .stat-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #D4AF37;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }

    .stat-value {
        font-size: 32px;
        font-weight: bold;
        color: #333;
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
        'quality_bonus': 1,
    }

# Header
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
