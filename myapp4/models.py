from django.db import models

# Create your models here.
class Add_Post(models.Model):
    sarlavha = models.CharField(max_length=128, null=False)
    matn = models.TextField
    image = models.ImageField(upload_to="post")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.CharField(max_length=128)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    new = models.ForeignKey(Add_Post, on_delete=models.CASCADE)


