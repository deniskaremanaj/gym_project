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


class WelcomeApiView(APIView):
    serializer_class = serializers.WelcomeSerializer

    def get(self, request):

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Welcome!', 'an_apiview': an_apiview})

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


class UserMemberViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MemberProfileSerializer
    queryset = models.MemberProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserInstructorViewSet(viewsets.ModelViewSet):
    queryset = models.InstructorProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
