# Task Manager Telegram Bot 🤖✅
Telegram orqali vazifalarni boshqarish uchun oddiy va samarali bot. Loyiha Python, `TinyDB` va `python-telegram-bot` kutubxonasi asosida qurilgan.

## Imkoniyatlar 
---
- Vazifalar qoshish (`/add`)
- Vazifalar ro'yxatini ko'rish (`/list`)
- Inline tugmalar orqali vazifa holatini o'zgartirish (✅/◻️)
- Vazifalarni o'chirish

## Texnologiyalar
- **Python 3.11.11**
- **python-telegram-bot==13.5**
- **TinyDB**




## Bot Ishlash Workflowi
```python
Workflow
    participant Foydalanuvchi
    participant Telegram Bot
    participant TinyDB

    Foydalanuvchi->>Telegram Bot: /list
    Telegram Bot->>TinyDB: SELECT user_id=12345
    TinyDB-->>Telegram Bot: Vazifalar ro'yxati
    Telegram Bot-->>Foydalanuvchi: Inline tugmalar bilan ro'yxat

    Foydalanuvchi->>Telegram Bot: Inline tugmani bosadi (callback_data="toggle_1")
    Telegram Bot->>TinyDB: UPDATE status WHERE doc_id=1
    TinyDB-->>Telegram Bot: Status yangilandi
    Telegram Bot-->>Foydalanuvchi: Yangilangan ro'yxat

    