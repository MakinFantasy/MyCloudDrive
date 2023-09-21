from django.contrib.auth.models import User
from django.db import models


def get_user_directory_path(instance, filename):
    return 'user{0}/{1}'.format(instance.user_id, filename)


class FileTb(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    file_file = models.FileField(upload_to=..., null=True, blank=True)
    file_name = models.CharField(max_length=50, null=True, blank=True)
    file_type = models.CharField(max_length=50, null=True, blank=True)
    file_description = models.TextField(max_length=255, null=True, blank=True)
    file_size = models.CharField(max_length=50, blank=True)
    file_created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"{self.file_name}, {self.file_description}"
