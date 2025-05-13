# 🕰️ Remind-me-later API

This Django REST API allows users to schedule reminders with a message, a scheduled datetime, and a delivery method (SMS or Email). It provides endpoints to create, list, and filter reminders.

---

## 🚀 Features

- ✅ Create reminders with:
  - Message text
  - Scheduled datetime
  - Reminder method (SMS or Email)
- 📄 List all existing reminders

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
![Screenshot (520)](https://github.com/user-attachments/assets/39a50d1e-5af6-4cc7-b0ce-21e812f39cb0)

![Screenshot (521)](https://github.com/user-attachments/assets/c9fdc93c-1de4-4010-9eb1-3132a6bf4c48)




