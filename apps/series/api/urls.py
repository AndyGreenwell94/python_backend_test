from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

router.register(
    'series',
    views.SeriesViewset,
    base_name='series',
)

urlpatterns = router.urls
