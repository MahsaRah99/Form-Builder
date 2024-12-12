from rest_framework import generics, status
from rest_framework.response import Response as Respnse
from rest_framework.views import APIView

from .models import Form, Question, Response
from .serializers import FormSerializer, QuestionSerializer, ResponseSerializer


class FormRetrieveView(generics.RetrieveAPIView):
    serializer_class = FormSerializer
    queryset = Form.objects.all()


class QuestionRetrieveView(generics.RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class FormSubmitView(APIView):
    def post(self, request, form_id):
        form = Form.objects.get(id=form_id)
        question_ids = [question.id for question in form.question_set.all()]

        responses_data = request.data
        responses_to_create = []

        for response_data in responses_data:

            question_id = response_data.get("question")
            if question_id not in question_ids:
                return Respnse(
                    {"detail": "Invalid question ID"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            response_data["form"] = form.id
            response_data["question"] = question_id

            serializer = ResponseSerializer(data=response_data)
            if serializer.is_valid():

                responses_to_create.append(serializer.validated_data)
            else:
                return Respnse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        Response.objects.bulk_create([Response(**data) for data in responses_to_create])

        return Respnse(
            {"detail": "Responses successfully saved"}, status=status.HTTP_201_CREATED
        )
