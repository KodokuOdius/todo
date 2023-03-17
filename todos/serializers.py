from rest_framework.serializers import *
from .models import Todo


class TodoSerializers(ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'body']