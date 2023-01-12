from django.urls import path ,include
from .views import *
urlpatterns = [
    path('table1/',table1_view),
    path('table2/<tableId>',table2_view),
    path('table3/<tableId>',table3_view),
path('addSubTable/<tableId>/<tableModel>',addSubTable_view),
]
