from rest_framework import routers
from .viewsets import BookViewSet

#Creamos las rutas para poder hacer las operaciones de crud
router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls