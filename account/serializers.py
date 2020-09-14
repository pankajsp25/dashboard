from rest_framework import serializers
from django.contrib.auth import get_user_model

from account.models import Profile

User = get_user_model()


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',)


class ProfileViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileSerializers(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    birthday = serializers.DateField(required=False)
    designation = serializers.CharField(required=False)
    profile_image = serializers.ImageField(required=False)
    bio = serializers.CharField(required=False)

    def create(self, validated_data):
        user = User.objects.create(
            first_name = validated_data.get('first_name'),
            last_name = validated_data.get('last_name'),
            email = validated_data.get('email'),
            username = validated_data.get('username'),
        )
        user.profile.phone = validated_data.get('phone')

        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.profile.phone = validated_data.get('phone', instance.profile.phone)
        instance.profile.bio = validated_data.get('bio', instance.profile.bio)
        instance.profile.profile_image = validated_data.get('profile_image', instance.profile.profile_image)

        instance.save()

        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data['phone'] = instance.profile.phone
        data['birthday'] = instance.profile.birthday
        data['designation'] = instance.profile.designation
        profile_img = instance.profile.profile_image
        data['profile_image'] = profile_img.url if profile_img else None
        data['bio'] = instance.profile.bio

        return data
