from django.shortcuts import render, get_object_or_404
from apps.blog.models import Post, Categoria

# Create your views here.

def blog(request):
    
    categoria = Categoria.objects.all()
    posts = Post.objects.all()
    
    unique_categories = set()  # Conjunto para almacenar categorías únicas
    
    for post in posts:
        for categoria in post.badge.all():
            unique_categories.add(categoria)
    
    context = {
        'posts': posts,
        'categoria': categoria,
        'unique_categories': unique_categories
    }
     
    return render(request, "blog/blog.html", context)

# ------------------------------------------------------------------------
def categoria(request, categoria_id):

    categoria = Categoria.objects.get(id=categoria_id)
    categorias = Categoria.objects.all()  # Todas las categorías

    post = Post.objects.filter(badge=categoria)

    return render(request, 'blog/categoria.html', {'posts': post, 'categoria': categoria, 'categorias': categorias})

# ------------------------------------------------------------------------

def ver_descripcion_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    categoria = Categoria.objects.all()
    
    context = {
        'post': post,
        'post_description': f'posts/post_{post.id}.html'
    }
    
    return render(request, f'blog/descripcion_post.html', context)