from rest_framework import serializers
from django.contrib.auth import get_user_model
from . import models


class Task(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        'task-detail', source='id', read_only=True)
    owner = serializers.SlugRelatedField(
        slug_field='username',
        queryset=get_user_model().objects.all())
    categories = serializers.SlugRelatedField(
        slug_field='name',
        queryset=models.Category.objects.all(),
        many=True)

    class Meta:
        model = models.Task
        fields = ('id', 'name', 'owner', 'categories', 'done', 'url')


class Category(serializers.ModelSerializer):
    tasks = Task(many=True)

    class Meta:
        model = models.Category
        fields = ('id', 'name', 'tasks')


class MyCategory(serializers.ModelSerializer):
    tasks = Task(many=True, source='my_tasks')

    class Meta:
        model = models.Category
        fields = ('id', 'name', 'tasks')
