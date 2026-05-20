# Real-Time IPL Telegram Notification System

A production-style real-time IPL notification system built using Django, Django REST Framework, PostgreSQL, APScheduler, Docker, and Telegram Bot API.

This system fetches live IPL match data from Cricbuzz Rapid API, detects match events such as wickets, sixes, over completions, and match results, then automatically sends real-time Telegram notifications based on user preferences.

---

## Live Deployment

https://real-time-ipl-telegram-notification.onrender.com

---

# Features

* Real-time IPL live match syncing
* Wicket alerts
* Six alerts
* Over completion alerts
* Match result notifications
* User-based notification preferences
* Duplicate notification prevention
* Notification logging system
* APScheduler background jobs
* JWT Authentication
* Environment variable support
* Dockerized multi-container setup
* Production-style service-layer architecture
* PostgreSQL database integration
* Multi-environment configuration support

---

# Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
- Gunicorn
- Render
- NeonDB
* APScheduler
* Docker
* Docker Compose
* Telegram Bot API
* Rapid API (Cricbuzz)
* JWT Authentication

---

# Project Structure

```text
Real-Time IPL Telegram Notification System/
│
├── apps/
│   ├── matches/
│   ├── notifications/
│   └── users/
│
├── core/
├── utils/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
├── README.md
├── .env
├── .env.docker
└── .gitignore
```

---

# System Architecture

```text
User Preferences
        ↓
Live Match Syncing
        ↓
Event Detection Engine
        ↓
Notification Service
        ↓
Telegram Bot API
        ↓
Notification Logs
```

---

# Database Design

## User

Stores authentication details.

## UserPreference

Stores notification preferences:

* wicket alerts
* six alerts
* over updates
* result alerts

## Match

Stores IPL match information.

## MatchState

Tracks previous match state to prevent duplicate notifications.

## NotificationLog

Stores notification delivery history.

---

# Notification Events

The system automatically detects:

* Wicket events
* Six events
* Over changes
* Match completion

---

# Scheduler Flow

APScheduler automatically runs background tasks at fixed intervals.

```text
Scheduler
    ↓
Fetch Live Matches
    ↓
Sync Match Data
    ↓
Detect Events
    ↓
Send Telegram Notifications
```

---

# Telegram Integration

Notifications are delivered directly using Telegram Bot API.

## Example Notification

```text
🏏 WICKET ALERT

MI vs CSK

MI: 106/2
CSK: 90/2

Over: 10.2

🔥 Big breakthrough!
```

---

# Docker Support

The entire project is fully Dockerized using Docker Compose.

## Containers

* Django Application Container
* PostgreSQL Database Container

## Docker Architecture

```text
Docker Compose
│
├── Django Container
│     ├── DRF APIs
│     ├── Scheduler
│     └── Notification Engine
│
└── PostgreSQL Container
```

---

# Environment Configuration

The project supports multiple environments.

## Local Environment

`.env`

```env
DB_NAME=ipl_notification_system_db
DB_USER=postgres
DB_PASSWORD=
DB_HOST=127.0.0.1
DB_PORT=5432
```

## Docker Environment

`.env.docker`

```env
DB_NAME=ipl_notification_system_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/ankitojha17/real-time-ipl-telegram-notification-system.git
```

---

# Local Setup

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Migrations

```bash
python manage.py migrate
```

## Run Server

```bash
python manage.py runserver
```

---

# Docker Setup

## Build Containers

```bash
docker compose build
```

## Start Containers

```bash
docker compose up
```

## Run Migrations Inside Docker

```bash
docker compose exec web python manage.py migrate
```

## Create Superuser

```bash
docker compose exec web python manage.py createsuperuser
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

* Service-layer architecture
* Clean separation of concerns
* Background scheduler
* Exception handling
* Logging support
* Duplicate prevention logic
* Environment-based configuration
* Notification history tracking
* Dockerized deployment support

---

# Future Improvements

* Celery + Redis integration
* WebSocket live updates
* WhatsApp Cloud API integration
* Kubernetes deployment
* CI/CD pipeline
* Admin analytics dashboard

---

# Author

Ankit Ojha
