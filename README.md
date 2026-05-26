# 🎤 Telegram Voice Bot

Telegram-бот для генерации озвучки текста с помощью ElevenLabs API.

---

## ✨ Возможности

- 🎙 Выбор голоса через Telegram-клавиатуру
- 🧠 Генерация озвучки через ElevenLabs
- 🔊 Отправка готового аудио пользователю
- 📁 Сохранение аудиофайлов локально
- 🔐 Безопасное хранение токенов через `.env`

---

## 🛠 Используемые технологии

- Python
- pyTelegramBotAPI
- ElevenLabs API
- python-dotenv

---

## 📂 Структура проекта

```text
voice_bot/
│
├── generated/
├── .gitignore
├── README.md
├── requirements.txt
├── .env
│
├── config.py
├── voice.py
└── main.py
```

---

## ⚙️ Установка и запуск

1. Клонировать репозиторий
```bash
git clone <repository_url>
```

2. Установить зависимости
```bash
pip install -r requirements.txt
```

3. Создать `.env`
```env
BOT_TOKEN=your_telegram_token
ELEVEN_API_KEY=your_elevenlabs_api_key
```

4. Запустить бота
```bash
python main.py
```

---

## 🚀 Как работает бот

1. Пользователь запускает бота командой /start
2. Бот показывает доступные голоса
3. Пользователь выбирает голос
4. Пользователь отправляет текст
5. Бот генерирует озвучку
6. Бот отправляет готовый аудиофайл

---
