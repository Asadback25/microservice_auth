from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(trim_whitespace=True)
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        style={"input_type": "password"}
    )

    def validate(self, data):
        if not data.get("username") or not data.get("password"):
            raise serializers.ValidationError("Username and password are required")
        return data