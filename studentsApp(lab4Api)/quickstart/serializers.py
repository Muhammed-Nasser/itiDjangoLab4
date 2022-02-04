from django.contrib.auth.models import User
from home.models import student
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email',]


class studentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = student
        fields = ['fullname', 'email']