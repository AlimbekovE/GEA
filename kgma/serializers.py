from rest_framework import serializers
from . models import Kgma

class KgmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kgma
        fields = ('title', 'text')

        def create(self, validated_data):
            return Kgma.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.text = validated_data.get('text', instance.text)
            instance.save
            return instance