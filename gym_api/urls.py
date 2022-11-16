from gym_api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('welcome-viewset', views.WelcomeViewSet, base_name='welcome-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('welcome-view/', views.WelcomeApiView.as_view()),
    path('', include(router.urls)),
]
