from django.contrib import admin
from django.urls import path
from urlapp import views

urlpatterns = [
path('one/',views.first_view),
path('two/',views.second_view),
path('three/',views.third_view),

]
