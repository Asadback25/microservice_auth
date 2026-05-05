from rest_framework_simplejwt.tokens import RefreshToken


def _build_claims(user):
    return {
        "user_id": str(user.id),  # UUID
        "username": user.username,
        "role": user.role.name if user.role else None
    }


def generate_tokens(user):
    refresh = RefreshToken.for_user(user)

    claims = _build_claims(user)

    # refresh token ga qo‘shamiz
    for key, value in claims.items():
        refresh[key] = value

    # access token ga ham qo‘shiladi avtomatik
    access = refresh.access_token

    return {
        "access": str(access),
        "refresh": str(refresh)
    }