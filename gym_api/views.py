from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from gym_api import serializers
from gym_api import models
from rest_framework.authentication import TokenAuthentication
from gym_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


class WelcomeApiView(APIView):
    serializer_class = serializers.WelcomeSerializer

    def get(self, request):

        text = [
            '"A list of gym subscriptions"',
        ]

        return Response({'message': 'Welcome!', 'text': text})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Welcome {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):

        return Response({'method': 'DELETE'})


class InstructorProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.InstructorProfileSerializer
    queryset = models.InstructorProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class MemberProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MemberProfileSerializer
    queryset = models.MemberProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

    # def perform_update(self, serializer):
    #     item = serializer.validated_data
    #     instructor = item.get('instructor')
    #     instructor.save()
    #     serializer.save(schedule=instructor.schedule)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.UserFeedItemSerializer
    queryset = models.UserFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)


class PlanViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.PlanSerializer
    queryset = models.Plan.objects.all()
    permission_classes = (IsAuthenticated, permissions.UpdateOwnPlan)


class PlanItemsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.PlanItemsSerializer
    queryset = models.PlanItems.objects.all()
    permission_classes = (IsAuthenticated, permissions.UpdateOwnPlan)
