# 🕰️ Remind-me-later API

This Django REST API allows users to schedule reminders with a message, a scheduled datetime, and a delivery method (SMS or Email). It provides endpoints to create, list, and filter reminders.

---

## 🚀 Features

- ✅ Create reminders with:
  - Message text
  - Scheduled datetime
  - Reminder method (SMS or Email)
- 📄 List all existing reminders
- 🔍 Filter reminders by delivery method and date
- 🔧 Easy to extend with more delivery options (e.g. Push, WhatsApp)

---

## 📦 API Endpoints

### 🔸 1. Create a Reminder

**POST** `/api/reminders/`

#### Request Body

```json
{
  "message": "Take your medicine",
  "remind_at": "2025-05-14T09:00:00Z",
  "method": "email"
}
```



