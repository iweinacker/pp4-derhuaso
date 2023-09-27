from django.urls import path
from .views import reservation_view

urlpatterns = [
    # path('', reservation_view.as_view(), name='home'),
    path('', reservation_view, name='home'),
]
