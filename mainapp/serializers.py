from rest_framework import serializers
from .models import Content
from assignment_api.settings import AUTH_USER_MODEL
from .models import User
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.validators import EmailValidator

class CreateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[EmailValidator(message="Enter a valid email address.")],required=True)
    
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        validators=[
            MinLengthValidator(8),
            RegexValidator(
                regex=r'^(?=.*[a-z])(?=.*[A-Z]).+$',
                message="Password must contain at least one lowercase letter, one uppercase letter."
            )
        ]
    )
    full_name = serializers.CharField(max_length=255, required=True)
    phone_no = serializers.CharField(max_length=10, required=True)
    pincode = serializers.CharField(max_length=6, required=True)


    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'full_name', 'phone_no', 'pincode']
        extra_kwargs = {'password': {'write_only': True}}


    def validate_phone_no(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("Phone number must be a 10-digit numeric value.")
        return value
    
    
    def validate_pincode(self, value):
        if not value.isdigit() or len(value) != 6:
            raise serializers.ValidationError("Pincode must be a 6-digit numeric value only.")
        return value


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class LoginUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }



class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = "__all__"

    def validate_user(self, value):
        print(value, "fasd")
        user = self.context['request'].user
        print("userser", user)
        if user.role == 'author' and user != value:
            raise serializers.ValidationError("You can only create content for yourself.")
        return value

    # def validate(self, data):
    #     user = self.context['request'].user
    #     if user.role == 'author' and user.id != data['author'].id:
    #         raise serializers.ValidationError("You can only create content for yourself.")
    #     return data
