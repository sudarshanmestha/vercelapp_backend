# core/serializers.py

from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    _has_phone_field = False  # 💥 This prevents the error

    email = serializers.EmailField(required=True)

    def validate(self, data):
        print("✅ CustomRegisterSerializer is used")  # For debug
        return super().validate(data)
