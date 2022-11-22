from rest_framework import serializers
from gym_api import models


class WelcomeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)


class InstructorProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InstructorProfile
        fields = ('id', 'name', 'email', 'password', 'phone_number', 'schedule')
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
            phone_number=validated_data['phone_number'],
            schedule=validated_data['schedule']
        )
        return user


class MemberProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MemberProfile
        fields = ('id', 'email', 'name', 'password', 'phone_number', 'instructor', 'subscriptions', 'services', 'schedule')
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
            phone_number=validated_data['phone_number'],
            instructor=validated_data['instructor'],
            subscriptions=validated_data['subscriptions'],
            services=validated_data['services'],
            schedule=validated_data['schedule'],
        )
        return user


class UserFeedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Plan
        fields = ('id', 'member', 'instructor', 'starting_day', 'ending_day', 'goal')


class PlanItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlanItems
        fields = ('id', 'plan', 'exercise', 'day', 'repeat', 'description')
