from rest_framework.validators import UniqueValidator

from .models import user
from rest_framework import serializers
from rest_framework import validators




class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=user.objects.all())]
    )
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = user
        fields = (
            'username', 'email', 'password1', 'password2', 'id', 'phone_number'
        )

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({
                'password': 'Password does not match!'
            })
        return super(RegisterSerializer, self).validate(attrs)


    def create(self, validated_data):
        User = user.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password1'],
            phone_number=validated_data['phone_number']
        )




        return User