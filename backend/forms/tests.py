from django.core.exceptions import ValidationError
from django.test import TestCase

from .enums import NumericConstraints, QuestionTypes
from .models import Form, Question, Response


class FormAndResponseTestCase(TestCase):

    def setUp(self):
        self.form = Form.objects.create(
            title="Sample Form", description="A form to test questions and responses."
        )

        self.short_question = Question.objects.create(
            form=self.form,
            question_type=QuestionTypes.SHORT_RESPONSED,
            question_text="What is your name?",
            is_required=True,
        )
        self.short_not_required_question = Question.objects.create(
            form=self.form,
            question_type=QuestionTypes.SHORT_RESPONSED,
            question_text="How are you today?",
            is_required=False,
        )
        self.long_question = Question.objects.create(
            form=self.form,
            question_type=QuestionTypes.LONG_RESPONSED,
            question_text="Describe your project.",
            is_required=False,
        )
        self.numeric_question = Question.objects.create(
            form=self.form,
            question_type=QuestionTypes.NUMERIC_RESPONSED,
            question_text="What is your age?",
            is_required=True,
            numeric_constraint=NumericConstraints.INTEGER,
        )
        self.email_question = Question.objects.create(
            form=self.form,
            question_type=QuestionTypes.EMAIL_RESPONSED,
            question_text="What is your email?",
            is_required=True,
        )

    def test_valid_responses(self):
        response = Response.objects.create(
            question=self.short_question, form=self.form, short_response="Adele Adkins"
        )
        self.assertEqual(response.short_response, "Adele Adkins")

        response = Response.objects.create(
            question=self.long_question,
            form=self.form,
            long_response="This is a description of my project.",
        )
        self.assertEqual(response.long_response, "This is a description of my project.")

        response = Response.objects.create(
            question=self.numeric_question, form=self.form, numeric_response=30
        )
        self.assertEqual(response.numeric_response, 30)

        response = Response.objects.create(
            question=self.email_question,
            form=self.form,
            email_response="adele@email.com",
        )
        self.assertEqual(response.email_response, "adele@email.com")

    def test_invalid_responses(self):
        with self.assertRaises(ValidationError):
            Response.objects.create(
                question=self.short_question,
                form=self.form,
                short_response="short response",
                long_response="extra long response",
            )

        with self.assertRaises(ValidationError):
            Response.objects.create(
                question=self.email_question, form=self.form, numeric_response=56
            )

        with self.assertRaises(ValidationError):
            Response.objects.create(
                question=self.numeric_question, form=self.form, numeric_response=30.5
            )

        with self.assertRaises(ValidationError):
            Response.objects.create(question=self.short_question, form=self.form)

    def test_non_required_field_responses(self):
        response = Response.objects.create(
            question=self.short_not_required_question, form=self.form
        )
        self.assertIsNone(response.short_response)

    def test_invalid_question_constraints(self):
        with self.assertRaises(ValidationError):
            Question.objects.create(
                form=self.form,
                question_type=QuestionTypes.SHORT_RESPONSED,
                question_text="Invalid constraint",
                numeric_constraint=NumericConstraints.FLOAT,
            )
