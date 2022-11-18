from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserMemberManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class InstructorProfile(AbstractBaseUser, models.Model):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    is_staff = models.BooleanField(default=True)

    MORNING = 'AM'
    AFTERNOON = 'PM'
    SCHEDULE_CHOICES = [
        (MORNING, '07:00-15:00'),
        (AFTERNOON, '15:00-23:00')
    ]
    SCHEDULE = models.CharField(
        max_length=2,
        choices=SCHEDULE_CHOICES
    )

    objects = UserMemberManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.email


class MemberProfile(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    is_staff = models.BooleanField(default=False)
    instructor = models.ForeignKey(InstructorProfile, on_delete=models.CASCADE)

    ONEMONTH = '1M'
    THREEMONTH = '3M'
    SIXMONTH = '6M'
    UNLIMITED = 'UL'
    SUBSCRIPTIONS_CHOICES = [
        (ONEMONTH, 'One month'),
        (THREEMONTH, 'Six month'),
        (SIXMONTH, 'One year'),
        (UNLIMITED, 'Unlimited'),
    ]
    SUBSCRIPTION = models.CharField(
        max_length=2,
        choices=SUBSCRIPTIONS_CHOICES,
        default=UNLIMITED,
    )

    LOSINGWEIGHT = 'LW'
    GAINWEIGHT = 'GW'
    BODYBUILDER = 'BD'
    ATHLETICISM = 'AT'
    SERVICES_CHOICES = [
        (LOSINGWEIGHT, 'Losing weight'),
        (GAINWEIGHT, 'Gain weight'),
        (BODYBUILDER, 'Bodybuilder'),
        (ATHLETICISM, 'Athleticism'),
    ]
    SERVICES = models.CharField(
        max_length=2,
        choices=SERVICES_CHOICES,
        default=LOSINGWEIGHT
    )

    objects = UserMemberManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name


class UserFeedItem(models.Model):
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text


class Plan(models.Model):
    member = models.ForeignKey('gym_api.MemberProfile', on_delete=models.CASCADE)
    instructor = models.ForeignKey('gym_api.InstructorProfile', on_delete=models.CASCADE)
    starting_day = models.DateField(auto_now_add=False)
    ending_day = models.DateField(auto_now_add=False)
    goal = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.member.name} {self.goal}'


class PlanItems(models.Model):
    plan = models.ForeignKey('gym_api.Plan', on_delete=models.CASCADE)
    exercise = models.CharField(max_length=100)
    day = models.DateField()
    repeat = models.IntegerField()
    description = models.CharField(max_length=255)
