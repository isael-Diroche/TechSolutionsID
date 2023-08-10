from django.urls import path

from apps.blog.views import blog, categoria, ver_descripcion_post

urlpatterns = [

    path('', blog, name="Blog"),
    path('categoria/<int:categoria_id>/', categoria, name="categoria"),
    path('post/<int:post_id>/', ver_descripcion_post, name="post"),

]
