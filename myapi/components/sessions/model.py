from django.db import models


class Session(models.Model):
    name = models.CharField(null=False, max_length=300, unique=True)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
