# 🤖 دليل إعداد الـ Chatbot الذكي مع Claude API

## 📋 المتطلبات

- Python 3.8+
- Anthropic Claude API Key
- المكتبات المذكورة في `requirements.txt`

## 🚀 خطوات الإعداد

### 1️⃣ الحصول على Anthropic API Key

1. اذهب إلى [console.anthropic.com](https://console.anthropic.com/)
2. قم بإنشاء حساب أو تسجيل الدخول
3. انتقل إلى قسم "API Keys"
4. انسخ مفتاح API الخاص بك

### 2️⃣ تعيين متغير البيئة

**الطريقة الأولى: ملف .env**

قم بنسخ `.env.example` إلى `.env`:

```bash
cp .env.example .env
```

ثم عدّل `.env` وأضف مفتاح API الخاص بك:

```
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxx
CLAUDE_MODEL=claude-3-5-sonnet-20241022
```

**الطريقة الثانية: متغير البيئة العام**

```bash
export ANTHROPIC_API_KEY="sk-ant-xxxxxxxxxxxxxxxxxxxx"
```

### 3️⃣ تثبيت المكتبات

```bash
pip install -r requirements.txt
```

### 4️⃣ تشغيل التطبيق

```bash
streamlit run app_enhanced_fixed.py
```

## 📖 كيفية استخدام الـ Chatbot

### الخطوة 1: رفع الملفات
1. انتقل إلى صفحة "📚 المصادر"
2. قم برفع الملفات (PDF, Word, Excel, TXT)
3. سيتم استخراج النص من الملفات تلقائياً

### الخطوة 2: طرح الأسئلة
1. في الـ Sidebar على اليسار، ستجد "🤖 مساعدك الذكي"
2. اكتب سؤالك في حقل الإدخال
3. اضغط Enter أو زر الإرسال
4. سيجيب الـ Chatbot بناءً على الملفات المرفوعة

### الخطوة 3: عرض المصادر
- سيعرض الـ Chatbot مصادر الإجابة (أسماء الملفات) تحت كل إجابة
- يمكنك التوسيع لرؤية المزيد من تفاصيل الملفات المحملة

## 🏗️ بنية نظام RAG

```
chatbot_rag.py
├── DocumentRAG Class
│   ├── add_document() - إضافة ملف إلى النظام
│   ├── get_relevant_context() - البحث عن السياق الصلة
│   ├── chat() - الإجابة على السؤال مع Claude API
│   ├── clear_history() - مسح سجل المحادثة
│   ├── clear_documents() - مسح الملفات
│   └── get_document_summary() - الحصول على ملخص الملفات
```

## 🔧 معالجة الأخطاء الشائعة

### ❌ خطأ: "ANTHROPIC_API_KEY غير موجود"
**الحل:** تأكد من تعيين المتغير البيئي كما هو موضح أعلاه

### ❌ خطأ: "خطأ في قراءة PDF"
**الحل:** تأكد من أن ملف PDF ليس محمياً أو تالفاً

### ❌ خطأ: "الـ Chatbot غير متاح"
**الحل:** تحقق من الاتصال بالإنترنت وصحة API Key

## 📊 ملفات مدعومة

- **PDF**: `.pdf`
- **Word**: `.docx`, `.doc`
- **Excel**: `.xlsx`, `.xls`
- **Text**: `.txt`, `.csv`
- **الصور**: `.png`, `.jpg`, `.jpeg` (للعرض فقط)

## 🌐 النشر على Streamlit Cloud

لنشر التطبيق على Streamlit Cloud:

1. انسخ المشروع إلى GitHub
2. اذهب إلى [streamlit.io/cloud](https://streamlit.io/cloud)
3. اختر "Create app"
4. اربط مستودع GitHub الخاص بك
5. عيّن المتغيرات البيئية:
   - `ANTHROPIC_API_KEY` = مفتاح API الخاص بك

## 💡 نصائح مهمة

1. **حفظ API Key**: لا تشارك API Key الخاص بك مع أحد
2. **استخدام المشاريع المختلفة**: يمكنك تشغيل نسخ متعددة من التطبيق لمشاريع مختلفة
3. **تحديث الملفات**: الملفات المرفوعة محفوظة في الـ Session - ستُمسح عند إعادة تشغيل التطبيق
4. **حجم الملفات**: حاول استخدام ملفات بحجم معقول للأداء الأفضل

## 🆘 الدعم والمساعدة

للحصول على دعم إضافي:
- تحقق من [Anthropic API Documentation](https://docs.anthropic.com/)
- اقرأ [Streamlit Documentation](https://docs.streamlit.io/)
- تواصل مع فريق الدعم الخاص بك

---

**آخر تحديث:** 2026-05-04
