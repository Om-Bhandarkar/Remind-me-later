from django.db import models

# Create your models here
class Reminder(models.Model):
    REMINDER_TYPES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
    ]

    message = models.TextField()
    remind_at = models.DateTimeField()
    reminder_type = models.CharField(max_length=20, choices=REMINDER_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message[:20]} at {self.remind_at}"
