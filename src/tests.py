from django.test import TestCase
from apps.blog.models import Post
# Create your tests here.


class MiModeloTestCase(TestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
    
    def setUp(self):
        Post.objects.create(titulo="Ejemplo", contenido="este es un texto de ejemplo", imagen="""C:\isael\Proyectos\DEV-2022\TechSolutionsID\src\static\img\about-us.png""", autor = "Isael", categorias="Ninguna")
