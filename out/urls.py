from django.urls import path ,include
from .views import *
urlpatterns = [
    path('table1/',table1_view),
    path('table2/<tableId>',table2_view),
    path('table3/<tableId>',table3_view),
    path('table4/<tableId>',table4_view),
    path('addSubTable/<tableId>/<tableModel>',addSubTable_view),
    path('updateRow/<modelName>/<rowId>/<tableId>',updateRow_view),
    path('deleteRow/<modelName>/<rowId>/<tableId>',deleteRow_view),
]
