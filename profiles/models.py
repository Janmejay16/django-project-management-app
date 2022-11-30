from django.db.models import *

# Create your models here.
class Profile(Model):
    user_roles = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('member', 'Member'),
    ]

    email = EmailField("Email Address", max_length=255, unique=True)
    first_name = CharField("First Name", max_length=255, blank=True, null=True)
    last_name = CharField("Last Name", max_length=255, blank=True, null=True)
    role = CharField(choices=user_roles, max_length=10, default='member')
    mobile = CharField(max_length=13, null=True, blank=True)
    password = CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_role(self):
        return f"{self.role}"

    def get_id(self):
        return f"{self.id}"