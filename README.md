# IPL Telegram Notification System

A production-style real-time IPL notification system built using Django, Django REST Framework, PostgreSQL, APScheduler, and Telegram Bot API.

This system fetches live IPL match data from Cricbuzz Rapid API, detects match events like wickets, sixes, over completions, and match results, then automatically sends real-time Telegram notifications based on user preferences.

---

# Features

- Real-time IPL live match syncing
- Wicket alerts
- Six alerts
- Over completion alerts
- Match result notifications
- User-based notification preferences
- Duplicate notification prevention
- Notification logging system
- APScheduler background jobs
- JWT Authentication
- Environment variable support
- Production-style service-layer architecture
- PostgreSQL database integration

---

# Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- APScheduler
- Telegram Bot API
- Rapid API (Cricbuzz)
- JWT Authentication

---

# Project Structure

```text
ipl_whatsapp_notification_system/
│
├── apps/
│   ├── users/
│   ├── matches/
│   └── notifications/
│
├── core/
├── utils/
├── manage.py
├── requirements.txt
├── README.md
└── .env
```

---

# Architecture Flow

```text
User Preferences
        ↓
Live Match Syncing
        ↓
Event Detection Engine
        ↓
Notification Service
        ↓
Telegram API
        ↓
Notification Logs
```

---

# Database Design

## User

Stores user authentication details.

## UserPreference

Stores notification preferences like:

- wicket alerts
- six alerts
- result alerts
- over update preferences

## Match

Stores live IPL match data.

## MatchState

Tracks previous scores and events to prevent duplicate notifications.

## NotificationLog

Stores notification history and delivery status.

---

# Scheduler Flow

APScheduler runs automatically every 15 seconds.

```text
runserver
    ↓
Scheduler Starts
    ↓
Fetch Live Matches
    ↓
Process Match Events
    ↓
Send Notifications
```

---

# Notification Events

The system automatically detects:

- Wicket events
- Six events
- Over changes
- Match completion

---

# Telegram Integration

Notifications are delivered directly to Telegram using Telegram Bot API.

Example Notification:

```text
🏏 WICKET ALERT

MI vs CSK

MI: 106/2
CSK: 90/2

Over: 10.2

🔥 Big breakthrough!
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/ankitojha17/ipl-whatsapp-notification-system.git
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env` file in root directory:

```env
DB_NAME=ipl_notification_system_db
DB_USER=postgres
DB_PASSWORD=
DB_HOST=127.0.0.1
DB_PORT=5432

RAPID_API_KEY=your_rapid_api_key

TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

---

# Run Migrations

```bash
python manage.py migrate
```

---

# Run Server

```bash
python manage.py runserver
```

---

# API Flow

```text
Rapid API
    ↓
CricketApiService
    ↓
MatchService
    ↓
Database Update
    ↓
EventService
    ↓
NotificationService
    ↓
Telegram Bot API
```

---

# Production-Style Features

- Service-layer architecture
- Clean separation of concerns
- Logging support
- Exception handling
- Background scheduler
- Notification history tracking
- Duplicate prevention logic
- Environment-based configuration

---

# Future Improvements

- Docker support
- Celery + Redis integration
- WebSocket live updates
- WhatsApp Cloud API integration
- Admin analytics dashboard

---

# Author

Ankit Ojha