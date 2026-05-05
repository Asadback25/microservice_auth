from users.models import Profile

class ProfileRepository:

    @staticmethod
    def create(user, **data):
        return Profile.objects.create(user=user, **data)

    @staticmethod
    def get_by_user(user):
        return Profile.objects.filter(user=user).first()

    @staticmethod
    def update(profile, **data):
        for key, value in data.items():
            setattr(profile, key, value)
        profile.save()
        return profile