from django.db import models
from django.utils import timezone # date ucun
from django.contrib.auth.models import User # ForeignKey ve Cascade ucun


class Post(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=160)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',null=True)


    class Meta:
        ordering = ['-date']

    # postlarin tarixe gore gorunmesi ucun


    def __str__(self):
        return self.title
    
# bu adminpanelde adinin gorunmesi ucun
