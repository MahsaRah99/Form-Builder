from rest_framework import serializers

from .models import Form, Question, Response
from .validators import validate_response


class FormSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Form
        fields = ("title", "description", "created_at", "questions")
        read_only_fields = ("created_at",)

    def get_questions(self, obj):
        questions = Question.objects.filter(form=obj).order_by("id")
        serializer = QuestionListSerializer(questions, many=True)
        return serializer.data
