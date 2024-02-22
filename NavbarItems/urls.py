from django.urls import path
from .views import DasteListView

urlpatterns = [
    path('dasteha/', DasteListView.as_view(), name='daste-list'),
]