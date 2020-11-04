from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    content=models.TextField()
    author=models.CharField(max_length=13)
    photo=models.ImageField(default='default.png',blank=True)
    thumbnail=models.ImageField(default='default.png',blank=True)
    video=models.FileField(upload_to='videos/',blank=True)
    slug=models.CharField(max_length=25)
    timeStamp=models.DateTimeField(blank=True)
def __str__(self):
    return 'Post of' + self.user.username

class BlogComment(models.Model):
    blogsno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',null=True,on_delete=models.CASCADE)
    timeStamp=models.DateTimeField(default=now)
def __str__(self):
    return 'comment by' + self.user.username
