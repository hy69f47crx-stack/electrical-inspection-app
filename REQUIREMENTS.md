# 📋 متطلبات المشروع التفصيلية
## Electrical Inspection Professional - Requirements Document

---

## 🎯 الأهداف الرئيسية

| الهدف | الأولوية | الحالة |
|------|---------|--------|
| جمع بيانات ميدانية دقيقة | 🔴 عالية جداً | ⏳ قيد التطوير |
| مقارنة البيانات مع المخطط | 🔴 عالية جداً | ⏳ قيد التطوير |
| حساب المستحقات المالية | 🔴 عالية جداً | ⏳ قيد التطوير |
| توليد تقارير احترافية | 🔴 عالية جداً | ⏳ قيد التطوير |
| تزامن البيانات السحابي | 🟡 متوسطة | ⏳ قيد التطوير |
| دعم عدة مشاريع متزامنة | 🟡 متوسطة | ⏳ قيد التطوير |
| إعدادات قابلة للتخصيص | 🟢 منخفضة | ⏳ قيد التطوير |

---

## 📱 متطلبات تطبيق الجوال

### الميزات الأساسية:

#### 1. إدارة المشاريع (Projects Management)
- [x] عرض قائمة المشاريع النشطة
- [x] بدء معاينة جديدة
- [x] عرض نسبة الإنجاز لكل مشروع
- [x] تفاصيل المشروع (الموقع، الفترة، المقاول)
- [ ] إضافة مشروع جديد
- [ ] تعديل بيانات المشروع
- [ ] أرشفة المشاريع المكتملة

#### 2. جمع البيانات الميدانية (Field Data Collection)

**لكل بند عمل يجب جمع:**
- [x] الكمية المخطط
- [x] الكمية المنفذة
- [x] تقييم الجودة (جيد/معيب/ناقص)
- [x] ملاحظات حرة
- [x] صور توضيحية (متعدد الصور)
- [x] موقع GPS
- [x] تاريخ ووقت المعاينة
- [ ] توقيع الخبير الرقمي
- [ ] توقيع المقاول (اختياري)

#### 3. أنواع الأعمال (9 أنواع):
- [x] الأسلاك (متر)
- [x] البايبات (متر)
- [x] اللوحة الرئيسية (لوحة)
- [x] اللوحات الفرعية (لوحة)
- [x] التأريض (موقع)
- [x] مآخذ القوى (نقطة)
- [x] نقاط الإنارة (نقطة)
- [x] تمديدات النحاس (متر)
- [x] أعمال عامة (متنوع)

#### 4. الملاحظات الإضافية:
- [x] ملاحظات نصية حرة
- [x] تقييم بسيط (جيد/معيب/ناقص)
- [x] تصنيفات محددة مسبقاً
- [ ] قوائم اختيار متعددة
- [ ] معايير تقييم آلية

#### 5. المعالجة بدون انترنت (Offline-First):
- [x] حفظ البيانات محلياً
- [x] العمل بدون اتصال انترنت
- [x] مزامنة تلقائية عند الاتصال
- [x] إشعارات حالة الاتصال
- [x] تتبع حالة المزامنة

#### 6. التزامن والمزامنة (Sync):
- [x] تزامن يدوي (الضغط على زر)
- [x] تزامن تلقائي عند الاتصال
- [ ] جدولة التزامن (كل ساعة مثلاً)
- [x] عرض حالة التزامن
- [x] عرض آخر وقت تزامن
- [ ] معالجة تضاربات البيانات

#### 7. الأداء والبطارية:
- [ ] استهلاك بطارية منخفض
- [ ] سرعة تحميل الصور
- [ ] ضغط الصور التلقائي
- [ ] حد أقصى لحجم الصور (2-5 MB)

#### 8. الواجهة والتصميم:
- [x] ألوان أزرق + أبيض فاتح
- [x] عربي كامل (RTL)
- [x] حجم خطوط مريح
- [x] أيقونات واضحة
- [ ] وضع ليلي (Night Mode)
- [ ] تكبير النصوص للمسنين

---

## 💻 متطلبات تطبيق الويب

### لوحة التحكم (Dashboard):
- [x] عرض إحصائيات سريعة
  - عدد المشاريع النشطة
  - نسبة الإنجاز الإجمالية
  - عدد البنود الناقصة
  - عدد الخبراء النشطين
- [x] رسوم بيانية للإنجاز
- [ ] رسوم بيانية للجودة
- [ ] تنبيهات (عناصر ناقصة، تأخيرات)
- [ ] الأخبار الأخيرة

### إدارة المشاريع (Projects):
- [x] قائمة المشاريع
- [ ] إضافة مشروع جديد
- [ ] تعديل بيانات المشروع
- [ ] حذف مشروع
- [ ] البحث والفلترة
- [ ] الترتيب حسب التاريخ/الإنجاز/الاسم

### التحليل والمقارنة (Analysis):
- [x] جدول مقارنة (مخطط vs منفذ)
- [x] رسم بياني للمقارنة
- [x] نسبة الإنجاز لكل بند
- [ ] تحليل الانحرافات
- [ ] تقارير الجودة
- [ ] تقارير العيوب

### الحسابات المالية (Calculations):
- [x] حساب نسبة الإنجاز
- [x] حساب المستحق بناءً على الإنجاز
- [x] خصم المسدد سابقاً
- [x] إضافة/خصم الغرامات والحوافز
- [x] الحساب النهائي
- [ ] حسابات متعددة العملات
- [ ] معدلات التضخم

### التقارير (Reports):
- [x] اختيار نوع التقرير (شامل/موجز/مالي)
- [x] اختيار المحتويات المطلوبة
- [x] معاينة قبل الطباعة
- [x] توليد PDF
- [x] طباعة مباشرة
- [ ] إرسال بريد إلكتروني
- [ ] حفظ على السحابة
- [ ] التوقيع الرقمي

### إدارة الفريق (Team Management):
- [ ] إضافة/حذف خبير
- [ ] تعيين الخبير للمشروع
- [ ] عرض نشاط الخبير
- [ ] إعدادات الصلاحيات
- [ ] سجل العمليات (Audit Log)

### الإعدادات (Settings):
- [x] معلومات الحساب الشخصي
- [x] الإعدادات العامة
- [ ] تفضيلات الإشعارات
- [ ] معايير التقييم (قابلة للتخصيص)
- [ ] القوالب المحفوظة

---

## 🗄️ متطلبات قاعدة البيانات

### الجداول والعلاقات:

#### جدول المستخدمين (Users):
```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    specialization VARCHAR(255),
    phone VARCHAR(20),
    role ENUM('admin', 'inspector', 'viewer'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP
);
```

#### جدول المشاريع (Projects):
```sql
CREATE TABLE projects (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    project_type ENUM('residential', 'commercial', 'industrial'),
    contractor_name VARCHAR(255),
    contract_value DECIMAL(12, 2),
    start_date DATE,
    end_date DATE,
    status ENUM('active', 'completed', 'on_hold', 'archived'),
    created_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users(id)
);
```

#### جدول البنود (Items):
```sql
CREATE TABLE items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT NOT NULL,
    item_type ENUM('wires', 'pipes', 'main_panel', 'sub_panels', 'grounding', 'power_outlets', 'lights', 'copper', 'general'),
    planned_quantity DECIMAL(10, 2),
    unit_of_measure VARCHAR(50),
    floor_number INT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);
```

#### جدول الملاحظات الميدانية (Observations):
```sql
CREATE TABLE observations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    item_id INT NOT NULL,
    inspector_id INT NOT NULL,
    actual_quantity DECIMAL(10, 2),
    quality_status ENUM('compliant', 'defective', 'missing'),
    notes TEXT,
    photo_url VARCHAR(500),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    observed_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES items(id) ON DELETE CASCADE,
    FOREIGN KEY (inspector_id) REFERENCES users(id)
);
```

#### جدول الحسابات (Calculations):
```sql
CREATE TABLE calculations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT NOT NULL,
    total_contract_value DECIMAL(12, 2),
    completion_percentage DECIMAL(5, 2),
    earned_amount DECIMAL(12, 2),
    paid_amount DECIMAL(12, 2),
    deductions DECIMAL(12, 2),
    bonuses DECIMAL(12, 2),
    final_payable DECIMAL(12, 2),
    calculated_by INT,
    calculated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(id),
    FOREIGN KEY (calculated_by) REFERENCES users(id)
);
```

#### جدول التقارير (Reports):
```sql
CREATE TABLE reports (
    id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT NOT NULL,
    report_type ENUM('comprehensive', 'summary', 'financial'),
    pdf_url VARCHAR(500),
    created_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    signed_at TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(id),
    FOREIGN KEY (created_by) REFERENCES users(id)
);
```

---

## 🔐 متطلبات الأمان

### المصادقة (Authentication):
- [x] تسجيل دخول باسم مستخدم وكلمة مرور
- [ ] توثيق ثنائي (2FA)
- [ ] تسجيل دخول من جهات خارجية (Google/Apple)
- [ ] استعادة كلمة المرور

### التفويض (Authorization):
- [ ] أدوار مختلفة (Admin/Inspector/Viewer)
- [ ] صلاحيات على مستوى المشروع
- [ ] صلاحيات على مستوى البيانات

### التشفير:
- [x] تشفير كلمات المرور (bcrypt)
- [x] HTTPS للاتصالات
- [ ] تشفير البيانات المحلية (Mobile)
- [ ] توقيع API

### التدقيق (Audit):
- [x] سجل جميع العمليات
- [x] من قام بالتعديل وفي أي وقت
- [ ] تتبع التغييرات

---

## 📊 معايير الأداء

| المعيار | القيمة المطلوبة | الأولوية |
|--------|-----------------|----------|
| سرعة تحميل الصفحة | < 2 ثانية | 🔴 عالية |
| سرعة المزامنة | < 30 ثانية | 🔴 عالية |
| حجم التطبيق | < 50 MB | 🟡 متوسطة |
| استهلاك البطارية | < 10% / ساعة | 🟡 متوسطة |
| دعم المستخدمين | 100+ | 🟢 منخفضة |

---

## 🧪 متطلبات الاختبار

### الاختبارات اليدوية (Manual Testing):
- [ ] اختبار جميع الشاشات
- [ ] اختبار التنقل بين الشاشات
- [ ] اختبار الإدخال البيانات
- [ ] اختبار المزامنة
- [ ] اختبار الطباعة والتقارير

### الاختبارات الآلية (Automated Testing):
- [ ] اختبارات Unit
- [ ] اختبارات Integration
- [ ] اختبارات E2E
- [ ] اختبارات الأداء

### الاختبارات الأمان (Security Testing):
- [ ] اختبار Penetration
- [ ] اختبار SQL Injection
- [ ] اختبار XSS
- [ ] اختبار CSRF

---

## 📚 متطلبات التوثيق

- [ ] دليل المستخدم (User Guide)
- [ ] دليل المسؤول (Admin Guide)
- [ ] توثيق API
- [ ] توثيق قاعدة البيانات
- [ ] دليل التثبيت والنشر
- [ ] FAQ وحل المشاكل

---

## 🚀 متطلبات النشر (Deployment)

### البيئات (Environments):
- [ ] بيئة التطوير (Development)
- [ ] بيئة الاختبار (Staging)
- [ ] بيئة الإنتاج (Production)

### المنصات:
- [ ] iOS (App Store)
- [ ] Android (Google Play)
- [ ] الويب (Cloud Hosting)

### CI/CD:
- [ ] بناء آلي (Automated Build)
- [ ] اختبار آلي (Automated Tests)
- [ ] نشر آلي (Automated Deployment)

---

## 📈 معدل النمو والتوسع

### المرحلة الأولى (MVP):
- 3-10 خبراء
- 5-10 مشاريع
- 9 أنواع أعمال

### المرحلة الثانية:
- 50-100 خبير
- 50-100 مشروع
- دعم معايير إضافية

### المرحلة الثالثة:
- 1000+ خبير
- 1000+ مشروع
- شركاء خارجيين

---

## 💾 النسخ الاحتياطي والاسترجاع

- [ ] نسخة احتياطية يومية تلقائية
- [ ] نسخة احتياطية أسبوعية
- [ ] نسخة احتياطية شهرية
- [ ] اختبار الاسترجاع شهرياً
- [ ] توثيق عملية الاسترجاع

---

## 📅 جدول المشروع المقترح

| المرحلة | المدة | الميزات |
|--------|------|--------|
| التخطيط والتصميم | أسبوع | معمارية، تصميم UI/UX |
| التطوير الأساسي | أسبوعان | API، قاعدة بيانات، أساسيات التطبيقات |
| تطوير الميزات | أسبوعان | التقارير، الحسابات، المزامنة |
| الاختبار الشامل | أسبوع | QA، الأمان، الأداء |
| التدريب والنشر | أسبوع | التوثيق، التدريب، النشر |

---

## 🎯 نقاط الفحص الحرجة (Critical Checkpoints)

- [ ] موافقة على التصميم (Sprint 0)
- [ ] تطبيق Mobile يعمل بدون انترنت (Sprint 2)
- [ ] تطبيق Web يعرض البيانات صحيحة (Sprint 2)
- [ ] نظام التقارير يعمل بشكل صحيح (Sprint 3)
- [ ] المزامنة تعمل بدون فقدان البيانات (Sprint 3)
- [ ] اختبار أمان كامل (Sprint 4)
- [ ] موافقة نهائية للإطلاق (Sprint 5)

---

**آخر تحديث:** مايو 2026  
**الحالة:** جاهز للتطوير 🟢
