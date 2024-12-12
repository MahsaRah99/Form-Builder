from django.urls import path

from . import views

app_name = "forms"

urlpatterns = [
    path("retrieve/<int:pk>/", views.FormRetrieveView.as_view(), name="form-retrieve"),
    path(
        "question/<int:pk>/",
        views.QuestionRetrieveView.as_view(),
        name="question-retrieve",
    ),
    path("submit/<int:form_id>/", views.FormSubmitView.as_view(), name="form-submit"),
]
