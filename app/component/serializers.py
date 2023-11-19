from rest_framework import serializers
from .models import Issue,User


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['title', 'description']


class UserSerializer(serializers.ModelSerializer):
    claimed_issues = IssueSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'points', 'claimed_issues']
