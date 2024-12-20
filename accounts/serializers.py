from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email ', 'bio','profile_pic']
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.email = validated_data.get('email',instance.username) 
        instance.bio = validated_data.get('bio', instance.bio)
        instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
        instance.save()
        return instance   

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username','email' ,'password']

    def create(self, validated_data):
        user = user.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']

        )    
        return user
class UserLoginSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField()

        def validate(self, data):
            user = CustomUser.objects.filter(username=data['username'])
            if not user:
                raise serializers.ValidationError('User not found')
            return data    
    