#from attr import fields
from rest_framework import serializers
from .models import Todo #importing the todo model

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')
