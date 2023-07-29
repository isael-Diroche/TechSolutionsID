from django.urls import path

from apps.blog.views import *

urlpatterns = [

    path('', blog, name="Blog"),
    path('categoria/<int:categoria_id>/', categoria, name="categoria"),

]
