from rest_framework import serializers


class VerifyOtpSerializer(serializers.Serializer):
    username = serializers.CharField(trim_whitespace=True)
    code = serializers.CharField(max_length=6, min_length=6)

    def validate_username(self, value):
        return value.strip().lower()

    def validate_code(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("OTP must contain only digits")
        return value


class ResendOtpSerializer(serializers.Serializer):
    username = serializers.CharField(trim_whitespace=True)

    def validate_username(self, value):
        return value.strip().lower()