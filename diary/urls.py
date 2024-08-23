from django.urls import path
from .views import add_mark, edit_mark, delete_mark, UserMarksMonthArchiveView


urlpatterns = [
    # path('add/', add_mark, name='add_mark'),
    # path('edit/<int:pk>/', edit_mark, name='edit_mark'),
    # path('delete/<int:pk>/', delete_mark, name='delete_mark'),
    path('<str:username>/<int:year>/<int:month>/', UserMarksMonthArchiveView.as_view(), name='user-dairy'),
]

app_name = "diary"