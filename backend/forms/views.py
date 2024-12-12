from rest_framework import generics, status
from rest_framework.response import Response as Respnse
from rest_framework.views import APIView

from .models import Form, Question, Response
from .serializers import FormSerializer, QuestionSerializer, ResponseSerializer


class FormRetrieveView(generics.RetrieveAPIView):
    serializer_class = FormSerializer
    queryset = Form.objects.all()
