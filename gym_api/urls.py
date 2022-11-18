from gym_api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('member-profile', views.MemberProfileViewSet)
router.register('instructor-profile', views.InstructorProfileViewSet)
router.register('user-feed', views.UserProfileFeedViewSet)
router.register('plan', views.PlanViewSet)
router.register('plan-items', views.PlanItemsViewSet)

urlpatterns = [
    path('welcome-view/', views.WelcomeApiView.as_view()),
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),
]
