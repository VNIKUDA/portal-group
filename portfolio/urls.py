from django.urls import path
from portfolio import views

urlpatterns = [
    path('portfolio/', views.portfolio_list, name='portfolio_list'),
    path('portfolio/create/', views.portfolio_create, name='portfolio_create'),
    path('portfolio/edit/<int:pk>/', views.portfolio_edit, name='portfolio_edit'),
    path('portfolio/delete/<int:pk>/', views.portfolio_delete, name='portfolio_delete'),
]
