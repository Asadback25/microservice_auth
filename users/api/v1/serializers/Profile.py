from rest_framework import serializers
from datetime import date


class ProfileSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=50)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=50)
    bio = serializers.CharField(required=False, allow_blank=True, max_length=500)
    phone_number = serializers.CharField(required=False, allow_blank=True)
    birth_date = serializers.DateField(required=False)

    def validate_first_name(self, value):
        value = value.strip()
        if value and len(value) < 2:
            raise serializers.ValidationError("First name too short")
        return value

    def validate_phone_number(self, value):
        if value and not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits")
        return value

    def validate_birth_date(self, value):
        if value and value > date.today():
            raise serializers.ValidationError("Birth date cannot be in future")
        return value