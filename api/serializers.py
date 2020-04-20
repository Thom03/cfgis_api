from rest_framework import serializers
from api.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """Serialization of Profile Model"""

    class Meta:
        model = UserProfile
        fields = ('title', 'company', 'address', 'phone', 'city', 'photo')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serialization of User Model"""
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            """Profile creation serialization"""
            profile_data = validated_data.pop('profile')
            password = validated_data.pop('password')
            user = User(**validated_data)
            user.set_password(password)
            user.save()
            UserProfile.objects.create(user=user, **profile_data)
            return user

        def update(self, instance, validated_data):
            profile_data = validated_data.pop('profile')
            profile = instance.profile

            instance.email = validated_data.get('email', instance.email)
            instance.save()

            profile.title = profile_data.get('title', profile.title)
            profile.company = profile_data.get('company', profile.company)
            profile.address = profile_data.get('address', profile.address)
            profile.phone = profile_data.get('phone', profile.phone)
            profile.city = profile_data.get('city', profile.city)
            profile.photo = profile_data.get('photo', profile.photo)
            profile.save()

            return instance
