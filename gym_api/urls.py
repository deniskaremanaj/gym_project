from gym_api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('member-profile', views.UserMemberViewSet)
router.register('instructor-profile', views.UserInstructorViewSet)

urlpatterns = [
    path('welcome-view/', views.WelcomeApiView.as_view()),
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),
]
