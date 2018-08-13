from rest_framework import routers

from .views import FilmViewSet

# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'movies', FilmViewSet)

# URLs настраиваются автоматически роутером
urlpatterns = router.urls