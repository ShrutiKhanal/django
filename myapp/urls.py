from django.urls import path
from .views import home, index, view_name, view_name_jon, view_name_jane, json_view

urlpatterns = [
    path("name/jon/", view_name_jon),
    path("name/jane/", view_name_jane),
    path("get-name/<str:name>/", view_name),  #placeholder, dynamic, <str:name>: path converter
    path('index/', index),
    path('json-view/', json_view),
    path('', home)
]