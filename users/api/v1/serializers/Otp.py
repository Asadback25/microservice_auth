from rest_framework import serializers

class VerifyOtpSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6, min_length=6)

    def validate_code(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("OTP faqat raqamlardan iborat bo'lishi kerak")
        return value

class ResendOtpSerializer(serializers.Serializer):
    username = serializers.CharField(trim_whitespace=True)

    def validate_username(self, value):
        return value.strip().lower()
