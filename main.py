import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()

from users.models import CustomUser

username = "asad"

user = CustomUser.objects.get(username=username)


password = "Kelajak5002@"

user.set_password(password)

user.save()

print(user.password)