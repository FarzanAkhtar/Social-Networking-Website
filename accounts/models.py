from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete='CASCADE')

    def get_absolute_url(self):
        return reverse('accounts:profile-view', kwargs= {'pk': self.pk})


    def __str__(self):
        return self.user.username



def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


class ProfileDetails(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)







