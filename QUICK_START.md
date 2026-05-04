# ⚡ دليل البدء السريع

## في 5 دقائق فقط

### 1️⃣ احصل على API Key (2 دقيقة)

```bash
# اذهب إلى هذا الرابط
https://console.anthropic.com/api/keys

# سجل الدخول أو أنشئ حساب
# انسخ API Key الخاص بك
```

### 2️⃣ أعداد التطبيق (1 دقيقة)

```bash
# انتقل إلى مجلد المشروع
cd ~/Documents/Claude/Projects/مهندس\ كهربائي\ مساعد

# نسخ ملف الإعدادات
cp .env.example .env

# افتح .env وأضف API Key
# استخدم محررك المفضل:
nano .env
```

في الملف، ستجد:
```
ANTHROPIC_API_KEY=your_api_key_here
```

استبدل `your_api_key_here` بمفتاحك الفعلي.

### 3️⃣ ثبّت المكتبات (1 دقيقة)

```bash
pip install -r requirements.txt
```

### 4️⃣ شغّل التطبيق (30 ثانية)

```bash
streamlit run app_enhanced_fixed.py
```

سيفتح التطبيق تلقائياً في متصفحك على `http://localhost:8501`

---

## 📝 إذا واجهت مشاكل

| المشكلة | الحل |
|--------|------|
| خطأ "API Key غير موجود" | تحقق من أنك أضفت المفتاح في ملف .env بشكل صحيح |
| خطأ "لا يمكن استيراد streamlit" | شغّل `pip install streamlit` |
| الـ chatbot لا يرد | تأكد من وجود ملفات مرفوعة في صفحة "المصادر" |
| الجلسة بطيئة | جرّب ملفات أصغر أو أعد تحميل الصفحة |

---

## ✅ تجربة التطبيق

1. **انتقل إلى صفحة "📚 المصادر"**
2. **ارفع ملف PDF أو Word أو Excel**
3. **في الـ Sidebar، اسأل الـ Chatbot عن محتوى الملف**
4. **سيجيب بناءً على الملفات المرفوعة** ✨

---

## 🌐 نشر التطبيق على الإنترنت

```bash
# دخّل على Streamlit Cloud
https://streamlit.io/cloud

# اختر "Create app" وربط GitHub
# عيّن متغير البيئة: ANTHROPIC_API_KEY
# انقر "Deploy"
```

---

**الآن أنت جاهز! 🎉**
