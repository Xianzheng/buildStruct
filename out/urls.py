from django.urls import path ,include
from .views import *
urlpatterns = [
    path('table1/',table1_view),
    path('table2/',table2_view),
]
