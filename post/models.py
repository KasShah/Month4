from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=155)
    photo = models.ImageField(upload_to='posts', null=True, blank=True)
    about = models.TextField()
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.id} {self.title}'
