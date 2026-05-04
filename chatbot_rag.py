"""
نظام RAG (Retrieval Augmented Generation) للـ Chatbot الذكي
يستخدم Claude API للإجابة على الأسئلة بناءً على الملفات المرفوعة
"""

import os
from typing import List, Tuple, Optional
import json
from anthropic import Anthropic
from dotenv import load_dotenv

# تحميل متغيرات البيئة
load_dotenv()

class DocumentRAG:
    """نظام RAG للتعامل مع المستندات والإجابة على الأسئلة"""

    def __init__(self):
        """تهيئة عميل Claude API والتخزين المؤقت للمستندات"""
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY غير موجود. "
                "الرجاء تعيين متغير البيئة ANTHROPIC_API_KEY"
            )

        self.client = Anthropic()
        self.model = os.getenv('CLAUDE_MODEL', 'claude-3-5-sonnet-20241022')

        # تخزين المستندات والنصوص المستخرجة
        self.documents: dict[str, str] = {}  # {filename: text_content}
        self.conversation_history: list = []  # سجل المحادثة

    def add_document(self, filename: str, content: str) -> None:
        """
        إضافة مستند إلى نظام RAG

        Args:
            filename: اسم الملف
            content: محتوى النص المستخرج من الملف
        """
        if content and content.strip():
            self.documents[filename] = content

    def get_relevant_context(self, query: str, top_k: int = 3) -> Tuple[str, List[str]]:
        """
        البحث عن أكثر المستندات صلة بالسؤال

        استخدام بحث نصي بسيط (يمكن تطويره لاحقاً بـ embeddings)

        Args:
            query: السؤال
            top_k: عدد المستندات الصلة المراد إرجاعها

        Returns:
            tuple: (context_text, source_files)
        """
        if not self.documents:
            return "", []

        # تقسيم المستندات إلى فقرات
        paragraphs_with_sources = []
        for filename, content in self.documents.items():
            # تقسيم إلى فقرات بناءً على الأسطر الفارغة
            lines = content.split('\n')
            current_para = []

            for line in lines:
                if line.strip():
                    current_para.append(line)
                elif current_para:
                    para_text = ' '.join(current_para)
                    if len(para_text.strip()) > 10:  # تجاهل الفقرات الصغيرة جداً
                        paragraphs_with_sources.append({
                            'text': para_text,
                            'source': filename,
                            'relevance': self._calculate_relevance(query, para_text)
                        })
                    current_para = []

            # آخر فقرة
            if current_para:
                para_text = ' '.join(current_para)
                if len(para_text.strip()) > 10:
                    paragraphs_with_sources.append({
                        'text': para_text,
                        'source': filename,
                        'relevance': self._calculate_relevance(query, para_text)
                    })

        # ترتيب حسب الصلة وأخذ أفضل top_k
        sorted_paras = sorted(
            paragraphs_with_sources,
            key=lambda x: x['relevance'],
            reverse=True
        )[:top_k]

        # بناء النص السياقي
        context_parts = []
        sources = set()

        for para_info in sorted_paras:
            if para_info['relevance'] > 0:
                context_parts.append(f"[من: {para_info['source']}]\n{para_info['text']}")
                sources.add(para_info['source'])

        context = "\n\n---\n\n".join(context_parts)
        return context, list(sources)

    def _calculate_relevance(self, query: str, text: str) -> float:
        """
        حساب درجة الصلة بين السؤال والنص
        (بحث بسيط يمكن تطويره لاحقاً)

        Args:
            query: السؤال
            text: النص المراد حساب صلته

        Returns:
            درجة الصلة (0-1)
        """
        query_words = set(query.lower().split())
        text_words = text.lower().split()

        # عد الكلمات المطابقة
        matches = sum(1 for word in query_words if word in text_words)

        # حساب النسبة
        if not query_words:
            return 0

        return min(1.0, matches / len(query_words))

    def chat(self, user_message: str) -> Tuple[str, List[str]]:
        """
        إجابة السؤال باستخدام Claude API مع السياق من المستندات

        Args:
            user_message: السؤال من المستخدم

        Returns:
            tuple: (الإجابة، قائمة الملفات المصدر)
        """
        # البحث عن السياق الصلة
        context, source_files = self.get_relevant_context(user_message)

        # بناء رسالة النظام
        system_prompt = """أنت مساعد ذكي متخصص في الإجابة على أسئلة المشاريع الهندسية والمعاينات الكهربائية.

إذا كان لديك سياق من الملفات المرفوعة، استخدمه للإجابة بدقة.
إذا لم يكن هناك سياق، أجب بناءً على معرفتك العامة.

تأكد من:
1. الإجابة بالعربية بشكل واضح
2. استخدام المعلومات من السياق إن وجدت
3. الإشارة إلى المصادر عند الاقتباس
4. التركيز على المعلومات الهندسية والتقنية"""

        # إضافة السياق إلى الرسالة إذا وجدنا ملفات صلة
        if context:
            user_message_with_context = f"""السياق من الملفات المرفوعة:
---
{context}
---

السؤال: {user_message}"""
        else:
            user_message_with_context = user_message

        # إضافة الرسالة إلى السجل
        self.conversation_history.append({
            "role": "user",
            "content": user_message_with_context
        })

        try:
            # استدعاء Claude API
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                system=system_prompt,
                messages=self.conversation_history
            )

            assistant_message = response.content[0].text

            # إضافة الرد إلى السجل
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })

            return assistant_message, source_files

        except Exception as e:
            error_message = f"خطأ في الإجابة: {str(e)}"
            return error_message, []

    def clear_history(self) -> None:
        """مسح سجل المحادثة"""
        self.conversation_history = []

    def clear_documents(self) -> None:
        """مسح المستندات المخزنة"""
        self.documents = {}
        self.clear_history()

    def get_document_summary(self) -> str:
        """الحصول على ملخص المستندات المرفوعة"""
        if not self.documents:
            return "لا توجد ملفات مرفوعة"

        summary = f"تم تحميل {len(self.documents)} ملف(ات):\n"
        for filename, content in self.documents.items():
            word_count = len(content.split())
            summary += f"• {filename} ({word_count} كلمة)\n"

        return summary


def create_rag_system() -> DocumentRAG:
    """إنشاء نظام RAG جديد"""
    return DocumentRAG()
