from rest_framework import serializers
from . models import About

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('title', 'text')

        def create(self, validated_data):
            return About.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.text = validated_data.get('text', instance.text)
            instance.save
            return instance