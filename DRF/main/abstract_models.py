from django.db import models


class CreatedAt(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdatedAt(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDelete(models.Model):
    class Meta:
        abstract = True
    is_active = models.BooleanField(null=False, default=True)

    def delete(self):
        self.is_active = False
        self.save()

    def restore(self):
        self.is_active = True
        self.save()
