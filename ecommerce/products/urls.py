from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from .import views


def index(request):
    return HttpResponse("This is http responses from an app called products")

def admin(request):
    return admin.site.urls




urlpatterns = [
    path("test/", index),

    path('test/',index),

    #path('',views.index),
    path('',views.new_html)
]
