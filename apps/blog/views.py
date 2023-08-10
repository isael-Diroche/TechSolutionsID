from django.shortcuts import render, get_object_or_404
from apps.blog.models import Post, Categoria

# Create your views here.

def blog(request):
    
    categoria = Categoria.objects.all()
    posts = Post.objects.all()
    
    context = {
        'posts': posts,
        'categoria': categoria
    }
    
    return render(request, "blog/blog.html", context)

# ------------------------------------------------------------------------
def categoria(request, categoria_id):

    categoria = Categoria.objects.get(id=categoria_id)
    post = Post.objects.filter(categorias = categoria)

    return render(request, 'blog/categoria.html', {'categoria': categoria, 'posts': post})

# ------------------------------------------------------------------------

def ver_descripcion_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    categoria = Categoria.objects.all()
    
    context = {
        'post': post,
    }
    
    return render(request, 'posts/descripcion_post.html', context)