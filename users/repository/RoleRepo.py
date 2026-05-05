from users.models import Role


class RoleRepository:

    @staticmethod
    def get_by_name(name: str):
        return Role.objects.filter(name=name).first()

    @staticmethod
    def get_default_role():
        return Role.objects.filter(name="user").first()

    @staticmethod
    def assign_role(user, role):
        user.role = role
        user.save()
        return user