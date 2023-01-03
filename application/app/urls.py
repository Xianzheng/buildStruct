from django.urls import path
from .basic_views import *
from .ext_view import *
from .layout_view import *
urlpatterns = [
    path('hello/',hello),
    path('index/',index_view),
    path('tableDetail/<tableId>',tableDetail_view),
    path('updateRow/<rowId>/<tableId>',updateRow_view),
    path('deleteRow/<rowId>/<tableId>',deleteRow_view),
    path('addRow/<tableId>',addRow_view),
    path('analyze/<tableId>',analyze_view),
    path('levelOne/',levelOne_view),
    path('levelTwo/<tableId>',levelTwo_view),
    path('levelThree/<tableId>',levelThree_view),
    path('levelFour/<tableId>',levelFour_view),
    path('levelFive/<tableId>',levelFive_view),
    path('addSubTable/<tableId>/<tableModel>',addSubTable_view),
]