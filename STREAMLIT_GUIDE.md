# 🚀 دليل تشغيل التطبيق على Streamlit

## ⚡ ماذا هو Streamlit؟

```
Streamlit هو إطار عمل Python لإنشاء تطبيقات ويب بسيطة وقوية:

✅ مميزاته:
├─ لا تحتاج HTML/CSS/JavaScript
├─ كود Python بسيط فقط
├─ تفاعلي ومرن جداً
├─ سهل الرفع والنشر
├─ مجاني تماماً
└─ يعمل على الويب والجوال
```

---

## 📋 الخطوة 1: التنصيب

### على Windows:

```bash
# 1. افتح Command Prompt أو PowerShell
# 2. اكتب:

pip install -r requirements.txt

# أو اكتب مباشرة:

pip install streamlit pandas plotly
```

### على Mac/Linux:

```bash
# 1. افتح Terminal
# 2. اكتب:

pip3 install -r requirements.txt

# أو اكتب مباشرة:

pip3 install streamlit pandas plotly
```

### التحقق من التثبيت:

```bash
streamlit --version
```

---

## 🎯 الخطوة 2: تشغيل التطبيق محلياً

### الطريقة الأولى: من نفس المجلد

```bash
# 1. افتح Terminal/Command Prompt
# 2. انتقل للمجلد:

cd /Users/fahadalkandri/Documents/Claude/Projects/مهندس\ كهربائي\ مساعد/

# 3. اكتب:

streamlit run app.py

# 4. سيفتح متصفح تلقائياً على:
# http://localhost:8501
```

### الطريقة الثانية: من أي مكان

```bash
streamlit run /Users/fahadalkandri/Documents/Claude/Projects/مهندس\ كهربائي\ مساعد/app.py
```

### النتيجة:

```
✅ التطبيق يعمل الآن!

الرابط المحلي: http://localhost:8501

علامات في Terminal:
├─ Local URL: http://localhost:8501
├─ Network URL: http://192.168.x.x:8501
└─ External URL: سيظهر إذا كان هناك اتصال
```

---

## 📱 الخطوة 3: الوصول من الهاتف

### عندما يعمل التطبيق:

```bash
# في Terminal ستشاهد:

Local URL: http://localhost:8501
Network URL: http://192.168.1.100:8501  ← انسخ هذا
```

### على هاتفك:

```
1️⃣ اتأكد من اتصال الهاتف بنفس شبكة WiFi
2️⃣ افتح متصفح (Chrome/Safari)
3️⃣ اكتب الرابط: http://192.168.1.100:8501
4️⃣ Enter → ستجد التطبيق!
```

---

## ☁️ الخطوة 4: رفع على Streamlit Cloud (مجاني)

### الطريقة الأسهل والأفضل:

```
1️⃣ أنشئ حساب على:
   https://streamlit.io/cloud

2️⃣ اختر GitHub (أسهل طريقة):
   ├─ وصل حسابك GitHub
   ├─ اختر Repository
   └─ اختر Branch و File

3️⃣ Streamlit سينشر التطبيق تلقائياً:
   ├─ URL متاح عالعلن
   ├─ يعمل 24/7
   └─ مجاني تماماً

4️⃣ الرابط سيكون مثلاً:
   https://your-app-name.streamlit.app
```

### خطوات التفصيلية لـ GitHub:

#### الخطوة أ: أرسل الملفات لـ GitHub

```bash
# 1. أنشئ Repository جديد:
#    https://github.com/new

# 2. الاسم: electrical-inspection-app

# 3. جعله Public ومع README

# 4. انسخ الملفات للمجلد:
#    ├─ app.py
#    ├─ requirements.txt
#    └─ README.md (اختياري)

# 5. رفع الملفات:

git add .
git commit -m "Initial commit"
git push origin main
```

#### الخطوة ب: ربط مع Streamlit Cloud

```
1. اذهب https://share.streamlit.io
2. اختر GitHub account
3. اختر Repository: electrical-inspection-app
4. اختر Branch: main
5. اختر File: app.py
6. Click "Deploy"

الانتظار: 2-3 دقائق
النتيجة: URL عام يعمل!
```

---

## 🌐 خيارات الرفع الأخرى

### 1. Heroku (مجاني مع حدود):

```
الخطوات:
├─ أنشئ حساب Heroku
├─ أنشئ app جديد
├─ اربط مع GitHub
├─ Deploy branch
└─ سيعمل تلقائياً

الرابط: https://your-app.herokuapp.com
```

### 2. Render (مجاني جداً):

```
الخطوات:
├─ اذهب render.com
├─ أنشئ Web Service جديد
├─ اختر GitHub Repository
├─ أدخل: streamlit run app.py
└─ Deploy

الرابط: https://your-app.onrender.com
```

### 3. Replit (الأسهل):

```
الخطوات:
├─ اذهب replit.com
├─ أنشئ Repl جديد (Python)
├─ انسخ app.py
├─ أضيف requirements.txt
├─ اضغط Run
└─ سيعمل فوراً

الرابط: https://your-repl.replit.dev
```

---

## 🔧 كود Streamlit شرح سريع

### البنية الأساسية:

```python
import streamlit as st

# 1. العنوان
st.title("العنوان الرئيسي")

# 2. النص
st.write("نص عادي")

# 3. الأزرار
if st.button("اضغط هنا"):
    st.success("تم!")

# 4. المدخلات
name = st.text_input("اسمك:")
age = st.number_input("عمرك:")

# 5. الرسوم البيانية
import plotly.graph_objects as go
fig = go.Figure(data=[...])
st.plotly_chart(fig)

# 6. الجداول
import pandas as pd
df = pd.DataFrame({...})
st.dataframe(df)

# 7. التخزين المؤقت
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# 8. الأعمدة والصفوف
col1, col2 = st.columns(2)
with col1:
    st.write("عمود 1")
with col2:
    st.write("عمود 2")

# 9. التبويبات
tabs = st.tabs(["التبويب 1", "التبويب 2"])
with tabs[0]:
    st.write("محتوى التبويب 1")
```

---

## 📊 ملف app.py الحالي يحتوي على:

### المميزات المضافة:

```
✅ 5 صفحات كاملة
├─ Dashboard (مع رسوم بيانية Plotly)
├─ Manual Input (نماذج و Text Input)
├─ Sources (رفع ملفات)
├─ Analysis (جداول مقارنة)
└─ Reports (اختيارات التقارير)

✅ 4 مخططات بيانية:
├─ Bar Chart (مقارنة الأعمال)
├─ Pie Chart (توزيع الحالات)
├─ Line Chart (تطور الإنجاز)
└─ وصول الهاتف على Radar Chart (قريباً)

✅ تخزين بيانات:
├─ Session State للبيانات المؤقتة
├─ حفظ المشروع والأسعار والمعايير
└─ تحديث تلقائي

✅ واجهة احترافية:
├─ Sidebar للملاحة
├─ Tabs للتنظيم
├─ Columns للتخطيط
└─ Responsive للجوال
```

---

## 🆘 استكشاف الأخطاء

### المشكلة: "streamlit: command not found"

```
الحل:
1. تأكد من تثبيت Python 3.8+
2. أعد تثبيت Streamlit:
   pip install --upgrade streamlit
3. جرب مع python -m:
   python -m streamlit run app.py
```

### المشكلة: "ModuleNotFoundError: No module named 'plotly'"

```
الحل:
pip install plotly
أو:
pip install -r requirements.txt
```

### المشكلة: "الرابط لا يعمل من الهاتف"

```
الحل:
1. تأكد من WiFi نفسه للحاسوب والهاتف
2. استخدم Network URL (ليس localhost)
3. في Firewall: اسمح بـ port 8501
4. جرب تعطيل VPN إذا كان متفعلاً
```

### المشكلة: "تحديثات التطبيق لا تظهر"

```
الحل:
1. اضغط R في Streamlit (في الأعلى)
2. أو أغلق ال Terminal واعد تشغيل:
   streamlit run app.py
3. امسح ذاكرة المتصفح (Ctrl+Shift+Delete)
```

---

## 📈 المميزات التي يمكن إضافتها لاحقاً

```
🚀 قادم قريباً:
├─ تحميل ملفات حقيقية (PDF, Excel)
├─ ChatBot ذكي محتقق من المصادر
├─ حسابات مالية متقدمة
├─ توليد تقارير PDF
├─ قاعدة بيانات (SQLite/PostgreSQL)
├─ مصادقة المستخدمين
├─ نسخ احتياطية تلقائية
└─ إشعارات وتنبيهات
```

---

## 🎯 ملخص سريع

### للتشغيل الآن:

```bash
# 1. التثبيت (مرة واحدة):
pip install -r requirements.txt

# 2. التشغيل:
streamlit run app.py

# 3. الوصول:
http://localhost:8501 (الحاسوب)
http://192.168.1.x:8501 (الهاتف)
```

### للرفع على الإنترنت:

```
1. أنشئ GitHub account
2. أرسل الملفات لـ GitHub
3. اذهب share.streamlit.io
4. اختر Repository
5. اضغط Deploy
6. سيعطيك URL عام!
```

---

## 💡 نصائح مهمة

```
✅ استخدم Local Server للتطوير
✅ اختبر على الهاتف قبل الرفع
✅ احفظ التحديثات في Git
✅ اقرأ docs Streamlit للمميزات الجديدة
✅ جرب Cache للسرعة:
   @st.cache_data
   def load_data():
       return pd.read_csv('file.csv')
```

---

**جاهز للبدء؟** 🚀

```bash
streamlit run app.py
```

استمتع بالتطبيق! 🎉

---

**أسئلة؟**
```
📖 Streamlit Docs: https://docs.streamlit.io
🆘 Community: https://discuss.streamlit.io
🐛 Issues: https://github.com/streamlit/streamlit/issues
```

**آخر تحديث**: مايو 2026  
**الإصدار**: 3.0  
**الحالة**: ✅ جاهز للاستخدام الآن!
