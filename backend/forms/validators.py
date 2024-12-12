from django.core.exceptions import ValidationError


def validate_response(data, question, is_required):

    response_fields = [
        "short_response",
        "long_response",
        "email_response",
        "numeric_response",
    ]
    valid_field = {
        "SR": "short_response",
        "LR": "long_response",
        "ER": "email_response",
        "NR": "numeric_response",
    }.get(question.question_type)

    if not valid_field:
        raise ValidationError(f"Unsupported question type: {question.question_type}")

    response_data = {
        key: value for key, value in data.items() if key in response_fields
    }

    provided_fields = {key for key, value in response_data.items() if value is not None}

    if response_data.get(valid_field) is None:
        if is_required:
            raise ValidationError(f"{valid_field} is required for this question.")
        else:
            if len(provided_fields) > 0:
                raise ValidationError(
                    f"Only {valid_field} should be provided for this question."
                )
    else:
        if len(provided_fields) > 1:
            raise ValidationError(
                f"Only {valid_field} should be provided for this question."
            )

    if (
        valid_field == "numeric_response"
        and response_data.get("numeric_response") is not None
    ):
        numeric_response = response_data.get("numeric_response")

        if (
            question.numeric_constraint == "INT"
            and not float(numeric_response).is_integer()
        ):
            raise ValidationError("Response must be an integer for this question.")
