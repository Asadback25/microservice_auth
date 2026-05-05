from users.models import CustomUser

class UserRepositories:

    @staticmethod
    def create_user(**data):
        user = CustomUser.objects.create_user(**data)
        user.save()
        return user

    @staticmethod
    def get_by_email(email: str):
        return CustomUser.objects.get(email=email)

    @staticmethod
    def get_by_username(username: str):
        return CustomUser.objects.get(username=username)

    @staticmethod
    def get_by_id(user_id: str):
        return CustomUser.objects.get(id=user_id)

    @staticmethod
    def update_user(user, **data):
        for key, value in data.items():
            setattr(user, key, value)
        user.save()
        return user