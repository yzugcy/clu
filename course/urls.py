from django.urls import path

from course import views

app_name = "course"


urlpatterns = [
    path("", views.CourseListView.as_view(), name="list"),
]
