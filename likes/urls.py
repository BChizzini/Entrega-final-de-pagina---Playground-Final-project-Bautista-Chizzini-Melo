from django.urls import path
from .views import like_car, comment_car

urlpatterns = [
    path('like/<int:pk>/', like_car, name='like_car'),
    path('comment/<int:pk>/', comment_car, name='comment_car'),
]