import django_filters
from django.contrib.auth import get_user_model
from . import models


class Task(django_filters.FilterSet):
    owner = django_filters.ModelChoiceFilter(to_field_name="username", queryset=get_user_model().objects.all())
    categories = django_filters.ModelMultipleChoiceFilter(to_field_name="name", queryset=models.Category.objects.all())

    class Meta:
        model = models.Task
        fields = ['done', 'owner', 'categories']

