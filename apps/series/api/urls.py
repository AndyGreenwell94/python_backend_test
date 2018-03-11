from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

router.register(
    'series',
    views.SeriesViewset,
    base_name='series',
)

router.register(
    'episodes',
    views.EpisodeViewset,
    base_name='episodes',
)

urlpatterns = router.urls
