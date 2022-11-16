from rest_framework import serializers
from gym_api import models


class WelcomeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)


class MemberProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MemberProfile
        fields = ('id', 'email', 'name', 'password', 'phone_number')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        user = models.MemberProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            phone_number=validated_data['phone_number']
        )
        return user


class InstructorProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InstructorProfile
        fields = ('id', 'name', 'email', 'password', 'phone_number')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        user = models.InstructorProfile.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data['phone_number']
        )
        return user
