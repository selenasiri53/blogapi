from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post

# Outline for serializers.py:

# from rest_framework import serializers
# from .models import Component

# class ComponentSerializer(serializers.ModelSerializer): # built-in django

    #class Meta:
        #fields = ('id', 'list_fields_to_use',) # 
        # model = Component // explicitly set the model here