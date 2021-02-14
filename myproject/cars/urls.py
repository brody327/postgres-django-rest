from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'drivers', views.HeroViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest-framework.urls', namespace='rest-framework'))
    # path("<int:pk>/", views.car_detail, name="car_detail"),
]