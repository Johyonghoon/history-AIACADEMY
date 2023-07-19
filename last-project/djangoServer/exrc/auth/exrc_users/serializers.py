from rest_framework import serializers

from exrc.auth.exrc_users.models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

    def create(self, validated_data):
        return Users.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return Users.objects.filter(pk=instance, **validated_data)

    def delete(self, instance, validated_data):
        pass
