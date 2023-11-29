from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=155)
    photo = models.ImageField(upload_to='posts', null=True, blank=True)
    about = models.TextField()
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(
        Category,
        blank=True,
        related_name='products'
    )

    def __str__(self):
        return f'{self.id} {self.title}'


class Comment(models.Model):
    post = models.ForeignKey(
        'post.Product',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

