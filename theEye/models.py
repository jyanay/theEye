from django.db import models


class Session(models.Model):
    session_id = models.UUIDField()

    def __str__(self):
        return str(self.session_id)


class Event(models.Model):
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    category = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    data = models.JSONField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f'Session ID: {self.session_id}, Category:{self.category}, ' \
               f'Event: {self.name}, Timestamp {self.timestamp}'

    class Meta:
        ordering = ['-timestamp']




