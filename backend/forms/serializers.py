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


class QuestionSerializer(serializers.ModelSerializer):
    form_name = serializers.StringRelatedField(source="form")

    class Meta:
        model = Question
        fields = (
            "form_name",
            "question_type",
            "question_text",
            "is_required",
            "place_holder",
            "numeric_constraint",
        )
        read_only_fields = ("form_name",)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["numeric_constraint"] = instance.get_numeric_constraint_display()
        return data


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            "question_type",
            "question_text",
            "is_required",
            "place_holder",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["question_type"] = instance.get_question_type_display()
        return data


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = [
            "form",
            "question",
            "short_response",
            "long_response",
            "email_response",
            "numeric_response",
        ]

    def validate(self, data):
        question = data.get("question")
        is_required = question.is_required

        validate_response(data, question, is_required)

        return data
