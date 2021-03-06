from django.db import models


from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    github_profile_site = models.URLField(blank=True)
    #profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username
class Peer(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


    class Meta:
        ordering=('name',)
    
class Clubs(models.Model):
    title=models.CharField(max_length=100)
    members=models.ManyToManyField(Peer)

    def __str__(self):
        return self.title

    class Meta:
        ordering=('title',)


