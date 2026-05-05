class ProfileService:

    @staticmethod
    def get_profile(user):
        return user.profile

    @staticmethod
    def update_profile(user, data):
        profile = user.profile

        for key, value in data.items():
            setattr(profile, key, value)

        profile.save()
        return profile