# 🔌 API Integration Checklist - Task #4

**الحالة الحالية:** جاري العمل  
**المتطلب:** Streamlit Backend يعمل على `http://localhost:8501`

---

## 📋 قائمة التكامل الشاملة

### المرحلة 1: التأكد من البيئة ✅

- [x] API Client جاهز (`src/utils/api.js`)
- [x] Custom Hooks جاهزة (`useProjects`, `useChat`, `useInspections`)
- [x] Components والـ Pages منشأة
- [ ] Backend يعمل على المنفذ الصحيح

**الفعل**: تشغيل Backend
```bash
cd ..
streamlit run app.py
```

---

### المرحلة 2: اختبار الـ API Endpoints

#### ✅ Projects API

```javascript
// في App.jsx أو أي صفحة
import { projectsAPI } from './utils/api';

// Test 1: الحصول على جميع المشاريع
try {
  const response = await projectsAPI.getAll();
  console.log('Projects:', response.data);
} catch (error) {
  console.error('Error:', error.message);
}

// Test 2: إنشاء مشروع جديد
const newProject = await projectsAPI.create({
  name: 'مشروع اختبار',
  description: 'هذا مشروع اختبار API'
});
```

**الخطوات**:
1. [ ] تشغيل Streamlit Backend
2. [ ] فتح المتصفح على `http://localhost:3000`
3. [ ] فتح Developer Tools (F12)
4. [ ] الذهاب إلى صفحة Projects
5. [ ] محاولة إضافة مشروع جديد
6. [ ] التحقق من Console للأخطاء
7. [ ] التحقق من Network tab

#### ✅ Inspections API

```javascript
// اختبار حفظ التصميم
const designData = {
  objects: [
    {
      id: 1,
      type: 'line',
      x1: 10,
      y1: 10,
      x2: 100,
      y2: 100,
      color: '#333',
      lineWidth: 2
    }
  ],
  timestamp: new Date().toISOString()
};

await inspectionsAPI.saveDesign(inspectionId, designData);
```

#### ✅ Chat API

```javascript
// اختبار الـ Chatbot
const message = 'مرحبا، كيف حالك؟';
const response = await chatbotAPI.sendMessage(message);
console.log('Bot response:', response.data.message);
```

#### ✅ Files API

```javascript
// اختبار تحميل ملف
const file = new File(['content'], 'test.txt', { type: 'text/plain' });
const response = await filesAPI.upload(file, projectId);
console.log('File uploaded:', response.data);
```

---

### المرحلة 3: معالجة الأخطاء

#### Error Handling في API Client

```javascript
// تحسين البيانات المُرجعة
apiClient.interceptors.response.use(
  (response) => {
    // التعامل مع الاستجابة الناجحة
    return response.data || response;
  },
  (error) => {
    // معالجة الأخطاء
    const errorMessage = error.response?.data?.message || error.message;
    console.error('API Error:', errorMessage);
    throw new Error(errorMessage);
  }
);
```

#### في المكونات

```jsx
const { projects, isLoading, error } = useProjects();

if (error) {
  return (
    <div className="error-message">
      ❌ خطأ: {error}
      <button onClick={() => refetch()}>إعادة محاولة</button>
    </div>
  );
}
```

**التحقق**:
- [ ] أخطاء الشبكة معالجة
- [ ] رسائل الخطأ واضحة
- [ ] العودة من الأخطاء سهلة
- [ ] Fallback UIs موجودة

---

### المرحلة 4: البيانات الديناميكية

#### تحميل البيانات عند الحمل

```jsx
// في Dashboard.jsx
const { projects, isLoading } = useProjects();

useEffect(() => {
  // يتم التحميل تلقائياً عند الـ mount
}, []);

if (isLoading) return <Spinner />;

return (
  <div>
    {projects.map(p => (
      <ProjectCard key={p.id} project={p} />
    ))}
  </div>
);
```

**التحقق**:
- [ ] البيانات تحمل تلقائياً
- [ ] Loading states واضحة
- [ ] البيانات تُعرض بشكل صحيح
- [ ] Refresh يعيد التحميل

#### تحديث البيانات عند الإنشاء/التعديل

```jsx
// في Projects.jsx
const { createProject } = useProjects();

const handleCreate = (data) => {
  createProject(data);
  // Query يُحدَّث تلقائياً
};
```

**التحقق**:
- [ ] مشروع جديد يظهر مباشرة
- [ ] قائمة المشاريع تُحدَّث
- [ ] No manual refresh needed

---

### المرحلة 5: الحالة والـ Caching

#### React Query Configuration

```javascript
// في App.jsx
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 60 * 5,        // 5 دقائق
      cacheTime: 1000 * 60 * 10,       // 10 دقائق
      retry: 1,                         // إعادة محاولة واحدة
      refetchOnWindowFocus: false,      // عدم التحديث عند العودة
    },
  },
});
```

**التحقق**:
- [ ] البيانات مخزنة بشكل صحيح
- [ ] Refetch يعمل عند الحاجة
- [ ] Memory usage معقول
- [ ] Performance مقبول

---

### المرحلة 6: التعامل مع الملفات

#### تحميل الملفات

```jsx
const handleFileUpload = async (e) => {
  const files = e.target.files;
  
  for (const file of files) {
    try {
      const response = await filesAPI.upload(file, projectId);
      console.log('File uploaded:', response.data);
    } catch (error) {
      console.error('Upload failed:', error);
    }
  }
};
```

**التحقق**:
- [ ] الملفات تحمل بنجاح
- [ ] Progress bar يعمل
- [ ] Multiple files supported
- [ ] Error handling جيد

---

### المرحلة 7: الـ Chatbot Real-time

#### WebSocket Integration (المرحلة التالية)

```javascript
// Future implementation
import io from 'socket.io-client';

const socket = io('http://localhost:8501');

socket.on('chat_response', (data) => {
  console.log('New message:', data);
});
```

**المهام**:
- [ ] WebSocket server في Backend
- [ ] Client connection
- [ ] Real-time message updates
- [ ] Typing indicators

---

## 🧪 اختبار شامل

### قائمة الاختبار اليدوية:

#### 1. Dashboard
- [ ] الإحصائيات تحمل
- [ ] المشاريع الأخيرة تظهر
- [ ] الأزرار السريعة تعمل
- [ ] Responsive على الجوال

#### 2. Projects Page
- [ ] البحث يعمل
- [ ] الإضافة تعمل
- [ ] التعديل يعمل
- [ ] الحذف يعمل (مع تأكيد)
- [ ] بدون تحديث الصفحة

#### 3. Inspector Page
- [ ] DesignCanvas يرسم
- [ ] الحفظ يعمل
- [ ] التفاصيل تحمل
- [ ] الملفات تحمل
- [ ] التبويبات تعمل

#### 4. Chat
- [ ] الرسائل تُرسل
- [ ] الرد يظهر
- [ ] السجل يحفظ
- [ ] Clear يعمل

#### 5. Error Cases
- [ ] Backend معطوب
- [ ] Network error
- [ ] Invalid data
- [ ] Timeout

---

## 🐛 استكشاف الأخطاء

### المشكلة: 404 Not Found

```
Error: 404 - Not Found
```

**الحل**:
1. تحقق من الـ Backend endpoints
2. تحقق من الـ URL في `api.js`
3. تأكد من أن Streamlit يعمل
4. شغّل Streamlit مع `--logger.level=debug`

### المشكلة: CORS Error

```
Access to XMLHttpRequest blocked by CORS policy
```

**الحل**:
1. إضافة CORS headers في Backend
2. استخدام proxy في development
3. تحقق من `REACT_APP_BACKEND_URL`

### المشكلة: Timeout

```
Error: Request timeout
```

**الحل**:
1. زيادة timeout في `.env`
2. تحقق من سرعة الشبكة
3. تحقق من حجم البيانات

---

## 📊 Monitoring

### في Browser Console:

```javascript
// تفعيل logging
window.DEBUG = true;

// معاينة البيانات المخزنة
localStorage.getItem('react-query-state')
```

### في Network Tab:

- تحقق من جميع الـ requests
- تحقق من الـ status codes
- تحقق من الوقت المستغرق
- تحقق من الرد (Response)

---

## ✅ Completion Checklist

- [ ] جميع الـ Endpoints تعمل
- [ ] البيانات تحمل بشكل صحيح
- [ ] معالجة الأخطاء جيدة
- [ ] Performance مقبول
- [ ] Responsive design يعمل
- [ ] الملفات تحمل بنجاح
- [ ] الـ Chat يعمل (بدون WebSocket الآن)
- [ ] التوثيق كامل
- [ ] الاختبارات تمرّ
- [ ] Ready for next phase

---

## 🚀 الخطوة التالية

عند اكتمال هذه المرحلة:

1. **Task #5**: دمج Chatbot كامل مع WebSocket
2. إضافة Authentication و User Profiles
3. Optimization والـ Performance
4. Deployment

---

## 📞 المساعدة

عند الحاجة:
1. اسأل في Slack #electrical-app
2. افتح GitHub Issue
3. راجع الـ Logs في Backend

---

**الحالة:** 🟡 **جاري العمل**  
**الأولوية:** 🔴 **عالية**  
**المدة المتوقعة:** 2-3 أيام

تم إعداد هذا الملف: 4 مايو 2024
