from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import *

from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import *


class DetailTodo(RetrieveAPIView):
    serializer_class = TodoSerializers
    queryset = serializer_class.Meta.model.objects.all()


class ListTodo(ListAPIView):
    serializer_class = TodoSerializers
    queryset = serializer_class.Meta.model.objects.all()
