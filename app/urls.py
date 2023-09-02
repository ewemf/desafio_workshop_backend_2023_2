from django.urls import path
from rest_framework import routers
from .views import DesenvolvedorViewSet, JogoViewSet, ClienteViewSet

router = routers.DefaultRouter()
router.register(r'desenvolvedor', DesenvolvedorViewSet)
router.register(r'jogo', JogoViewSet)
router.register(r'cliente', ClienteViewSet)
urlpatterns = router.urls