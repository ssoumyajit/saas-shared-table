from django.db import models
from django.contrib.auth.models import User


class Tenant(models.Model):
    name = models.CharField(max_length=30)  # cipherdojo


class FkToTenant(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Post(FkToTenant):
    post = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post


class Comments(FkToTenant):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    replied_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

# https://github.com/agiliq/building-multi-tenant-applications-with-django/tree/master/shared-db/tenants
