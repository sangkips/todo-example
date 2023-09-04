from rest_framework import serializers

from todoapi.models import Todo

#serializers
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
