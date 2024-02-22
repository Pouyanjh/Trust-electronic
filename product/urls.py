from django.urls import path
from .views import Popproductview, topproductview, productallview

urlpatterns = [
    path('pop/', Popproductview.as_view()),
    path('top/', topproductview.as_view()),
    path('allp/', productallview.as_view()),
]