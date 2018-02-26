from rest_framework import serializers
from . models import Apply

class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = ('name', 'email', 'phone', 'message')

        def create(self, validated_data):
            return Apply.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.email = validated_data.get('email', instance.email)
            instance.phone = validated_data.get('phone', instance.phone)
            instance.message = validated_data.get('message', instance.message)
            instance.save
            return instance