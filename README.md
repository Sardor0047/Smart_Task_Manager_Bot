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
```bash
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
```
----
# Let's proceed how to build maniger bot

- ##  What is python-telegram-bot==13.5?
    - This package make easier to work with telegram APIs
    - I used to build with Version v13.5 features :
    - i show you how launch bot and rycicling with texts 
    ```python
    from telegram.ext import Updater, CommandHandler

    updater = Updater(token="TOKEN", use_context=True)
    dispatcher = updater.dispatcher

    def start(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Salom!")

    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()
    ```
    - ``CommandHandler``: Handles commands like /start, /help, etc.
    - ```MessageHandler```: Processes messages such as text, images, and voice.
    - ```CallbackQueryHandler```: Works when inline buttons are pressed.
- ## What is TinyDB ?
    - A document-oriented database (like MongoDB but simpler).
    - Stores data in JSON format (easy to read/write).
    - Perfect for small apps, prototypes, or learning.
    ### Instalation
    ```bash 
    pip install tinydb
    ```
    ### Create a Database
    ```python
    from tinydb import TinyDB

    # Create/connect to a database (creates 'tasks.json' file)
    db = TinyDB('tasks.json')
    ```

    ### Insert Data
    - Add a document (like a Python dictionary):
    ```python
    task = {
    'user_id': 1,
    'text': 'Learn Python',
    'status': 'active'
    }

    # Insert a document and get its ID
    task_id = db.insert(task)
    print(f"Task ID: {task_id}")  # Output: Task ID: 1
    ```
    ### Read Data
    - Use Query() to search:

    ```python
    from tinydb import Query

    Task = Query()

    # Get all tasks for user_id=1
    user_tasks = db.search(Task.user_id == 1)
        print(user_tasks)  # Output: [{'user_id': 1, 'text': 'Learn Python', ...}]

    # Get all active tasks
    active_tasks = db.search(Task.status == 'active')
    ```
    ### Delete Data
    - Remove documents
    ```python 
    # Delete task with ID=1
    db.remove(doc_ids=[1])

    # Delete all tasks for user_id=1
    db.remove(Task.user_id == 1)
    ```

    