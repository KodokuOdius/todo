from django.db.models import *


class Todo(Model):
    title = CharField(max_length=255)
    body = TextField()

    def __str__(self) -> str:
        return self.title

