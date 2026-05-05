from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()

    password1 = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8)

    def validate(self, data):
        password1 = data.get("password1")
        password2 = data.get("password2")

        if not password1 or not password2:
            raise serializers.ValidationError("Password is required")

        if password1 != password2:
            raise serializers.ValidationError("Passwords do not match")

        return {
            "username": data["username"],
            "email": data["email"],
            "password": password1,
        }